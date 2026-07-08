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
| m03_l01–05 | ✅ | ☐ | ☐ | HIGH drift; scroll-strip ✅ l04/l05 (−330); l01–03 Archetype B clean |
| m04_l01–05 | ✅ | ◐ | ◐ | HIGH drift; scroll-strip ✅ (l01_fundamentals/l02/l03 −330, l04/l05 −452); l01_introduction_to_lighting Archetype B clean. **Sweep B l01 (2026-07-08):** content version-accurate as-is (only drift was MegaLights → deferred to l04 per Ray); real fig01 mobility_control.png added (110267→110899, +632); browser QA ✅. l02–05 Sweep-B pending. |
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

### Session 3 — 2026-07-08 (Sweep B begins — M4 L01 `lighting_fundamentals.html`)

**Live state re-verified:** Unreal MCP bridge up (SlateInspector + EditorApp + SceneTools). Level `/Temp/Untitled_1` has a DirectionalLight. `m04_l01_introduction_to_lighting.html` still **0 bytes** (dupe flag stands); index links 4.1 → `lighting_fundamentals.html` (110267 B pre-edit).

**Ray's decisions this session:**
1. **MegaLights → SKIP in L01, defer to L04.** Full-file scan (grep Lumen/MegaLights/Lightmass/bake/5.4-5.6/raytrace) found **no MegaLights mention** in L01 and everything else version-accurate for 5.8 (UE4→UE5 Lumen evolution, Lumen SW/HW RT in Performance section all still true). ⇒ **no prose drift to fix**; this pass is figure-only.
2. **Build the Mobility capture now.**

**Figure added:** `images/m04_l01/m04_l01_fig01_mobility_control.png` (725×60, 6052 B) — real SlateInspector capture of the Mobility row in the DirectionalLight Details panel. Inserted in "How to Change Light Mobility" before the Pro-Tip card, with caption (`&#183;` separators, 0 new em-dashes) + alt text. **110267→110899 (+632).**

**Capture pipeline established (REUSABLE — see memory `unreal-mcp-image-capture-http`):** SlateInspector `Screenshot` returns base64 in the tool result, which cannot be reliably hand-transcribed to disk (large base64 corrupts). Solution: drive the editor's MCP HTTP endpoint `http://127.0.0.1:8000/mcp` directly from PowerShell (initialize → notifications/initialized → tools/call `call_tool`), parse the SSE `data:` line → `result.content[0].text` (escaped JSON) → `returnValue.data`, decode base64 to PNG. Zero transcription. Needed for Build C (Module 11) captures.

**Capture quirks (for later polish):** docked Details panel value column is collapsed by default (name column eats ~all width) → Mobility toggle unreadable. Widened via SlateInspector `Drag(co17→b47)` which moved the dock divider (panel 134→323 units); a 2nd drag was byte-identical (maxed). At max width the 3 toggle buttons still clip to **"Stat / Stat / Mov"** (Static/Stationary/Movable) — caption disambiguates. A cleaner full-label recapture would need Ray to pre-widen the panel or undock Details.

**QA:** served dir (WSL `python3 -m http.server 8137 --bind 0.0.0.0`), HTTP checks: page 200 (110899), image 200 (image/png, 6052 B), img tag + caption present in DOM. ✅

**Still FLAGGED for Ray (unresolved):** (1) `m04_l01_introduction_to_lighting.html` = 0 bytes / dupe vs `lighting_fundamentals.html`; (2) materials/lighting filename dupes; (3) MegaLights "Experimental" (live) vs "prod-ready" (doc) — to be handled in L04; (4) Bonus Marketplace→Fab rename pending. Also: 3 pre-existing em-dashes remain in L01 prose (untouched — in wording Ray may revise).

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
