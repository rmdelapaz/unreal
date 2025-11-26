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

## Project Overview

**Project Name:** Introduction to Unreal Engine 5

**Project Type:** Unreal Engine 5 Course (Game Engine Learning)

**Working Directory:** \\wsl$\Ubuntu\home\practicalace\projects\unreal

**Reference Template/Materials:** \\wsl$\Ubuntu\home\practicalace\projects\typescript (for HTML/CSS structure and styling)
---

## Current Status

**Last Updated:** November 25, 2025

**Current Phase:** Fixing lesson structure and CSS styling

**Progress:** Module 1 Lesson 1 in progress (3 parts: A, B, C)

**Next Task:** Replace styles/main.css with complete CSS from TypeScript project, then verify parts B and C have correct heading structure

---

## Project Structure

### Completed Files
- ✅ intro_to_unreal_curriculum.md - Full curriculum outline
- ✅ styles/ - Directory created
- ✅ js/ - Directory created
- ✅ favicon.ico and favicon.png - Project icons
- ✅ m01_l01_what_is_unreal_engine_a.html - Part A with corrected heading structure

### In Progress
- 🔄 styles/main.css - Needs replacement with complete TypeScript template CSS
- 🔄 m01_l01_what_is_unreal_engine_b.html - Needs heading structure verification
- 🔄 m01_l01_what_is_unreal_engine_c.html - Needs heading structure verification
- 🔄 m01_l01_what_is_unreal_engine.html - Complete single-file version (may need updates)

### Pending
- ⏳ index.html - Course home page
- ⏳ m01_l02_installation_and_setup.html - Module 1, Lesson 2
- ⏳ All remaining lessons from curriculum

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
- ✅ **Mermaid diagrams**: Include proper CDN script in `<head>`
  ```html
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
  ```
- ✅ **Illustrations**: Use SVG, HTML5 canvas, and emojis when useful for visual explanations
- ✅ **Canvas elements**: Every `<canvas>` element **MUST have a unique name/id**
  ```html
  <canvas id="unique-canvas-name" width="600" height="400"></canvas>
  ```
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

## Multi-Part File Structure

**When files are too large, split into parts (a, b, c, etc.):**

### Part A includes:
- [Opening elements - DOCTYPE, head, etc.]
- [Initial structure]

### Parts B, C, etc.:
- [Content continuation]

### Final Part:
- [Closing elements]
- [Navigation]
- [Scripts]

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

**Total Items Planned:** [NUMBER]
**Items Completed:** [NUMBER]
**Completion Percentage:** [XX%]

### Session History
- **November 25, 2025:** Fixed m01_l01_what_is_unreal_engine_a.html heading structure (removed "Lesson 1.1:" prefix from h1 to match TypeScript template). Identified critical CSS issue: styles/main.css is incomplete and missing navigation styles (.nav-container, .nav-links, .breadcrumb), causing nav links to stack vertically. Solution: replace with complete CSS from TypeScript project.

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
