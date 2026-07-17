# -*- coding: utf-8 -*-
"""Insert the Kyle (§12) section into sherry_celebration_pipeline.html, embedding the
two delivered PNGs as base64. Also corrects §10's viewport-size claim and refreshes the hero."""
import base64, io, os, re, sys

HTML = "/home/practicalace/projects/unreal/sherry_celebration_pipeline.html"
SHOTS = "/mnt/d/mydata/3dassets"

def b64(name):
    with open(os.path.join(SHOTS, name), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

hero_b64 = b64("Kyle_Happy_UE.png")
close_b64 = b64("Kyle_Happy_Closeup.png")

s = io.open(HTML, encoding="utf-8").read()
orig_len = len(s)

KYLE = u'''
<!-- KYLE_SECTION_START -->
<h2 id="hybrid">12 &middot; HYBRID G9 (Kyle) &mdash; hands-on-hips + a bone-only smile</h2>
<p>Validated 2026-07-16 on <code>kyle.fbx</code> (230.3&nbsp;MB, G9 male: <strong>realistic Masculine_01
skin + Amy&rsquo;s TOON anime hair</strong>). <strong>Zero new traps bit.</strong> The pre-flight was accurate
(1 skeleton root, 0 duplicate bones, skin textures assigned) and the import was clean first try:
<code>SK_Kyle</code>, 153 bones, 136,656 verts, <strong>0 morph targets</strong>, 31 material slots. Total cost:
one import, one material pass, a 64-control rig, one pose solve &mdash; no Daz round-trip, no editor restart.</p>

<div class="grid">
  <figure>
    <img alt="Kyle, happy, hands on hips, in-engine studio" src="data:image/png;base64,__HERO__">
    <figcaption>&#9989; <code>Kyle_Happy_UE.png</code> &mdash; hybrid G9 male, confident hands-on-hips,
    chest open, chin level. 64-control rig; the wrists are placed by a <strong>two-bone analytic IK
    solve</strong> (0.0000&nbsp;cm error), not by aiming. PPV clamp <strong>N&nbsp;=&nbsp;5.8</strong>.</figcaption>
  </figure>
  <figure>
    <img alt="Kyle close-up, genuine smile" src="data:image/png;base64,__CLOSE__">
    <figcaption><code>Kyle_Happy_Closeup.png</code> &mdash; a genuine smile from <em>bones only</em>
    (0 morph targets): lip corners up, <strong>cheeks raised</strong>, brows up, slight squint. The
    close-up is what caught jaw&nbsp;&minus;4&deg; reading as <em>gritted teeth</em>.</figcaption>
  </figure>
</div>

<div class="callout do">
  <h4>What the hybrid actually cost &mdash; only §9 Trap&nbsp;1, and only 3 slots</h4>
  <p>A hybrid is <strong>not</strong> the sum of both figures&rsquo; problems. Kyle&rsquo;s toon content was
  <em>only</em> the hair: <code>G9AnimeHair_ToonOutline</code> is the single unskinned mesh, so it arrives as
  exactly <strong>3 <code>_ncl1_1</code> slots</strong> (<code>Scalp_ncl1_1</code>, <code>BaseHair_ncl1_1</code>,
  <code>TopHair_ncl1_1</code>) &mdash; not Amy&rsquo;s 22. Mask them (<code>BLEND_Masked</code> +
  <code>Constant(0)&rarr;MP_OpacityMask</code>) and the toon problem is over. Everything else (skin, eyes,
  brows, clothing) behaved as a plain realistic G9.</p>
  <p><strong>Slot-name arithmetic identifies the outline set instantly:</strong> 31 slots = 28 real + 3
  <code>_ncl1_1</code>. The suffix maps 1:1 onto the outline mesh&rsquo;s material count. Count first,
  don&rsquo;t hunt.</p>
</div>

<div class="callout avoid">
  <h4>Trap C did NOT bite &mdash; and the reason inverts the Guardsman rule</h4>
  <p>Guardsman&rsquo;s white beard came from the exporter writing a <em>transparency</em> map into the FBX
  diffuse slot for materials with <strong>no diffuse image</strong>. Kyle has the same set-up
  (<code>Scalp</code>, <code>Eyebrows_Primary/Secondary</code> have Daz diffuse colours but no diffuse image)
  &mdash; and the exporter did <strong>not</strong> do it here. Those materials imported as a
  <code>MaterialExpressionVectorParameter</code> holding the <em>exact</em> Daz diffuse
  (<code>Scalp</code>&nbsp;=&nbsp;<code>[0.2235, 0.0902, 0.051]</code>) &mdash; a flat colour node, no texture.
  <strong>That is already correct: leave it alone.</strong></p>
  <p><code>MAHLineMask.tif</code> / <code>MAHLineMaskBase.tif</code> <em>were</em> wired to
  <code>MP_BaseColor</code> &mdash; but <strong>only on the two outline slots</strong>, which get masked out
  anyway. Harmless.</p>
  <p>&#128308; <strong>So the real diagnostic is the NODE TYPE, not the texture name.</strong> One
  <code>get_property_input</code> sweep over every slot answers it in a single call:
  <code>VectorParameter</code> &rArr; no texture ever existed &rArr; nothing to fix.
  <code>TextureSample</code> named <code>*tr*</code>/<code>*LineMask*</code>/<code>*_O</code> &rArr; Trap&nbsp;C
  &rArr; replace with <code>Constant3Vector(&lt;Daz diffuse&gt;)</code>. <strong>Don&rsquo;t pre-emptively
  &ldquo;fix&rdquo; Trap&nbsp;C from the Daz colours alone</strong> &mdash; check what UE actually built. I nearly
  rewired 6 correct materials.</p>
  <p>&#9888; <code>ObjectTools.get_properties(expr, ["Texture"])</code> <strong>raises</strong> on a
  <code>VectorParameter</code>, and the error <em>escapes</em> a <code>try/except</code> in the script sandbox
  (errors are collected and re-raised at the end, killing the whole script). <strong>Branch on the node class
  first</strong> &mdash; parse <code>refPath.split(":")[-1]</code>.</p>
</div>

<div class="callout avoid">
  <h4>Don&rsquo;t trust a brief&rsquo;s guess about wardrobe brightness &mdash; SAMPLE THE TEXTURE</h4>
  <p>The session brief said &ldquo;Kyle wears a <em>light</em> shirt/shorts, so he will need a
  <em>higher</em> exposure N.&rdquo; Both textures average <strong>RGB (17,17,17) &mdash; near-black</strong>.
  <strong>Guardsman&rsquo;s <code>N&nbsp;=&nbsp;5.8</code> was already correct and needed no sweep at all</strong>
  &mdash; a 20-minute exposure sweep avoided by one 5-line PowerShell <code>System.Drawing</code> pixel
  average over the <code>.images</code> sidecar. Do this <em>before</em> touching the PPV.</p>
</div>

<div class="callout do">
  <h4>Toon ANIME hair is SOLID geometry &mdash; no opacity masks, no TR maps</h4>
  <p>Kyle&rsquo;s (and Amy&rsquo;s) <code>G9AnimeHair</code> is modelled solid, like a helmet &mdash; unlike
  Guardsman&rsquo;s Toulouse hair <em>cards</em>. <strong>Tell: the hair diffuse maps are
  <code>.jpg</code></strong> (<code>MAHBaseMidBrown</code>, <code>MAHTopMidBrown</code>) &mdash; a JPG has no
  alpha, so there is nothing to cut out. Card-based hair always ships <code>.tif</code>/<code>.png</code> TR
  maps. &rArr; <strong>Skip §11 Trap&nbsp;D&rsquo;s <code>BLEND_Masked</code> + <code>TwoSided</code> + TR-map
  wiring entirely.</strong> Only the <code>MP_Specular 0.02</code> / <code>MP_Roughness 0.85</code> half still
  applies &mdash; the 3600&nbsp;cd rim light blows out solid hair just as happily as cards.</p>
</div>

<div class="callout avoid">
  <h4>HANDS ON HIPS &mdash; solve the elbow, don&rsquo;t aim it</h4>
  <p>Aiming upperarm/forearm at hand-picked directions <em>cannot</em> put the wrist on the hip: the wrist is
  a <strong>position</strong> constraint, so it needs a <strong>two-bone (analytic IK) solve</strong>. This is a
  genuine addition to §3&rsquo;s aim-only recipe, and it is ~15 lines:</p>
  <pre><code>S = p[upperarm]; a = |p[forearm]-p[upperarm]|; b = |p[hand]-p[forearm]|
W = p[hip] + (&plusmn;16.0, -3.5, 6.6)          # the iliac crest, in the POSED hip frame
d = |W-S|; u = (W-S)/d
x0 = (a&sup2;-b&sup2;+d&sup2;)/(2d);  r = sqrt(a&sup2;-x0&sup2;);  C = S + x0*u
pole = (&plusmn;0.95, -0.31, 0.05)              # elbow flares OUT (mostly) and BACK
E = C + r * normalize(pole - u*(pole&middot;u)) # project the pole into the circle plane
aim(upperarm, forearm, normalize(E-S));  aim(forearm, hand, normalize(W-p[forearm]))</code></pre>
  <p>The two aims then place the wrist <strong>exactly</strong> &mdash; measured error
  <strong>0.0000&nbsp;cm</strong> on both arms. The elbow interior angle falls out at <strong>76.2&deg;</strong>,
  anatomically right for hands-on-hips (a ~104&deg; bend).</p>
  <p>&#128308; <strong>The pole vector is the whole look, and my first guess was wrong.</strong>
  <code>(0.78, -0.62, 0.08)</code> sent the elbows <em>backward</em>
  (<code>E&nbsp;=&nbsp;(&plusmn;32.9, -17.8, 116.3)</code>) and from a front-on camera they vanished behind the
  torso &mdash; the shot lost the classic triangle silhouette entirely. <code>(0.95, -0.31, 0.05)</code>
  &rarr; <code>E&nbsp;=&nbsp;(&plusmn;36.2, -11.3, 117.6)</code> and the triangles read.
  <strong>Hands-on-hips is a SILHOUETTE pose: flare the elbows mostly &plusmn;X (lateral), only slightly
  &minus;Y.</strong> Judge it from the shooting camera, not in 3D.</p>
  <p>Define <code>W</code> <strong>relative to the posed <code>p[hip]</code></strong>, not in world space, so it
  tracks the spine lean. Wrist at <code>hip + (&plusmn;16.0, &minus;3.5, 6.6)</code> =
  <code>(&plusmn;16.0, &minus;2.4, 102.9)</code> sits correctly on the waist/crest for a ~172&nbsp;cm G9 male.</p>
</div>

<div class="callout note">
  <h4>Hands-on-hips fingers: a WRAP, not a fist</h4>
  <p>Reuse §11&rsquo;s fist recipe with the curl angles dialled right down: <strong>35&deg;/40&deg;/25&deg;</strong>
  (vs the fist&rsquo;s 88/100/72) &rarr; <code>mid3&rarr;wrist</code> <strong>16.88&nbsp;cm (rest) &rarr;
  14.68&nbsp;cm</strong>. A fist is ~7.6. <em>That gap is the difference between &ldquo;hand resting on
  hip&rdquo; and &ldquo;punching his own hip&rdquo;.</em></p>
  <p>The empirical sign search again chose <strong>&minus;1 left / +1 right</strong> &mdash; mirrored, the free
  correctness check. <code>knuckle_axis &middot; fingerDir = &minus;0.243</code> (&asymp;76&deg;, near-&perp;)
  &#10004; so one fixed global axis works per hand. <strong>Thumb: AIM it backward, never curl it</strong>
  &mdash; <code>aim(thumb1, thumb2, &rarr;(&mp;0.30, &minus;0.86, &minus;0.41))</code>. Thumb behind + fingers
  forward = gripping the crest.</p>
  <p>&#9888; <strong><code>aim()</code> does not constrain hand ROLL about the finger axis</strong> &mdash; it
  applies the minimal rotation, so the palm inherits whatever roll the arm solve produced. It happened to land
  palm-to-hip here and needed no correction. If a future hand lands palm-out, roll it about
  <code>normalize(p[mid1]-p[hand])</code> (that axis leaves the finger direction invariant) rather than
  re-aiming.</p>
</div>

<div class="callout avoid">
  <h4>A HAPPY face from bones: TRANSLATE the face bones, don&rsquo;t just rotate them</h4>
  <p>Guardsman&rsquo;s furrow used pure rotation. For a <em>smile</em> that is <strong>too weak</strong> &mdash;
  rotating a leaf bone about its own origin moves the surrounding skin by almost nothing (an 8&deg; twist over a
  ~2&nbsp;cm cluster &asymp; 0.3&nbsp;cm). Because we key <strong>absolute world transforms</strong>, we can simply
  <strong>move</strong> the bone, which translates its whole skin cluster. Daz face rigs are built for exactly
  this. What shipped (+Y-facing, <code>dz</code>-grounded):</p>
  <div class="tablewrap">
  <table>
    <thead><tr><th>bone</th><th>translate (x,y,z)</th><th>rotate</th></tr></thead>
    <tbody>
      <tr><td>l/r <code>lipcorner</code></td><td><code>(&plusmn;0.60, &minus;0.35, +1.05)</code> up+back+out</td><td><code>Rx(+10)</code></td></tr>
      <tr><td>l/r <code>cheeklower</code></td><td><code>(&plusmn;0.22, +0.15, +0.80)</code> <strong>raised</strong></td><td><code>Rx(+7)</code></td></tr>
      <tr><td>l/r <code>squint</code></td><td><code>(&mp;0.10, +0.08, +0.34)</code></td><td><code>Rx(+5)</code></td></tr>
      <tr><td>l/r <code>browinner</code>/<code>browouter</code>/<code>centerbrow</code></td><td><code>(0,0,+0.42/+0.34/+0.36)</code></td><td><code>Rx(+8/+7/+8)</code></td></tr>
      <tr><td><code>lowerjaw</code></td><td>&mdash;</td><td><code>Rx(&minus;2)</code></td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Cheeks raised is non-negotiable</strong> &mdash; lip corners alone read as a fake, pasted-on smile
  (Duchenne). <strong>Brows <code>Rx(+8)</code> is the exact opposite sign of Guardsman&rsquo;s furrow
  <code>Rx(&minus;16)</code></strong>: same axis, same figure family &mdash; the sign <em>is</em> the emotion.</p>
  <p>&#128308; <strong>Jaw <code>Rx(&minus;4)</code> read as GRITTED TEETH; <code>Rx(&minus;2)</code> reads as a
  warm smile.</strong> A 2&deg; difference flipped the expression from grimace to genuine. Shoot the close-up and
  look &mdash; this is not computable.</p>
  <p><strong>Sanity-check numbers, not vibes:</strong> posed <code>lipcorner</code> z <strong>rose
  1.05&nbsp;cm</strong> vs rest, and <code>l_eye</code> z=162.7 stayed above <code>head</code> z=156.4 &#10004;.</p>
  <p>&#9888; <strong>The Guardsman check &ldquo;eye y forward of chin y&rdquo; does NOT generalise.</strong> On
  Kyle the chin is forward of the eyes <em>at rest</em> (<code>chin</code> y=9.15 vs <code>l_eye</code> y=8.05)
  &mdash; that is facial anatomy, not a pose error. <strong>Compare posed-vs-rest for the same figure; never
  port a landmark threshold between figures.</strong></p>
</div>

<div class="callout note">
  <h4>Confident stance: the head must counter the spine (again)</h4>
  <p>Chest open = spine leans <strong>back</strong> <code>Rx(+1.0/+1.5/+1.0/+0.5)</code> = <strong>+4&deg;
  total</strong>; the head inherits all of it, so <code>neck1 Rx(&minus;2)</code>,
  <code>neck2 Rx(&minus;1.5)</code>, <code>head Rx(&minus;0.5)</code> = <strong>&minus;4</strong> &rarr;
  <strong>net 0&deg; = chin level</strong> &#10004;. (Guardsman leaned &minus;16 and countered +10 for a net
  &minus;6 chin-tuck &mdash; same arithmetic, opposite sign.) Shoulders back+down:
  <code>aim(shoulder, upperarm, &rarr;(&plusmn;0.972, &minus;0.16, &minus;0.17))</code> &mdash;
  <strong>no +Z shrug</strong>. My first attempt used +6&deg; of spine lean; it shifted the head back ~4&nbsp;cm
  and read as <em>leaning away</em>. <strong>4&deg; is the ceiling for &ldquo;chest open&rdquo; before it becomes
  &ldquo;leaning back&rdquo;.</strong></p>
</div>

<div class="callout do">
  <h4>The viewport is FULL 1857&times;825 with the pose live &mdash; the docked-Sequencer shrink is not inevitable</h4>
  <p>Amy and Guardsman shipped from a letterboxed <strong>1422&times;527</strong> because the docked Sequencer
  panel shrank the viewport. This session&rsquo;s captures came back at the <strong>full
  1857&times;825</strong> (content letterboxed 3:2 to <code>x&asymp;310..1547</code>) <strong>with the Control Rig
  pose live and correct</strong>.</p>
  <p>&#128308; <strong>So &ldquo;the viewport grew to 1857&times;825&rdquo; is NOT a reliable tell that the pose
  reverted to A-pose</strong> (§10 claimed it was). Kyle rendered at full size <em>and</em> posed. <strong>Verify a
  suspected revert by reading <code>get_euler_transform</code> back, or just look at the frame &mdash; never by
  the viewport size.</strong> Practical win: ~2.4&times; the pixels, so crops are far less starved. Final hero
  <code>470&times;794</code>, close-up <code>400&times;530</code>, both straight viewport grabs +
  a <code>System.Drawing</code> crop.</p>
</div>

<div class="callout">
  <h4>Kyle geometry facts (verified, not assumed)</h4>
  <ul>
    <li><strong>Faces +Y, his left = +X</strong> &mdash; <code>l_eye</code> y=+8.05 / <code>chin</code> y=+9.15
    forward of <code>head</code> y=&minus;0.59; <code>l_ear</code> y=&minus;0.11 behind; <code>l_eye</code>
    x=+3.12 vs <code>r_eye</code> x=&minus;3.12. Signs carry over from Amy/Mimi/Guardsman.</li>
    <li><strong>Rest-rotation histogram: all 153 bones = <code>(pitch 0, yaw 0, roll 90)</code></strong> &rarr;
    the aim math is licensed.</li>
    <li>~172&nbsp;cm (<code>head</code> z=156.4, brow z=164.8). <code>hip</code> z=96.2. Arm: upperarm
    <strong>24.8&nbsp;cm</strong>, forearm <strong>26.6&nbsp;cm</strong>.</li>
    <li>The last 9 &ldquo;bones&rdquo; are mesh-node transforms (<code>Genesis9_Shape</code>,
    <code>G9BaseShirt_Shape</code>, &hellip;). Never pose them.</li>
    <li>The unskinned <code>G9AnimeHair_ToonOutline</code> contributes <strong>no bone</strong> &mdash; 10 mesh
    nodes but only 9 <code>_Shape</code> bones.</li>
  </ul>
</div>

<div class="callout note">
  <h4>The §10 four-call rule held &mdash; with one refinement</h4>
  <ol>
    <li><code>create</code> + <code>import_bones_from_asset</code> + <code>add_event_node</code> + 64&times;
    (<code>add_control</code> + force scale&nbsp;1 + Get/SetTransform + <code>connect_pins</code>) &rarr;
    <code>save_assets</code>. <strong>Chunk it ~22 controls per call</strong> &mdash; a 64-control build times
    the MCP call out; three chunks each completed.</li>
    <li><code>create_level_sequence</code> &rarr; <code>open_sequence</code> &rarr; <code>add_actors</code>
    &rarr; <code>find_or_create_track</code>.</li>
    <li><strong>Dump the rest pose and run the math OUTSIDE the sandbox.</strong> Two
    <code>get_global_transform</code> sweeps (72 + 81 bones) + one <code>get_bone_parent</code> sweep &rarr;
    plain JSON &rarr; <strong>solve in local Python</strong>. Better than §5&rsquo;s in-sandbox math: no module
    limits, and you can <code>assert</code> the R0 round-trip and print a report before keying anything.</li>
    <li><code>open_sequence</code> &rarr; <code>set_playhead_frame(0)</code> &rarr; 64&times;
    <code>set_euler_transform</code> <strong>from a literal table</strong> &rarr; <code>force_evaluate</code>.
    <strong><code>keyed: 64</code> again proved nothing</strong> &mdash; the readback is what proved it.</li>
  </ol>
  <p>&#9888; <strong>An MCP timeout is NOT a failure.</strong> The material batch, the chunk-3 rig build and the
  verification sweep all returned <code>Request timed out</code> and had <strong>all</strong> completed.
  <strong>Always re-query state before redoing the work</strong> &mdash; re-running a build blindly would have
  created 20 duplicate controls.</p>
  <p>&#128308; <code>describe_toolset</code> on <code>ControlRigTools</code>/<code>SequencerTools</code> blows
  the token limit (69&ndash;125&nbsp;k chars). It spills to a file; <code>python -c "import json; ..."</code> over
  that file to pull just the schemas you need.</p>
  <p>&#128308; <strong><code>call_tool</code> takes <code>toolset_name</code> + a BARE <code>tool_name</code> +
  <code>arguments</code></strong>. Inside <code>execute_tool_script</code> it is the opposite &mdash; the name must
  be <strong>fully qualified</strong> (<code>editor_toolset.toolsets.scene.SceneTools.find_actors</code>). The old
  <code>execute_tool('SceneTools.find_actors', &hellip;)</code> shorthand is <strong>stale</strong>.</p>
</div>
<!-- KYLE_SECTION_END -->

'''

KYLE = KYLE.replace("__HERO__", hero_b64).replace("__CLOSE__", close_b64)

# ---- 1. insert §12 after the Guardsman section ----
END = u"<!-- GUARDSMAN_SECTION_END -->"
if u"<!-- KYLE_SECTION_START -->" in s:
    s = re.sub(u"<!-- KYLE_SECTION_START -->.*?<!-- KYLE_SECTION_END -->\n*", u"", s, flags=re.S)
    print("removed existing Kyle section (idempotent re-run)")
assert END in s, "guardsman end marker missing"
s = s.replace(END, END + u"\n" + KYLE, 1)

# ---- 2. correct §10's viewport-size claim at its source ----
old10 = u"the viewport suddenly grows"
n10 = s.count(old10)
s = s.replace(
    u"Tell-tale: the viewport suddenly grows",
    u"<strong>Note (corrected on Kyle, §12): the viewport SIZE is not a reliable tell</strong> &mdash; "
    u"Kyle captured at the full 1857&times;825 <em>with the pose live</em>. Confirm a revert with a "
    u"<code>get_euler_transform</code> readback. Historically the viewport grew")

# ---- 3. refresh the hero subtitle + add a tag ----
s = s.replace(
    u'See <a href="#male" style="color:var(--accent)">§11</a>.',
    u'See <a href="#male" style="color:var(--accent)">§11</a>. '
    u'<strong>2026-07-16 (3rd pass):</strong> a <strong>hybrid</strong> G9 (realistic skin + toon anime hair) '
    u'posed happy, hands-on-hips &mdash; a two-bone elbow solve and a bone-only smile, zero new traps. '
    u'See <a href="#hybrid" style="color:var(--accent)">§12</a>.', 1)
s = s.replace(
    u'<span class="tag">G9 Toon</span>',
    u'<span class="tag">G9 Toon</span><span class="tag">Hybrid G9</span>', 1)
s = s.replace(
    u"Now covers <strong>realistic G9</strong> (Sherry, Mimi, <strong>Guardsman</strong>) and "
    u"<strong>G9 Toon</strong> (Amy).",
    u"Now covers <strong>realistic G9</strong> (Sherry, Mimi, <strong>Guardsman</strong>), "
    u"<strong>G9 Toon</strong> (Amy) and <strong>hybrid</strong> (Kyle).", 1)

io.open(HTML, "w", encoding="utf-8").write(s)
print("viewport-claim sites patched:", n10)
print("hero img bytes:", len(hero_b64), "close img bytes:", len(close_b64))
print("html:", orig_len, "->", len(s))
