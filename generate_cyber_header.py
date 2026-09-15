import math
import os

os.makedirs("/opt/brody-workspace/github-profile-setup/assets", exist_ok=True)

# Generate points for 3D Robotic Cybernetic Face Wireframe
raw_points = []

# Forehead & Brow
for x in [-30, -20, -10, 0, 10, 20, 30]:
    raw_points.append((x, 50, 18))
    raw_points.append((x*0.85, 40, 25))

# Cyber Visor / Optic Sensors
for x in [-24, -16, -8, 8, 16, 24]:
    raw_points.append((x, 24, 28))
    raw_points.append((x, 16, 26))

# Central Neural Spine
raw_points.append((0, 30, 28))
raw_points.append((0, 20, 30))
raw_points.append((0, 10, 32))
raw_points.append((0, 0, 34))

# Cheekbones & Cyber Armor Plates
for y in [14, 0, -14]:
    raw_points.append((-32, y, 14))
    raw_points.append((-22, y, 24))
    raw_points.append((-12, y, 28))
    raw_points.append((12, y, 28))
    raw_points.append((22, y, 24))
    raw_points.append((32, y, 14))

# Nose Ridge
raw_points.append((-6, 5, 32))
raw_points.append((6, 5, 32))
raw_points.append((-8, -4, 30))
raw_points.append((8, -4, 30))

# Mouth Vocoder Array
for x in [-16, -8, 0, 8, 16]:
    raw_points.append((x, -20, 26))
    raw_points.append((x*0.75, -26, 24))

# Jawline & Mandible
for x, y, z in [(-28, -24, 10), (-20, -34, 18), (-12, -42, 22), (0, -45, 26), (12, -42, 22), (20, -34, 18), (28, -24, 10)]:
    raw_points.append((x, y, z))

# Cranium Arc
for angle_deg in range(15, 166, 25):
    rad = math.radians(angle_deg)
    rx = 34 * math.cos(rad)
    ry = 34 * math.sin(rad) + 18
    for z in [-16, 0, 16]:
        raw_points.append((rx * (1 - abs(z)/40), ry, z))

# Neck Actuators
for y in [-54, -64]:
    for x in [-14, -7, 0, 7, 14]:
        raw_points.append((x, y, 10))

ascii_chars = ["0", "1", "<>", "::", "+", "#", "[]", "//", "X"]

frames = 30
svg_w, svg_h = 800, 420
dur = 4.0 # 4 seconds cycle

# Build CSS Keyframes for GitHub Compatibility
css_rules = [
  "@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }",
  ".blinking { animation: blink 1s infinite; }"
]

# Generate frame keyframe animation classes using CSS opacity/display
for f in range(frames):
    pct_start = round((f / frames) * 100, 2)
    pct_end = round(((f + 1) / frames) * 100, 2)
    css_rules.append(f"""
@keyframes f_{f} {{
  0%, {pct_start}% {{ opacity: 0; visibility: hidden; }}
  {pct_start + 0.01}%, {pct_end}% {{ opacity: 1; visibility: visible; }}
  {pct_end + 0.01}%, 100% {{ opacity: 0; visibility: hidden; }}
}}
.frame-{f} {{
  animation: f_{f} {dur}s step-end infinite;
}}""")

css_style = "\n".join(css_rules)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="100%" height="{svg_h}">
<defs>
  <style type="text/css">
    <![CDATA[
    {css_style}
    ]]>
  </style>
  <radialGradient id="cyber-glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.25"/>
    <stop offset="100%" stop-color="#05070a" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9"/>
    <stop offset="50%" stop-color="#7000ff" stop-opacity="0.9"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.9"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
    <feMerge>
      <feMergeNode in="coloredBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<!-- Background Frame -->
<rect width="{svg_w}" height="{svg_h}" fill="#05070a" rx="8" stroke="#1f293d" stroke-width="1.5"/>
<rect x="8" y="8" width="{svg_w-16}" height="{svg_h-16}" fill="none" stroke="#00f0ff" stroke-opacity="0.15" stroke-width="1" rx="4"/>

<!-- Left HUD Radial Glow -->
<circle cx="210" cy="210" r="160" fill="url(#cyber-glow)"/>

<!-- HUD Reticle & Markings -->
<g opacity="0.35" stroke="#00f0ff" stroke-width="0.8" fill="none">
  <circle cx="210" cy="210" r="145" stroke-dasharray="6,8"/>
  <circle cx="210" cy="210" r="165" stroke-dasharray="24,12,6,12"/>
  <line x1="25" y1="210" x2="395" y2="210" stroke-dasharray="3,6"/>
  <line x1="210" y1="25" x2="210" y2="395" stroke-dasharray="3,6"/>
  <path d="M 20 35 L 20 20 L 35 20" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 380 20 L 395 20 L 395 35" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 20 385 L 20 400 L 35 400" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 380 400 L 395 400 L 395 385" stroke="#00f0ff" stroke-width="2"/>
</g>

<!-- Left HUD Telemetry Text -->
<text x="25" y="42" fill="#00f0ff" font-size="10" font-family="'Fira Code', monospace" letter-spacing="1.5" opacity="0.85">SYS_ID: CYBER_CORE_V4.9</text>
<text x="25" y="56" fill="#8b5cf6" font-size="9" font-family="'Fira Code', monospace" letter-spacing="1" opacity="0.8">NODE_TARGET: 0x7F_RIVAI</text>
<text x="25" y="385" fill="#00f0ff" font-size="9" font-family="'Fira Code', monospace" letter-spacing="1" opacity="0.7">MODE: 3D_ROBOTIC_POINT_CLOUD</text>
<text x="25" y="398" fill="#10b981" font-size="9" font-family="'Fira Code', monospace" letter-spacing="1" opacity="0.95">● KERNEL_STATUS: OPERATIONAL</text>

<!-- Right Terminal Deck -->
<g transform="translate(420, 35)">
  <rect width="355" height="350" rx="6" fill="#090d16" stroke="#00f0ff" stroke-opacity="0.3" stroke-width="1"/>
  <path d="M 0 6 Q 0 0 6 0 L 349 0 Q 355 0 355 6 L 355 30 L 0 30 Z" fill="#111827"/>
  <line x1="0" y1="30" x2="355" y2="30" stroke="#1f293d" stroke-width="1"/>
  <circle cx="16" cy="15" r="4" fill="#ef4444"/>
  <circle cx="28" cy="15" r="4" fill="#f59e0b"/>
  <circle cx="40" cy="15" r="4" fill="#10b981"/>
  <text x="56" y="19" fill="#6b7280" font-size="10" font-family="'Fira Code', monospace" letter-spacing="1">riva@autonomous-node:~</text>

  <text x="20" y="60" fill="#00f0ff" font-size="16" font-family="'Fira Code', monospace" font-weight="bold" letter-spacing="1" filter="url(#glow)">RIVA IMANUDIN</text>
  <text x="20" y="78" fill="#93c5fd" font-size="11" font-family="'Fira Code', monospace" letter-spacing="0.5">> Fullstack Software &amp; AI Systems Architect</text>

  <line x1="20" y1="92" x2="335" y2="92" stroke="url(#line-grad)" stroke-width="1.5"/>

  <text x="20" y="118" fill="#38bdf8" font-size="11" font-family="'Fira Code', monospace" font-weight="bold">[SYSTEM SPECIFICATION]</text>
  <text x="20" y="138" fill="#94a3b8" font-size="10" font-family="'Fira Code', monospace">  Primary Stack  : Next.js 15 / TypeScript / React</text>
  <text x="20" y="154" fill="#94a3b8" font-size="10" font-family="'Fira Code', monospace">  Backend Core   : Laravel / PHP 8.4 / Node.js</text>
  <text x="20" y="170" fill="#94a3b8" font-size="10" font-family="'Fira Code', monospace">  Data &amp; Persistence : PostgreSQL / MySQL / Supabase</text>
  <text x="20" y="186" fill="#94a3b8" font-size="10" font-family="'Fira Code', monospace">  Infrastructure : Docker / Nginx / Linux DevOps</text>
  <text x="20" y="202" fill="#94a3b8" font-size="10" font-family="'Fira Code', monospace">  AI Architecture : Autonomous Agents &amp; Vision AI</text>

  <line x1="20" y1="218" x2="335" y2="218" stroke="#1f293d" stroke-width="1"/>

  <text x="20" y="242" fill="#a78bfa" font-size="11" font-family="'Fira Code', monospace" font-weight="bold">[SYSTEM DIRECTIVE]</text>
  <text x="20" y="262" fill="#cbd5e1" font-size="10.5" font-family="'Fira Code', monospace">  "Engineering high-performance,</text>
  <text x="20" y="278" fill="#cbd5e1" font-size="10.5" font-family="'Fira Code', monospace">   resilient software &amp; autonomous</text>
  <text x="20" y="294" fill="#cbd5e1" font-size="10.5" font-family="'Fira Code', monospace">   AI agent networks."</text>

  <line x1="20" y1="310" x2="335" y2="310" stroke="#1f293d" stroke-width="1"/>

  <text x="20" y="330" fill="#10b981" font-size="10" font-family="'Fira Code', monospace">> EXECUTION_STATE: READY</text>
  <rect x="180" y="322" width="7" height="11" fill="#00f0ff" class="blinking"/>
</g>

<!-- 3D Robot Mesh Group -->
<g id="robot-mesh" transform="translate(210, 205)" font-family="'Fira Code', monospace">
'''

for f in range(frames):
    angle = (2 * math.pi * f) / frames
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)
    
    pitch = math.radians(6 * math.sin(angle))
    sin_p = math.sin(pitch)
    cos_p = math.cos(pitch)
    
    transformed = []
    for idx, (x, y, z) in enumerate(raw_points):
        x1 = x * cos_a + z * sin_a
        y1 = y
        z1 = -x * sin_a + z * cos_a
        
        x2 = x1
        y2 = y1 * cos_p - z1 * sin_p
        z2 = y1 * sin_p + z1 * cos_p
        
        fov = 160
        scale = fov / (fov + z2 + 45)
        proj_x = x2 * scale * 2.7
        proj_y = -y2 * scale * 2.7
        
        char = ascii_chars[(idx + f) % len(ascii_chars)]
        
        if z2 > 12:
            color = "#00f0ff"
            opacity = 0.95
            size = 10 * scale
            weight = "bold"
        elif z2 > -8:
            color = "#3b82f6"
            opacity = 0.7
            size = 8.5 * scale
            weight = "normal"
        else:
            color = "#8b5cf6"
            opacity = 0.35
            size = 7 * scale
            weight = "normal"
            
        transformed.append((z2, proj_x, proj_y, char, color, opacity, size, weight))
        
    transformed.sort(key=lambda item: item[0])
    
    frame_svg = f'<g class="frame-{f}">\n'
    
    for i in range(0, len(transformed)-1, 2):
        z_val, x_a, y_a, _, col, op, _, _ = transformed[i]
        _, x_b, y_b, _, _, _, _, _ = transformed[i+1]
        if z_val > 0:
            frame_svg += f'<line x1="{x_a:.1f}" y1="{y_a:.1f}" x2="{x_b:.1f}" y2="{y_b:.1f}" stroke="{col}" stroke-width="0.5" opacity="{op*0.35}"/>\n'
            
    for z_val, px, py, ch, col, op, sz, wt in transformed:
        frame_svg += f'<text x="{px:.1f}" y="{py:.1f}" fill="{col}" opacity="{op:.2f}" font-size="{sz:.1f}" font-weight="{wt}" text-anchor="middle" dominant-baseline="central">{ch}</text>\n'
        
    frame_svg += '</g>\n'
    svg += frame_svg

svg += '</g>\n</svg>'

with open("/opt/brody-workspace/github-profile-setup/assets/cyber-header.svg", "w") as out:
    out.write(svg)

print("Generated GitHub-compatible CSS animated cyber-header.svg successfully!")
