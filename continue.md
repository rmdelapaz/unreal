# Project Continuation Guide Template

## ⚠️ CRITICAL: File System Location

**This project is located on the USER'S COMPUTER at:**

\\wsl$\Ubuntu\home\practicalace\projects\unreal


### 🚨 MANDATORY FILE SYSTEM RULES

Claude has access to TWO different file systems:
1. **User's Computer** - Paths with `\\wsl$\` or `D:\` or `G:\` prefixes
2. **Claude's Computer** - Paths like `/home/claude` or `/mnt/user-data`

**FOR THIS PROJECT:**
- ✅ **ALWAYS USE:** `Filesystem:write_file`, `Filesystem:read_text_file`, `Filesystem:list_directory`, etc.
- ❌ **NEVER USE:** `create_file`, `bash_tool`, `str_replace`, `view` (these are for Claude's computer)

**Path Format Recognition:**
- `\\wsl$\Ubuntu\...` = User's computer → Use Filesystem tools
- `D:\...` or `G:\...` = User's computer → Use Filesystem tools  
- `/home/claude/...` = Claude's computer → Use computer use tools
- `/mnt/user-data/...` = Claude's computer → Use computer use tools

**If you see a path starting with `\\wsl$\`, `D:\`, or `G:\` - STOP and use Filesystem tools!**

---

## 🚨 START EVERY SESSION WITH THIS CHECKLIST

Before doing ANY work, Claude must read this file and output:

✓ File system location: [User's computer at \\wsl$\Ubuntu\home\practicalace\projects\unreal]
✓ Tools to use: [Filesystem:read_text_file, Filesystem:write_file, Filesystem:edit_file]
✓ Current status: [fill in from "Current Status" section]
✓ Next task: [fill in from "Next Task" field]

**DO NOT PROCEED until this checklist is complete and confirmed by user.**

---

## Project Overview

**Project Name:** Introduction to Unreal Engine 5

**Project Type:** Unreal Engine 5 Course (Game Engine Learning)

**Working Directory:** \\wsl$\Ubuntu\home\practicalace\projects\unreal

**Reference Template/Materials:** \\wsl$\Ubuntu\home\practicalace\projects\typescript (for HTML/CSS structure and styling)
---

## Current Status

**Last Updated:** July 7, 2026

> ⚠️ **This file's older status claims were STALE and have been corrected.** The course is content-complete (all 10 modules, 38 lessons, built and linked in index.html). The `parts/` folder reflects an OLD numbering (Module 3 was once Blueprints; it is now Materials, with Blueprints at Module 5). Trust `index.html` + combined root files as source of truth.

**Current Phase:** 5.4 → 5.8 update + visual-enhancement initiative. See `unreal_58_update_progress.md` (primary tracker) and `image_style_guide.md`.

**Progress:** All 10 modules content-complete. Now updating engine target 5.4→5.8, adding real UE screenshots, and building a new AI-Assisted Workflows (Unreal MCP) module.

**Next Task:** Resolve 3 open decisions in `unreal_58_update_progress.md`, then begin the version sweep (M4 Lighting first — highest drift).

---

## Project Structure

### Completed Files
- ✅ intro_to_unreal_curriculum.md - Full curriculum outline
- ✅ index.html - Course home page with all module/lesson links
- ✅ styles/main.css - Complete CSS from TypeScript template
- ✅ js/ - Directory with course enhancement scripts
- ✅ favicon.ico and favicon.png - Project icons

**Module 1 (Combined):**
- ✅ m01_l01_what_is_unreal_engine.html
- ✅ m01_l02_installation_and_setup.html
- ✅ m01_l03_your_first_project.html
- ✅ m01_l04_unreal_editor_interface.html
- ✅ parts/ - Folder with archived Module 1 parts

**Module 2 (Parts Created - Awaiting User Combination):**
- ✅ m02_l01_understanding_levels_[a,b,c].html
- ✅ m02_l02_actors_and_components_[a,b,c].html
- ✅ m02_l03_bsp_geometry_[a,b,c].html
- ✅ m02_l04_static_meshes_and_assets_[a,b,c].html
- ✅ m02_l05_materials_and_lighting_[a,b,c].html

### In Progress
- ⏳ None currently

### Pending
- ⏳ None. The course is **content-complete** (11 modules, 41 lessons + bonus + 6 pipeline pages) and the 5.4→5.8 modernization sweep is finished. See `unreal_58_update_progress.md` for the per-lesson log. This "Pending" list (Module 3 = Blueprints, etc.) reflected an OLD numbering and is obsolete — trust `index.html`.

---

## File Creation Guidelines

### Technical Requirements
- ✅ Mobile-friendly responsive design
- ✅ External CSS file (DO NOT use inline style tags in `<head>`)
- ✅ Link to favicon in every file
- ✅ Consistent naming convention (specify: underscores_only, camelCase, etc.)
- ✅ NO numbered headings in HTML content
- ✅ Include rich examples, analogies, metaphors, real-world scenarios
- ✅ Follow reference template structure exactly

### Required Structure Elements
- ✅ Skip to main content link for accessibility
- ❌ **NO progress indicator bar** (explicitly excluded per user preference)
- ✅ Top navigation with mobile menu toggle
- ✅ Breadcrumb navigation
- ✅ Sticky table of contents using `<details>` element
- ✅ Proper semantic sections with IDs matching TOC
- ✅ Learning objectives card (if applicable)
- ✅ Hands-on exercises with collapsible hints/solutions
- ✅ Lesson navigation (Previous/Home/Next)
- ✅ Footer

### Code & Illustrations

#### Visual Aid Decision Framework

**CRITICAL**: Choose the RIGHT visualization type for each concept. Use this decision tree:

```
Need a visual? Ask:
├─ Is it a PROCESS or FLOW?
│  ├─ Yes → Use MERMAID (flowchart, sequence, state diagram)
│  └─ No → Continue...
├─ Is it a UI MOCKUP or STATIC DIAGRAM?
│  ├─ Yes → Use SVG (panels, toolbars, layouts, cards)
│  └─ No → Continue...
├─ Does it need CUSTOM RENDERING or ANIMATION?
│  └─ Yes → Use CANVAS (3D viz, gradients, interactive demos)
```

#### 1. Mermaid Diagrams

**WHEN TO USE MERMAID:**
- ✅ Workflows and process flows ("First this, then that, then...")
- ✅ Logic/decision trees ("If X, do Y, else do Z")
- ✅ Event sequences ("User clicks → System responds → Result")
- ✅ State machines ("Idle → Loading → Ready → Error")
- ✅ Class hierarchies and relationships
- ✅ Dependency graphs
- ✅ Timelines and sequences

**EXAMPLES WHERE MERMAID EXCELS:**
- Blueprint execution flow: BeginPlay → Initialize → Event Tick loop
- Material setup workflow: Import texture → Create material → Assign to mesh
- Actor communication: Player → Casts to → Door → Opens
- Build lighting process: Pre-calculate → Bake → Generate lightmaps
- State machines: Menu → Playing → Paused → Game Over

**IMPLEMENTATION:**
```html
<!-- In <head> -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ 
      startOnLoad: true,
      theme: 'default',
      themeVariables: {
          primaryColor: '#f0f0f0',
          primaryTextColor: '#333',
          primaryBorderColor: '#667eea'
      }
  });
</script>

<!-- In content -->
<pre class="mermaid">
flowchart LR
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[Alternative]
</pre>
```

**MERMAID DIAGRAM TYPES:**
- `flowchart` / `graph`: Process flows, workflows
- `sequenceDiagram`: Event interactions, communication
- `stateDiagram-v2`: State machines, mode transitions
- `classDiagram`: Inheritance, relationships
- `graph TD` / `graph LR`: Top-down or left-right layouts

#### 2. SVG Graphics

**WHEN TO USE SVG:**
- ✅ UI panel mockups (Details panel, Content Browser, Material Editor)
- ✅ Static diagrams with precise shapes (gizmos, icons, layouts)
- ✅ Reference cards (comparison tables with visual elements)
- ✅ Annotated screenshots/wireframes
- ✅ Organizational charts and hierarchies (when NOT a flow)
- ✅ Interface elements (buttons, dropdowns, checkboxes)

**EXAMPLES WHERE SVG EXCELS:**
- Material Editor interface mockup with node palette, canvas, preview
- Outliner panel showing hierarchy with expand/collapse icons
- Transform gizmo showing X/Y/Z axis arrows
- PBR material input cards (Base Color, Roughness, Metallic)
- Light type comparison cards (Directional, Point, Spot, Rect)
- Toolbar layouts with button groups

**IMPLEMENTATION:**
```html
<svg width="100%" height="400" viewBox="0 0 800 400" style="max-width: 800px; margin: 2rem auto; display: block; border: 2px solid #667eea; background: #f9f9f9;">
    <!-- SVG content: shapes, text, groups -->
    <rect x="10" y="10" width="100" height="50" fill="#667eea"/>
    <text x="60" y="40" text-anchor="middle" fill="#fff">Label</text>
</svg>
<p class="caption"><em>Figure: Description of what the SVG shows.</em></p>
```

**SVG BEST PRACTICES:**
- Use `viewBox` for responsive scaling
- Group related elements with `<g>` tags
- Use meaningful fills/strokes (#667eea for primary, #4CAF50 for success, etc.)
- Add text labels and annotations directly in SVG
- Include legends/keys when showing multiple categories

#### 3. Canvas Elements

**WHEN TO USE CANVAS:**
- ✅ Custom 3D-like visualizations (isometric cubes, coordinate systems)
- ✅ Gradient-based rendering (roughness spheres, lighting demos)
- ✅ Animated or interactive concepts (rotation, transformations)
- ✅ Pixel-level control needed (texture previews, custom effects)
- ✅ Complex mathematical visualizations (curves, surfaces)
- ✅ Anything requiring programmatic drawing with JavaScript

**EXAMPLES WHERE CANVAS EXCELS:**
- 3D coordinate system with X/Y/Z axes in isometric view
- Roughness demonstration with gradient spheres (0.0 to 1.0)
- Material node flow with Bezier curve connections
- Mesh anatomy showing vertices, edges, polygons in 3D
- UV mapping unwrap visualization (3D → 2D)
- Rotation/pivot point comparisons with rendered objects

**IMPLEMENTATION:**
```html
<!-- CRITICAL: Canvas MUST have unique id! -->
<canvas id="descriptive-unique-id" width="700" height="400" style="max-width: 100%; border: 2px solid #667eea; display: block; margin: 2rem auto; background: #f9f9f9;"></canvas>
<p class="caption"><em>Figure: Description of the visualization.</em></p>

<script>
    (function() {
        const canvas = document.getElementById('descriptive-unique-id');
        const ctx = canvas.getContext('2d');
        
        // Drawing code here
        // ALWAYS wrap in IIFE to avoid global scope pollution
    })();
</script>
```

**CANVAS REQUIREMENTS:**
- ⚠️ **MANDATORY**: Every canvas needs a unique `id` attribute
- ⚠️ **MANDATORY**: Wrap JavaScript in IIFE: `(function() { ... })()`
- Use descriptive IDs: `rotation-demo-canvas`, `uv-mapping-viz`, `mesh-anatomy-diagram`
- Set explicit width/height in pixels (not CSS - affects rendering)
- Include `max-width: 100%` in style for responsiveness

**CANVAS BEST PRACTICES:**
- Clear/reset canvas at start: `ctx.fillRect(0, 0, width, height)`
- Use `ctx.save()` / `ctx.restore()` for transform isolation
- Add titles and labels with `ctx.fillText()`
- Include legends or annotations for clarity
- Test rendering at different sizes

#### Visual Aid Strategy

- ✅ **Proactive Planning**: Consider visuals during lesson outline, not as afterthought
- ✅ **Quantity**: Aim for 3-7 visual aids per lesson, distributed throughout
- ✅ **Quality over Quantity**: One great Mermaid flowchart beats three mediocre diagrams
- ✅ **Mix Types**: Use all three types (Mermaid, SVG, Canvas) when appropriate
- ✅ **Ask the Question**: "Would a visual help here?" for every complex concept

**RED FLAGS** (Use a visual!):
- Describing a multi-step process → Mermaid flowchart
- Explaining UI layout or panel structure → SVG mockup  
- Describing spatial relationships or 3D concepts → Canvas visualization
- Comparing multiple items side-by-side → SVG cards or table with visual elements
- Event sequences or communication → Mermaid sequence diagram
- ✅ **Emojis** for section headers and visual interest
- ✅ **Code samples**: Properly escaped HTML entities, wrapped in `<pre><code class="language-[lang]"></code></pre>`
- ✅ **Styled cards** for notes, warnings, tips, definitions (use inline styles on card divs)
- ✅ **Tables** for comparisons and reference information
- ✅ **Collapsible sections** using `<details>` and `<summary>`

### Card Styling Reference
```html
<!-- Definition Card (Purple gradient) -->
<div class="card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
    <h4>📖 Definition</h4>
    <p style="color: white;"><strong>Term:</strong> Definition text</p>
</div>

<!-- Success/Tip Card (Green) -->
<div class="card" style="background: #e8f5e9; border-left: 4px solid #4CAF50;">
    <h4>✅ Pro Tip</h4>
    <p>Tip text</p>
</div>

<!-- Warning Card (Yellow) -->
<div class="card" style="background-color: #fff3cd; border-left: 4px solid #ffc107;">
    <h4>⚠️ Watch Out</h4>
    <p>Warning text</p>
</div>

<!-- Info Card (Blue) -->
<div class="card" style="background: #e3f2fd; border-left: 4px solid #2196F3;">
    <h4>💡 Information</h4>
    <p>Info text</p>
</div>

<!-- Exercise Card (Blue) -->
<div class="card" style="background: #e3f2fd; border-left: 4px solid #2196F3;">
    <h3>🏋️ Exercise Title</h3>
    <!-- Exercise content -->
</div>
```

### Teaching Style
- **Tone**: Friendly, accessible instructor voice
- **Audience**: New developers learning the technology
- **Approach**: Patient, clear explanations with plenty of examples  
- **Pacing**: Pause after each file completion and ask for confirmation to continue

---

## Multi-Part File Workflow

**Development Process for Large Lessons:**

1. **Create parts** (a, b, c) during development **IN THE ROOT FOLDER**:
   - Part A: DOCTYPE, head, opening sections
   - Part B: Middle content sections
   - Part C: Final sections, navigation, closing tags
   - **CRITICAL**: Create files like `m0X_l0Y_lesson_name_a.html` directly in root, NOT in /parts/

2. **User combines and moves parts** (Claude does NOT do this step):
   - User concatenates parts into combined file
   - User moves part files to /parts/ subfolder for archival

3. **Final user-facing file structure**:
   - File name: `m0X_l0Y_lesson_name.html` (no _a/_b/_c suffix)
   - Contains all content from parts merged together
   - This is the file users will access

**Working Directory Structure During Development:**
```
project/
├── m01_l01_lesson_name_a.html (development - IN ROOT)
├── m01_l01_lesson_name_b.html (development - IN ROOT)
├── m01_l01_lesson_name_c.html (development - IN ROOT)
├── m01_l02_lesson_name_a.html (development - IN ROOT)
├── ... (all parts stay in root during development)
```

**Working Directory Structure After User Combines:**
```
project/
├── m01_l01_lesson_name.html (combined - user-facing)
├── m01_l02_lesson_name.html (combined - user-facing)
├── parts/
│   ├── m01_l01_lesson_name_a.html (archived)
│   ├── m01_l01_lesson_name_b.html (archived)
│   └── m01_l01_lesson_name_c.html (archived)
```

---

## Tool Selection Strategy

### When to Edit vs. Write

**Use `Filesystem:edit_file` when:**
- User says "edit", "update", "fix", "change"
- Making targeted changes to existing files
- Updating specific sections or values
- More efficient - only sends the changes, not entire file

**Use `Filesystem:write_file` when:**
- User says "create", "write", "make a new file"
- Creating brand new files
- Complete rewrites where most content changes
- User explicitly requests a rewrite

**Parameter names for edit_file:**
```javascript
{
  "path": "file/path.ext",
  "edits": [
    {
      "oldText": "exact text to find",
      "newText": "replacement text"
    }
  ]
}
```

**CRITICAL**: Default to `edit_file` for updates unless the change is so extensive that rewriting is more efficient!

---

## Workflow for New Chat Session

1. **Read this continue.md file completely**
2. **Verify file system location** - Check the path format
3. **Use correct tools** - Filesystem tools for user's computer
4. **Choose edit vs write** - Default to edit_file for updates
5. **Review completed files list** - Understand what's done
6. **Check current status** - Know where we are
7. **Continue from "Next Task"** - Pick up where we left off
8. **Pause after each file** - Ask for confirmation
9. **Update this continue.md** - Document progress before ending

---

## Quick Start Command for New Session

```
I'm continuing the [PROJECT NAME] project.

Current status: [STATUS SUMMARY]
Working directory: [PATH]
Reference materials: [PATH]

⚠️ CRITICAL: This is on MY COMPUTER at [PATH]
Please use Filesystem tools (Filesystem:write_file, etc.)

Please read the continue.md file and let's continue with [NEXT TASK].
```

---

## Important Reminders

### For Claude:
- **Always verify path format before choosing tools**
- **When in doubt, ask which file system to use**
- **Path with `\\wsl$\` = Filesystem tools required**
- **Read existing files to match style and structure**
- **Create complete, production-ready content**
- **Pause after each major file for user confirmation**

### For User:
- **State "Use Filesystem tools" if Claude uses wrong ones**
- **Provide full path including `\\wsl$\` prefix**
- **Stop Claude immediately if wrong tool is used**
- **Update continue.md at end of each session**

---

## Reference Materials

### Key Documentation Links
- [Link 1]
- [Link 2]
- [Link 3]

### Internal Templates/References
- [Path to template 1]
- [Path to reference file 2]

---

## Notes & Project-Specific Guidelines

### Critical Structural Requirements
1. **Heading Format:** Main h1 should NOT include "Lesson X.X:" prefix (e.g., `<h1>🎮 What is Unreal Engine?</h1>` not `<h1>🎮 Lesson 1.1: What is Unreal Engine?</h1>`)
2. **Breadcrumb keeps full title:** The breadcrumb DOES include "Lesson 1.1:" text
3. **NO progress indicator bar:** User explicitly requested this be excluded from template
4. **CSS Template:** Use TypeScript project's styles/main.css as the definitive CSS template (includes navigation styles, dark mode, responsive design)

### Known Issues Fixed
- ✅ Part A heading corrected from "Lesson 1.1: What is Unreal Engine?" to "What is Unreal Engine?"
- ⏳ CSS file needs complete replacement (current version missing navigation styles)

---

## Progress Tracking

**Total Modules:** 11 modules + Bonus + 6 Production Pipeline pages (see intro_to_unreal_curriculum.md / index.html)
**Modules Completed:** All 11 (content-complete; 41 lessons)
**Current initiative:** 5.4→5.8 modernization + real-capture sweep — **COMPLETE** (see `unreal_58_update_progress.md`)
**Overall Progress:** 100% built and linked

> ⚠️ The numbers below this line and in the "Session History" are historical snapshots from early development (Nov 2025, ~20% era). They are kept for provenance only — do NOT read them as current status.

### Session History
- **November 25, 2025 (Session 1):** Fixed m01_l01_what_is_unreal_engine_a.html heading structure. Identified and resolved CSS issue by replacing styles/main.css with complete TypeScript template CSS.
- **November 25, 2025 (Session 2):** Completed all Module 1 lessons (1.1-1.4). Created multi-part files, combined into single user-facing files. Added SVG graphics (toolbar layouts, docking diagrams, keyboard shortcuts) to Lesson 1.4. All combined files delivered.
- **November 25, 2025 (Session 3):** Completed all Module 2 lessons (2.1-2.5). Created 15 part files (a/b/c for each lesson). Total 31 visual aids across module: Mix of Mermaid diagrams, SVG mockups (UI panels, cards, diagrams), and Canvas visualizations (3D demos, gradients, interactive concepts). Updated continue.md with comprehensive Visual Aid Decision Framework covering when to use Mermaid vs SVG vs Canvas, with examples and implementation details.

---

## Troubleshooting

### Common Issues

**Issue 1: Claude uses wrong file system tools**
- Solution: Explicitly state "Use Filesystem:write_file" in instructions
- Prevention: Verify path format shows user's computer

**Issue 2: Navigation links stacking vertically instead of horizontally**
- Solution: The styles/main.css file is incomplete - missing `.nav-links { display: flex; }` and other navigation styles. Replace entire main.css with the complete version from \\wsl$\Ubuntu\home\practicalace\projects\typescript\styles\main.css
- Prevention: Always verify CSS file has navigation styles before creating HTML lessons

**Issue 3: Heading structure doesn't match template**
- Solution: Main h1 should be clean topic name only (no "Lesson X.X:" prefix). Breadcrumb keeps the full "Lesson 1.1: Topic" format
- Prevention: Compare against TypeScript project lesson files for correct structure

---

**Template Version:** 1.0
**Created:** 2024
**Purpose:** Ensure continuity across chat sessions and prevent file system tool confusion
