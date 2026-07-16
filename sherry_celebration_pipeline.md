# Daz G9 → Unreal: Celebration-Shot Pipeline & Lessons

Non-MetaHuman pipeline. Daz Genesis 9 FBX → Blender pose → Unreal Engine 5.8 (unreal-mcp bridge).
Companion to `sherry_celebration_pipeline.html` (same content, styled + images embedded).

**Result:** `D:\mydata\3dassets\Sherry_Celebration_UE.png` (arms-overhead open-mouth shout, textured, eyes forward).
**Blender EEVEE reference (same pose):** `D:\mydata\3dassets\Sherry_Celebration.png`.
**Reusable UE assets:** `/Game/CelebFull/` (SherryCelebFull mesh + SherryEyeFix_Anim + _Skeleton).

---

## Goal
Render an existing Daz G9 character (**Sherry**, plain textured FBX, no MetaHuman) in an
**arms-overhead, open-mouth "goal celebration" shout**, cleanly, **inside Unreal**.
Pose authored in Blender + baked to a 2-frame FBX anim (the in-engine euler Control Rig can't lift arms fully overhead).

## The core problem
Applying the Blender-baked anim via an `AnimationSingleNode` component made the mesh render **zero pixels** —
no silhouette — even though the actor was present, in-frustum, and reported **valid ~160 cm bounds**.
Remove the anim → renders perfectly. So the *animation* destroyed the render.

> **"Valid bounds + zero pixels = broken skinning."** Bounds come from bone *positions* (stay sane);
> the skin matrices (pose × inverse-bind) deform the verts and can collapse the mesh to a degenerate blob
> while bounds still read full size. It is never a hidden/missing actor.

## Root cause — BIND-POSE mismatch (not scale)
- `SK_Sherry` was imported from the **original Daz** `Sherry.fbx` → carries the **Daz bind pose**.
- The anim was authored in **Blender**, which **re-derives** the armature rest pose on import + apply-transform.
- A **Blender-bind** anim on a **Daz-bind** mesh → skin matrices explode → invisible.
- **Proof (the A/B test that cracked it):** the identical anim is invisible on `SK_Sherry` but renders a clean,
  correctly-scaled arms-up figure on a mesh **re-imported from the same Blender FBX**.

**Fix in one line:** apply the Blender anim only to a mesh imported from the *same* Blender FBX.
Re-import the character standalone; never retarget the Blender anim onto the original Daz-imported mesh.

---

## AVOID (false leads that burned the most time)
- **Don't assume it's purely scale.** Scale *was* also wrong (Blender bind at meter scale, hip ≈ 0.87;
  UE reads coords literally for anim-on-existing-skeleton → collapses to a ~1.6 cm blob). But fixing scale
  alone only turned "invisible" into "tiny collapsed blob." The root was the bind mismatch. Chasing scale first cost the most.
- **Don't use FBX `global_scale` / unit tricks.** Blender dumps `global_scale` into `UnitScaleFactor`
  (saw it become 10000) or, with `FBX_SCALE_NONE`, leaves coords untouched — neither reliably changes what UE reads. Unpredictable collapse.
- **Don't manually multiply verts / edit-bones / fcurves ×100.** It makes coords literally 87 cm but
  **breaks the mesh** (invisible even in ref pose) and desyncs the anim.
- **Don't import a huge / heavily-edited FBX on a loaded editor.** A ×100-scaled *full* FBX import
  **hung the game thread ~13 min** ("Loading FBX Scene", MCP dead) → forced restart → lost unsaved studio.
  The clean 42 MB rename-only full mesh imports fine (~4 min).
- **Don't trust the thumbnail renderer for scale.** It auto-frames, so a collapsed/tiny mesh still fills the
  frame and looks fine. Good for a reliable pose sanity-check, useless for scale.
- **Don't use auto-exposure for stills.** Auto-histogram flickers frame-to-frame. Use **manual** exposure on an unbound PPV.
- **Don't expect MCP-added lights to illuminate.** Only the level's own saved lights work → re-aim the existing sun.
- **Don't inherit raw Daz materials by accident.** A fresh standalone import lands with flat DefaultLit
  "plastic" skin + opaque white eyes → looks washed-out. Carry the fixed materials over (step 4).

## The recipe that worked
1. **Blender headless re-export, rename only — no scaling.** Load pose FBX; rename Blender-dup bones
   `X.001`→`X_001` (and patch matching action fcurve data-paths); keep all meshes; export:
   ```python
   bpy.ops.export_scene.fbx(
       filepath=DST, use_selection=False,
       global_scale=1.0, apply_unit_scale=False, apply_scale_options='FBX_SCALE_NONE',
       add_leaf_bones=False, bake_anim=True, bake_anim_use_all_bones=True,
       primary_bone_axis='Y', secondary_bone_axis='X',
       object_types={'ARMATURE','MESH'}, mesh_smooth_type='FACE')
   ```
2. **Import STANDALONE** (no target skeleton) with `import_materials=True, import_textures=True, import_animations=True`
   → complete character + own `_Skeleton` + `_Anim`, all sharing the Blender bind. (Times out the MCP call but
   completes; watch project log for "Waiting for skinned assets".)
3. **Spawn & apply its own anim.** Actor at origin, yaw 180 (faces −Y camera); component
   `animationMode=AnimationSingleNode`, `animationData.animToPlay=<the _Anim>`. Poses live, no PIE.
4. **Carry over fixed materials** (slot names match — same character): skin `Head/Body/Arms/Legs` (MSM_Subsurface);
   `Eye_Left/Eye_Right`; translucent "clear moisture" on `EyeMoisture_Left/Right` + `Tear`; `Mouth/Teeth/Mouth_Cavity`.
5. **Fix eyes (UE FBX eye-bone quirk).** Eyes render rolled-up (sclera only) in UE though the Blender render shows
   them forward — `l_eye`/`r_eye` local rotation doesn't survive the round-trip (`primary_bone_axis='Y'` remap).
   Cheap fix: headless Blender → **delete `l_eye`/`r_eye` rotation fcurves** (revert to rest = forward vs head) →
   export light **body-only** FBX (~2.8 MB) → import **onto the existing standalone skeleton** → swap actor `animToPlay`.
6. **Studio & lighting.** Throttle off (`EditorPerformanceSettings.bThrottleCPUWhenNotForeground=false`);
   re-aim the level's existing atmosphere sun to front-light (she faces −Y → aim toward +Y, yaw ≈ 82–90, pitch ≈ −32);
   unbound PPV manual exposure `AEM_Manual`, bias ≈ −3.5 to −4.3.
7. **Capture (WP level).** Move the editor viewport camera to the shot **first** (streams WP cells, else black);
   capture over HTTP (curl → `127.0.0.1:8000/mcp`, `CaptureViewport` + `captureTransform`), decode SSE `data:` lines.
8. **Post-process.** The red "CachedLightingPreExposure clipped" warning (appears at exposure ≳ 12) and the orange
   cyclorama-box wireframe both cross her raised arms → can't crop out. In PowerShell `System.Drawing`:
   **interpolate across those thin horizontal bands** (locate via red/orange pixel scan), then **crop inside the box
   side-edges** to a waist-up frame (drops floor line, feet-sprite, gizmo, flag).

## Capture gotcha table
| Symptom | Cause / fix |
|---|---|
| Black off-screen capture | Editor throttle → `bThrottleCPUWhenNotForeground=false`; move editor camera to shot (WP streaming) |
| Character a dark silhouette | Back-lit → re-aim sun to travel toward her front (+Y) |
| Exposure blows/crushes between shots | Auto-histogram unstable → manual exposure |
| Red "Exposure NN clipped" text over subject | Lumen overlay, not MCP-removable → inpaint the band in post |
| Orange box framing the studio | Cyclorama wireframe → crop inside edges / inpaint top edge |
| Bulb/gear/flag icons | Editor sprites → hide each actor's `.Sprite`+`.BillboardComponent_0` (bVisible=false) or crop |
| Editor hangs on FBX import | Too-heavy/over-edited FBX → keep light; restart if game thread spins with no log progress |

## Skin & lighting tuning (applied — fixes the "too light / too bright" pass)
The fresh import + subsurface fix renders the skin **lighter than Blender EEVEE**. Uniformly dimming lights/exposure
does NOT help — it darkens skin AND backdrop equally, so the skin stays "as light relative to the backdrop." The skin
albedo itself must come down. What worked:
- **Darken skin albedo** on the 4 skin materials (`Head/Body/Arms/Legs`, shared `/Game/SherryFixed/`): insert a
  `MaterialExpressionMultiply` between the base-color `TextureSample_0` (RGB) and `MP_BaseColor`, `ConstB = 0.6`
  (batched via `ProgrammaticToolset.execute_tool_script`).
- **Deepen the subsurface** glow that was lightening the skin: the `Constant3Vector_0` on `MP_SubsurfaceColor` was a
  bright reddish `{0.85, 0.38, 0.32}` → set to `{0.34, 0.15, 0.12}`.
- **Dim the studio** so the backdrop reads mid-grey not blown white: sun ≈ 0.85, both skylights ≈ 0.15–0.22,
  PPV manual `autoExposureBias ≈ -5.5`. (Note: the on-screen "Exposure NN" number rises as you lower the bias — ignore it, judge by eye.)

(Skin material edits are on the shared `/Game/SherryFixed/` materials, so they also darken `SK_Sherry` — intended, same character.)

## Remaining
- Clean hero framing is **waist-up**; full-body reintroduces the floor line, feet-sprite, and more box wireframe.
- Faint interpolation remnants at the top crop corners (where the box edge met the side walls) — crop tighter if it bothers.

## One-line takeaways
- Invisible mesh + valid bounds = **broken skinning** (bind mismatch or degenerate scale), never a hidden actor.
- A **Blender-authored anim belongs on a Blender-imported mesh** — never on the original Daz-imported skeleton.
- **Don't fight FBX units** — export clean (rename dupes, no manual scaling), let UE read coords as-is.
- **Keep FBX imports light** to avoid game-thread hangs. Assets survive restarts; unsaved level/studio state does not.
- **Manual exposure + re-aim existing sun + camera-first WP streaming + post-process overlays** = repeatable clean still.
- **Fix eyes by deleting eye-bone tracks**; always re-carry the fixed subsurface/eye materials after a fresh import.
- Watch VRAM: after many imports the editor logged "Video memory exhausted (~106 MB over budget)" — restart before it gets flaky.
