# Daz G9 → Unreal: Character-Shot Pipeline & Lessons

Non-MetaHuman pipeline. Daz Genesis 9 FBX → Unreal Engine 5.8 (unreal-mcp bridge).
Covers **realistic G9** (Sherry, Mimi, **Guardsman**) and **G9 Toon** (Amy) figures,
plus **HYBRID** figures (**Kyle** — realistic skin + toon anime hair).
Companion to `sherry_celebration_pipeline.html` (same content, styled + images embedded).
**Toolbox: `daztools/`** (durable, beside this doc) — `fbxstruct.py` (skeleton roots / dup bones /
skin status — **run this on every new FBX before importing**), `fbxmat.py` (Daz surface values →
`daz_materials.json`), `cap.sh` + `parse2.py` (viewport capture over MCP HTTP).

**Delivered shots:** `Sherry_Celebration_UE.png` (Blender path, legacy) ·
`Mimi_Celebration_NoBlender.png` (in-engine, 256×256 thumbnail proof) ·
`Amy_Celebration_UE.png` + `Amy_Celebration_Closeup.png` (in-engine, three-point studio, Daz skintone) ·
`Guardsman_Fight_UE.png` + `Guardsman_Fight_Closeup.png` (in-engine, **realistic G9 male, combat stance
with closed fists** — 58-control rig incl. every finger) ·
`Kyle_Happy_UE.png` + `Kyle_Happy_Closeup.png` (in-engine, **hybrid G9 male, happy hands-on-hips** —
64-control rig, two-bone elbow solve, bone-only smile).
**Studio set:** `/Game/studioset` (floor + backdrop + key/fill/rim + softbox + PPV + `Studio_CineCam`).

### The studio set (soft-light rig, calibrated)
Subject at `(0,1000,0)` facing **+Y**; camera at **+Y looking −Y**; backdrop at **−Y behind her**.
Floor = `/Engine/BasicShapes/Cube` @ `(0,1000,-5)` scale `(14,14,0.1)`; backdrop = same @ `(0,640,250)`
scale `(14,0.1,5)`. Dim the env: DirectionalLight **0.15**, SkyLight **0.40**, hide `VolumetricCloud`.
- **KEY** 760cd / 4700K / **sourceRadius 60 + softSourceRadius 45** ← the source SIZE is what softens the
  shadow; a point-sized light gives a razor edge. **Only shadow caster.**
- **FILL** 210cd / 6300K **castShadows:False** · **RIM** 3600cd / 7600K **castShadows:False**
  (killing their shadows removes the 2nd + 3rd backdrop shadows outright).
- **SOFTBOX** `/Script/Engine.RectLight` @ `(0,1330,190)`, `sourceWidth 320` × `sourceHeight 260`, 120cd,
  5600K, castShadows:False — an area source is inherently soft.
- **Exposure = unbound PPV, clamp `AutoExposureMin == MaxBrightness`.** Higher N = DARKER.
  **NOT `autoExposureBias`** — that's the wrong knob and cost real time.
  Per-subject: **Amy (pale toon) 6.1–7.0 · Guardsman (male in dark leather) `N = 5.8`.**
  Measured sweep (sample the pixels; the law is counter-intuitive — **higher N = darker AND warmer**):

  | N | face RGB | warmth R−B | armour | backdrop |
  |---|---|---|---|---|
  | 4.2 | (242,212,194) | 48 | (115,99,88) | 185 — blown |
  | **5.8** | — | — | — | **mid-grey ✓ shipped** |
  | 5.2 | (229,186,162) | 67 | (80,67,59) | 147 |
  | 7.2 | (172,112,87) | 85 | (32,25,21) — crushed | 70 — too dark |

  🔴 **The field names are camelCase**: `Settings.autoExposureMinBrightness` / `autoExposureMaxBrightness`.
  The PascalCase `AutoExposureMinBrightness` you see in the dump is only the `bOverride_` flag — regexing
  for it returns `true`, not a number, and looks like the value is missing.
- Key:fill ≈ **3.6:1** keeps form; ~1.8:1 reads flat.
- Aim lights with `ActorTools.look_at(spot, target)`; hide each light's `BillboardComponent_0`/`ArrowComponent0`.
- 🔴 **MCP-added lights DO illuminate.** The old "unsolved blocker" note was wrong — a dark scene's
  auto-exposure was blowing them out. Lock exposure first, then the lights behave.

> ## ⚠️ SUPERSEDED 2026-07-16 — Blender is NOT necessary. See "Blender-free path" below.
> The Blender round-trip (§"The recipe that worked") shipped Sherry, but it was solving
> problems it created itself. Re-tested on **Mimi** (`/Game/MimiTest/SK_Mimi`, Daz G9):
> the identical arms-overhead open-mouth shout was authored **entirely in-engine**.
> Proof: `D:\mydata\3dassets\Mimi_Celebration_NoBlender.png`.
> Keep the sections below for the *capture/lighting/material* lessons, which still apply.
> The **posing** half is obsolete.

**Result (Blender path):** `D:\mydata\3dassets\Sherry_Celebration_UE.png` (arms-overhead open-mouth shout, textured, eyes forward).
**Blender EEVEE reference (same pose):** `D:\mydata\3dassets\Sherry_Celebration.png`.
**Reusable UE assets:** `/Game/CelebFull/` (SherryCelebFull mesh + SherryEyeFix_Anim + _Skeleton).

---

## HYBRID G9 (Kyle) — 2026-07-16. Hands-on-hips + a bone-only smile. Cheapest pass yet
Validated on `kyle.fbx` (230.3 MB, G9 male: **realistic Masculine_01 skin + Amy's TOON anime hair**).
Delivered `Kyle_Happy_UE.png` + `Kyle_Happy_Closeup.png`. **Zero new traps bit.** The pre-flight
(1 skeleton root, 0 dup bones, skin textures assigned) was accurate and the import was clean first try:
`SK_Kyle`, 153 bones, 136,656 verts, **0 morph targets**, 31 material slots.
Total: one import, one material pass, a 64-control rig, one pose solve. No Daz round-trip, no restart.

### ✅ What the hybrid actually cost — only §9 Trap 1, and only 3 slots
A hybrid is **not** the sum of both figures' problems. Kyle's toon content was *only* the hair:
- `G9AnimeHair_ToonOutline` is the single unskinned mesh → it arrives as exactly **3 `_ncl1_1` slots**
  (`Scalp_ncl1_1`, `BaseHair_ncl1_1`, `TopHair_ncl1_1`), not Amy's 22. Mask them
  (`BLEND_Masked` + `Constant(0)→MP_OpacityMask`) and the toon problem is over.
- **Slot-name arithmetic identifies the outline set instantly:** 31 slots = 28 real + 3 `_ncl1_1`.
  The `_ncl1_1` suffix maps 1:1 onto the outline mesh's material count. Count first, don't hunt.
- Everything else (skin, eyes, brows, clothing) behaved as a plain realistic G9.

### 🔴 Trap C did NOT bite — and the reason is worth knowing (it inverts the Guardsman rule)
Guardsman's white beard came from the exporter writing a *transparency* map into the FBX diffuse slot
for materials with **no diffuse image**. Kyle has the same set-up (`Scalp`, `Eyebrows_Primary/Secondary`
have Daz diffuse colours but no diffuse image) — and the exporter did **not** do it here:
- Those materials imported as **`MaterialExpressionVectorParameter` = the exact Daz diffuse**
  (`Scalp` = `[0.2235, 0.0902, 0.051]`, `Eyebrows_Primary` = `[0.149, 0.1137, 0.098]` — matching
  `fbxmat.py` to 4 dp). A flat colour node, no texture. **That is already correct — leave it alone.**
- `MAHLineMask.tif` / `MAHLineMaskBase.tif` *were* wired to `MP_BaseColor`, but **only on the two
  outline slots** (`BaseHair_ncl1_1`, `TopHair_ncl1_1`) — which get masked out anyway. Harmless.
- 🔴 **So the real diagnostic is the NODE TYPE, not the texture name.** One `get_property_input`
  sweep over every slot answers it in one call:
  **`VectorParameter` ⇒ no texture existed ⇒ nothing to fix.  `TextureSample` named `*tr*`/`*LineMask*`/`*_O`
  ⇒ Trap C ⇒ replace with `Constant3Vector(<Daz diffuse>)`.** Don't pre-emptively "fix" Trap C from the
  Daz colours alone — check what UE actually built. I nearly rewired 6 correct materials.
- ⚠️ `ObjectTools.get_properties(expr, ["Texture"])` **raises** on a `VectorParameter`, and the error
  escapes a `try/except` in the script sandbox (it is collected and re-raised at the end, killing the
  whole script). **Branch on the node class first** — parse `refPath.split(":")[-1]` — then read
  `Texture` only for `TextureSample`, `DefaultValue` only for `VectorParameter`.

### 🔴 Don't trust the brief's guess about wardrobe brightness — SAMPLE THE TEXTURE
The session brief said "Kyle wears a LIGHT shirt/shorts, so he will need a HIGHER exposure N."
Both textures average **RGB (17,17,17) — near-black**. `G9SE_Shirt_ES6_BaseColor.jpg` and
`G9SE_Shorts_ES6_BaseColor.jpg` are 2048² and essentially black. **Guardsman's `N = 5.8` was already
correct and needed no sweep at all** — a 20-minute exposure sweep avoided by one 5-line PowerShell
`System.Drawing` pixel average over the `.images` sidecar. Do this *before* touching the PPV.

### ✅ Toon ANIME hair is SOLID geometry — no opacity masks, no TR maps
Amy's/Kyle's `G9AnimeHair` is modelled solid (a helmet), unlike Guardsman's Toulouse hair *cards*.
- Tell: the hair diffuse maps are **`.jpg`** (`MAHBaseMidBrown`, `MAHTopMidBrown`) — a JPG has no alpha,
  so there is nothing to cut out. Card-based hair always ships `.tif`/`.png` TR maps.
- ⇒ **Skip §11 Trap D's `BLEND_Masked` + `TwoSided` + TR-map wiring entirely.** Only the
  `MP_Specular 0.02` / `MP_Roughness 0.85` half applies (still needed — the 3600 cd rim light
  blows out solid hair just as happily as cards).
- The whole "which TR map goes on which hair slot" problem simply does not exist for anime hair.

### 🔴 HANDS ON HIPS — solve the elbow, don't aim it
Aiming upperarm/forearm at hand-picked directions cannot put the wrist on the hip; the wrist is a
*position* constraint, so it needs a **two-bone (analytic IK) solve**. This is a genuine addition to
§3's aim-only recipe, and it is ~15 lines:
```
S = p[upperarm]; a = |p[forearm]-p[upperarm]|; b = |p[hand]-p[forearm]|
W = p[hip] + (±16.0, -3.5, 6.6)          # the iliac crest, in the POSED hip frame
d = |W-S|; u = (W-S)/d
x0 = (a²-b²+d²)/(2d);  r = sqrt(a²-x0²);  C = S + x0*u
pole = (±0.95, -0.31, 0.05)              # elbow flares OUT (mostly) and BACK
E = C + r * normalize(pole - u*(pole·u)) # project the pole into the circle plane
aim(upperarm, forearm, normalize(E-S));  aim(forearm, hand, normalize(W-p[forearm]))
```
- **The two aims then place the wrist EXACTLY** — measured error **0.0000 cm** on both arms. The
  elbow interior angle falls out at **76.2°**, which is anatomically right for hands-on-hips (a
  ~104° bend). Never eyeball this: the doc's own rule.
- 🔴 **The pole vector is the whole look, and my first guess was wrong.** `(0.78, -0.62, 0.08)` sent
  the elbows *backward* (`E = (±32.9, -17.8, 116.3)`) and from a front-on camera they vanished behind
  the torso — the shot lost the classic triangle silhouette entirely. **`(0.95, -0.31, 0.05)` →
  `E = (±36.2, -11.3, 117.6)`** and the triangles read. **Hands-on-hips is a SILHOUETTE pose: flare
  the elbows mostly ±X (lateral), only slightly −Y.** Judge it from the shooting camera, not in 3D.
- Define `W` **relative to the posed `p[hip]`**, not in world space, so it tracks the spine lean.
- Wrist at `hip + (±16.0, −3.5, 6.6)` = `(±16.0, −2.4, 102.9)` sits correctly on the waist/crest for a
  ~172 cm G9 male. Hip bone is at `z≈96.3`; ±16 cm clears the body surface.

### Hands-on-hips fingers: a WRAP, not a fist
Reuse §11's fist recipe with the curl angles dialled right down:
- **`35°/40°/25°`** (vs the fist's 88/100/72) → `mid3→wrist` **16.88 cm (rest) → 14.68 cm**. A fist is
  ~7.6. That gap *is* the difference between "hand resting on hip" and "punching his own hip".
- The empirical sign search again chose **−1 left / +1 right** — mirrored, the free correctness check.
  `knuckle_axis · fingerDir = −0.243` (≈76°, near-⊥) ✓ so one fixed global axis works per hand.
- **Thumb: AIM it backward, never curl it** — `aim(thumb1, thumb2, →(∓0.30, −0.86, −0.41))`,
  `aim(thumb2, thumb3, →(∓0.24, −0.90, −0.36))`. Thumb behind + fingers forward = gripping the crest.
- ⚠️ **`aim()` does not constrain hand ROLL about the finger axis** — it applies the minimal rotation,
  so the palm inherits whatever roll the arm solve produced. It happened to land palm-to-hip here and
  needed no correction. If a future hand lands palm-out, roll it about `normalize(p[mid1]-p[hand])`
  (that axis leaves the finger direction invariant) rather than re-aiming.

### 🔴 A HAPPY face from bones: TRANSLATE the face bones, don't just rotate them
Guardsman's furrow used pure rotation. For a smile that is **too weak** — a rotation about a leaf
bone's own origin moves the skin around it by almost nothing (an 8° twist over a ~2 cm cluster ≈ 0.3 cm).
Because we key **absolute world transforms**, we can simply **move** the bone, which translates its whole
skin cluster. Daz face rigs are built for exactly this. What shipped (+Y-facing, `dz`-grounded):

| bone | translate (x,y,z) | rotate |
|---|---|---|
| l/r `lipcorner` | `(±0.60, −0.35, +1.05)` up+back+out | `Rx(+10)` |
| l/r `cheeklower` | `(±0.22, +0.15, +0.80)` **raised** | `Rx(+7)` |
| l/r `squint` | `(∓0.10, +0.08, +0.34)` | `Rx(+5)` |
| l/r `browinner` / `browouter` / `centerbrow` | `(0,0,+0.42/+0.34/+0.36)` | `Rx(+8/+7/+8)` |
| `lowerjaw` | — | `Rx(−2)` |

- **Cheeks raised is non-negotiable** — lip corners alone read as a fake/pasted-on smile (Duchenne).
- **Brows `Rx(+8)` is the exact opposite sign of Guardsman's furrow `Rx(−16)`.** Same axis, same figure
  family; the sign *is* the emotion.
- 🔴 **Jaw `Rx(−4)` read as GRITTED TEETH; `Rx(−2)` reads as a warm smile.** A 2° difference flipped the
  expression from grimace to genuine. Shoot the close-up and look — this is not computable.
- **Sanity check numbers, not vibes:** posed `lipcorner` z **rose 1.05 cm** vs rest, and `l_eye`
  z=162.7 stayed above `head` z=156.4 ✓.
- ⚠️ **The Guardsman check "eye y forward of chin y" does NOT generalise.** On Kyle the chin is forward
  of the eyes *at rest* (`chin` y=9.15 vs `l_eye` y=8.05) — it is facial anatomy, not a pose error.
  **Compare posed-vs-rest for the same figure; never port a landmark threshold between figures.**

### Confident stance: the head must counter the spine (again)
Chest open = spine leans **back** `Rx(+1.0/+1.5/+1.0/+0.5)` = **+4° total**; the head inherits all of it,
so `neck1 Rx(−2)`, `neck2 Rx(−1.5)`, `head Rx(−0.5)` = **−4** → **net 0° = chin level** ✓.
(Guardsman leaned −16 and countered +10 for a net −6 chin-tuck; same arithmetic, opposite sign.)
Shoulders back+down: `aim(shoulder, upperarm, →(±0.972, −0.16, −0.17))` — **no +Z shrug**.
First attempt used +6° of spine lean; it shifted the head back ~4 cm and read as leaning away. **4° is
the ceiling for "chest open" before it becomes "leaning back."**

### ✅ The viewport is FULL 1857×825 with the pose live — the docked-Sequencer shrink is not inevitable
Amy and Guardsman shipped from a letterboxed **1422×527** because the docked Sequencer panel shrank the
viewport. This session's captures came back at the **full 1857×825** (content letterboxed 3:2 to
`x≈310..1547`) **with the Control Rig pose live and correct**.
- 🔴 **So "viewport grew to 1857×825" is NOT a reliable tell that the pose reverted to A-pose** (§10
  claims it is). Kyle rendered at full size *and* posed. **Verify a suspected revert by reading
  `get_euler_transform` back, or just look at the frame — never by the viewport size.**
- Practical win: ~2.4× the pixels, so crops are much less starved. Final hero `470×794`,
  close-up `400×530`, both straight viewport grabs + a `System.Drawing` crop.

### Kyle geometry facts (verified, not assumed)
- **Faces +Y, his left = +X** — `l_eye` y=+8.05 / `chin` y=+9.15 forward of `head` y=−0.59;
  `l_ear` y=−0.11 behind; `l_eye` x=+3.12 vs `r_eye` x=−3.12. Signs carry over from Amy/Mimi/Guardsman.
- **Rest-rotation histogram: all 153 bones = `(pitch 0, yaw 0, roll 90)`** → aim math licensed.
- ~172 cm (`head` z=156.4, brow z=164.8). `hip` z=96.2. Arm: upperarm **24.8 cm**, forearm **26.6 cm**.
- The last 9 "bones" are mesh-node transforms (`Genesis9_Shape`, `G9BaseShirt_Shape`, …). Never pose them.
- The unskinned `G9AnimeHair_ToonOutline` contributes **no bone** — 10 mesh nodes but only 9 `_Shape` bones.

### Kyle: the working call sequence (the §10 four-call rule held, with one refinement)
1. `create` + `import_bones_from_asset` + `add_event_node` + 64× (`add_control` + force scale 1 +
   Get/SetTransform + `connect_pins`) → `save_assets`. **Chunk it ~22 controls per call** (a 64-control
   build times the MCP call out; three chunks each completed).
2. `create_level_sequence` → `open_sequence` → `add_actors` → `find_or_create_track`.
3. **Dump the rest pose and run the math OUTSIDE the sandbox.** Two `get_global_transform` sweeps
   (72 + 81 bones) + one `get_bone_parent` sweep → plain JSON → **solve in local Python**. Better than
   §5's in-sandbox math: no module limits, and you can `assert` the R0 round-trip and print a report.
4. `open_sequence` → `set_playhead_frame(0)` → 64× `set_euler_transform` **from a literal table** →
   `force_evaluate`. **`keyed: 64` again proved nothing** — the readback is what proved it.
- ⚠️ **An MCP timeout is NOT a failure.** The material batch, the chunk-3 rig build and the verification
  sweep all returned `Request timed out` and had **all** completed. **Always re-query state before
  redoing the work** — re-running a build blindly would have created 20 duplicate controls.
- 🔴 **`describe_toolset` on `ControlRigTools`/`SequencerTools` blows the token limit.** It spills to a
  file; `python -c "import json; ..."` over that file to pull just the schemas you need. Cheaper than
  paging it.

---

## Realistic G9 MALE (Guardsman) — 2026-07-16. Four NEW traps, all upstream of the rig
Validated on `guardsman.fbx` (G9 male, Viking leather armour + Toulouse hair + Mavick beard).
Delivered `Guardsman_Fight_UE.png` + `Guardsman_Fight_Closeup.png`. **The posing math below (§Blender-free
path) needed no changes at all** — every problem this figure had was in the *export* or the *materials*.
Counting meshes and skins is NOT enough to call an FBX clean: `guardsman.fbx` was "15 meshes, 15/15 skinned,
0 ToonOutline, 0 `_ncl1_1`" and was still unusable. **Count skeleton ROOTS.**

### 🔴 Trap A — 15 PRIVATE SKELETONS (Daz "Merge Clothing into Figure Skeleton" = OFF)
The first `guardsman.fbx` gave every mesh node **its own full copy of the G9 skeleton**. UE saw 15 unrelated
hierarchies, **shattered the character into 7 SkeletalMeshes with 7 Skeletons**, and suffix-renamed the
clashes (`hip`→`hip455`, `head`→`head445`). One Control Rig cannot pose parts that don't share a skeleton.

| | `amy.fbx` (poses fine) | `guardsman.fbx` BEFORE | AFTER re-export |
|---|---|---|---|
| skeleton roots (`hip`) | **1** | **15** | **1** |
| `Model/Root` nodes | 2 | 15 | 1 |
| LimbNode bones | 151 | 612 | 147 |
| bone names duplicated | 0 | **118** | 4 (harmless) |

- **Diagnose in 10 s, before importing:** `daztools/fbxstruct.py <file.fbx>` — a binary-FBX walker that
  reports object counts, **skeleton roots**, the duplicate-bone-name histogram, and per-mesh skin status.
  Run it on EVERY new Daz FBX. It is far cheaper than a 4-minute import that then has to be undone.
- **FIX: re-export from Daz with `Merge Clothing into Figure Skeleton` = ON.** Ray flipped it and the file
  went 15 roots → 1. **Unlike the toon-outline case (§Trap 1), this dialog option DOES work — do not
  conflate the two.** The residual 4 dupes (`l/r_toes`, `l/r_metatarsal` ×2, contributed by the boots) live
  inside the single hierarchy, get suffix-renamed on import (`l_toes1`, `r_toes3`…) and are harmless — a
  fighting stance never touches toes.
- ⚠️ **A Daz re-export can be byte-identical.** The 13:17 export was *exactly* 190,762,176 bytes — same as
  the 12:15 one — i.e. the dialog change never reached the file. **Check the file SIZE changed** before
  re-importing; the working re-export was 189,771,152. (Same failure mode as the toon-outline exports.)
- ⚠️ **The shattered import names the merged asset after an arbitrary mesh node.** The body was NOT missing —
  it was inside `Genesis9Eyelashes_Shape` (398 bones, 318k verts, 22 slots incl. Head/Body/Arms/Legs).
  Don't conclude "the export lost the body" from the asset names; open them.

### 🔴 Trap B — the figure may have NO SKIN TEXTURES AT ALL (and the grey is not a tint)
`guardsman`'s 7 skin surfaces (`Head, Body, Arms, Legs, Fingernails, Toenails, Mouth_Cavity`) imported as a
flat `VectorParameter` = **0.4784 neutral grey**, no `TextureSample`. This is **not** a UE import bug and
**not** an exporter bug: the Daz scene has no skin preset applied. He is a G9 base figure wearing textured
armour over an untextured body.
- **§Trap 3's fix is UNDEFINED here.** `BaseColor = texture × Constant3Vector(DiffuseColor)` needs a texture.
  The `0.4784` grey **is the entire skin colour**, not a multiplier — multiplying nothing by it gives grey.
- **Per-figure, always check:** Amy's skin diffuse was a warm **tint** `[0.878, 0.737, 0.639]`;
  Guardsman's is neutral **grey** `[0.478, 0.478, 0.478]`. Neutral grey ⇒ suspect a missing skin preset.
- **Diagnose from the `.duf`** (gzipped JSON): read **`scene.materials`**, not `material_library` —
  the library holds only *base defaults with no images* and will show 0 images for EVERY material,
  including clothing that demonstrably has textures. (I misdiagnosed exactly this before re-parsing.)
  The tell: `diffuse image = None` on the skin surfaces while clothing/eyes/hair all resolve to real paths.
  Cross-check: the `.images`/`.fbm` sidecar folders contain no `*_Head_D_*` / `*_Body_D_*` maps.
- **FIX without any Daz round-trip:** G9 Starter Essentials ships base skins in the Daz library at
  `…/My DAZ 3D Library/Runtime/Textures/DAZ/Characters/Genesis9/Base/Masculine_01..04` (and
  `Feminine_01..04`) — `{Head,Body,Legs,Arms,Nails}_{D,NM,R,SSS}` at `1001/1002/1003/1004/1005`.
  **Same G9 UV layout**, so they map perfectly onto any G9 mesh. `TextureTools.import_file` them and wire
  D→BaseColor, NM→Normal (`SamplerType: SAMPLERTYPE_Normal`). Shipped with `Masculine_01`; swapping variant
  is a one-line change. (Nails has no `NM` map; eyelashes have no `_O` opacity map — don't assume the set.)
- Keep §Trap 3's skin shading verbatim — it still applies: `MSM_Subsurface`, `MP_Roughness 0.68`,
  `MP_Specular 0.10`, `Constant3Vector(0.62,0.24,0.18) → MP_SubsurfaceColor`.

### 🔴 Trap C — a TRANSPARENCY map wired as BaseColor → a WHITE BEARD
The beard (`Hair1`) rendered as a **white fuzzy mass**. Cause: its Daz material has **no diffuse image**, so
the exporter wrote the *transparency* map `MBtr` into the FBX's diffuse texture slot, and UE faithfully
wired that white-on-black mask to `MP_BaseColor`.
- **Tell:** a material whose BaseColor texture is named `*tr*` / `*TR*` / `*_O` / `*Opacity*`.
  Check with `get_property_input(MP_BaseColor)` → `get_properties(expr, ["Texture"])`.
- 🔴 **Check the NODE TYPE first — this trap is NOT implied by "no diffuse image"** (learned on Kyle,
  §Hybrid). Kyle's `Scalp`/`Eyebrows` have no diffuse image *and no Trap C*: they imported as a
  `VectorParameter` holding the exact Daz diffuse, which is already correct. Only a **`TextureSample`**
  named `*tr*`/`*LineMask*`/`*_O` is Trap C. A `VectorParameter` means the exporter wrote nothing —
  leave it alone. (`get_properties(expr,["Texture"])` also *raises* on a VectorParameter.)
- **FIX:** `MP_BaseColor = Constant3Vector(<the Daz diffuse from fbxmat.py>)` — for the beard
  `[0.2118, 0.1843, 0.1216]` — and keep the TR map where it belongs, on `MP_OpacityMask` (`BLEND_Masked`).

### 🔴 Trap D — white streaks on hair are SPECULAR BLOWOUT, not a broken opacity mask
Hair cards showed hard white edge streaks. It looks exactly like an alpha-mask artifact. It isn't.
- **The one-capture diagnostic (generalises §Trap 1's red-debug trick):** wire a distinct
  `Constant3Vector → MP_EmissiveColor` per suspect material (Hair=green, Strands=blue, Base=red,
  beard=yellow) and shoot once. Hair went green and the beard yellow — **the white streaks took NO debug
  colour at all**, which rules out every one of those materials (emissive *adds*; a blown highlight stays
  white). That leaves the lighting: the studio's **3600 cd rim light** blowing out glossy hair at grazing angles.
- **FIX:** hair/beard `MP_Specular 0.02`, `MP_Roughness 0.85`. Streaks gone. `BLEND_Masked` + `TwoSided`,
  opacity from the real TR maps (`SW_Toulouse_TR1`, `SW_ToulouseT_Base_TR`, `MBtr`, `OpacityCutout01_Thin`).
- Eye films (`EyeMoisture_Left/Right`, `Tear`) import as **opaque white** and sit over the iris →
  `BLEND_Translucent`, `MP_Opacity 0.06`, `MP_Roughness 0.05`, `MP_Specular 1.0`.

### Guardsman geometry facts (verified, not assumed)
- **Faces +Y, his left = +X** — same as Amy/Mimi, so every sign convention carries over unchanged.
  Proof: `l_eye` y=+7.52 and `chin` y=+8.47 are *forward* of `head` y=−0.63 / `l_ear` y=−0.23;
  `l_eye` x=+3.04 vs `r_eye` x=−3.04. **Still check per figure — Sherry faces −Y.**
- **Rest-rotation histogram: all 163 bones = `(0,0,90)`** (161 exact + 2 `-0.0` sign noise) → the aim math is licensed.
- A-pose arm `l_upperarm→l_forearm` = `(0.679, 0.022, −0.734)` — within a hair of Mimi's `(0.669, 0.021, −0.744)`.
- ~172 cm (head at z=157.7). 163 bones, 386,648 verts, **0 morph targets** → one rig poses body AND face.
- The last 15 "bones" are the mesh-node transforms (`Genesis9_Shape`, `ToulouseHR_Shape`, …). Never pose them.

---

## Daz TOON figures (Genesis 9 Toon) — the extra traps, and the fixes
Validated 2026-07-16 on **Amy** (`amy.fbx` / `amy2.fbx`, Daz G9 **Toon**, 162 bones, 159k verts, 0 morphs).
Delivered: `D:\mydata\3dassets\Amy_Celebration_UE.png` + `Amy_Celebration_Closeup.png`.
A toon figure is NOT just a realistic figure with flat textures — it ships **extra geometry and extra
materials that exist only for Iray/3Delight** and actively break in Unreal. All of it is fixable in-engine;
**none of it needs a Daz re-export** (proven — see the export-dialog note below).

### Trap 1 — TOON OUTLINE geometry (duplicate, unskinned, invisible until you pose)
`amy.fbx` has **14 mesh nodes but only 9 skin deformers**. The 5 without skin are Daz's toon outline meshes:
`Genesis9_ToonOutline`, `Bra_5382_ToonOutline`, `G9AnimeHair_ToonOutline`, `G9ToonMouth_ToonOutline`,
`Undies_002 UV_4046_ToonOutline` — inflated, flipped-normal copies rendered black to fake a cartoon edge.
- They are **not skinned**, so they **freeze in bind pose** while the real body poses → you get *two* bodies,
  one A-posed, one posed. **In the rest pose they coincide exactly, so the duplication is invisible.**
- They arrive as the **`_ncl1_1` material slots** (29 real + 22 outline = **51 slots**). The outline copy is
  the one you SEE (it's outside the real body) and it has **no textures** → this is the true cause of
  *"the skin renders dark grey/metallic"*. Do not chase textures; the outlines are the bug.
- **Diagnostic that cracks it in one capture:** assign an emissive-RED debug material to every `_ncl1_1`
  slot, pose the figure, and look — the red copy stays in A-pose, the real one raises its arms.
- **FIX:** assign a `BLEND_Masked` material with `Constant(0) → MP_OpacityMask` to all 22 `_ncl1_1` slots
  (+ `G9ToonEyeSocket_Eye_Socket`), then **re-spawn the actor**. Leave every skinned mesh alone.
- 🔴 **The Daz FBX export dialog CANNOT remove them — verified across 3 exports.** `Include Props = off`
  AND `Merge Followers = off` AND `Include Subdivision Data = off` all produced a byte-identical
  14-mesh/9-skinned/5-outline file. The Staging list DOES show them (`No Props | Prop | Genesis 9 Toon …
  105,283 vertices` = the body outline, ~4× the real body's 25,182) and they're written anyway. Only
  deleting the `*_ToonOutline` nodes in the Daz **Scene** tab would work — but the UE-side mask is easier.
  **Don't burn the user's time on the dialog.**

### Trap 2 — toon HELPER meshes (skinned, so they survive, and they render)
`G9ToonShadowPlane`, `G9ToonFloatingIris`, `G9ToonEyeSocket`, `Genesis9ToonBrowsPaint`, `G9ToonMouth`.
The **shadow plane** is the worst: a flat Iray-only plane that renders as a **maroon/pink slab smeared over
the torso and legs**. Mask slot `Shadow`.
- 🔴 **`Eye_Socket` is NOT a helper — it is the SCLERA. Do NOT mask it.** Its name reads like Iray scaffolding,
  but its Daz diffuse is `[0.851, 0.8392, 0.8196]` — **near-white**. Masking it leaves **black around the iris**
  (the inside of the eyeball showing through). I made exactly this mistake; Ray caught it in close-up.
  **Tell:** check the DiffuseColor before masking anything — near-white = it's visible anatomy, not a helper.
  Mask only `G9ToonEyeSocket_Eye_Socket` (diffuse `[0,0,0]` = the outline copy, correctly hidden).

### Trap 3 — the Daz SKINTONE is in the FBX; Unreal throws it away
UE imports each Daz material as **only** `TextureSample → BaseColor` and discards every other surface value.
Read straight out of `amy2.fbx` (`daztools/fbxmat.py`, a small binary-FBX reader; FBX 7400, 32-bit offsets),
every skin material carries:
```
DiffuseColor  [0.8784, 0.7373, 0.6392]   <- THE skin tint. Never applied by the importer.
Specular      [0.2, 0.2, 0.2]
Shininess     [20.0]
```
**That missing multiply is the skintone.** Without it skin renders grey; with it, warm:

| | avg RGB | warmth (R−B) |
|---|---|---|
| Daz albedo (texture × DiffuseColor) | (209,167,142) | 67 |
| Unreal as-imported | (161,148,146) | **15** ← grey |
| after the fix | (193,166,145) | **48** ← warm |

**FIX per material:** `BaseColor = TextureSample.RGB × Constant3Vector(DiffuseColor)`.
All 30 values dump to `daztools/daz_materials.json`.
- 🔴 **DO NOT convert Daz `Shininess` to roughness literally.** `sqrt(2/(20+2))` = **0.30**, which is a
  *glossy* surface — Ray's verdict on that render was *"plasticky, almost like a blow-up doll."* Daz's Phong
  shininess is not a PBR roughness and the naive conversion produces vinyl. **For skin use
  `MP_Roughness ≈ 0.68`, `MP_Specular ≈ 0.10`** (0.62 / 0.12 for hair + clothing), and set the material to
  **`shadingModel: MSM_Subsurface`** with a warm `Constant3Vector(0.62, 0.24, 0.18) → MP_SubsurfaceColor`.
  Subsurface is what makes skin read as flesh rather than plastic — matching the `MSM_Subsurface` fix the
  Sherry path also needed. Matte + SSS eats light, so **open the exposure clamp** afterwards (7.0 → ~6.1).
- ⚠️ **Exposure destroys the tint.** UE's tonemapper desaturates highlights toward white: at PPV clamp
  N=4.6 warmth collapsed to R−B=15; **N=7.0 → R−B=48**. **Lower exposure = warmer skin.** Counter-intuitive
  but measurable — sample the pixels, don't trust your eye.
- ⚠️ It will never hit 67: that's *albedo* vs a *lit render* through UE's tonemapper. Same class of gap as
  the documented "skin renders lighter in UE than Blender EEVEE" — not a bug.

### Trap 4 — alpha-cutout decals go solid-black when you rewire BaseColor
`Brow` (= `Genesis9ToonBrowsPaint`), `Eyelashes`, `Highlight_Upper/Lower` are **alpha-cutout decal meshes**
with black/white Daz diffuse. Applying Trap 3's fix without the alpha makes the whole quad opaque — a
**black bar across her eyes**. Only visible in close-up; the wide shot hid it.
**FIX:** set `BLEND_Masked` and wire `TextureSample.A → MP_OpacityMask` on those four.

### Toon-figure checklist (in order)
1. Import; check `get_material_slots` — **51 slots with `_ncl1_1` = toon outlines present**.
2. Mask the 22 `_ncl1_1` slots + `G9ToonEyeSocket_Eye_Socket` (OpacityMask=0).
3. Mask `Shadow` only - **NOT `Eye_Socket`** (that is the sclera; masking it blacks out the eyes).
4. Apply Daz `DiffuseColor` × texture to every material; add Specular/Roughness.
5. Fix alpha on `Brow` / `Eyelashes` / `Highlight_*` (BLEND_Masked + texture alpha).
6. **Re-spawn the actor** (materials don't refresh on a live actor).
7. Build the rig, then — **in a SEPARATE call** — the Sequencer track (see the CR/track warning below).

---

## The Blender-free path (2026-07-16, validated on Mimi)

### Why the old "Control Rig can't do dynamic poses" verdict was wrong
The prior conclusion — *"euler controls GIMBAL-cap: upperarm abduction saturates at ~horizontal;
you cannot reach overhead with pitch OR roll alone"* — is a **misdiagnosis**. Two facts kill it:

1. **Every Daz G9 bone shares one rest rotation.** Dumping all 167 bones of `SK_Mimi` gives a
   rotation histogram of exactly one entry: `{"0.0,0.0,90.0": 167}`. No bone carries a per-bone
   orientation; limb direction lives **only** in the child's position offset. Consequence: every
   bone's *local* rest rotation is identity, and the control frame is uniformly rolled 90° about X.
2. **So single-axis dialing moves the arm along a skewed axis, and never reaches overhead.** That
   reads exactly like a gimbal cap, but nothing is locked. The orientation is perfectly
   representable — you just have to *compute* the euler triple instead of nudging one channel.

**The proof:** aiming `l_upperarm` at the overhead direction lands on `[0.28, 0.0, 0.96]` — exact,
no saturation. The euler triple that produces it is **`(pitch 57.19, yaw -155.77, roll -79.52)`**.
Nobody finds that by hand. *That* was the real blocker: the method, not the rig.

### What dropping Blender deletes
Blender authored the aim, but it also **caused** three of the pipeline's worst problems. Remove it
and they cease to exist — they aren't "solved", they're gone:

| Old problem | Why it existed | Status without Blender |
|---|---|---|
| Invisible mesh / BIND-POSE mismatch (the multi-session mystery) | Blender re-derives the armature rest on import+apply | **Impossible.** The anim is authored on `SK_Mimi`'s own Daz-bind skeleton. |
| Eyes render rolled-up (sclera only) | `primary_bone_axis='Y'` remap on Blender FBX export | **Gone.** Eye bones are never touched or re-axised. |
| 42 MB re-import, ~4 min, hangs the game thread | Standalone re-import of the Blender mesh | **Gone.** The mesh is already in-engine; nothing is re-imported. |
| Raw Daz materials on the fresh import → re-carry all materials | Standalone import | **Gone.** Same asset, materials already correct. |

### The recipe (all over unreal-mcp; no external DCC)
1. **Import the Daz FBX once, standalone** → `SK_Mimi` + `SK_Mimi_Skeleton` (167 bones, 507k verts,
   `get_morph_target_names` → `[]`, so face is 100% bones — one rig poses body AND face).
2. **Read the rest pose.** `ControlRigTools.get_global_transform(item={Bone}, initial=True)` per bone.
   Confirm the single-rest-rotation histogram; that's the licence for the aim math below.
3. **Build the rig** (`ControlRigTools`): `create` → `import_bones_from_asset` →
   `add_event_node(FORWARD_SOLVE)`. Per posed bone B:
   `add_control(B_ctrl)` **with NO parent** → `RigUnit_GetTransform(Control B_ctrl, GlobalSpace)` →
   `RigUnit_SetTransform(Bone B, GlobalSpace, bPropagateToChildren=true)`; chain `ExecutePin`
   **parents-first**. Pin refPath is deterministic: `node.refPath + '.' + pinName`.
4. 🔴 **`add_control` with no parent creates the control with `scale = (0,0,0)`** — every space,
   initial and current. Left alone, `control_global = offset × value` has scale 0, the Set writes
   scale-0 bones, and **every posed bone collapses to zero pixels while the untouched ones render
   fine**. Fix immediately after creating each control:
   `set_global_transform(item={Control}, transform=identity+scale 1, initial=True)` **and** `initial=False`.
   (The old bone-parented rig never hit this — parenting to a bone copies the bone's rest transform, scale 1 included.)
5. **Compute the pose** (plain Python in `ProgrammaticToolset.execute_tool_script`; `math` is allowed).
   Simulate the skeleton: `p[b]` = rest global location, `q[b]` = `R0` for all b, where
   `R0 = quat(-0.7071, 0, 0, 0.7071)` (= UE Rotator `(0,0,90)`; a right-hand-rule **-90° about X**).
   - `rotate(b, R)`: for every bone in `subtree(b)`: `p[d] = p[b] + R·(p[d]-p[b])`; `q[d] = R ∘ q[d]`.
   - `aim(b, child, desired)`: `rotate(b, quat_from_to(p[child]-p[b], desired))` — aim by **limb
     direction** (bone-head → child-head), never by the bone's own axis. Same principle the Blender
     script used; G9 bones don't point along their limbs.
   - Order matters: **spine → shoulders → arms → neck/head/jaw**, so each aim sees post-parent positions.
6. **Convert `q` → UE Rotator** with UE's exact `FQuat`→`FRotator` formula (validate it round-trips
   `R0` ↔ `(0,0,90)`), then key each control **as an absolute world transform**:
   `SequencerControlRigTools.set_euler_transform(location=p[b], rotation=q2rot(q[b]), scale=1, frame=0)`.
   Unparented controls have identity offset, so the keyed value *is* the world transform — no offset math.
7. **Attach**: `SequencerTools.create_level_sequence` → `open_sequence` → `add_actors` →
   `SequencerControlRigTools.find_or_create_track(control_rig_asset_path=...)` → `set_playhead_frame(0)`
   → `force_evaluate()`. Pose is live in the level viewport, no PIE.
8. **(Optional) Bake to a standalone AnimSequence** — only needed if you want the pose without
   Sequencer driving it (e.g. `AnimationSingleNode` stills). `SequencerImportExportTools.export_fbx`
   → `SkeletalMeshTools.import_file(skeleton=SK_Mimi_Skeleton, import_animations=True)` →
   `MimiCeleb_Anim`. This FBX hop is **UE→UE**, so the bind still matches — it is *not* the old
   Blender round-trip. Skip it entirely for Sequencer/MRQ renders.

### Geometry facts worth keeping (per-figure — verify, don't assume)
- **Mimi faces +Y** (eyes/chin at +Y, hair braids at −Y); her left is +X. **Sherry faces −Y.**
  Facing genuinely differs per figure — always check `l_eye`/`chin` vs `head`, and hair vs face.
- Rest arms are an **A-pose**, ~48° below horizontal: `l_upperarm→l_forearm` = `(0.669, 0.021, -0.744)`.
- With face at +Y: **jaw open** = rotate `lowerjaw` about **+X by −25°**; **head up** / **brows up** =
  about **+X positive**; **spine lean-back** = about **+X positive**. (Signs flip for a −Y-facing figure.)
- Arms overhead V: upperarm → `(±0.28, 0, 0.96)`, forearm → `(±0.12, 0, 0.99)`; modest 15° shrug on
  the shoulder (`(±0.96, -0.07, 0.27)`) — anatomically right for overhead, and it did **not** distort.

### 🔴 FOUR separate tool calls: build rig → create track → compute pose → KEY
**Broader than previously documented (corrected on Guardsman 2026-07-16).** The old rule said "build the CR
in one call, the track in another". That is necessary but **not sufficient**. What actually happens is that
**Sequencer keys silently fail to persist if the same call also did heavy Control-Rig work** — and a
"successful" `keyed: 58` is returned either way. Two distinct failures, same symptom:

1. `create_level_sequence` + `find_or_create_track` + `set_euler_transform` in ONE call → keys land nowhere.
2. 163× `ControlRigTools.get_global_transform` (reading the rest pose) **then** keying in the same call →
   keys land nowhere. Touching the CR blueprint's hierarchy appears to reset the track's control values.

**Symptom either way:** every control evaluates at IDENTITY → `Set bone GlobalSpace = (0,0,0)` → the figure
collapses into a smear at his feet (hands on the floor, torso a hollow tube). It looks *exactly* like broken
skinning from a bad FBX — **it is not**. On Guardsman it produced a puddle, then (with one control keyed) a
vertical tube: head correctly at z≈154 with the whole body stretched to the origin.

**The working sequence — four calls, no exceptions:**
1. `create` → `import_bones_from_asset` → `add_event_node` → per bone `add_control` + force scale 1 +
   `RigUnit_GetTransform`/`RigUnit_SetTransform` + `connect_pins` → `save_assets`.
2. `create_level_sequence` → `open_sequence` → `add_actors` → `find_or_create_track`.
3. Read the rest pose + run the aim math → **return the 58-row `[ctrl, x,y,z, pitch,yaw,roll]` table**.
4. `open_sequence` → `set_playhead_frame(0)` → `set_euler_transform` per row **from a literal table**
   (no rig reads in this call) → `force_evaluate`.

🔴 **ALWAYS verify with a readback — never trust `keyed: N`:**
`SequencerControlRigTools.get_euler_transform(seq, crPath, ctrl, frame=0)`. Identity `(0,0,0)` = the keys
did not land. This is the *only* way to tell this apart from the scale-0 bug below.
- **Distinguishing the two collapse causes** (they look identical in the viewport):
  `get_controls_info` → type should be `EULER_TRANSFORM`, and `ControlRigTools.get_global_transform` on a
  control should show **scale 1**. On Guardsman both were correct, which *disproved* scale-0 and pointed at
  the keys. Don't "fix" scale-0 twice; read the state.
- **Re-spawning the actor is the reset** for bad anim/rig state (a bad AnimSequence leaves the mesh garbled
  even after clearing `animToPlay`).
- ⚠️ **The pose is live — closing Sequencer reverts it to A-pose.** Re-open + re-key to restore.
  🔴 **But the viewport SIZE is not the tell** (corrected on Kyle 2026-07-16): Kyle captured at the full
  **1857×825 with the pose live and correct**, so "the viewport grew to 1857×825" does **not** imply a
  revert. Confirm a suspected revert with a `get_euler_transform` readback, or just look at the frame.

### Combat stance / fists — the recipe (Guardsman, 2026-07-16)
58 controls: `hip`, `spine1-4`, `neck1-2`, `head`, `lowerjaw`, l/r `shoulder/upperarm/forearm/hand`,
l/r `thigh/shin/foot`, **all 30 finger bones**, 5 brow bones. Angles that shipped, for a +Y-facing figure:
- **Bladed stance:** `rotate(hip, Rz(+22°))` — +Z brings his left side toward the camera (orthodox lead).
- **Weight forward:** `spine1 Rx(−7)`, `spine2 Rx(−5)`, `spine3 Rx(−4)` (−X pitches toward +Y).
- 🔴 **The head must COUNTER the spine lean.** The spine's −16° is *inherited* by the head, so adding a
  −18° chin tuck on top pitched him ~−34° and he **stared at the floor**. Correct: `neck1 Rx(+4)`,
  `neck2 Rx(+3)`, `head Rx(+3)` → net ≈ −6° = chin down, eyes up through the brow. Plus `neck1 Rz(−14)`,
  `head Rz(−8)` to square the face back to camera against the bladed torso.
  **Sanity check the numbers, not the vibe:** posed `l_eye` z=159.6 must sit *above* `head` z=154.7, and
  eye y=20.6 *forward* of chin y=20.3.
- **Brows down/furrowed:** `browinner Rx(−16)`, `centerbrow Rx(−12)`, `browouter Rx(−7)`. Jaw `Rx(−2)`.
- **Guard:** `shoulder → (±0.95, 0.30, 0.02)` (**no +Z shrug — it reads hunched**);
  `upperarm → (±0.13, 0.22, −0.97)` (elbows down/in); `forearm → (∓0.22, 0.42, 0.88)` lead / `(0.30, 0.18, 0.94)` rear.
- **Stagger:** `l_thigh → (0.13, 0.26, −0.96)`, `r_thigh → (−0.14, −0.20, −0.97)`, shins counter-bent.
  Foot span 25.9 cm, stagger 13.4 cm.
- **Ground it:** after posing, `dz = rest_min_foot_z − posed_min_foot_z`, add `dz` to every `p[b]`.
  Cheap, exact, and avoids IK entirely.
- 🔴 **FISTS.** Curl axis = the **knuckle line** `p[pinky1] − p[index1]` (verify it's ⊥ the finger:
  `axis·fingerDir = −0.15` ✓). Rotating about it leaves the axis invariant, so **one fixed global axis works
  for all three phalanges**. **Pick the sign empirically** — snapshot `p`/`q`, try both, keep the one that
  minimises `mid3→wrist`. It correctly chose **−1 for the left hand and +1 for the right** (mirrored),
  which is a free correctness check. Angles **88°/100°/72°** → `mid3→wrist` **15.61 cm (rest) → 7.57 cm (fist)**.
  72/85/60 left a loose claw at 9.28 — *measure it, don't eyeball it*.
  Close the splay: rotate each `<finger>1` about the palm normal `cross(axis, fingerDir)` by −7/0/+5/+10°.
- 🔴 **Do NOT curl the thumb on the knuckle axis — it splays it outward** (shipped-looking fist with a
  thumbs-up sticking off it). **AIM it across instead:** `aim(thumb1, thumb2, →index2)`,
  `aim(thumb2, thumb3, →mid2)`. Check `thumb3→mid1 ≈ 4.15 cm`.

### 🔴 The CineCam blocks the shot and blurs it — check it before blaming anything else
Two things cost a confusing first capture on Guardsman, both trivial once seen:
- **The camera's own body is in frame.** `Studio_CineCam` sits at `(0,1182,152)` between a `+Y` viewport
  camera and the subject, and its editor proxy mesh renders as a big grey box **over the subject's head**.
  Hide `CameraProxyMeshComponent_0` **and** `DrawFrustumComponent_0` (`bVisible:false`) — or shoot from
  inside it. (§Capture gotcha table's "bulb/gear/flag sprites" rule generalises: the CineCam is a prop too.)
- 🔴 **`CaptureViewport` applies the CineCam's DoF**, and the saved cam had drifted to **35 mm focused at
  103 cm** (the doc's "85 mm / focus 178" is stale) → *everything* rendered soft and it reads like a broken
  render. **For working shots just turn DoF off:** `CameraComponent.FocusSettings.focusMethod = "Disable"`.
  Otherwise set `manualFocusDistance` to the real shooting distance.

### The CineCamera / true-portrait limit (unsolved over MCP)
`CaptureViewport` always renders the **level viewport camera at 90° FOV** — never a CineCameraActor's
focal length. Two escapes both fail over this bridge:
- **`SequencerTools.set_camera_cut_binding` is BROKEN** — `"call() takes at most 0 arguments (1 given)"`
  (same error logged in an earlier session). So you cannot lock the viewport to the cine camera.
- **No Movie Render Queue toolset exists** in the registry.

**What DOES work:** perspective compression is a function of **distance only**, not focal length — so
shooting the viewport from the correct 85mm distance and cropping to its framing is *geometrically identical*
to an 85mm lens. The catch is **resolution**: 85mm on 36×24 = 16.1° vertical vs the viewport's 40.7°, a 0.381
crop → a 1422×527 viewport yields only **134×201**. Unusable. With Sequencer docked (required, since it drives
the pose) there aren't enough pixels.
**Therefore:** a real 85mm portrait needs the UI — pilot/lock the CineCamera in the editor, or render the
sequence through MRQ by hand. A `Studio_CineCam` (85mm, f/2.8, 36×24 sensor, focus 178cm, at `(0,1182,152)`
= the correct portrait distance) is **already built and saved in `/Game/studioset`** and ready for either.
Viewport-grab close-ups carry visible wide-angle exaggeration — fine for review, not for final.

### 🔴 The black-capture blocker is VRAM EXHAUSTION — not World Partition
**This corrects a long-standing misattribution.** Every black `CaptureViewport` this session (in
`photobooth` **and** `ThirdPersonMap`) was the GPU evicting textures/shadow maps under VRAM pressure.
The engine says so on-screen, in red:

> `Video memory has been exhausted (127.051 MB over budget). Expect extremely poor performance.`

It is easy to miss because the warning text is **black-on-black in a black frame**. It only became
visible when the camera was aimed **up at the lit sky**. Diagnosis notes:
- **The sky rendering fine while everything else is black is the tell.** Sky/atmosphere is a pure
  shader with no streamed textures, so it survives eviction; terrain, characters and shadow maps don't.
- Cause this session: a 507k-vert Daz import + the duplicate mesh the FBX import creates, stacked on
  two already-resident MetaHumans (`BP_MH_Mimi`, `BP_MH_Sherry` are very heavy).
- **Relief without a restart:** `SceneTools.remove_from_scene` the MetaHuman actors + spare skeletal
  actors, and `AssetTools.delete` the duplicate `MimiCeleb` mesh the import made (you only need `_Anim`).
  That took it **127 MB → 50 MB → warning cleared**.
- ⚠️ **But clearing the warning did NOT restore the render** — once the RHI has thrashed, the viewport
  keeps producing low-frequency grey/dark mush at every exposure. **Restart the editor.** (`/Game/`
  assets survive; unsaved level state does not.) Do this *before* a shot, not after 200 tool calls.
- Ruled out as causes, with evidence: framing (`FocusOnActors` independently chose the exact camera
  already in use), actor presence (`GetVisibleActors` listed Mimi, the Landscape, all 3 DirectionalLights,
  SkyAtmosphere), and exposure (a manual-PPV bias sweep 0/4/8 changed brightness but never recovered detail).
- A `StartPIE(bSimulate)`/`StopPIE` cycle made it **worse**, not better. Don't reach for it.

### Verification trick: use the thumbnail renderer, not the viewport
`EditorAppToolset.CaptureAssetImage('/Game/MimiRig/MimiCeleb_Anim')` renders the baked pose at 256×256
with its own lighting and auto-framing. It is **level-independent and survives the VRAM/streaming mess
entirely** — it produced a clean lit textured render in the same editor where every viewport capture was
black. It also diagnosed the scale-0 collapse instantly: legs rendered in rest, everything hip-up
vanished — i.e. exactly the controlled bones. Useless for scale/lighting; ideal for "is the pose right".
- ⚠️ `ActorTools.get_actor_bounds` returns the **SkeletalMesh asset's static bounds**, not the animated
  ones (it echoed `x ±67.373, z −0.12..181.35` — byte-identical to the asset — while the pose was live).
  **Do not use it as a pose check.** This is a fresh trap: the old rule *"valid bounds + zero pixels =
  broken skinning"* assumed bounds track the pose. They don't.

### Remaining gaps (honest)
- **Eyes not verified.** At 256×256 the face is too small to confirm iris vs sclera. The Blender-era
  eye-roll cause (`primary_bone_axis` remap) is absent here, but that's reasoning, not a render.
- **No lit hero still of Mimi** to sit next to `Sherry_Celebration_UE.png` — the editor's VRAM was
  already thrashed by the time the pose was proven, and Ray opted to skip the restart. Not a pipeline
  limitation: the fix is known (restart, then shoot). Everything below in this doc (studio, exposure,
  overlays, post-process) is still the guidance for that half.
- The skin-albedo / subsurface tuning in §"Skin & lighting tuning" is Sherry-specific and would need
  redoing on Mimi's materials.
- **Do NOT save `photobooth.umap` in its current state** — this session removed `BP_MH_Mimi`,
  `BP_MH_Sherry` and two skeletal actors from it to free VRAM. Those removals are deliberately unsaved;
  a restart restores them. Saving the level would delete them for real.

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

## unreal-mcp API signatures that cost time (get these right first)
| Call | Gotcha |
|---|---|
| `ObjectTools.set_properties` | takes **`values` as a JSON *string***, not a `properties` dict. `{"instance":…, "values": json.dumps({...})}` |
| `ObjectTools.get_properties` | takes **`properties`** (a list) + **`instance`**. Asymmetric with the setter. |
| `ControlRigTools.set_pin_value` | requires **`graph`** as well as `pin`; omitting it fails for every value format and looks like a format problem. `Item` = `(Type=Control,Name="x_ctrl")`; `Space` already defaults to `GlobalSpace`. |
| `SceneTools.find_actors` | `name`, `tag`, `collision_channels` are all **required** (pass `""`,`""`,`[]`). |
| `ActorTools.get_actor_label` | errors on most actors — use `refPath.split(".")[-1]` instead. |
| `SequencerControlRigTools.get_controls_info` / `get_euler_transform` | need **`sequence`**; `get_euler_transform` returns a **JSON string**, not a dict — `json.loads` it. |
| `AssetTools.write_file` | only writes under the project `Content/`/`Saved/` roots — you cannot stage scratch JSON at `/Game/x.json`. Return data from the script instead. |
| `_StrictDict.get(k, default)` | unsupported in the script sandbox — use `d["k"]` in a `try`. |
| script sandbox | only `time, math, datetime, copy, re, json`. `execute_tool(name, json_str)` returns a dict-like; define `run()` returning a dict. |
| **`call_tool` itself** | args are **`toolset_name`** + a **BARE `tool_name`** (no prefix) + **`arguments`**. Passing `params`, or a fully-qualified `tool_name`, fails with `Tool 'x' not found`. **Inside `execute_tool_script` it is the opposite** — there the name must be **fully qualified** (`editor_toolset.toolsets.scene.SceneTools.find_actors`). The doc's old `execute_tool('SceneTools.find_actors', …)` shorthand is **stale**. |
| `MaterialTools.get_property_input(...)["expression"]` | may be a **plain refPath string** or a `{"refPath":…}` dict depending on the node — normalise both or `x["refPath"]` throws `string indices must be integers`. |
| `MaterialExpressionConstant` / `Constant3Vector` | property names are lowercase **`r`** and **`constant`** (an FLinearColor `{r,g,b,a}`), not `R`/`Constant`. |
| errors inside `execute_tool_script` | a failing `execute_tool` **escapes `try/except`** — errors are collected and re-raised at the end, killing the whole script. **Branch before calling**, don't catch after. |
| `describe_toolset` on `ControlRigTools` / `SequencerTools` / `SequencerControlRigTools` | 69–125 k chars — **blows the token limit** and spills to a file. `python -c "import json…"` over that file to extract just the schemas you need. |
| `ControlRigTools` pin names | the execute pin is **`ExecutePin`** (not `ExecuteContext`). `RigUnit_GetTransform` = `Item, Space, bInitial, Transform, CachedIndex`; `RigUnit_SetTransform` = `ExecutePin, Item, Space, bInitial, Value, Weight, bPropagateToChildren, CachedIndex`. The FORWARD_SOLVE event node exposes only `ExecutePin`. |
| MCP **timeouts** | a `Request timed out` is **not** a failure — the material batch, a 20-control rig chunk and a verification sweep all timed out and had fully completed. **Re-query state before redoing anything**, or you will duplicate work. |

## Capture gotcha table
| Symptom | Cause / fix |
|---|---|
| Whole frame soft/blurred | `CaptureViewport` honours `Studio_CineCam` DoF → set `FocusSettings.focusMethod="Disable"` |
| Grey box over the subject's head | the CineCam's own proxy mesh → hide `CameraProxyMeshComponent_0` + `DrawFrustumComponent_0` |
| `cap.sh` prints "NO IMAGE" but the b64 is visibly there | the endpoint answers as **plain JSON** *or* SSE depending on call → use `daztools/parse2.py` (handles both + both payload shapes) |
| `cap.sh: line 26: python: command not found` | the WSL box has only `python3`. **Fixed in the toolbox 2026-07-16** — `cap.sh` now resolves `PY_BIN=$(command -v python3 \|\| command -v python)`. The capture itself had already succeeded; only the decode step failed, so just re-run `parse2.py` on the existing `_cap_raw.txt`. |
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
- **Count skeleton ROOTS, not meshes.** "15 meshes, 15/15 skinned, 0 outlines" was still an unusable FBX —
  it had 15 private skeletons. `fbxstruct.py` answers this in 10 s, before a 4-minute import.
- **A wrist on a hip is a POSITION constraint → two-bone analytic IK, not `aim()`.** 15 lines, and it
  lands the wrist at **0.0000 cm** error with a 76° elbow. The **pole vector is the whole look**: flare
  the elbows laterally (±X), not backward, or the front-on silhouette dies.
- **Check the NODE TYPE, not the texture name, before "fixing" Trap C** — a `VectorParameter` means the
  exporter wrote nothing and the Daz colour is already correct. "No diffuse image" does not imply Trap C.
- **Sample the wardrobe texture before sweeping exposure.** Kyle's "light shirt" averaged RGB (17,17,17);
  the brief was wrong and the existing N=5.8 was already right.
- **Toon ANIME hair is solid geometry** (its diffuse maps are `.jpg` = no alpha) — no TR maps, no
  `BLEND_Masked`. Only the specular fix applies. Hair *cards* ship `.tif` TR maps; that's the tell.
- **For facial expressions, TRANSLATE the bones** — rotating a leaf face bone about its own origin barely
  moves the skin. And **jaw −4° reads as gritted teeth, −2° as a warm smile**: shoot it and look.
- **Never port a landmark threshold between figures** — "eye y forward of chin y" is true for Guardsman
  and false for Kyle *at rest*. Compare posed-vs-rest on the same figure.
- **A viewport that grew to 1857×825 does NOT mean the pose reverted** — Kyle rendered full-size *and*
  posed. Prove a revert with `get_euler_transform`, not with the window size.
- **An MCP timeout is not a failure — re-query before you redo.** Three timed-out calls had all completed.
- **A Daz re-export that is byte-identical didn't happen** — check the file size changed.
- **A neutral-grey Daz skin diffuse means no skin preset is applied**, not a tint to multiply. G9 Starter
  Essentials' `Masculine_0N`/`Feminine_0N` base skins wire straight on (same UVs) — no Daz round-trip needed.
- **Read `scene.materials` in the `.duf`, never `material_library`** (the latter shows 0 images for everything).
- **Sequencer keys need their own tool call** — rig reads or track creation in the same call silently
  discard them, and `keyed: N` still returns success. **Read back `get_euler_transform`.**
- **A collapsed figure has two different causes** (scale-0 controls vs keys that never landed) that look
  identical — check control type/scale *and* the keyed values before "fixing" either.
- **Emissive debug colours identify a material; if the artifact takes no colour, it's the lighting** (that's
  how the white hair streaks were traced to rim-light specular, not to an opacity mask).
- **Measure the pose, don't eyeball it** — `mid3→wrist` told me the "fist" was a claw; the eye/chin z told me
  he was staring at the floor.
- Invisible mesh + valid bounds = **broken skinning** (bind mismatch or degenerate scale), never a hidden actor.
- A **Blender-authored anim belongs on a Blender-imported mesh** — never on the original Daz-imported skeleton.
- **Don't fight FBX units** — export clean (rename dupes, no manual scaling), let UE read coords as-is.
- **Keep FBX imports light** to avoid game-thread hangs. Assets survive restarts; unsaved level/studio state does not.
- **Manual exposure + re-aim existing sun + camera-first WP streaming + post-process overlays** = repeatable clean still.
- **Fix eyes by deleting eye-bone tracks**; always re-carry the fixed subsurface/eye materials after a fresh import.
- Watch VRAM: after many imports the editor logged "Video memory exhausted (~106 MB over budget)" — restart before it gets flaky.
