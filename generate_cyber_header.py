import math
import os

# Create assets directory
os.makedirs("/opt/brody-workspace/github-profile-setup/assets", exist_ok=True)

# Generate a high-end 3D robotic cybernetic skull/face wireframe ASCII animation SVG
raw_points = []

# Forehead & Brow
for x in [-32, -22, -12, 0, 12, 22, 32]:
    raw_points.append((x, 52, 18))
    raw_points.append((x*0.85, 42, 26))

# Cyber Visor / Optic Sensor array
for x in [-26, -18, -10, 10, 18, 26]:
    raw_points.append((x, 26, 30))
    raw_points.append((x, 18, 28))

# Central Neural Spine / Bridge
raw_points.append((0, 32, 30))
raw_points.append((0, 22, 32))
raw_points.append((0, 12, 34))
raw_points.append((0, 0, 36))

# Cheekbones & Cyber Armor Plates
for y in [16, 0, -16]:
    raw_points.append((-34, y, 14))
    raw_points.append((-25, y, 25))
    raw_points.append((-14, y, 30))
    raw_points.append((14, y, 30))
    raw_points.append((25, y, 25))
    raw_points.append((34, y, 14))

# Nose / Intake Ridge
raw_points.append((-7, 6, 34))
raw_points.append((7, 6, 34))
raw_points.append((-9, -4, 32))
raw_points.append((9, -4, 32))

# Mouth / Vocoder Array
for x in [-18, -9, 0, 9, 18]:
    raw_points.append((x, -22, 28))
    raw_points.append((x*0.75, -28, 25))

# Jawline & Cyber Mandible
for x, y, z in [(-30, -26, 12), (-22, -37, 20), (-13, -44, 24), (0, -48, 28), (13, -44, 24), (22, -37, 20), (30, -26, 12)]:
    raw_points.append((x, y, z))

# Cranium Dome (Wireframe Arc)
for angle_deg in range(15, 166, 22):
    rad = math.radians(angle_deg)
    rx = 36 * math.cos(rad)
    ry = 36 * math.sin(rad) + 20
    for z in [-18, 0, 18]:
        raw_points.append((rx * (1 - abs(z)/45), ry, z))

# Neck Cyber Actuators
for y in [-58, -68]:
    for x in [-15, -8, 0, 8, 15]:
        raw_points.append((x, y, 12))

ascii_chars = ["0", "1", "<>", "::", "+", "#", "[]", "//", "X"]

frames = 40
svg_w, svg_h = 800, 420

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="100%" height="{svg_h}" style="background:#05070a; border-radius:8px; font-family:'Fira Code', 'JetBrains Mono', 'Courier New', monospace;">
<defs>
  <radialGradient id="cyber-glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.22"/>
    <stop offset="100%" stop-color="#05070a" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9"/>
    <stop offset="50%" stop-color="#7000ff" stop-opacity="0.9"/>
    <stop offset="100%" stop-color="#00f0ff" stop-opacity="0.9"/>
  </linearGradient>
  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
    <feMerge>
      <feMergeNode in="coloredBlur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<!-- Outer High-Tech Frame -->
<rect width="{svg_w}" height="{svg_h}" fill="#05070a" rx="8" stroke="#1f293d" stroke-width="1.5"/>
<rect x="8" y="8" width="{svg_w-16}" height="{svg_h-16}" fill="none" stroke="#00f0ff" stroke-opacity="0.15" stroke-width="1" rx="4"/>

<!-- Left HUD Canvas Background Glow -->
<circle cx="210" cy="210" r="170" fill="url(#cyber-glow)"/>

<!-- HUD Reticle & Radar Markings -->
<g opacity="0.35" stroke="#00f0ff" stroke-width="0.8" fill="none">
  <circle cx="210" cy="210" r="145" stroke-dasharray="6,8"/>
  <circle cx="210" cy="210" r="165" stroke-dasharray="24,12,6,12"/>
  <line x1="25" y1="210" x2="395" y2="210" stroke-dasharray="3,6"/>
  <line x1="210" y1="25" x2="210" y2="395" stroke-dasharray="3,6"/>
  <!-- Corner Tech Accents -->
  <path d="M 20 35 L 20 20 L 35 20" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 380 20 L 395 20 L 395 35" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 20 385 L 20 400 L 35 400" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 380 400 L 395 400 L 395 385" stroke="#00f0ff" stroke-width="2"/>
</g>

<!-- Left Panel Telemetry Data -->
<text x="25" y="42" fill="#00f0ff" font-size="10" letter-spacing="1.5" opacity="0.85">SYS_ID: CYBER_CORE_V4.9</text>
<text x="25" y="56" fill="#8b5cf6" font-size="9" letter-spacing="1" opacity="0.8">NODE_TARGET: 0x7F_RIVAI</text>
<text x="25" y="385" fill="#00f0ff" font-size="9" letter-spacing="1" opacity="0.7">MODE: 3D_ROBOTIC_POINT_CLOUD</text>
<text x="25" y="398" fill="#10b981" font-size="9" letter-spacing="1" opacity="0.95">● KERNEL_STATUS: OPERATIONAL</text>

<!-- Right Terminal Deck -->
<g transform="translate(420, 35)">
  <!-- Main Terminal Box -->
  <rect width="355" height="350" rx="6" fill="#090d16" stroke="#00f0ff" stroke-opacity="0.3" stroke-width="1"/>
  <!-- Header Bar -->
  <path d="M 0 6 Q 0 0 6 0 L 349 0 Q 355 0 355 6 L 355 30 L 0 30 Z" fill="#111827"/>
  <line x1="0" y1="30" x2="355" y2="30" stroke="#1f293d" stroke-width="1"/>
  <circle cx="16" cy="15" r="4" fill="#ef4444"/>
  <circle cx="28" cy="15" r="4" fill="#f59e0b"/>
  <circle cx="40" cy="15" r="4" fill="#10b981"/>
  <text x="56" y="19" fill="#6b7280" font-size="10" letter-spacing="1">riva@autonomous-node:~</text>

  <!-- Terminal Content -->
  <text x="20" y="60" fill="#00f0ff" font-size="16" font-weight="bold" letter-spacing="1" filter="url(#glow)">RIVA IMANUDIN</text>
  <text x="20" y="78" fill="#93c5fd" font-size="11" letter-spacing="0.5">> Fullstack Software &amp; AI Systems Architect</text>

  <line x1="20" y1="92" x2="335" y2="92" stroke="url(#line-grad)" stroke-width="1.5"/>

  <!-- Spec Fields -->
  <text x="20" y="118" fill="#38bdf8" font-size="11" font-weight="bold">[SYSTEM SPECIFICATION]</text>
  <text x="20" y="138" fill="#94a3b8" font-size="10">  Primary Stack  : Next.js 15 / TypeScript / React</text>
  <text x="20" y="154" fill="#94a3b8" font-size="10">  Backend Core   : Laravel / PHP 8.4 / Node.js</text>
  <text x="20" y="170" fill="#94a3b8" font-size="10">  Data &amp; Persistence : PostgreSQL / MySQL / Supabase</text>
  <text x="20" y="186" fill="#94a3b8" font-size="10">  Infrastructure : Docker / Nginx / Linux DevOps</text>
  <text x="20" y="202" fill="#94a3b8" font-size="10">  AI Architecture : Autonomous Agents &amp; Vision AI</text>

  <line x1="20" y1="218" x2="335" y2="218" stroke="#1f293d" stroke-width="1"/>

  <!-- System Directive -->
  <text x="20" y="242" fill="#a78bfa" font-size="11" font-weight="bold">[SYSTEM DIRECTIVE]</text>
  <text x="20" y="262" fill="#cbd5e1" font-size="10.5">  "Engineering high-performance,</text>
  <text x="20" y="278" fill="#cbd5e1" font-size="10.5">   resilient software &amp; autonomous</text>
  <text x="20" y="294" fill="#cbd5e1" font-size="10.5">   AI agent networks."</text>

  <line x1="20" y1="310" x2="335" y2="310" stroke="#1f293d" stroke-width="1"/>

  <text x="20" y="330" fill="#10b981" font-size="10">> EXECUTION_STATE: READY</text>
  <rect x="180" y="322" width="7" height="11" fill="#00f0ff">
    <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
  </rect>
</g>
'''

dur = 4.0 # 4 second animation cycle
svg += f'<g id="robot-mesh" transform="translate(210, 205)">\n'

for f in range(frames):
    angle = (2 * math.pi * f) / frames
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)
    
    pitch = math.radians(7 * math.sin(angle))
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
        
        fov = 170
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
    
    frame_svg = f'<g id="f_{f}">\n'
    frame_svg += f'<animate attributeName="display" values="'
    vals = []
    for i in range(frames):
        vals.append("inline" if i == f else "none")
    frame_svg += ";".join(vals) + f'" dur="{dur}s" repeatCount="indefinite"/>\n'
    
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

print("Generated assets/cyber-header.svg successfully!")
