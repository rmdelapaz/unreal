# -*- coding: utf-8 -*-
import re, io, sys

F = "m01_l04_unreal_editor_interface.html"
html = io.open(F, "r", encoding="utf-8").read()
orig_len = len(html.encode("utf-8"))
emdash_before = html.count("—")

def rep(old, new, n=1):
    c = html.count(old)
    assert c == n, "expected %d of %r, found %d" % (n, old[:60], c)
    return html.replace(old, new)

# ---------- GROUP 1: World Outliner -> Outliner (17) ----------
pairs = [
    ("Organize complex scenes with the World Outliner",
     "Organize complex scenes with the Outliner"),
    ('href="#world-outliner" class="toc-link">World Outliner</a>',
     'href="#world-outliner" class="toc-link">Outliner</a>'),
    ("E[4. World Outliner<br/>Scene Hierarchy]",
     "E[4. Outliner<br/>Scene Hierarchy]"),
    ("<td><strong>World Outliner</strong></td>",
     "<td><strong>Outliner</strong></td>"),
    ("<li><strong>World Outliner:</strong> Your inventory list",
     "<li><strong>Outliner:</strong> Your inventory list"),
    ("<!-- World Outliner (top right) -->",
     "<!-- Outliner (top right) -->"),
    (">④ World Outliner</text>",
     ">④ Outliner</text>"),
    ("<!-- Section 4: World Outliner -->",
     "<!-- Section 4: Outliner -->"),
    ("<h2>World Outliner</h2>",
     "<h2>Outliner</h2>"),
    ("The World Outliner is your hierarchical",
     "The Outliner is your hierarchical"),
    ("<h3>World Outliner Interface</h3>",
     "<h3>Outliner Interface</h3>"),
    ("Right-click in World Outliner",
     "Right-click in the Outliner"),
    ("In World Outliner, drag the Point Light",
     "In the Outliner, drag the Point Light"),
    ("<h3>World Outliner Settings</h3>",
     "<h3>Outliner Settings</h3>"),
    ("<h4>World Outliner</h4>",
     "<h4>Outliner</h4>"),
    ("Focus World Outliner",
     "Focus Outliner"),
    ("<li><strong>World Outliner:</strong> Hierarchical list",
     "<li><strong>Outliner:</strong> Hierarchical list"),
]
for o, n in pairs:
    html = rep(o, n, 1)

# ---------- GROUP 2: doc links -> dev.epicgames.com ----------
html = rep("https://docs.unrealengine.com/5.5/en-US/unreal-editor-interface/",
           "https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-interface", 1)
html = rep("https://docs.unrealengine.com/5.5/en-US/keyboard-shortcuts-in-unreal-engine/",
           "https://dev.epicgames.com/documentation/en-us/unreal-engine/keyboard-shortcuts-in-unreal-engine", 1)

# ---------- GROUP 3: Marketplace -> Fab (toolbar table) ----------
html = rep("<td>\U0001F6D2 <strong>Marketplace</strong></td>",
           "<td>\U0001F6D2 <strong>Fab</strong></td>", 1)
html = rep("<td>Browse Unreal Marketplace for assets</td>",
           "<td>Browse Fab (fab.com), Epic's content library</td>", 1)
html = rep("<td>Free content available monthly</td>",
           "<td>Opens from the Content Browser toolbar</td>", 1)

# ---------- GROUP 5: Content Browser SVG -> img (fig01) ----------
cb_new = ('<img src="images/m01_l04/m01_l04_fig01_content_browser.png" '
    'alt="The Unreal Editor Content Browser panel in UE 5.8: the Favorites and folder tree on the left '
    '(All, Content, Ballroom, Engine), the Add, Import, Save All and Fab toolbar buttons, the path bar '
    '(All &gt; Content), the asset search field, and the asset view showing the Ballroom folder." '
    'style="max-width: 100%; height: auto; display: block; margin: 2rem auto; border-radius: 8px; border: 2px solid #667eea;">\n'
    '                <p style="text-align: center; font-style: italic; color: #666; margin-top: 0.5rem;">'
    '<em>Figure: The Content Browser in UE 5.8 &#183; folder tree (left), asset view (center), the search '
    'and filter bar, and the toolbar with Add, Import, Save All, and the Fab button.</em></p>')
html, ncb = re.subn(
    r'<!-- SVG: Content Browser Panel Mockup -->.*?<em>Figure: The Content Browser interface showing folder tree, asset view, search, and filters\.</em></p>',
    lambda m: cb_new, html, count=1, flags=re.DOTALL)
assert ncb == 1, "content browser block not replaced (%d)" % ncb

# ---------- GROUP 6: Toolbar SVG -> img (fig04) ----------
tb_new = ('<img src="images/m01_l04/m01_l04_fig04_main_toolbar.png" '
    'alt="The Unreal Editor 5.8 main toolbar: Save and Open Level buttons, the Selection Mode dropdown, '
    'the Add, Blueprints and Cinematics dropdowns, and the Play, Skip, Stop and Step simulation controls." '
    'style="max-width: 100%; height: auto; display: block; margin: 2rem auto; border-radius: 8px; border: 2px solid #667eea;">\n'
    '                <p style="text-align: center; font-style: italic; color: #666; margin-top: 0.5rem;">'
    '<em>Figure: The UE 5.8 Main Toolbar &#183; Save and Open, the Selection Mode dropdown, the Add / '
    'Blueprints / Cinematics menus, and the Play simulation controls.</em></p>')
html, ntb = re.subn(
    r'<!-- SVG Toolbar Diagram -->\s*<div class="card"[^>]*>.*?</svg>\s*</div>',
    lambda m: tb_new, html, count=1, flags=re.DOTALL)
assert ntb == 1, "toolbar block not replaced (%d)" % ntb

# ---------- GROUP 7: insert Outliner figure (fig02) ----------
out_anchor = ('                    <li><strong>Type Icons:</strong> Visual indicators of actor type (mesh, light, camera, etc.)</li>\n'
              '                </ul>\n')
out_fig = out_anchor + (
    '                \n'
    '                <img src="images/m01_l04/m01_l04_fig02_outliner.png" '
    'alt="The Unreal Editor Outliner in UE 5.8 showing the Ballroom level hierarchy: nested folders '
    '(Columns, Figure, Shell, Castle, HLOD, Lighting, Landscape), the Item Label / Sequencer / Type columns, '
    'per-actor visibility eye icons (the Castle folder is hidden), and the selected DirectionalLight. '
    'The status bar reads 156 actors, 1 selected." '
    'style="max-width: 100%; height: auto; display: block; margin: 2rem auto; border-radius: 8px; border: 2px solid #667eea;">\n'
    '                <p style="text-align: center; font-style: italic; color: #666; margin-top: 0.5rem;">'
    '<em>Figure: The Outliner in UE 5.8 &#183; the level\'s actors grouped in folders, with the Type column, '
    'visibility eye icons, and the selected DirectionalLight highlighted.</em></p>\n')
html = rep(out_anchor, out_fig, 1)

# ---------- GROUP 8: insert Details figure (fig03) ----------
det_anchor = ('                    <li><strong>Different actor types:</strong> Each type has unique properties</li>\n'
              '                </ul>\n')
det_fig = det_anchor + (
    '                \n'
    '                <img src="images/m01_l04/m01_l04_fig03_details_panel.png" '
    'alt="The Unreal Editor Details panel in UE 5.8 with a DirectionalLight selected: the component tree at the top, '
    'the property search field and category filter chips (General, Actor, LOD, Misc, Physics, Rendering, Streaming, All), '
    'and the Transform and Light categories showing Location, Rotation, Scale, Mobility, Intensity (6.0 lux), Light Color, and Temperature." '
    'style="max-width: 100%; height: auto; display: block; margin: 2rem auto; border-radius: 8px; border: 2px solid #667eea;">\n'
    '                <p style="text-align: center; font-style: italic; color: #666; margin-top: 0.5rem;">'
    '<em>Figure: The Details panel is context-sensitive &#183; here it shows the selected DirectionalLight\'s '
    'Transform and Light properties, grouped into expandable categories.</em></p>\n')
html = rep(det_anchor, det_fig, 1)

# ---------- write + report ----------
io.open(F, "w", encoding="utf-8").write(html)
new_len = len(html.encode("utf-8"))
print("bytes: %d -> %d (%+d)" % (orig_len, new_len, new_len - orig_len))
print("em-dashes: %d -> %d" % (emdash_before, html.count("—")))
print("World Outliner remaining:", html.count("World Outliner"))
print("Marketplace remaining:", html.count("Marketplace"))
print("docs.unrealengine.com/5.5 remaining:", html.count("docs.unrealengine.com/5.5"))
print("dev.epicgames links:", html.count("dev.epicgames.com"))
print("<svg count:", html.count("<svg"))
print("<img count:", html.count("<img"))
print("images/m01_l04 refs:", html.count("images/m01_l04/"))
