#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restyle the "In This Lesson" collapsible TOC in the Unreal course lesson files
to behave like the blender_course version:

  - custom summary (icon + label + chevron that rotates 180 deg when open),
    with the native <details> disclosure triangle hidden;
  - when COLLAPSED, the whole card becomes a small round floating-action button
    (FAB) pinned to the upper-left corner (click to reopen).

The behavior is driven by a `.toc-card` CSS block ported from
blender_course/styles/main.css into this course's styles/main.css (every CSS
variable it references already exists here), plus a markup swap in each lesson.

Idempotent: re-running skips files/CSS already converted.
Run from the course root:  python3 apply_blender_toc_collapse.py
"""
import io, os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(ROOT, "styles", "main.css")

# ---- CSS block (ported from blender_course/styles/main.css) --------------------
CSS_MARKER = "/* ===== Collapsible \"In This Lesson\" TOC (ported from blender_course) ===== */"
TOC_CSS = CSS_MARKER + """
.toc-card {
    position: sticky;
    top: 80px;                 /* clears the sticky main nav */
    z-index: 90;               /* below nav (100), above content */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: var(--spacing-xl);
    transition: box-shadow 0.3s ease, transform 0.2s ease, background-color 0.3s;
}

/* Hide native disclosure marker; we render our own chevron */
.toc-card summary { list-style: none; }
.toc-card summary::-webkit-details-marker { display: none; }
.toc-card summary::marker { content: ''; }

.toc-card summary {
    cursor: pointer;
    font-weight: bold;
    padding: var(--spacing-sm) var(--spacing-md);
    user-select: none;
    display: flex;
    align-items: center;
    gap: var(--spacing-sm);
}
.toc-card .toc-icon  { font-size: 1.25rem; line-height: 1; }
.toc-card .toc-label { font-size: 1.1rem; font-weight: bold; }
.toc-card .toc-chevron {
    margin-left: auto;
    font-size: 0.85rem;
    color: var(--text-light);
    transition: transform 0.3s ease;
}
.toc-card[open] .toc-chevron { transform: rotate(180deg); }

.toc-card nav { padding: 0 var(--spacing-md) var(--spacing-md); }

.toc-card .toc-link {
    color: var(--text-color);
    text-decoration: none;
    transition: color 0.2s;
}
.toc-card .toc-link:hover { color: var(--primary-color); }
.toc-card .toc-link.active { color: var(--primary-color); font-weight: 600; }

/* ---- Collapsed state: floating action button (upper-left, below nav) ---- */
.toc-card:not([open]) {
    position: fixed;
    top: 76px;
    left: var(--spacing-lg);
    right: auto;
    bottom: auto;
    width: 44px;
    height: 44px;
    padding: 0;
    margin: 0;
    border: none;
    border-radius: 50%;
    background: var(--primary-color);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    z-index: 95;
    overflow: hidden;
}
.toc-card:not([open]):hover {
    transform: scale(1.08);
    background: var(--primary-hover);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}
.toc-card:not([open]) summary {
    width: 100%;
    height: 100%;
    padding: 0;
    justify-content: center;
    color: white;
}
.toc-card:not([open]) .toc-icon { font-size: 1.25rem; color: white; }

/* Keep label/chevron for screen readers but hide them visually in FAB mode */
.toc-card:not([open]) .toc-label,
.toc-card:not([open]) .toc-chevron {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

/* Dark surface for the OPEN card (matches the .card dark override) */
@media (prefers-color-scheme: dark) {
    .toc-card[open] { background: #2d2d30; }
}
:root[data-theme="dark"] .toc-card[open] { background: #2d2d30; }

/* On small screens, hug the left edge a little tighter */
@media (max-width: 767px) {
    .toc-card:not([open]) {
        top: 68px;
        left: var(--spacing-md);
        width: 40px;
        height: 40px;
    }
    .toc-card:not([open]) .toc-icon { font-size: 1.1rem; }
}
"""

# ---- Markup swap ---------------------------------------------------------------
# Matches the fixed prefix: <details ...sticky...> <summary> <h2>...In This Lesson</h2>
# </summary> <nav aria-label="Table of Contents" ...> ; the following <ol>...toc links
# ...</ol></nav></details> is preserved untouched.
PREFIX_RE = re.compile(
    r'<details class="card" open style="position: sticky.*?'
    r'<nav aria-label="Table of Contents"[^>]*>',
    re.S,
)
NEW_PREFIX = (
    '<details class="card toc-card" open>\n'
    '                <summary aria-label="Toggle table of contents">\n'
    '                    <span class="toc-icon" aria-hidden="true">\U0001F4D1</span>\n'
    '                    <span class="toc-label">In This Lesson</span>\n'
    '                    <span class="toc-chevron" aria-hidden="true">▾</span>\n'
    '                </summary>\n'
    '                <nav aria-label="Table of Contents">'
)


def update_css():
    css = io.open(CSS_PATH, encoding="utf-8").read()
    if CSS_MARKER in css:
        return "css: already present (skipped)"
    if not css.endswith("\n"):
        css += "\n"
    css += "\n" + TOC_CSS + "\n"
    io.open(CSS_PATH, "w", encoding="utf-8").write(css)
    return "css: appended .toc-card block"


def update_lesson(path):
    s = io.open(path, encoding="utf-8").read()
    if 'class="card toc-card"' in s:
        return "skip (already converted)"
    n = len(PREFIX_RE.findall(s))
    if n != 1:
        return "SKIP! expected 1 match, found %d" % n
    s = PREFIX_RE.sub(NEW_PREFIX, s, count=1)
    io.open(path, "w", encoding="utf-8").write(s)
    return "converted"


def main():
    print(update_css())
    files = sorted(glob.glob(os.path.join(ROOT, "m*_l*.html"))) + \
            sorted(glob.glob(os.path.join(ROOT, "bonus_*.html")))
    converted = skipped = failed = 0
    for f in files:
        r = update_lesson(f)
        if r == "converted":
            converted += 1
        elif r.startswith("skip"):
            skipped += 1
        else:
            failed += 1
            print("  %-45s %s" % (os.path.basename(f), r))
    print("lessons: %d converted, %d skipped, %d failed (of %d)" %
          (converted, skipped, failed, len(files)))


if __name__ == "__main__":
    main()
