import math

# Generate an animated SVG of a 3D rotating cyber robotic cybernetic skull/face wireframe / ASCII point-cloud
# 3D points representing a robotic android/cyborg face mask
raw_points = []

# Forehead & Brow
for x in [-30, -20, -10, 0, 10, 20, 30]:
    raw_points.append((x, 50, 20))
    raw_points.append((x*0.9, 40, 25))

# Eyes & Visor (Cyber optic frame)
for x in [-25, -18, -12, 12, 18, 25]:
    raw_points.append((x, 25, 28))
    raw_points.append((x, 20, 26))

# Center cyber core / bridge
raw_points.append((0, 30, 28))
raw_points.append((0, 20, 30))
raw_points.append((0, 10, 32))
raw_points.append((0, 0, 34))

# Cheekbones & Cyber Plates
for y in [15, 0, -15]:
    raw_points.append((-32, y, 15))
    raw_points.append((-24, y, 24))
    raw_points.append((-15, y, 28))
    raw_points.append((15, y, 28))
    raw_points.append((24, y, 24))
    raw_points.append((32, y, 15))

# Nose / Sensory Ridge
raw_points.append((-6, 5, 32))
raw_points.append((6, 5, 32))
raw_points.append((-8, -5, 30))
raw_points.append((8, -5, 30))

# Mouth / Vocoder lines
for x in [-16, -8, 0, 8, 16]:
    raw_points.append((x, -20, 26))
    raw_points.append((x*0.8, -25, 24))

# Jawline & Chin Matrix
for x, y, z in [(-28, -25, 10), (-20, -35, 18), (-12, -42, 22), (0, -45, 25), (12, -42, 22), (20, -35, 18), (28, -25, 10)]:
    raw_points.append((x, y, z))

# Cranium dome (wireframe mesh)
for angle_deg in range(0, 180, 25):
    rad = math.radians(angle_deg)
    rx = 34 * math.cos(rad)
    ry = 34 * math.sin(rad) + 20
    for z in [-15, 0, 15]:
        raw_points.append((rx * (1 - abs(z)/40), ry, z))

# Neck actuators
for y in [-55, -65]:
    for x in [-14, -7, 0, 7, 14]:
        raw_points.append((x, y, 10))

ascii_chars = ["0", "1", "<>", "::", "+", "#", "[]", "//", "{"]

frames = 40
svg_w, svg_h = 750, 420

keyframes_svg = []

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="100%" height="{svg_h}" style="background:#090d16; border-radius:12px; font-family:'Fira Code', 'Courier New', monospace;">
<defs>
  <radialGradient id="cyber-glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.18"/>
    <stop offset="100%" stop-color="#090d16" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#7000ff" stop-opacity="0.9"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.8"/>
  </linearGradient>
  <filter id="glow">
    <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
    <feMerge>
      <feMergeNode in="coloredBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<!-- Background & HUD Grid -->
<rect width="{svg_w}" height="{svg_h}" fill="#090d16" rx="12"/>
<circle cx="210" cy="210" r="180" fill="url(#cyber-glow)"/>

<!-- HUD UI Elements -->
<g opacity="0.4" stroke="#00f0ff" stroke-width="0.8" fill="none">
  <circle cx="210" cy="210" r="150" stroke-dasharray="4,8"/>
  <circle cx="210" cy="210" r="170" stroke-dasharray="20,10,5,10"/>
  <line x1="30" y1="210" x2="390" y2="210" stroke-dasharray="2,6"/>
  <line x1="210" y1="30" x2="210" y2="390" stroke-dasharray="2,6"/>
  <rect x="25" y="25" width="12" height="12"/>
  <rect x="385" y="25" width="12" height="12"/>
  <rect x="25" y="385" width="12" height="12"/>
  <rect x="385" y="385" width="12" height="12"/>
</g>

<!-- HUD Telemetry Text Left/Top -->
<text x="35" y="45" fill="#00f0ff" font-size="10" letter-spacing="2" opacity="0.8">// SYSTEM: NEURAL_CORE_V3</text>
<text x="35" y="60" fill="#7000ff" font-size="9" letter-spacing="1" opacity="0.8">LOC: 0x7F_RIVAI_NODE</text>
<text x="35" y="380" fill="#00f0ff" font-size="9" opacity="0.6">RENDER: 3D_POINT_CLOUD</text>
<text x="35" y="395" fill="#00ffaa" font-size="9" opacity="0.7">STATUS: OPTIMAL_RUNNING</text>

<!-- Center-Right Holographic Identity Panel -->
<g transform="translate(420, 50)">
  <!-- Terminal Border -->
  <rect width="300" height="320" rx="8" fill="#0d1322" stroke="#00f0ff" stroke-width="1" stroke-opacity="0.3"/>
  <rect width="300" height="28" rx="8" fill="#131c31"/>
  <circle cx="15" cy="14" r="4" fill="#ff5f56"/>
  <circle cx="28" cy="14" r="4" fill="#ffbd2e"/>
  <circle cx="41" cy="14" r="4" fill="#27c93f"/>
  <text x="60" y="18" fill="#8b949e" font-size="10" letter-spacing="1">terminal@riva-core:~$</text>

  <text x="20" y="60" fill="#00f0ff" font-size="14" font-weight="bold" filter="url(#glow)">RIVA IMANUDIN</text>
  <text x="20" y="80" fill="#a5b4fc" font-size="11">// Systems &amp; Autonomous AI Architect</text>
  
  <line x1="20" y1="95" x2="280" y2="95" stroke="url(#line-grad)" stroke-width="1"/>

  <text x="20" y="125" fill="#6ee7b7" font-size="11">> STACK: FULLSTACK / DEVOPS</text>
  <text x="20" y="145" fill="#94a3b8" font-size="10">  • Next.js 15 / TypeScript / React</text>
  <text x="20" y="163" fill="#94a3b8" font-size="10">  • Laravel / PHP 8.4 / Node.js</text>
  <text x="20" y="181" fill="#94a3b8" font-size="10">  • Docker / Nginx / Linux Server</text>
  <text x="20" y="199" fill="#94a3b8" font-size="10">  • Autonomous AI Agents &amp; IoT</text>

  <line x1="20" y1="220" x2="280" y2="220" stroke="#1e293b" stroke-width="1"/>

  <text x="20" y="245" fill="#38bdf8" font-size="11">> ARCHITECTURE DIRECTIVE:</text>
  <text x="20" y="265" fill="#cbd5e1" font-size="10">  "Transforming complex infrastructure</text>
  <text x="20" y="280" fill="#cbd5e1" font-size="10">   into high-resilience autonomous</text>
  <text x="20" y="295" fill="#cbd5e1" font-size="10">   intelligence &amp; clean web systems."</text>

  <rect x="20" y="308" width="8" height="2" fill="#00f0ff">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</g>
'''

# Now build the animated 3D robotic point-cloud ASCII face
# We will use SVG animations (<g id="frameX"> with display toggle or opacity)
dur = 4.0 # 4 seconds full rotation loop

svg += f'<g id="robot-mesh" transform="translate(210, 210)">\n'

for f in range(frames):
    angle = (2 * math.pi * f) / frames
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)
    
    # Slight pitch oscillation
    pitch = math.radians(8 * math.sin(angle))
    sin_p = math.sin(pitch)
    cos_p = math.cos(pitch)
    
    t_start = round(f / frames, 3)
    t_end = round((f + 1) / frames, 3)
    
    # Calculate transformed points
    transformed = []
    for idx, (x, y, z) in enumerate(raw_points):
        # Rotate Y
        x1 = x * cos_a + z * sin_a
        y1 = y
        z1 = -x * sin_a + z * cos_a
        
        # Pitch X
        x2 = x1
        y2 = y1 * cos_p - z1 * sin_p
        z2 = y1 * sin_p + z1 * cos_p
        
        # Perspective projection
        fov = 160
        scale = fov / (fov + z2 + 40)
        proj_x = x2 * scale * 2.8
        proj_y = -y2 * scale * 2.8 # invert Y for SVG
        
        char = ascii_chars[(idx + f) % len(ascii_chars)]
        
        # Depth shading
        if z2 > 10:
            color = "#00f0ff"
            opacity = 0.95
            size = 10 * scale
            weight = "bold"
        elif z2 > -10:
            color = "#3b82f6"
            opacity = 0.7
            size = 8.5 * scale
            weight = "normal"
        else:
            color = "#6366f1"
            opacity = 0.35
            size = 7 * scale
            weight = "normal"
            
        transformed.append((z2, proj_x, proj_y, char, color, opacity, size, weight))
        
    # Sort by Z (depth) so front renders over back
    transformed.sort(key=lambda item: item[0])
    
    frame_svg = f'<g id="f_{f}">\n'
    frame_svg += f'<animate attributeName="display" values="'
    vals = []
    for i in range(frames):
        vals.append("inline" if i == f else "none")
    frame_svg += ";".join(vals) + f'" dur="{dur}s" repeatCount="indefinite"/>\n'
    
    # Render lines / connections between adjacent high-depth points for cyber-wireframe feel
    for i in range(0, len(transformed)-1, 2):
        z_val, x_a, y_a, _, col, op, _, _ = transformed[i]
        _, x_b, y_b, _, _, _, _, _ = transformed[i+1]
        if z_val > 0:
            frame_svg += f'<line x1="{x_a:.1f}" y1="{y_a:.1f}" x2="{x_b:.1f}" y2="{y_b:.1f}" stroke="{col}" stroke-width="0.5" opacity="{op*0.4}"/>\n'
            
    # Render points/ASCII chars
    for z_val, px, py, ch, col, op, sz, wt in transformed:
        frame_svg += f'<text x="{px:.1f}" y="{py:.1f}" fill="{col}" opacity="{op:.2f}" font-size="{sz:.1f}" font-weight="{wt}" text-anchor="middle" dominant-baseline="central">{ch}</text>\n'
        
    frame_svg += '</g>\n'
    svg += frame_svg

svg += '</g>\n</svg>'

with open("/opt/brody-workspace/github-profile-setup/cyber-robot-3d.svg", "w") as out:
    out.write(svg)

print("Generated cyber-robot-3d.svg successfully!")
