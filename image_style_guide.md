# Image Style Guide — Unreal Course Visual Enhancement (v1)

> Canonical source of truth for all figures added during the 5.8 update.
> Companion to `unreal_58_update_progress.md`. Read both before adding any visual.

---

## Core principle (Ray's decision)

**Use a REAL capture wherever a literal editor state exists.** Synthetic diagrams are only for things that have no literal on-screen form (flows, comparisons, abstractions). If a reader could open UE 5.8 and *see* the thing, the figure should be a real capture of that thing — not a drawing of it.

---

## The four image sources & when each is used

### 1. Unreal Slate screenshots — `SlateInspectorToolset`
**Use for:** every UI-panel figure. Details panel, Content Browser, Material Editor, Plugins window, Editor Preferences, Outliner, toolbars, Niagara editor, UMG Designer, Project Settings, packaging dialogs.
**Workflow:** Observe() the target window → screenshot → Unobserve(). Frame tightly on the panel being taught.
**This replaces:** existing hand-drawn SVG "UI mockups" (e.g. the Material Editor mockup, Outliner panel SVG, toolbar-layout SVGs).

### 2. Unreal viewport captures — `EditorAppToolset` + `SceneTools`
**Use for:** 3D results that must be literally true. Lighting setups (directional/point/spot/rect, Lumen on/off), material spheres (roughness/metallic ladders), placed actors, post-process looks, Niagara effects in a level.
**Workflow:** build a minimal scene via SceneTools/PrimitiveTools → frame camera → capture.
**This replaces:** Canvas "roughness sphere gradient" demos, lighting-result illustrations.

### 3. Blender renders — BlenderMCP (as in the Blender course)
**Use for:** conceptual 3D that is NOT about the UE editor itself. Mesh anatomy (verts/edges/faces), coordinate systems, UV-unwrap concepts, pivot/transform abstractions.
**Rationale:** these teach a concept, not a UE screen; a clean Blender render is clearer and version-stable.

### 4. SVG / Canvas / Mermaid — inline, authored (existing framework)
**KEEP for:** process flows (Mermaid), decision trees, side-by-side conceptual comparisons, event sequences, architecture diagrams (e.g. the MCP `agent → MCP → Toolset Registry → editor` diagram), performance comparisons. Anything with no literal editor state.
**Decision tree unchanged** from `continue.md`: PROCESS/FLOW → Mermaid; static abstract diagram → SVG; custom/animated/gradient → Canvas.

---

## Replace vs. keep — quick test

> Ask: "Could a reader open UE 5.8 and see exactly this?"
> - **Yes** → real capture (source 1 or 2). Replace any existing synthetic version.
> - **No, it's a concept** → Blender render (3) or SVG/Canvas/Mermaid (4). Keep existing if still accurate.

Do NOT replace a synthetic diagram that teaches an abstraction just because a capture is possible — a flowchart of Blueprint execution is clearer than a screenshot of a node graph. Judgment over dogma.

---

## Figure conventions

- **Folder:** `images/mXX_lYY/` (create per lesson as needed).
- **Naming:** `mXX_lYY_figNN_short_description.png` (e.g. `m04_l04_fig02_lumen_on_off.png`).
- **Dimensions:** capture at 2× where possible; target display width ≤ 100% of content column. Slate panels: crop to the panel, no OS chrome.
- **Every figure gets a caption:** `<p class="caption"><em>Figure: …</em></p>`.
- **Alt text mandatory** (accessibility parity with existing lessons).
- **Experimental features** shown in a capture must be labelled "Experimental in UE 5.8" in caption or adjacent card.

## HTML integration rules (inherited from project conventions)

- All edits via `Filesystem:edit_file` (dryRun → commit → `get_file_info`), never blind overwrite of a lesson.
- Zero new em-dashes; use `&#183;` where a separator is needed.
- Respect existing table-overflow hygiene: wrap wide tables in `.table-wrap`; keep `svg:not([style*="position"]) { max-width:100% }` behavior; images get `max-width:100%`.
- Track invariants after every commit: byte count, element count, em-dash count, verified against the real UNC file.
- Pause after each lesson for Ray's confirmation. Warn when context grows long; prefer a fresh chat over auto-compaction.

## Density target

3–7 figures per lesson (existing framework), now weighted toward real captures. Quality over quantity: one true viewport capture of "Lumen on vs off" beats three drawn approximations.
