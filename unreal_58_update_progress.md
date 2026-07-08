# Unreal Course — 5.4 → 5.8 Update + Visual Enhancement — Progress Tracker

> **Source-of-truth doc for this initiative.** Newest entry leads. Read this + `image_style_guide.md` before any action.
> Working dir: `\\wsl$\Ubuntu\home\practicalace\projects\unreal` (Filesystem tools only; never `\\wsl.localhost\`).

---

## ⚠️ Reconciliation notice (read first)

The pre-existing `continue.md` and `journal.txt` are **STALE** and must not be trusted for status:

- `continue.md` claims "~20% complete, Module 3 (Blueprints) is next." **False.** It was last updated before Modules 3–10 existed.
- `journal.txt` is newer (through Module 7) but also trails the disk.
- The `parts/` folder preserves an **OLD module numbering** where Module 3 = Blueprints. The course was later **reorganized**: Module 3 is now *Materials & Textures*, and Blueprints moved to *Module 5*. Filenames in `parts/` are fossils — do NOT use them to infer current structure.

**TRUE SOURCE OF TRUTH: `index.html` + the combined root `mXX_lYY_*.html` files.** Everything below is derived from those.

---

## Ground-truth course structure (from index.html, verified)

Course is **content-complete**: 10 modules, 38 lessons, all built and linked, all progress bars at 100%.

| Module | Title | Lessons | Version-drift risk (5.4→5.8) |
|--------|-------|---------|------------------------------|
| M1 | Getting Started | 4 | Low (UI refresh) |
| M2 | Levels and Actors | 5 | Med (Modeling, Mesh Terrain context) |
| M3 | Materials and Textures | 5 | **High** (Substrate, Toon Shader, MI UI) |
| M4 | Lighting Your World | 5 | **High** (Lumen, MegaLights prod-ready, Lumen-Lite) |
| M5 | Introduction to Blueprints | 5 | Low–Med |
| M6 | Player Interaction and Input | 5 | Med (Enhanced Input) |
| M7 | User Interface with UMG | 5 | Low |
| M8 | Audio Basics | 3 | Low |
| M9 | Particles and Visual Effects | 3 | Med (validate vs live NiagaraToolset) |
| M10 | Packaging and Publishing | 3 | Med (settings/UI) |
| Bonus | Using Marketplace Assets | 1 | Low (Fab, not Marketplace) |
| **NEW** | **AI-Assisted Workflows (Unreal MCP)** | TBD | New content |

---

## Verified environment facts (this session)

- **UE 5.8 shipped** (Unreal Fest Chicago, June 17 2026). Last planned major UE5 release before UE6.
- **Official Unreal MCP plugin** exists in 5.8 (Experimental). Embeds MCP server in editor at `http://127.0.0.1:8000/mcp`. Enable via Edit > Plugins (pulls in Toolset Registry). Auto-start in Editor Preferences > Model Context Protocol. `ModelContextProtocol.GenerateClientConfig` writes `.mcp.json`. Client names: ClaudeCode, Cursor, VSCode, Gemini, Codex, All.
- **Live MCP bridge confirmed** this session: full editor toolset reachable, including `SlateInspectorToolset` (UI screenshots) and `EditorAppToolset` (viewport capture). → Real screenshots are viable.

---

## Open decisions (need Ray's call before/ during sweep)

**RESOLVED 2026-07-07:**

1. **Version string** → Set everything to **"UE 5.8"** (index.html requirement card, curriculum header + `Software Required`, resources section, any in-lesson "5.4+" mentions). Do a full grep-style sweep for "5.4", "5.5", "5.6", "5.4+" across all files.
2. **Progress indicator** → **STRIP everywhere.** continue.md preference wins. Remove scroll progress-bar markup + its JS + CSS from every lesson that has it. (journal.txt was wrong to list it as a kept feature.) Verify none remain via sweep for progress-bar class/JS.
3. **MCP content** → **New Module 11: AI-Assisted Workflows.** Add to index.html as an 11th module card, add to curriculum, build lessons. Flag all MCP content "Experimental in UE 5.8."

---

## Per-lesson work log

> Columns: Version-sweep · Figures (real captures added) · QA. Status: ☐ todo · ◐ in progress · ✅ done.
> Invariant tracking per edited file: byte count (before→after), element count, em-dash count (target: 0 new; use `&#183;`).

| Lesson | Version-sweep | Real figures | Browser QA | Notes |
|--------|:---:|:---:|:---:|-------|
| m01_l01 | ✅ | ☐ | ☐ | 81,789 bytes baseline; Archetype A (no scroll-strip needed) |
| m01_l02 | ✅ | ☐ | ☐ | Archetype A |
| m01_l03 | ✅ | ☐ | ☐ | Archetype A |
| m01_l04 | ✅ | ☐ | ☐ | UI-heavy — high screenshot value; Archetype A |
| m02_l01–05 | ✅ | ☐ | ☐ | Archetype A |
| m03_l01 | ✅ | ✅ | ✅ | **Sweep B l01 (2026-07-08):** version-clean (0 drift, 27 em-dashes, all 8 TOC hrefs resolve). Figure-only + Ray-approved prose UI touch-ups. 3 REAL captures via temp `/Game/MCP_Temp_L01` assets (M_BasicColor + 3 params + 2 MIs, all built live via MaterialTools/MaterialInstanceTools, deleted after): fig01_material_editor.png (1800×797, real 5.8 Material Editor maximized + Home-framed, **replaced** the §4 SVG mockup) + fig02_material_instance_editor.png (780×857, MI Details panel: Appearance group, 3 checked override checkboxes, Parent=M_BasicColor — **added** to §5, addresses MI-UI drift) + fig03_material_spheres.jpg (1384×518 JPEG q88, shiny-red-plastic R0.3 vs matte-blue-rubber R0.9 from the two MIs' live preview viewports, stitched+labeled — **added** to hands-on). Prose: reordered §4 panel bullets to match real default layout (Graph/Preview/Details/Palette, dropped ①-④ overlay refs) + dropped stale UE4-era "Materials & Textures" submenu label ×2. 89815→80711 (−9104: −160-line SVG + 3 imgs); em-dashes 27 (0 new); HTTP QA ✅ (page+3 imgs 200/correct-MIME, refs in DOM, 0 progress residual); editor restored (temp assets deleted, camera at Ray's pose, DirectionalLight reselected). |
| m03_l02 | ✅ | ✅ | ✅ | **Sweep B l02 (Session 9, 2026-07-08):** version-clean (0 drift, 23 em-dashes 0 new, 7/7 TOC hrefs resolve). Figure-only. 3 REAL captures via temp `/Game/MCP_Temp_L02` (engine textures; deleted after): fig01 Texture Editor Details (Compression/sRGB✓/Mip Gen, **added** §Texture Settings) + fig02 real node graph TexCoord×Tiling→UVs→BaseColor (**replaced** §Texture Coordinates line-784 SVG; ⚠️ node preview swatch blank — flag 11) + fig03 textured sphere JPEG (**added** Hands-On). 92932→91104 (−1828); HTTP QA ✅. |
| m03_l03 | ✅ | ✅ | ✅ | **Sweep B l03 (Session 10, 2026-07-08):** version-clean (0 drift, 29 em-dashes 0 new, 8/8 TOC hrefs resolve). Figure-only + 1 UI touch-up (line-576 stale "Materials & Textures →" submenu → version-robust "creation menu", matching L01). 3 REAL captures via temp `/Game/MCP_Temp_L03` (MF_TilingControls MaterialFunction + M_LerpDemo material, both built live via MaterialTools incl. **first MaterialFunction build** create_function→FunctionInput/Output nodes; deleted after): fig01 real MF_TilingControls graph (**replaced** §3 line-599 SVG) + fig02 real Lerp node graph GrassColor/DirtColor/Mask→Base Color (**added** §2 after concept SVG) + fig03 terrain-blend result sphere JPEG (green/brown Lerp via noise mask, matte R0.9; **added** Hands-On Step 7). ⚠️ **flag 13:** fig01 & fig02 node graphs show BLANK WHITE preview thumbnails on FunctionInput/VectorParameter nodes (same headless quirk as flag 11 — deterministic, no expression prop or ref to suppress). 99075→94700 (−4375); HTTP QA ✅. |
| m03_l04 | ✅ | ✅ | ✅ | **Sweep B l04 (Session 11, 2026-07-08):** version-clean (0 drift, 24 em-dashes 0 new, 8/8 TOC hrefs resolve). Figure-only + 2 UI touch-ups (both stale "Materials & Textures →" submenu labels → version-robust "creation menu", lines 212 + 983; same as L01/L03 flag #10). 3 REAL captures via temp `/Game/MCP_Temp_L04` (M_ConfigurableSurface master with Base_Color_Tint/Roughness_Amount/Metallic_Amount/UV_Tiling/Detail_Normal params in 3 groups + 3 MIs, all built live; deleted after): fig01 real MI Editor Details (parameter groups + override checkboxes + Parent=M_ConfigurableSurface, **replaced** §1 mockup SVG) + fig02 real Scalar Parameter Details (Name/Group/Default/Slider Min-Max/Sort Priority; **added** §2; node selected via Find-Results→double-click since canvas has no refs) + fig03 3-instance result spheres (Red Plastic R0.2 / Gold Metal R0.4 Metallic / Blue Matte R0.85, stitched JPEG; **added** Hands-On Part 2). 96948→93475 (−3473); HTTP QA ✅; editor restored. |
| m03_l05 | ✅ | ✅ | ✅ | **Sweep B l05 (Session 12, 2026-07-08):** version-clean (0 drift, 37 em-dashes 0 new, all 11 TOC hrefs resolve). Predicted "Substrate+Toon = highest in-file drift" was FALSE — both are 0-hits course-wide (content GAP, like MegaLights). Ray: **author Substrate + Toon/NPR sections** + Substrate capture + swap mockup + 1 result sphere. Authored §7 Substrate (slab/BSDF vs fixed shading model, Front Material root, layering operators, Experimental) + §8 Stylized/Toon (two routes) + TOC/objectives/summary + 2 concept SVGs. **Live discovery: UE 5.8 ships `MaterialExpressionSubstrateToonBSDF`** → rewrote Toon prose (was wrongly "no dedicated toon model"). Substrate ENABLED in Ray's project (every root shows Front Material → classic-mockup swap would contradict classic prose, so skipped; flag #14). 3 real captures via temp `/Game/MCP_Temp_L05` (M_Substrate_CoatedMetal 2-slab+VerticalLayer, M_Substrate_Toon ToonBSDF, M_Emissive_Glow): fig01 emissive cyan glow sphere (JPEG, §Emissive) + fig02 Substrate VerticalLayer→FrontMaterial graph (PNG, §Substrate, replaced placeholder) + fig03 Substrate Toon BSDF cel-shaded sphere+node (PNG, §Toon). 122255→144392 (+22137); HTTP QA ✅; editor restored. **M3 Sweep B COMPLETE.** |
| m04_l01–05 | ✅ | ◐ | ◐ | HIGH drift; scroll-strip ✅ (l01_fundamentals/l02/l03 −330, l04/l05 −452); l01_introduction_to_lighting Archetype B clean. **Sweep B l01 (2026-07-08):** content version-accurate as-is (only drift was MegaLights → deferred to l04 per Ray); real fig01 mobility_control.png added — Mobility toggle w/ full Static/Stationary/Movable labels (810×60), captured from floating Details window + stitched (110267→110842, +575); browser QA ✅. **Sweep B l02 (2026-07-08):** content version-accurate for 5.8 (no drift — figure-only, same as l01); MegaLights still absent (lives in l04); 2 real captures added — fig01_outdoor_sky.jpg (live viewport: DirectionalLight+SkyAtmosphere+SkyLight+HeightFog+VolumetricClouds over landscape; cropped gizmo; 1400×675 JPEG 83KB) + fig02_atmosphere_sun_light.png (Atmosphere Sun Light checkbox enabled, DirectionalLight Details panel; 806×121 PNG). 99604→100810 (+1206); 0 new em-dashes (25); HTTP QA ✅. **Sweep B l03 (2026-07-08):** version-clean (0 drift; 12 "lumen" = the unit, not Lumen GI). Found + fixed a pre-existing CONTENT BUG (not drift): TOC promised IES Profiles + Light Functions sections that had NO body (3 dead anchors: #ies-profiles, #light-functions, #hands-on) yet objectives/hands-on/summary/quiz all relied on them. Per Ray: **authored both missing sections** (prose + 2 real Details captures + IES-shapes SVG + flicker Mermaid) and fixed #hands-on→#hands-on-exercise. 2 real captures (temp SpotLight added→captured→deleted, editor restored): fig01_ies_texture_slot.png (Light Profiles category: IES Texture/Use IES Intensity/IES Intensity Scale; 812×308) + fig02_light_function_slot.png (Light Function category: Material/Scale/Fade Distance/Disabled Brightness; 812×372). 82466→95746 (+13280); 0 new em-dashes (26); all 8 TOC links now resolve; HTTP QA ✅. **Sweep B l04 (2026-07-08):** version-clean (0 drift; 45 "lumen" all accurate for 5.8). **Corrected the record: MegaLights was NOT in this file or anywhere in the course** (grep course-wide = 0 hits; "prod-ready" hits are unrelated install/Blueprints prose). So flag #3 was a content GAP, not a contradiction. Per Ray: **authored a full "MegaLights (Experimental in UE 5.8)" section** (id `megalights`, new TOC entry + objective bullet; problem/stochastic-sampling+denoiser/complementary-to-Lumen/requirements/enable steps/when-to-use/watch-outs; concept SVG). 3 real captures (Ray: on/off + 2 panels) via ONE temp unbound PostProcessVolume: fig01_lumen_on_off.jpg (1400×343, side-by-side Lumen on vs off from identical interior camera, toggled via PPV GI-method override, burned labels, JPEG q88) + fig02_project_settings_gi.png (real Project Settings→Rendering→Global Illumination = Lumen, **replaced** Step-1 SVG) + fig03_ppv_lumen_settings.png (real PPV Details filtered to "Lumen", **replaced** Section-5 SVG). 98524→103744 (+5220; +10057 authored, −4837 SVG→img swaps); 38 em-dashes (0 new); all 9 TOC anchors resolve; HTTP QA ✅; editor restored. Flag #3 RESOLVED. **Sweep B l05 (2026-07-08):** version-clean (0 drift; the 15 "lumen" hits are all the AO-plus-Lumen interaction context, accurate for 5.8). TOC clean (all 8 hrefs resolve). Ray: prose as-is (figure-only, like l01/l02; Local Exposure left out as a 5.2 feature, pre-5.4 baseline). 3 real captures via ONE temp unbound PPV (placed off-frame at 54548,51063,789 so its orbit-pivot axis lines stayed out of shot): fig01_post_process_before_after.jpg (1400x343 JPEG q88, flagship before/after from Ray's interior cam: neutral vs strong cinematic grade [teal shadows / warm highlights / vignette 0.85 / bloom 2.0 / AO / -0.6 EV / chromatic aberration], grade set via ObjectTools on PPV Settings bOverride_* + FVector4 gain/sat/contrast) + fig02_exposure_settings.png (956x1056, real Lens>Exposure Details filtered "Exposure": Histogram, Comp -0.6, Min/Max EV100 6/13, Speed 2/2) + fig03_color_grading_settings.png (956x982, real Color Grading category via filter chip, Global subsection expanded, Saturation+Contrast overridden). All 3 ADDED to figure-only sections (those sections had no UI-mockup SVGs to replace; existing SVGs are legit concept diagrams). 115106->117640 (+2534); 24 em-dashes (0 new); HTTP QA passed (page 200 + all 3 imgs 200/correct-MIME, DOM refs present, 0 progress residual); editor restored (PPV gone via find_actors, DirectionalLight reselected, camera at Ray's exact pose 4548.6/1063.9/789.4, both observers dropped). **M4 Sweep B COMPLETE.** |
| m05_l01–05 | ✅ | ☐ | ☐ | Archetype A |
| m06_l01–05 | ✅ | ☐ | ☐ | scroll-strip ✅ Archetype D (−452 ea) |
| m07_l01–05 | ✅ | ☐ | ◐ | scroll-strip ✅ Archetype D (−452 ea); l01 browser spot-check ✅ |
| m08_l01–03 | ✅ | ☐ | ☐ | scroll-strip ✅ Archetype D (−452 ea) |
| m09_l01–03 | ✅ | ☐ | ☐ | validate vs NiagaraToolset; scroll-strip ✅ Archetype D (−452 ea) |
| m10_l01–03 | ✅ | ☐ | ☐ | scroll-strip ✅ Archetype D (−452 ea) |
| bonus_marketplace | ✅ | ☐ | ☐ | scroll-strip ✅ (−452); Marketplace→Fab rename pending (Sweep B) |
| NEW mcp_module | ☐ | ☐ | ☐ | build while bridge live |

---

## Session history (newest first)

### Session 12 — 2026-07-08 (Sweep B — M3 L05 `special_material_types.html` — Substrate + Toon sections authored + 3 real Substrate-era captures)

**Live state:** MCP bridge up (probe 200 + session id). Editor confirmed restored at end: temp folder `/Game/MCP_Temp_L05` gone (`exists`=false), camera at Ray's exact interior pose 4548.619,1063.882,789.431 / pitch −24.1999 yaw −134.398, DirectionalLight still selected, `ListObservers`=[]. Level viewport never touched (all work on asset-editor windows).

**Scan (WSL grep):** L05 = 122255 B, 37 em-dashes (all pre-existing prose), **zero** version strings (5.4–5.7), **zero** drift terms. Actual content = blend modes / translucent / masked / emissive (incl. Lumen) / decals / landscape / hands-on (Pulsing Sci-Fi Panel) — foundational UE5, version-accurate for 5.8. TOC clean (9 hrefs resolve). **The tracker's premise was WRONG:** "Substrate + Toon = highest in-file drift" — but Substrate/Strata = **0 hits course-wide**, Toon/NPR grep hits all false positives ("cartoon"/"Splatoon"/"Non-Photorealistic Art"). Like MegaLights (flag #3), this is a **content GAP, not in-file drift.**

**Ray's decisions (AskUserQuestion):** (1) content = **Substrate + Toon/NPR** (author both sections); (2) figures = **Substrate capture + swap weakest mockup + 1 result sphere**.

**Authored (2 new sections before Hands-On; section comments renumbered 7-10):** §7 **Substrate: Next-Generation Materials** (id `substrate`): Experimental-in-5.8 card + enable steps, classic-vs-Substrate paradigm, Slab BSDF definition, Front Material root node, layering operators (Horizontal/Vertical/Add/Weight/Coverage), why-it-matters, watch-out, pro-tip, classic-vs-Substrate concept SVG. §8 **Stylized & Toon Materials (NPR)** (id `toon`): two-routes framing + banding/outline concept SVG. TOC +2, Learning Objectives +2, Summary key-takeaway +1.

**⚠️ MID-SESSION CORRECTION (important):** `list_expression_classes(search="Substrate")` revealed **`MaterialExpressionSubstrateToonBSDF`** — UE 5.8 with Substrate ships a **dedicated Toon BSDF shading node.** My first-draft Toon prose ("Unreal has no dedicated toon shading model") was therefore **inaccurate for 5.8** and I rewrote the section: "two routes" = (a) Substrate Toon BSDF (surface cel-shading, Experimental, needs Substrate) with a real capture, (b) post-process materials (banding + Sobel outlines, universal) with the concept SVG. HTTP DOM check confirmed the inaccurate "no dedicated" phrase is gone.

**Substrate is ENABLED in Ray's project** (all Substrate expression classes live; materials compile with MP_FrontMaterial; corroborated by Session 8's observed Substrate preview panel). **Consequence + flag #14:** every material's root node shows **Front Material** (not classic BaseColor/Metallic/Roughness pins), so a real capture of a *classic* node-graph mockup (§Translucent etc.) would **contradict the classic-pin prose** — so I did NOT swap a classic mockup; the "result sphere" is a real render (no pin mismatch).

**Live asset authoring (temp `/Game/MCP_Temp_L05`, all deleted after):** `M_Substrate_CoatedMetal` (2× SubstrateSlabBSDF → SubstrateVerticalLayering Top/Bottom → MP_FrontMaterial); `M_Substrate_Toon` (SubstrateToonBSDF, BaseColor from warm-orange Constant3Vector → MP_FrontMaterial); `M_Emissive_Glow` (SubstrateSlabBSDF, HDR cyan Constant3Vector → slab "Emissive Color" → MP_FrontMaterial). **Pin facts:** SubstrateSlabBSDF inputs = Diffuse Albedo/F0/F90/Roughness/Anisotropy/Normal/Tangent/SSS MFP.../Emissive Color/Second Roughness/Fuzz.../Glint(Disabled); SubstrateVerticalLayering inputs = Top/Bottom/Top Thickness, output "" (green "BSDF"); SubstrateToonBSDF inputs = BaseColor/Metallic/Specular/Roughness/Normal/EmissiveColor/PatternUVs/Anisotropy/Tangent + `toonProfile` property. Constant3Vector value prop = `Constant` {r,g,b,a}. Substrate emissive lives on the SLAB's "Emissive Color" input (root has no Emissive Color pin in Substrate mode).

**3 real captures:**
1. `images/m03_l05/m03_l05_fig01_emissive_glow.jpg` (585×585 JPEG q88, 19KB) — §Emissive (after HDR/Bloom): the emissive material on the preview sphere, self-lit cyan glow. The "1 result sphere." (toned HDR from 8.0→2.3 for color over blow-out; cropped square to drop axis gizmo + Shaders badge.)
2. `images/m03_l05/m03_l05_fig02_substrate_graph.png` (1180×975 PNG, 198KB) — §Substrate: Substrate Vertical Layer operator (Top/Bottom/BSDF) → root node's **Front Material** pin, full Substrate pin set visible. **Replaced** the `<!-- fig01 -->` placeholder. Slabs off-frame (shown in the concept SVG).
3. `images/m03_l05/m03_l05_fig03_toon_bsdf.png` (1600×769 PNG, 685KB, downscaled from 2585) — §Toon: preview sphere cel-shaded (hard stepped terminator, flat bands) + the "**Substrate Toon BSDF - EXPERIMENTAL**" node → Front Material. Shipped-feature proof AND result.

**⚠️ NEW flag #14 (capture limitation):** Material Editor graph opens at **Zoom 1:1**, and a Substrate **Slab BSDF node is ~full-canvas-height** at 1:1 (18 pins) → two slabs can NEVER fit one clean shot; save+close+reopen did **NOT** auto-fit (unlike M3 L03's "Zoom −2"); and the SlateInspector observer on the reopened material-editor window **would not populate child refs** (cachedSnapshotSize stuck at 257 even after Unobserve/re-Observe), so I could not click the toolbar Home/zoom-to-fit. Worked around by cropping fig02 to the clean Vertical-Layer→Front-Material region. A Substrate **"out of budget / material simplified" yellow watermark** also overlays 2-slab preview graphs (cropped out).

**Invariants:** 122255→144392 (**+22137**: 2 authored sections + 2 concept SVGs + 3 figs + Toon rewrite); em-dashes **37 (0 new)** (WSL grep; captions use `&#183;`); all **11** TOC hrefs resolve (incl. new #substrate/#toon → real section ids); 3 imgs, 21 captions (16+5); 0 leftover placeholders. Photographic fig01 = JPEG; UI fig02/fig03 = PNG.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (144392), fig01 200 image/jpeg 18978B, fig02 200 image/png 198075B, fig03 200 image/png 685302B, all 3 `<img>` refs in DOM, both new section ids in DOM, "Substrate Toon BSDF"/"Front Material" present, inaccurate "no dedicated" phrase absent, 0 placeholders. ✅ Server stopped (SIGTERM exit 15 expected). Editor restored (temp gone `exists`=false, DirectionalLight selected, camera at Ray's exact pose, observers []).

**M3 Materials Sweep B COMPLETE (l01-l05).** Next: **Build C = new Module 11 — AI-Assisted Workflows (Unreal MCP)**, captured live while the bridge is up.

**Still FLAGGED for Ray (carry forward 1,2,4,5,6,7,8,9,10,11,12,13):** + **NEW (14):** Substrate is enabled project-wide, so real classic-material node-graph captures show Front Material (contradicting the lesson's classic-pin prose) — classic-mockup swap intentionally skipped; options: (a) leave as-is, (b) temporarily disable Substrate for classic captures, (c) accept Substrate-view captures. Plus the Zoom-1:1 / tall-Slab / observer-won't-repopulate limitation above. **(15):** consider a one-line note in L05 that Ray's project has Substrate enabled (so learners see Front Material where the classic prose shows Base Color/Opacity pins) — NOT added, Ray to decide. **(16):** fig01 emissive is built on a Substrate slab (renders identically to a classic emissive) — noted for transparency.

### Session 11 — 2026-07-08 (Sweep B — M3 L04 `material_instances_and_parameters.html` — real MI Editor + Scalar Parameter Details + 3-instance result spheres)

**Live state:** MCP bridge up (probe 200 + session id). Editor confirmed restored at end: temp folder `/Game/MCP_Temp_L04` gone (`exists`=false), camera at Ray's exact interior pose 4548.619,1063.882,789.431 / pitch −24.1999 yaw −134.398, DirectionalLight still selected, `ListObservers`=[], all asset-editor windows closed. Level viewport never touched (all work on asset-editor windows).

**Scan (WSL grep):** L04 = 96948 B, 24 em-dashes (all pre-existing prose), **zero** version strings (5.4–5.7), **zero** drift terms (no Substrate/Toon/MegaLights/Nanite/Virtual Texture/UDIM/Marketplace/Lumen/Strata). Foundational MI content (parent-instance relationship, Scalar/Vector/Texture parameters, parameter groups + sort priority, static switches, Dynamic Material Instances, MPCs, hands-on) — stable UE5, unchanged 5.4→5.8. TOC clean (all 8 hrefs resolve). ⇒ figure-only, like L01/L02/L03. Found the SAME stale UI label as L01/L03 (flag #10) **×2**: lines 212 + 983 "Materials & Textures → Material Instance / Material Parameter Collection".

**Ray's decisions (AskUserQuestion):** (1) prose = figure-only **+ the 2 submenu touch-ups**; (2) figures = **all three** (MI Editor + Scalar Parameter Details + result spheres).

**Prose touch-ups:** line 212 "Right-click in Content Browser → **Materials & Textures → Material Instance**" → "Right-click in Content Browser and choose **Material Instance** from the creation menu"; line 983 "Right-click → **Materials & Textures → Material Parameter Collection**" → "right-click and choose **Material Parameter Collection** from the creation menu" (both drop the UE4 submenu name + the "→" arrow, matching L01/L03).

**Live asset authoring:** temp `/Game/MCP_Temp_L04/M_ConfigurableSurface` — VectorParameter Base_Color_Tint (grp "01 - Surface") → BaseColor; 2× ScalarParameter Roughness_Amount/Metallic_Amount ("01 - Surface", sliderMin/Max 0-1, sortPriority) → Roughness/Metallic; ScalarParameter UV_Tiling ("03 - UV") + TextureCoordinate → Multiply → TextureSampleParameter2D Detail_Normal ("02 - Textures", samplerType `SAMPLERTYPE_Normal`, default `/Engine/EngineMaterials/T_Default_Material_Grid_N`) → Normal. 3 groups exactly matching the hands-on. Then 3 MIs via `MaterialInstanceTools.create` + `set_vector`/`set_scalar_parameter` (auto-enables the override checkbox): MI_ShinyPlastic_Red (red, R0.2, metallic **left at parent default → unchecked**), MI_BrushedMetal_Gold (gold, R0.4, Metallic 1.0), MI_MattePaint_Blue (blue, R0.85). Saved via `AssetTools.save_assets`.

**3 real captures:**
1. `images/m03_l04/m03_l04_fig01_material_instance_editor.png` (1147×1018 PNG) — real MI Editor Details of MI_ShinyPlastic_Red: Parameter Groups 01-Surface (Base_Color_Tint ✓ red + Roughness_Amount ✓ 0.2 checked, Metallic_Amount unchecked/inherited), 02-Textures (Detail_Normal — lavender normal swatch renders **correctly**, NOT blank), 03-UV, Save Sibling/Child, General → Parent = M_ConfigurableSurface. **Replaced** the §1 hand-drawn MI-editor mockup SVG. Directly serves the flagged MI-UI drift.
2. `images/m03_l04/m03_l04_fig02_scalar_parameter_details.png` (764×937 PNG) — real Material Editor Details of the Roughness_Amount ScalarParameter node: Parameter Name, Default Value 0.5, Group 01-Surface, Sort Priority 1, Control Type Numeric, Slider Min 0.0, Slider Max 1.0. **Added** to §2 after the Scalar-properties concept SVG (concept → real). **NEW reusable technique (solves the "SGraphPanel exposes no refs" limit for SELECTION, not capture):** Material Editor toolbar **Search button → Find Results** tab exposes a real list; `Type` the param name into the find box (submit) → `Snapshot` the results list → **double-click** the `listitem` → selects+focuses that graph node → the left **Details** panel (a normal SDetailsView) populates with the node's full properties, which DO get Slate refs and screenshot cleanly. You still can't screenshot canvas nodes (flag 11/13), but you CAN drive node selection this way.
3. `images/m03_l04/m03_l04_fig03_instance_spheres.jpg` (1708×606 JPEG q88) — the 3 MI editor preview spheres, each cropped to an identical 1700² square centered on the sphere, scaled to 560², stitched with burned labels: "Shiny Red Plastic · Roughness 0.2" (sharp specular), "Brushed Gold Metal · Roughness 0.4 · Metallic" (warm metallic reflections), "Matte Blue Paint · Roughness 0.85" (flat diffuse). **Added** to Hands-On before Part 3. Preview-viewport renders (like L01/L02/L03 fig C) — keeps Ray's level untouched.

**No blank-thumbnail quirk this time:** fig01/fig02 are Details **panels** (SDetailsView), not node-graph canvas captures, so flag 11/13 does not apply; the Detail_Normal preview swatch in the MI editor rendered correctly (lavender normal default). fig03 spheres are preview-viewport renders — clean.

**Invariants:** 96948→93475 (**−3473**: −§1 MI-editor SVG [~77 lines], +3 img/caption blocks, −2 "→" arrow chars; 2 prose touch-ups); em-dashes **24 (0 new)** (WSL grep; captions use `&#183;`); all **8** TOC hrefs still resolve to real section ids; 16 captions (13+3); 0 progress residual; old MI-editor SVG gone; both "Materials & Textures" labels gone. Photographic fig03 = JPEG, UI fig01/fig02 = PNG.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (93475), fig01 200 image/png 90838B, fig02 200 image/png 62890B, fig03 200 image/jpeg 58296B, all 3 `<img>` refs in DOM, old MI SVG absent, both submenu labels absent, 0 progress residual. ✅ Server stopped (SIGTERM exit 15 expected).

**Next:** Ray reviews L04. Then M3 L05 `special_material_types` (Substrate + Toon Shader — highest drift in the course). Then Build C (new Module 11 — AI-Assisted Workflows / Unreal MCP), captured live.

**Still FLAGGED for Ray, unresolved:** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit; (6) photographic figs now JPEG **×7** (M4 L02/L04/L05 fig01 + M3 L01/L02/L03/L04 fig03) breaking the `.png`-only rule — recommend the guide formally allow JPEG-photographic/PNG-UI; (7) course-wide TOC-href-vs-section-id audit; (8) figures partly ADDED vs swapped where sections lacked UI-mockup SVGs — confirm pattern; (9) result/sphere figs use the editor preview viewport, not Ray's level — confirm; (10) "Materials & Textures" submenu rephrase applied again here (L04 lines 212 + 983) from knowledge, not a live menu check; (11) M3 L02 fig02 TextureSample preview swatch blank; (12) M3 L02 §Compression SVG "DXT1/DXT5" vs real "BC1 or BC3 with A"; (13) M3 L03 fig01/fig02 node-graph captures show blank white preview thumbnails on FunctionInput/VectorParameter nodes (headless quirk) — Ray to decide keep vs revert to SVG.

### Session 10 — 2026-07-08 (Sweep B — M3 L03 `building_complex_materials.html` — Material Function graph + real Lerp graph + terrain-blend sphere)

**Live state:** MCP bridge up (probe 200 + session id). Editor confirmed restored at end: temp folder `/Game/MCP_Temp_L03` gone (`exists`=false), camera at Ray's exact interior pose 4548.619,1063.882,789.431 / pitch −24.1999 yaw −134.398, DirectionalLight still selected, no lingering Slate observers. Level viewport never touched (all work on asset-editor windows).

**Scan (WSL grep):** L03 = 99075 B, 29 em-dashes (all pre-existing prose), **zero** version strings (5.4–5.7), **zero** drift terms (no Substrate/Toon/MegaLights/Nanite/Virtual Texture/UDIM/Marketplace/Lumen/Strata). Foundational material-graph content (math nodes Add/Multiply/Lerp, Material Functions, texture blending, world-aligned/tri-planar, terrain-blend hands-on) — stable UE5, unchanged 5.4→5.8. TOC clean (all 8 hrefs resolve: 7 sections + main-content). ⇒ figure-only, like L01/L02. Found ONE stale UI label (not drift): line 576 "Materials & Textures → Material Function" = the same UE4-era submenu name Ray had me rephrase in M3 L01 (flag #10).

**Ray's decisions (AskUserQuestion):** (1) prose = figure-only **+ the line-576 touch-up**; (2) figures = **all three** (Material Function graph + real Lerp graph + terrain-blend result render).

**Prose touch-up:** line 576 "right-click and select **Materials & Textures → Material Function**" → "right-click (or click **+Add**) and choose **Material Function** from the creation menu" (version-robust, drops the UE4 submenu name + the "→" arrow char; matches L01).

**Live asset authoring (first MaterialFunction build via the toolset):** `MaterialTools.create_function` supports authoring MaterialFunctions. Built temp `/Game/MCP_Temp_L03/MF_TilingControls`: 3× `MaterialExpressionFunctionInput` (Scalar, named Tiling/OffsetU/OffsetV via ObjectTools `inputName`/`inputType`=FunctionInput_Scalar/`previewValue`/`sortPriority`) + TextureCoordinate → Multiply(×Tiling) + Append(OffsetU,OffsetV) → Add → `MaterialExpressionFunctionOutput` (`outputName`=UVs, input pin literally named "None"). Also temp `M_LerpDemo`: 2× VectorParameter (GrassColor green / DirtColor brown) → LinearInterpolate A/B, TexCoord→ComponentMask(r-only)→Alpha, Lerp→MP_BaseColor; then upgraded for fig03 (swapped alpha to a 3×-tiled MacroVariation TextureSample for an organic blend + Constant 0.9→MP_Roughness for a matte read + deepened both colors). `add_expression` works on Material OR MaterialFunction; new pin-name discoveries: Lerp = A/B/Alpha, ComponentMask has r/g/b/a bools, AppendVector = A/B.

**3 real captures:**
1. `images/m03_l03/m03_l03_fig01_material_function_graph.png` (1150×1001 PNG) — real MF_TilingControls graph, save+close+reopen so positions apply, reopened view auto-fit at "Zoom −2". **Replaced** the §3 line-599 hand-drawn SVG.
2. `images/m03_l03/m03_l03_fig02_lerp_blend_graph.png` (1250×610 PNG) — real Lerp node: GrassColor→A, DirtColor→B, TexCoord→Mask(R)→Alpha, →Base Color. **Added** to §2 after the "Lerp: Blending with a Mask" concept SVG (concept → real). VectorParameter *Default Value* color chips render correctly (green/brown).
3. `images/m03_l03/m03_l03_fig03_terrain_blend_result.jpg` (660×542 JPEG q88) — the terrain material on the Material Editor preview sphere: green grass + brown dirt mixed via a noise mask, matte. **Added** to Hands-On after Step 7. (Preview-viewport render, like L01/L02 fig C — keeps Ray's level untouched.)

**⚠️ NEW flag #13 (blank preview thumbnails):** both node-graph captures (fig01, fig02) show **blank WHITE preview thumbnails** on the FunctionInput and VectorParameter nodes. This is the SAME deterministic headless-capture quirk as flag #11 (TextureSample swatch) — it affects EVERY preview-capable node's large realtime-preview thumbnail (the small inline Default-Value/color chips DO render). Confirmed unavoidable: `bCollapsed` is not settable, no preview-visibility property exists on the expression, save+close+reopen does not fix it, and the graph canvas (SGraphPanel) exposes NO Slate refs so the per-node collapse chevrons can't be clicked. Accepted + flagged, consistent with how L02 fig02 (flag #11) was handled. Ray to decide keep-as-is vs revert either graph figure to its SVG. (Note: the noise TextureSample swatch in the fig03-state graph DID render gray — the quirk is inconsistent, root cause still unknown.)

**Invariants:** 99075→94700 (**−4375**: −line-599 §3 SVG [~90 lines], +3 img/caption blocks, +fig02 lead paragraph, −line-576 arrow char; prose touch-up); em-dashes **29 (0 new)** (WSL grep; captions use `&#183;`); all **8** TOC hrefs still resolve; 0 progress residual; old MF-graph SVG gone. Photographic fig03 = JPEG, UI fig01/fig02 = PNG.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (94700), fig01 200 image/png 319636B, fig02 200 image/png 308746B, fig03 200 image/jpeg 39643B, all 3 `<img>` refs in DOM, old MF SVG absent, 0 progress residual, img count 3. ✅ Server stopped (SIGTERM exit 15 expected).

**Next:** Ray reviews L03 (esp. the blank-thumbnail flag #13 on fig01/fig02 — keep, or revert either graph to SVG?). Then M3 L04 `material_instances_and_parameters` (MI UI core) → L05 `special_material_types` (Substrate + Toon Shader — highest drift).

**Still FLAGGED for Ray, unresolved:** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit; (6) photographic figs now JPEG ×6 (M4 L02/L04/L05 fig01 + M3 L01/L02/L03 fig03) breaking the `.png`-only rule — recommend the guide formally allow JPEG-photographic/PNG-UI; (7) course-wide TOC-href-vs-section-id audit; (8) real figures partly ADDED vs swapped where sections lacked UI-mockup SVGs — confirm pattern; (9) sphere/result figs use the editor preview viewport, not Ray's level — confirm; (10) M3 L01 "Materials & Textures" submenu rephrase applied again here (L03 line 576) from knowledge, not a live menu check; (11) M3 L02 fig02 TextureSample preview swatch blank; (12) §Compression SVG "DXT1/DXT5" vs real "BC1 or BC3 with A"; **NEW (13):** M3 L03 fig01/fig02 node-graph captures show blank white preview thumbnails on FunctionInput/VectorParameter nodes (headless quirk, same root as #11) — keep or revert to SVG?

### Session 9 — 2026-07-08 (Sweep B — M3 L02 `texture_basics.html` — Texture Editor panel + real material node graph + textured sphere)

**Live state:** MCP bridge up (probe 200 + session id). Level `/Temp/Untitled_1` unchanged; camera at Ray's interior pose 4548.6,1063.9,789.4 / pitch −24.2 yaw −134.4; DirectionalLight selected. Editor confirmed restored at end (temp folder gone `exists`=false, camera at exact pose, DirectionalLight still selected).

**Scan (WSL grep):** L02 = 92932 B, 23 em-dashes (all pre-existing prose), **zero** version strings (5.4–5.7), **zero** drift terms (no Substrate/Toon/MegaLights/Nanite/Virtual Texture/UDIM/Marketplace). Foundational texture content (formats, importing, compression/mipmaps/sRGB, UV mapping, texture coordinates/tiling, hands-on) — stable UE5, unchanged 5.4→5.8. TOC clean (all 7 hrefs resolve). ⇒ figure-only pass, like L01. 9 SVGs / 6 Mermaid / 0 real captures pre-edit; two SVGs were hand-drawn node-graph mockups (§Texture Coordinates line 784, §Hands-On complete material).

**Ray's decisions (AskUserQuestion):** (1) prose = figure-only **+ minor UI touch-ups**; (2) figures = **all three** (Texture Editor Details + real Material Editor node graph + textured sphere).

**Live asset authoring:** `/Game` had **no textures** (find_assets Texture2D = []), so used read-only **engine textures**: `/Engine/EngineMaterials/T_Default_Material_Grid_M` (color grid, LinearColor sampler), `T_Default_Material_Grid_N` (normal), `T_Default_MacroVariation` (grayscale→roughness). Built temp material `/Game/MCP_Temp_L02/M_TexturedTiling` (TextureCoordinate + ScalarParameter `Tiling`=4 → **Multiply** → 3× TextureSample.UVs → BaseColor/Normal/Roughness) — first use of node-to-node `connect_expressions` (input pins UVs/Tex/Apply View MipBias; outputs RGB/R/G/B/A/RGBA; Multiply A/B). **Gotcha:** engine grid M is stored Linear, needed `SAMPLERTYPE_LinearColor`; MacroVariation needed `SAMPLERTYPE_Color` (compile error told us). Texture refs must be **full object paths** `Package.AssetName` (bare package path rejected).

**3 real captures:**
1. `images/m03_l02/m03_l02_fig01_texture_editor_settings.png` (982×1545 PNG, 125919 B) — real 5.8 **Texture Editor Details** panel of `/Engine/EngineMaterials/DefaultDiffuse` (a stone-tile albedo): info header (Format DXT1, **Number of Mips 11**, Streamed), Level Of Detail (Mip Gen Settings, LOD Bias, Texture Group World), Compression (**Compression Settings = Default (BC1 or BC3 with A)**), Texture (**sRGB ✓**). Chosen over the grid texture precisely because its sRGB is ON (color texture) — matches the sRGB teaching. **Added** to §Texture Settings after the intro. Directly serves the flagged compression/mipmaps/sRGB teaching.
2. `images/m03_l02/m03_l02_fig02_texture_coordinate_node.png` (1360×548 PNG, 187369 B) — real Material Editor graph: TextureCoordinate + `Tiling` scalar (4.0) → Multiply → Texture Sample UVs → Base Color. **Replaced** the §Texture Coordinates line-784 hand-drawn node SVG. ⚠️ **The Texture Sample node's inline preview swatch rendered BLANK/white** (see quirk below) — otherwise the wiring/labels are complete and correct. FLAGGED for Ray.
3. `images/m03_l02/m03_l02_fig03_textured_sphere.jpg` (660×700 JPEG q88, 122446 B) — the 3-texture material on the Material Editor **preview sphere**: red/cyan grid tiled ~4×, grainy roughness variation, normal relief, reflecting the scene. **Added** to Hands-On after Step 6 (before the Success Check). Like L01 fig C, this is the editor's preview viewport, not spheres placed in Ray's level (keeps his level untouched) — same interpretation Ray is reviewing from L01.

**Node-graph capture was hard (recorded for reuse):** the material graph canvas (SGraphPanel) exposes **no widget refs** to SlateInspector — cannot click/focus/zoom it. The toolbar **"Home" button = recenter-on-root-at-1:1**, NOT zoom-to-fit; PressKey Home does nothing (graph unfocused). At 1:1 a 3-sample graph overflows and the far-left nodes (TexCoord/Scalar) hide **behind the left Preview/Details panel**. Workaround that finally worked: (a) **simplify** to one Texture Sample (deleted the other two — fig03 sphere already captured with all three), (b) set compact node positions via `materialExpressionEditorX/Y` (camelCase), (c) **save + close + reopen** the editor (live graph does NOT re-read positions; only a reopen rebuilds from asset data) — on reopen the default view fits at "Zoom −2" showing the whole chain. **Blank-swatch quirk:** the Texture Sample node's inline texture preview renders **white** in most opens and is NOT fixed by recompile, re-setting the texture, `CaptureAssetImage` warming, waiting, or reopening (captures were byte-identical = deterministic, not a timing race). It DID render in some earlier opens — inconsistent, root cause unresolved. Accepted the blank swatch for fig02 and flagged it.

**Prose:** figure-only — the scan + captures revealed **no stale UI labels** (Texture Editor prose matches the real 5.8 panel), so no touch-ups were applied. One optional touch-up surfaced (NOT changed): the §Compression SVG labels Default compression "DXT1/DXT5" while the real 5.8 dropdown says "**BC1 or BC3 with A**" (same formats, older vs newer naming) — flagged for Ray.

**Invariants:** 92932→91104 (**−1828**: −line-784 SVG, +3 img/caption blocks); em-dashes **23 (0 new)** (WSL grep; captions use `&#183;`); all **7** TOC hrefs still resolve; 0 progress residual; old `brickPreview` SVG gone. Photographic fig03 = JPEG, UI fig01/fig02 = PNG (per the flagged JPEG-photographic/PNG-UI convention).

**QA:** served WSL `python3 -m http.server 8137`; page 200 (91104), fig01 200 image/png 125919B, fig02 200 image/png 187369B, fig03 200 image/jpeg 122446B, all 3 `<img>` refs in DOM, brickPreview SVG absent, 0 progress residual, img count 3. ✅ Server stopped (SIGTERM exit 15 expected).

**Next:** Ray reviews L02 (esp. the fig02 blank-swatch quirk — keep it, or fall back to keeping the line-784 SVG?). Then M3 L03 `building_complex_materials.html` → L04 `material_instances_and_parameters` (MI UI core) → L05 `special_material_types` (Substrate + Toon Shader — highest drift).

**Still FLAGGED for Ray, unresolved:** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit; (6) photographic figures now JPEG ×5 (M4 L02/L04/L05 fig01 + M3 L01 fig03 + M3 L02 fig03) breaking the `.png`-only rule — recommend the guide formally allow JPEG-photographic / PNG-UI; (7) course-wide TOC-href-vs-section-id audit; (8) real figures partly ADDED vs swapped where sections lacked UI-mockup SVGs — confirm pattern; (9) fig03/L01-figC use the editor preview viewport, not spheres in Ray's level — confirm; (10) M3 L01 "Materials & Textures" submenu rephrase from knowledge; **NEW (11):** M3 L02 fig02's Texture Sample node preview swatch renders **blank/white** (unresolved editor-capture quirk) — accept the figure, or revert to the hand-drawn line-784 SVG? **NEW (12):** §Compression SVG says "DXT1/DXT5"; real 5.8 dropdown says "BC1 or BC3 with A" — optional label modernization.

### Session 8 — 2026-07-08 (Sweep B — M3 L01 `material_fundamentals.html` — Material Editor + MI editor + material spheres, all built live)

**Live state:** MCP bridge up (probe 200 + session id). Level `/Temp/Untitled_1` unchanged (DirectionalLight selected; camera at Ray's interior pose 4548.6,1063.9,789.4 / pitch −24.2 yaw −134.4). First lesson to author **new content assets** live (not just capture existing scene state).

**Scan (WSL grep):** L01 = 89815 B, 27 em-dashes (all pre-existing prose), **zero** version strings (5.4–5.7), **zero** drift terms (no Substrate/Toon/MegaLights/Lightmass/Nanite/Marketplace). Foundational PBR content (materials vs textures, PBR philosophy, 4 core channels, Material Editor, Material Instances, hands-on) — all stable UE5, unchanged 5.4→5.8. TOC clean (all 8 hrefs resolve). ⇒ figure-only pass, like M4 L01/L02/L05.

**Ray's decisions (AskUserQuestion):** (1) prose = figure-only **+ touch up minor UI paths**; (2) figures = **all three** (Material Editor window + Material Instance editor + material sphere result).

**Live asset authoring (new technique — MaterialTools/MaterialInstanceTools):** built the exact hands-on material under a temp folder `/Game/MCP_Temp_L01`: `create_material` M_BasicColor → `add_expression` ×3 (1 VectorParameter `Base_Color`, 2 ScalarParameter `Metallic_Amount`/`Roughness_Amount`) → `ObjectTools.set_properties` to name them + set defaults + shared group "Appearance" (property names are **camelCase**: `parameterName`, `defaultValue` LinearColor {r,g,b,a}, `group`, `sortPriority`; `set_properties` `values` arg is a **JSON string**) → `connect_to_output` (MP_BaseColor/MP_Metallic/MP_Roughness) → `recompile` → `layout_expressions`. Then 2 MIs via `MaterialInstanceTools.create` + `set_vector_parameter`/`set_scalar_parameter` (setting a value auto-enables the override checkbox — needed for fig B). `EditorApp.OpenEditorForAsset` opens the asset editor window; asset editors dock as **tabs in one window** (opening a 2nd/3rd asset added tabs to the same w545).

**3 real captures (all SlateInspector, PowerShell→MCP-HTTP; window maximized via the Maximize titlebar button b587 for spacious panels; "Home" toolbar button = zoom-to-fit the node graph):**
1. `images/m03_l01/m03_l01_fig01_material_editor.png` (1800×797) — real 5.8 Material Editor of M_BasicColor: Preview sphere (top-left), Details panel (Material Domain/Blend Mode/Shading Model=Default Lit, lower-left), the 3 parameter nodes wired into the main material node (center graph, Home-framed), Palette docked right. Cropped out the bottom "Substrate — Material Simplification Preview" panel (a real 5.8 docked panel, non-destructively via image crop) + downscaled. **Replaced** the §4 hand-drawn SVG mockup.
2. `images/m03_l01/m03_l01_fig02_material_instance_editor.png` (780×857) — MI editor Details panel for MI_BasicColor_RedPlastic: Parameter Groups → Appearance with **3 checked override checkboxes** (Base_Color red swatch, Metallic_Amount 0.0, Roughness_Amount 0.3), Save Sibling/Save Child, General → Parent = M_BasicColor. Cropped to the Details panel. **Added** to §5 (directly addresses the flagged "MI UI" HIGH-drift item — §5 previously had no screenshot).
3. `images/m03_l01/m03_l01_fig03_material_spheres.jpg` (1384×518, JPEG q88) — the two instances rendered live in each MI editor's 3D preview viewport, cropped to the sphere and stitched side-by-side with burned labels: "Shiny Red Plastic · Roughness 0.3" (sharp specular highlight) vs "Matte Blue Rubber · Roughness 0.9" (fully diffuse). **Added** to the hands-on after the expected-result paragraph. (Interpreted Ray's "viewport" as the MI editor's live preview viewport — a real render with scene reflections — to avoid mutating Ray's level; noted for confirmation.)

**Prose UI touch-ups (Ray-approved):** reordered the §4 "Key Interface Elements" bullets to match the real 5.8 **default** layout (Graph Canvas/Preview Top-Left/Details Lower-Left/Palette Right) and dropped the circled ①-④ references (real capture has no numbered overlays; added a note that panels are dockable). Dropped the stale UE4-era "**Materials & Textures →**" submenu label in Method 2 + the hint (rephrased to the version-robust "creation menu"/"+Add" wording rather than assert a specific 5.x submenu name I couldn't 100%-confirm without digging into Ray's live content-browser menu — flagged as a judgment call).

**Editor restored:** `AssetTools.delete("/Game/MCP_Temp_L01")` (folder gone, verified `exists`=false; the call timed out on the HTTP wrapper but completed server-side), temp asset-editor window closed, all observers Unobserved, camera confirmed still at Ray's exact pose (never moved — SlateInspector worked on separate windows, no SetCameraTransform), DirectionalLight still selected.

**Invariants:** 89815→80711 (**−9104**: −160-line §4 SVG mockup, +3 img/caption blocks, net); em-dashes **27 (0 new)** (WSL grep -o confirmed; captions use `&#183;`); all **8** TOC hrefs still resolve; residuals 0 (SVG comment / "Materials & Textures" / ①-④ all gone).

**QA:** served WSL `python3 -m http.server 8137`; page 200 (80711), fig01 200 image/png 566278B, fig02 200 image/png 104451B, fig03 200 image/jpeg 51557B, all 3 `<img>` refs in DOM, 0 progress residual, old SVG mockup absent. ✅ Server stopped (SIGTERM exit 15 expected).

**Next:** Ray reviews L01 (esp. the 3 real captures + the "MI editor preview viewport = fig C" interpretation + the "Materials & Textures" rephrase). Then M3 L02 `texture_basics.html` → L03 → L04 (`material_instances_and_parameters` — MI UI core) → L05 (`special_material_types` — Substrate + Toon Shader, highest drift).

**Still FLAGGED for Ray, unresolved:** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit; (6) photographic figures now JPEG ×4 (M4 L02/L04/L05 fig01 + M3 L01 fig03) breaking the `.png`-only naming rule — recommend the guide formally allow JPEG-photographic / PNG-UI and update `image_style_guide.md` if approved; (7) course-wide TOC-href-vs-section-id audit (M4 + M3 L01 clean, M4 L03 wasn't); (8) M4 L05 / M3 L01's real figures were partly ADDED (not swapped) where sections lacked UI-mockup SVGs — confirm that's the desired pattern. **NEW (9):** M3 L01 fig C uses the MI editor's live preview viewport rather than spheres placed in Ray's level — confirm that reading of "viewport" is acceptable (chosen to keep his level untouched). **NEW (10):** the "Materials & Textures" submenu rephrase was made from knowledge, not a live menu check — confirm the 5.8 label if Ray wants the exact submenu name restored.

### Session 7 — 2026-07-08 (Sweep B — M4 L05 `post_process_effects.html` — cinematic before/after + real PP panels)

**Live state:** MCP bridge up (probe 200 + session id). Level `/Temp/Untitled_1` unchanged (full outdoor+interior scene; DirectionalLight selected; camera at Ray's interior pose 4548.6,1063.9,789.4 / pitch -24.2 yaw -134.4). No pre-existing PostProcessVolume in the level (clean baseline).

**Scan (WSL grep):** L05 = 115106 B, 24 em-dashes (all pre-existing prose), **zero** version strings (5.4/5.5/5.6), **zero** drift terms (no MegaLights/Lightmass/Marketplace/Substrate/Nanite/deprecated). 15 "lumen" hits all in the accurate "AO + Lumen interaction" context. Post-process prose fully version-accurate for 5.8 (PP Volumes, EV100 auto-exposure Histogram/Basic/Manual, Color Grading Global/Shadows/Midtones/Highlights + White Balance + LUT, Bloom Standard/Convolution, lens flares/dirt/vignette/chromatic aberration, AO SSAO/GTAO-default/RTAO/DFAO). **No prose drift -> figure-only pass, like L01/L02.** TOC clean: all 8 hrefs resolve to real section ids (no L03-style dead-anchor defect). Optional note surfaced (NOT changed): Exposure section omits Local Exposure, but that shipped in UE 5.2 (pre-5.4 baseline), out of scope.

**Ray's decisions (AskUserQuestion):** (1) prose **as-is** (leave Local Exposure out); (2) figures **flagship before/after viewport + 2 Slate Details panels**.

**Capture method (all via ONE temp unbound PPV `MCP_TempPPV_L05`, priority 100):** EditorApp has no SetCVar, so post-process was toggled by adding an unbound PPV and setting `Settings` overrides via `ObjectTools.set_properties` (nested struct: `bOverride_*` flags + FVector4 color-grade vectors `{X,Y,Z,W}` + floats + enum string `"AEM_Histogram"` all accepted). **New gotcha (recorded):** a freshly spawned actor placed near the camera leaves an orange 3-axis **orbit-pivot** marker in-frame that `bShowUI:false` does NOT hide and clearing selection / re-asserting the camera does NOT remove; the fix is to place the temp actor **off-frame** (here 54548,51063,789, behind the camera) so the marker projects out of shot. (L04's flagship was clean because its PPV happened to sit off-frame.)

**3 real captures:**
1. `images/m04_l05/m04_l05_fig01_post_process_before_after.jpg` (1400x343, 42206 B) - **flagship**. Two `EditorApp.CaptureViewport` from Ray's identical interior pose: "before" = PPV present, no overrides (neutral, warm, flat); "after" = strong cinematic grade (ColorSaturation 0.8, ColorContrast 1.2, ColorGainShadows teal, ColorGainHighlights warm, WhiteTemp 4700, VignetteIntensity 0.85, BloomIntensity 2.0, AutoExposureBias -0.6, AO 0.8, SceneFringeIntensity 2.5). Cropped bottom 210px gizmo, each half scaled to 698w, 4px divider, burned "Before: No Post-Process" / "After: Cinematic Grade" labels, JPEG q88. Inserted after the Post-Process Pipeline SVG in Section 1 (concept -> real result). First push was too subtle in the blown-out white room, so the grade was strengthened + exposure pulled down so the whites stopped clipping and the grade registered.
2. `images/m04_l05/m04_l05_fig02_exposure_settings.png` (956x1056, 94591 B) - real `SlateInspector` capture of the PPV Details filtered to "Exposure": Metering Mode = Auto Exposure Histogram, Exposure Compensation -0.6, Min EV100 6.0, Max EV100 13.0, Speed Up/Down 2.0 (values pre-set to match Hands-On Step 3). Cropped out the top actor-list strip (hides the temp actor name) + trimmed below Speed Down. Added to Section 2 after the auto-exposure settings prose.
3. `images/m04_l05/m04_l05_fig03_color_grading_settings.png` (956x982, 63575 B) - real `SlateInspector` capture of the Color Grading category (selected via the Color Grading filter chip), Global subsection expanded showing Saturation + Contrast overridden alongside Gamma/Gain/Offset, with Temperature/Shadows/Midtones/Highlights/Misc subsections. Added to Section 3 after the Basic Color Adjustments prose.

**Add vs replace:** all 3 were **added**, not swapped for SVGs - Sections 1/2/3 had no UI-mockup SVGs to replace (their existing SVGs are legit concept diagrams: pipeline, EV scale, auto-exposure flow, adjustment swatches, tonal ranges). Flagged to Ray since his option text mentioned "replacing the weakest mockups."

**Editor restored:** temp PPV `remove_from_scene` (verified gone via `find_actors` = []), DirectionalLight reselected, both SlateInspector observers Unobserved, camera confirmed still at Ray's exact pose (used `captureTransform`, and the one `SetCameraTransform` was to the identical pose).

**Invariants:** 115106->117640 (**+2534**, all image markup + 3 captions); em-dashes **24 (0 new)** (captions use `&#183;` + hyphens); all **8** TOC hrefs still resolve; 21 captions total; 0 progress-bar residual.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (117640), fig01 200 image/jpeg 42206B, fig02 200 image/png 94591B, fig03 200 image/png 63575B, all 3 `<img>` refs in DOM, 0 progress residual. Passed. Server stopped (SIGTERM exit 15 expected).

**M4 Lighting Sweep B now COMPLETE (l01-l05).** Next: **M3 Materials** (Substrate/Toon Shader/MI UI - HIGH drift). Then Build C (new Module 11 - AI-Assisted Workflows / Unreal MCP), captured live.

**Still FLAGGED for Ray, unresolved:** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (4) Bonus Marketplace->Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted - offer WSL re-audit; (6) photographic figures are now JPEG x3 (L02 fig01, L04 fig01, L05 fig01) breaking the `.png`-only naming rule - recommend the guide formally allow JPEG-photographic / PNG-UI and update `image_style_guide.md` if approved; (7) course-wide TOC-href-vs-section-id audit (L04+L05 clean, L03 wasn't). **NEW (8):** the 3 real figures were ADDED (not replacements) because these sections lacked UI-mockup SVGs - confirm that's the desired pattern for figure-only sections vs. swapping concept SVGs.

### Session 6 — 2026-07-08 (Sweep B — M4 L04 `lumen_global_illumination.html` — MegaLights + real captures)

**Live state:** MCP bridge up (probe 200 + session id). Level `/Temp/Untitled_1` unchanged (full outdoor scene, DirectionalLight selected, camera at Ray's interior pose 4548.6,1063.9,789.4 / pitch −24.2 yaw −134.4). `r.DynamicGlobalIlluminationMethod` = 1 (Lumen).

**Scan (WSL grep):** L04 = 98524 B, 38 em-dashes (all pre-existing prose), **zero** version strings (5.4/5.5/5.6), zero Substrate/Nanite/Marketplace/Lightmass. Lumen prose fully version-accurate for 5.8 (default GI, Surface/Radiance cache, SW-default vs HW RT, project-settings names, Hit Lighting for Reflections). No prose drift.

**FLAG #3 REFRAMED + RESOLVED.** The tracker predicted "MegaLights lives here; doc says prod-ready vs live Experimental." **False premise — MegaLights appears NOWHERE in the course** (`grep -ril megalight` across all HTML = 0; "lumen-lite" = 0; the 3 "production-ready" hits are unrelated install-channel/Blueprints prose). So flag #3 was never a contradiction; it was a **content gap** — a headline UE 5.5→5.8 lighting feature entirely absent from the lighting module. Surfaced to Ray as a gap decision.

**Ray's decisions (AskUserQuestion):** (1) MegaLights → **author a full section**; (2) figures → **Lumen on/off viewport + 2 real Slate panels** (replace the 2 weakest UI-mockup SVGs).

**Authored — Section 7 "MegaLights (Experimental in UE 5.8)"** (id `megalights`, inserted between When-to-Use-Lumen and Hands-On; new TOC entry + Learning-Objective bullet; renumbered Hands-On→8 / Summary→9 comments): Experimental card, "shadowed lights are expensive" problem, stochastic-sampling + temporal/spatial denoiser (with a concept SVG: many lights → sample few per pixel → denoise → fixed cost), "MegaLights + Lumen are complementary" (Lumen = indirect GI/reflections, MegaLights = direct many-light shadows), requirements (HWRT + DX12/SM6), enable steps, when-to-use, Experimental watch-outs. All prose em-dash-free (`&#183;` separators).

**3 real captures (all via ONE temp unbound PostProcessVolume `MCP_TempPPV_L04`, priority 100):**
1. `images/m04_l04/m04_l04_fig01_lumen_on_off.jpg` (1400×343, 41413 B) — **flagship** side-by-side. Two `EditorApp.CaptureViewport` from the identical interior camera; Lumen toggled by setting the PPV `Settings.bOverride_DynamicGlobalIlluminationMethod`+`ReflectionMethod` override to `None` (off) then resetting (on). Cropped the viewport orientation gizmo (bottom 210 px), scaled each half to 698 w, 4 px divider, burned "Lumen ON"/"Lumen OFF" labels (System.Drawing), JPEG q88. Shows the honest difference: on = warm color bleed + soft corner occlusion; off = flat, cold, over-bright ambient. Inserted at end of Section 1.
2. `images/m04_l04/m04_l04_fig02_project_settings_gi.png` (1160×296, 17062 B) — real `SlateInspector` capture of **Project Settings → Engine → Rendering → Global Illumination → Dynamic Global Illumination Method = Lumen**. Opened Project Settings via the Edit menu (Click b29 → Click g169 "Project Settings…"), filtered its search to "Global Illumination", screenshot the results list `g195`, cropped tight. **Replaced** the Hands-On Step-1 Project-Settings SVG.
3. `images/m04_l04/m04_l04_fig03_ppv_lumen_settings.png` (800×1174, 70197 B) — real `SlateInspector` capture of the **Post Process Volume Details filtered to "Lumen"** (Ray Lighting Mode, Lumen Scene Lighting Quality, Lumen Scene Detail, Final Gather Quality, Screen Traces, Max Trace Distance, Advanced group). Select PPV → Observe → filter Details search `tb1` to "Lumen" → Screenshot list `g8`. **Replaced** the Section-5 Post-Process SVG.

**New capture technique (reusable):** EditorApp toolset has **no SetCVar** — to toggle Lumen on/off non-destructively, add an unbound Post Process Volume and flip `Settings.bOverride_DynamicGlobalIlluminationMethod`/`DynamicGlobalIlluminationMethod` via `ObjectTools.set_properties` (nested struct + `bOverride_*` flags + enum string `"None"` all accepted). Opening a settings window: main menu buttons open a **separate top-level popup window** (appears at the tail of a full `Snapshot`); click the menu button, snapshot all windows, click the item ref.

**Editor restored:** Project Settings window closed (`Windows close index 1`), Details "Lumen" filter cleared (Click tb1 → Ctrl+A → Delete), temp PPV `remove_from_scene` (verified gone via `find_actors`), DirectionalLight reselected, both observers `Unobserve`d. Viewport camera never moved (used `captureTransform` param, not `SetCameraTransform`).

**Invariants:** 98524→108581 (authoring) →103744 final (**+5220** net: +10057 authored MegaLights, −4837 from the two SVG→img swaps); em-dashes **38 (0 new)**; all **9** TOC anchors resolve to real section ids (no L03-style dead-anchor defect here); 0 progress-bar residual.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (103744), fig01 200 image/jpeg 41413B, fig02 200 image/png 17062B, fig03 200 image/png 70197B, all 3 `<img>` refs present, `#megalights` section + TOC link + h2 present, 0 progress residual. ✅

**Still FLAGGED for Ray (flag #3 now RESOLVED):** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit; (6) photographic captures are JPEG (now 2: L02 fig01 + L04 fig01) vs the `.png`-only naming rule — recommend the guide formally allow JPEG-photographic / PNG-UI; (7) course-wide TOC-anchor-vs-section-id audit (L04 was clean, but L03 wasn't — worth a sweep).

**Next:** Ray reviews L04 (esp. the on/off flagship + MegaLights section). Then M4 L05 (`post_process_effects.html`), then M3 Materials.

### Session 5 — 2026-07-08 (Sweep B — M4 L03 `interior_lighting.html`)

**Live state:** MCP bridge up (full toolset registry incl. SlateInspector + EditorApp + SceneTools). Level `/Temp/Untitled_1` unchanged full outdoor scene; only lights present were the DirectionalLight + SkyLight (no Point/Spot).

**Scan (WSL grep):** L03 = 82466 B, 26 em-dashes (all pre-existing prose), **zero** version strings (5.4/5.5/5.6), **zero** drift terms — no MegaLights/Lightmass/Marketplace/Nanite/VSM/raytrace and **no "Lumen" GI** (the 12 `lumen` hits are all the photometric unit *lumens*). Point/Spot/Rect/IES/Light Functions are stable UE5, unchanged 5.4→5.8. ⇒ no prose drift in scope (figure-only, like L01/L02).

**Discovered a pre-existing CONTENT BUG (not version drift):** the sticky TOC listed 8 sections but two of them — **IES Profiles** (`#ies-profiles`) and **Light Functions** (`#light-functions`) — had **no body content**; the lesson jumped Rect Lights → Hands-On. Yet both topics were promised in Learning Objectives, used in the Hands-On steps (Step 6 IES, Step 7 Light Function), fully covered in the Summary, tested in Knowledge Check (Q3 IES, Q5 Light Functions), and shown in the summary toolkit SVG. Net: **3 dead TOC anchors** (`#ies-profiles`, `#light-functions`, and `#hands-on` — whose section id was actually `hands-on-exercise`).

**Ray's decision:** **Author both missing sections** (option A) — real teaching prose + real editor captures + concept diagrams — and fix the anchor.

**Work done:**
- Authored **Section 5: IES Profiles** (id `ies-profiles`): what an IES profile describes (photometric web), 4 distribution shapes (Spot/Flood/Wall Wash/Batwing) as an inline SVG, importing a `.ies` (Texture Light Profile asset), applying via the **Light Profiles** category (IES Texture / Use IES Intensity / IES Intensity Scale), use cases, Pro-Tip.
- Authored **Section 6: Light Functions** (id `light-functions`): Material Domain = Light Function, Emissive-as-mask, creating the material, a flicker graph (Time → Noise → Lerp 0.5–1.0 → Emissive) as a Mermaid diagram, applying via the **Light Function** category (Movable-only), Watch-Out (cost), use cases (fire/gobos/caustics/failing fluorescents/TV glow), Pro-Tip (animate via Time node).
- Fixed the dead anchor: TOC `#hands-on` → `#hands-on-exercise` (matches the existing section id; all 8 TOC links now resolve).

**Figures added (2 real captures + 2 concept diagrams):**
1. `images/m04_l03/m04_l03_fig01_ies_texture_slot.png` (812×308, 18512 B) — SlateInspector capture of the **Light Profiles** category (IES Texture asset slot, Use IES Intensity checkbox, IES Intensity Scale) in a Spot Light's Details, isolated via the Details search box filtered to "IES".
2. `images/m04_l03/m04_l03_fig02_light_function_slot.png` (812×372, 26915 B) — same technique filtered to "Light Function": Light Function Material slot, Light Function Scale, Fade Distance, Disabled Brightness.
3. Inline SVG — four IES distribution shapes. 4. Inline Mermaid — the flicker node flow. (Concepts kept synthetic per style guide.)

**Capture method (non-destructive):** scene had no Point/Spot light, so added a temp **SpotLight** (`add_to_scene_from_class` `/Script/Engine.SpotLight`, parked at z=100000), `SelectActors` it, `Observe` w1, filtered the Details search box (`tb1`) to "IES" then "Light Function", `Screenshot` the results list (`g8`) each time, cropped to content (PowerShell System.Drawing). Then **fully restored**: cleared the search (Ctrl+A/Delete), `remove_from_scene` the temp SpotLight (verified gone, back to 156 actors), reselected the DirectionalLight, `Unobserve`. New text-snapshot helper script at this session's scratchpad `mcp_text.ps1` (saves a tool's string `returnValue` to a file, DataPath default `returnValue`) — companion to `mcp_capture.ps1`.

**Invariants:** 82466→95746 (**+13280**, authored content); em-dashes **26 (0 new)**; both new section ids present; all 8 TOC links resolve to real sections; no progress-bar residual.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (95746), fig01 200 image/png 18512B, fig02 200 image/png 26915B, both new sections + both `<img>` + captions in DOM, `#hands-on-exercise` id present, no dead `#hands-on`, 0 progress-bar residual. ✅

**Still FLAGGED for Ray (unchanged):** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (3) MegaLights "Experimental" (live) vs "prod-ready" (doc) — resolve in L04; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit; (6) L02 fig01 is `.jpg` (photographic viewport) breaking the `.png`-only naming rule — recommend allowing JPEG for photographic captures / PNG for UI panels; if approved, update `image_style_guide.md`. **NEW (7):** other lessons may carry the same missing-section / dead-anchor defect L03 had — worth a course-wide TOC-anchor-vs-section-id audit (offer).

**Next:** Ray reviews L03. Then M4 L04 (`lumen_global_illumination.html` — MegaLights lives here) → L05, then M3 Materials.

### Session 4 — 2026-07-08 (Sweep B — M4 L02 `directional_light_and_sky.html`)

**Live state:** MCP bridge up (probe: 200 + session id). Level `/Temp/Untitled_1` is now a **full outdoor scene** — DirectionalLight + SkyAtmosphere + SkyLight + ExponentialHeightFog + VolumetricCloud + Landscape (World Partition, 8×8 proxies) + interior archviz meshes + a SkeletalMeshActor (156 actors). So both L02 captures needed **zero scene mutation**.

**Scan (WSL grep):** L02 = 99604 B, 25 em-dashes (all pre-existing prose), **zero** version strings (5.4/5.5/5.6), **zero** drift terms (no MegaLights/Lightmass/Marketplace/deprecated/raytrace/Nanite/VSM). 24 Lumen mentions, all generic/accurate. ⇒ **No prose drift in 5.4→5.8 scope; figure-only pass** (Ray confirmed A+B). Optional note surfaced (NOT changed): CSM section omits that Virtual Shadow Maps are default in Lumen projects — but that predates 5.4, so out of scope.

**Ray's decision:** figures **A + B**.

**Figures added (both real, non-destructive):**
1. `images/m04_l02/m04_l02_fig01_outdoor_sky.jpg` (1400×675, 83445 B) — live `EditorApp.CaptureViewport` of the existing outdoor scene from a placed camera (loc −12000,−12000,2500; pitch −6, yaw −136, toward the pitch-−16° sun). Shows all four lesson components + volumetric clouds. Cropped bottom 227px to remove the viewport axis gizmo, downscaled, re-encoded JPEG q88 (PNG was 1.3MB → JPEG 83KB; **first photographic raster figure in the course — flag format choice to Ray**). Inserted in Hands-On after the synthetic "Complete Outdoor Lighting Setup" SVG (diagram → real result).
2. `images/m04_l02/m04_l02_fig02_atmosphere_sun_light.png` (806×121, 8113 B) — `SlateInspector` capture of the DirectionalLight Details panel filtered via the search box to **Atmosphere Sun Light** (checkbox **enabled/checked**, under "Atmosphere and Cloud"). Docked panel was fine (a single checkbox fits the narrow value column — no undock needed, unlike L01's Mobility toggle). Inserted in Section 1 right after the "Atmosphere Sun Light:" property paragraph.

**Capture-pipeline notes (reusable):** `EditorApp.CaptureViewport` via the MCP HTTP wrapper **requires** the "optional" params `captureTransform` + `annotations` to be present (wrapper errors "needs a default value" otherwise) — pass current camera transform + annotations with gridSpacing/maxLabelDistance 0 to disable overlays. `SlateInspector.Screenshot` base64 is at `returnValue.data`; `CaptureViewport` at `returnValue.image.data` (script `-DataPath`). Details-panel search-box filtering (Click textbox → Type → Screenshot the list → clear via Ctrl+A/Delete) is a clean way to isolate one property. Coords in Slate snapshots are physical px (~2.19× the logical window size).

**Editor left as found:** camera restored to Ray's original interior pose (4548.6,1063.9,789.4 / pitch −24.2 yaw −134.4); Details search filter cleared; observer removed; DirectionalLight left selected.

**QA:** served WSL `python3 -m http.server 8137`; page 200 (100810), fig01 200 image/jpeg 83445B, fig02 200 image/png 8113B, both `<img>`+captions in DOM, 0 progress-bar residual. ✅

**Still FLAGGED for Ray (unchanged):** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (3) MegaLights "Experimental" (live) vs "prod-ready" (doc) — resolve in l04; (4) Bonus Marketplace→Fab rename; (5) prior sessions' em-dash counts may be PS-undercounted — offer WSL re-audit. **NEW flag:** (6) first photographic figure is JPEG (`.jpg`), breaking the `.png`-only naming convention in `image_style_guide.md` — confirm JPEG is OK for photographic viewport captures (recommended; PNG was 16× larger).

**Next:** Ray reviews L02. Then M4 L03 (`interior_lighting.html`) → L04 (MegaLights) → L05, then M3 Materials.

### Session 3 — 2026-07-08 (Sweep B begins — M4 L01 `lighting_fundamentals.html`)

**Live state re-verified:** Unreal MCP bridge up (SlateInspector + EditorApp + SceneTools). Level `/Temp/Untitled_1` has a DirectionalLight. `m04_l01_introduction_to_lighting.html` still **0 bytes** (dupe flag stands); index links 4.1 → `lighting_fundamentals.html` (110267 B pre-edit).

**Ray's decisions this session:**
1. **MegaLights → SKIP in L01, defer to L04.** Full-file scan (grep Lumen/MegaLights/Lightmass/bake/5.4-5.6/raytrace) found **no MegaLights mention** in L01 and everything else version-accurate for 5.8 (UE4→UE5 Lumen evolution, Lumen SW/HW RT in Performance section all still true). ⇒ **no prose drift to fix**; this pass is figure-only.
2. **Build the Mobility capture now.**

**Figure added:** `images/m04_l01/m04_l01_fig01_mobility_control.png` (810×60, 5949 B) — real SlateInspector capture of the Mobility row in the DirectionalLight Details panel, **full Static/Stationary/Movable labels** (Movable selected). Inserted in "How to Change Light Mobility" before the Pro-Tip card, with caption (`&#183;` separators, 0 new em-dashes) + alt text. **110267→110842 (+575).**

**Capture pipeline established (REUSABLE — see memory `unreal-mcp-image-capture-http`):** SlateInspector `Screenshot` returns base64 in the tool result, which cannot be reliably hand-transcribed to disk (large base64 corrupts). Solution: drive the editor's MCP HTTP endpoint `http://127.0.0.1:8000/mcp` directly from PowerShell (initialize → notifications/initialized → tools/call `call_tool`), parse the SSE `data:` line → `result.content[0].text` (escaped JSON) → `returnValue.data`, decode base64 to PNG. Zero transcription. Needed for Build C (Module 11) captures.

**Capture quirks (RESOLVED):** docked Details panel value column is collapsed by default → Mobility toggle unreadable; docked drags only clipped it to "Stat/Stat/Mov". The `Drag(co17→b47)` actually **undocked** Details into a floating window (658 wide, properties list 632 units) — there the toggle renders **full labels**. Recaptured the Mobility row (`g61`) from the floating window (1422×60) and stitched out the wide name-column gap → final 810×60. NB: **left Ray's editor with Details floating** (offered to re-dock). Lesson for future captures: undock a panel to a floating window when its docked column is too narrow.

**QA:** served dir (WSL `python3 -m http.server 8137 --bind 0.0.0.0`), HTTP checks: page 200 (110899), image 200 (image/png, 6052 B), img tag + caption present in DOM. ✅

**Still FLAGGED for Ray (unresolved):** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (3) MegaLights "Experimental" (live) vs "prod-ready" (doc) — to be handled in L04; (4) Bonus Marketplace→Fab rename pending. Also: **25** pre-existing em-dashes in L01 prose (untouched; I added 0). ⚠️ **Tooling note:** count em-dashes with WSL `grep -o "—" file | wc -l`, NOT PowerShell 5.1 `Get-Content` — PS reads the UTF-8 files as ANSI and badly undercounts (reported 3 vs actual 25). Applies to all em-dash invariant checks this initiative.

**Next:** Ray reviews L01 (esp. mobility figure). Then M4 L02 → L03 → L04 (MegaLights lives here) → L05, then M3 Materials.

### Session 2 — 2026-07-07 (Sweep A — COMPLETE; Archetype D finish + browser QA)

**Edit protocol used:** `Filesystem:edit_file` dryRun→commit→`get_file_info`; byte-delta invariants tracked per file; zero new em-dashes.

**Byte-delta invariants (canonical, for remaining files):**
- Version string `Unreal Engine 5.4+`→`UE 5.8` = **−12 bytes** per hit.
- Archetype C inline scroll-block removal = **−330 bytes** per file.
- Archetype D = top markup block (−122) + inline scroll block (−330) = **−452 bytes** per file (VERIFIED across all 22 this session; the earlier −114/−444 estimate undercounted the markup block by 8 bytes; actual markup removal is 122 bytes incl. the blank line).

**b) Version edits — DONE (all 4):**
- `index.html`: Software info-card + system-requirements list → both `UE 5.8`. 38261→38237 (−24). ✅
- `intro_to_unreal_curriculum.md`: Software Required + Engine Version Target → both `UE 5.8`. 14862→14838 (−24). ✅

**c) Strip scroll indicator:**
- SHARED — DONE:
  - `styles/main.css`: removed `.progress-indicator` + `.progress-bar` rule blocks (retitled section "Interactive Elements") + removed `.progress-indicator` from `@media print` display:none list. → 18241 bytes. ✅ (index.html's `.progress-bar-container`/`.progress-fill` untouched — KEEP per-module completion bars.)
  - `js/course-enhancements.js`: removed reading-time block + progress-indicator scroll-listener block from DOMContentLoaded handler; syntax-highlight/canvas-note/ARIA/keyboard-nav intact. → 8668 bytes. ✅
- Archetype A (14 files, external-JS-only) — no body edits needed: m01_l01–04, m02_l01–05, m05_l01–05.
- Archetype B (3 files, already clean) — skip: m03_l01, m03_l02, m03_l03, m04_l01_introduction_to_lighting.
- Archetype C (inline scroll block only) — **DONE, all 5, each −330:** m03_l04 (97278→96948), m03_l05 (122585→122255), m04_l01_lighting_fundamentals (110597→110267), m04_l02 (99934→99604), m04_l03 (82796→82466). ✅
- Archetype D (top markup + inline scroll block): **DONE, all 22.** Each verified: both blocks matched exactly once, delta exactly −452, residual `progress-bar`/`progress-container` count 0, on-disk length re-read after write.
  - ✅ m04_l04_lumen_global_illumination (→98524, prior session).
  - ✅ 21 this session (each −452): m04_l05 (115558→115106), m06_l01 (86937→86485), m06_l02 (108111→107659), m06_l03 (95060→94608), m06_l04 (76215→75763), m06_l05 (94158→93706), m07_l01 (94967→94515), m07_l02 (92710→92258), m07_l03 (92229→91777), m07_l04 (99456→99004), m07_l05 (99420→98968), m08_l01 (95891→95439), m08_l02 (95604→95152), m08_l03 (93446→92994), m09_l01 (90150→89698), m09_l02 (91706→91254), m09_l03 (86441→85989), m10_l01 (79899→79447), m10_l02 (77719→77267), m10_l03 (81017→80565), bonus_using_marketplace_assets (71631→71179).

**d) FLAGGED (not resolved — Ray's call):**
- Duplicate m04_l01 files, NOT identical: `m04_l01_introduction_to_lighting.html` (clean/Archetype B) vs `m04_l01_lighting_fundamentals.html` (was Archetype C, now scroll-stripped). index.html links Lesson 4.1 → `m04_l01_lighting_fundamentals.html`. Needs keep/delete decision.
- Materials/lighting filename dupes flagged for same review.

**e) Browser spot-check: DONE** (served dir from WSL via `python3 -m http.server 8137`, viewed in Chrome). m07_l01 (Archetype D): renders clean, no scroll-progress strip, header/nav/breadcrumb/title/objectives all intact. index.html: DOM check `scrollProgressPresent:false`; all 10 per-module `.progress-fill` bars present at width:100% (Module 1 renders full green bar); Software card shows `UE 5.8`. No layout regressions on either page.

**Sweep A CLOSED (2026-07-07).** All mechanical work complete: version strings → UE 5.8 (verified zero 5.4/5.5/5.6 drift course-wide), scroll progress indicator stripped everywhere (markup + JS + CSS; DOM-confirmed gone across all HTML), browser QA ×2 passed. Per-module completion bars on index preserved.
**Next: Sweep B** (per-lesson content, highest drift first: M4 Lighting, then M3 Materials, then the rest) per `image_style_guide.md`, with live-RNA validation before each edit; then Build C (new Module 11). FLAGGED for Ray, still open: m04_l01 dupe (`introduction_to_lighting` vs `lighting_fundamentals`; index links 4.1 → `lighting_fundamentals`) + materials/lighting filename dupes. Bonus 'Marketplace'→'Fab' rename is part of Sweep B.

### Agreed execution order (2026-07-07)
1. **Sweep A** (mechanical, whole-course): version strings 5.4→5.8 across all files + strip scroll progress indicator (markup+JS+CSS) everywhere → spot-check browser QA on 2 lessons.
2. **Sweep B** (per-lesson content), highest drift first: **M4 Lighting** (Lumen/MegaLights/Lumen-Lite), then **M3 Materials** (Substrate/Toon Shader), then the rest. Live-RNA validation before each edit; real captures per `image_style_guide.md`.
3. **Build C**: new **Module 11 — AI-Assisted Workflows** (Unreal MCP), captured live while bridge is up.

### Session 1 — 2026-07-07 (Phase 0 complete)
- Reconciled true course state vs stale docs: course is **content-complete** (10 modules, 38 lessons), NOT 20%. `parts/` = old numbering fossil (M3 was Blueprints). Source of truth = index.html + combined root files.
- Confirmed UE 5.8 shipped + official Experimental MCP plugin; live bridge verified with SlateInspector (UI screenshots) + EditorApp (viewport capture) toolsets.
- Wrote `unreal_58_update_progress.md` (this file) + `image_style_guide.md`; corrected stale `continue.md`.
- Resolved 3 decisions: version→"UE 5.8"; progress bar→strip everywhere; MCP→new Module 11.
- **Next session:** start fresh chat, read this file, begin Sweep A.
