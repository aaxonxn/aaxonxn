import os

def build_svg(theme):
    if theme == "dark":
        bg_color = "#09090B"
        grid_color = "#FFFFFF"
        grid_opacity = "0.03"
        primary_accent = "#FF6B00"
        secondary_accent = "#38BDF8"
        text_primary = "#FFFFFF"
        text_secondary = "#94A3B8"
        border_color = "#27272A"
        portrait_file = "assets/portrait_dark.b64"
    else:
        bg_color = "#FAFAFA"
        grid_color = "#0F172A"
        grid_opacity = "0.05"
        primary_accent = "#EA580C"
        secondary_accent = "#0284C7"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        border_color = "#E2E8F0"
        portrait_file = "assets/portrait_light.b64"

    try:
        with open(portrait_file, "r") as f:
            b64_data = f.read().strip()
    except FileNotFoundError:
        b64_data = ""

    # Constants
    width = 1180
    height = 610
    left_w = 448
    padding = 40
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    
    <defs>
        <style>
            @keyframes fadeIn {{
                0% {{ opacity: 0; }}
                100% {{ opacity: 1; }}
            }}
            
            @keyframes typeIn {{
                0% {{ clip-path: inset(0 100% 0 0); }}
                100% {{ clip-path: inset(0 0 0 0); }}
            }}

            @keyframes pulseStatus {{
                0% {{ opacity: 0.4; }}
                50% {{ opacity: 1; }}
                100% {{ opacity: 0.4; }}
            }}

            @keyframes breathePortrait {{
                0% {{ opacity: 0.98; }}
                50% {{ opacity: 1; }}
                100% {{ opacity: 0.98; }}
            }}

            @keyframes driftParticle1 {{
                0% {{ transform: translateY(0px); opacity: 0.2; }}
                50% {{ transform: translateY(-4px); opacity: 0.8; }}
                100% {{ transform: translateY(0px); opacity: 0.2; }}
            }}

            @keyframes driftParticle2 {{
                0% {{ transform: translateY(0px); opacity: 0.2; }}
                50% {{ transform: translateY(4px); opacity: 0.6; }}
                100% {{ transform: translateY(0px); opacity: 0.2; }}
            }}

            .boot-layer {{
                opacity: 0;
                animation: fadeIn 0.8s ease-out forwards;
            }}

            #grid {{ animation-delay: 0.3s; }}
            #portrait-frame {{ animation-delay: 0.6s; }}
            #portrait-img {{ 
                animation: fadeIn 1s ease-out 0.9s forwards, breathePortrait 8s ease-in-out 2s infinite; 
                opacity: 0;
            }}
            #terminal-header {{ animation-delay: 1.2s; }}
            #research-panel {{ animation-delay: 1.5s; }}
            #projects-panel {{ animation-delay: 1.8s; }}
            
            #status-dot {{
                opacity: 0;
                animation: fadeIn 0.3s ease-out 2.1s forwards, pulseStatus 2s ease-in-out 2.4s infinite;
            }}
            #status-text {{ animation-delay: 2.1s; }}
            
            .particle {{ opacity: 0; }}
            .particle-1 {{ animation: fadeIn 1s ease-out 2.4s forwards, driftParticle1 8s ease-in-out 3.4s infinite; }}
            .particle-2 {{ animation: fadeIn 1s ease-out 2.6s forwards, driftParticle2 10s ease-in-out 3.6s infinite; }}

            .title {{ font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; font-weight: 800; font-size: 36px; fill: {text_primary}; letter-spacing: 1px; }}
            .subtitle {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 14px; fill: {secondary_accent}; letter-spacing: 0.5px; }}
            .label {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 12px; fill: {text_secondary}; text-transform: uppercase; letter-spacing: 1px; }}
            .data {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 14px; fill: {text_primary}; }}
            .data-dim {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 14px; fill: {text_secondary}; }}
            
        </style>
        
        <pattern id="grid-pattern" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_color}" stroke-width="1" opacity="{grid_opacity}"/>
            <circle cx="40" cy="40" r="1" fill="{grid_color}" opacity="{float(grid_opacity)*2}"/>
        </pattern>
        
        <clipPath id="portrait-clip">
            <rect x="0" y="0" width="360" height="460" rx="16"/>
        </clipPath>
    </defs>

    <g id="background">
        <rect width="{width}" height="{height}" fill="{bg_color}"/>
    </g>

    <g id="grid" class="boot-layer">
        <rect width="{width}" height="{height}" fill="url(#grid-pattern)"/>
    </g>

    <g id="decorative-geometry" class="boot-layer" style="animation-delay: 0.4s;">
        <path d="M 20 20 L 40 20 M 20 20 L 20 40" fill="none" stroke="{text_secondary}" stroke-width="2" opacity="0.3"/>
        <path d="M {width-20} 20 L {width-40} 20 M {width-20} 20 L {width-20} 40" fill="none" stroke="{text_secondary}" stroke-width="2" opacity="0.3"/>
        <path d="M 20 {height-20} L 40 {height-20} M 20 {height-20} L 20 {height-40}" fill="none" stroke="{text_secondary}" stroke-width="2" opacity="0.3"/>
        <path d="M {width-20} {height-20} L {width-40} {height-20} M {width-20} {height-20} L {width-20} {height-40}" fill="none" stroke="{text_secondary}" stroke-width="2" opacity="0.3"/>
        <line x1="{left_w}" y1="{padding * 2}" x2="{left_w}" y2="{height - padding * 2}" stroke="{border_color}" stroke-width="1"/>
    </g>

    <g id="portrait" transform="translate(44, 75)">
        <image id="portrait-img" href="data:image/png;base64,{b64_data}" x="0" y="0" width="360" height="460" clip-path="url(#portrait-clip)" preserveAspectRatio="xMidYMid slice"/>
    </g>

    <g id="portrait-frame" class="boot-layer" transform="translate(44, 75)">
        <rect x="0" y="0" width="360" height="460" rx="16" fill="none" stroke="{secondary_accent}" stroke-width="1" opacity="0.8"/>
        
        <!-- Corner Accents -->
        <rect x="-2" y="-2" width="8" height="8" rx="2" fill="{bg_color}" stroke="{secondary_accent}" stroke-width="1"/>
        <rect x="354" y="-2" width="8" height="8" rx="2" fill="{bg_color}" stroke="{secondary_accent}" stroke-width="1"/>
        <rect x="-2" y="454" width="8" height="8" rx="2" fill="{bg_color}" stroke="{secondary_accent}" stroke-width="1"/>
        <rect x="354" y="454" width="8" height="8" rx="2" fill="{bg_color}" stroke="{secondary_accent}" stroke-width="1"/>

        <!-- Top Label -->
        <rect x="20" y="-10" width="120" height="20" fill="{bg_color}"/>
        <text x="25" y="4" class="label" fill="{secondary_accent}">NEURAL PROFILE</text>
        
        <!-- Bottom AI Mark -->
        <text x="290" y="445" class="label" fill="{secondary_accent}" opacity="0.5">AI_PROFILE</text>
    </g>

    <g id="information-panel" transform="translate({left_w + 40}, 75)">
        
        <!-- HEADER -->
        <g id="terminal-header" class="boot-layer">
            <rect x="-20" y="-3" width="3" height="30" fill="{primary_accent}"/>
            <text x="0" y="25" class="title">AARON GEORGE</text>
            <text x="0" y="55" class="subtitle">Artificial Intelligence Engineer</text>
            <text x="0" y="80" class="label" fill="{text_secondary}">Machine Learning • Robotics • Computer Vision • Multi-Agent Systems</text>
            <line x1="-20" y1="105" x2="600" y2="105" stroke="{border_color}" stroke-width="1" stroke-dasharray="4 4"/>
        </g>
        
        <!-- SYSTEM INFO -->
        <g id="system-info" class="boot-layer" style="animation-delay: 1.3s;">
            <text x="0" y="140" class="data-dim">Engineer ...... </text><text x="140" y="140" class="data">Aaron George</text>
            <text x="0" y="165" class="data-dim">Role .......... </text><text x="140" y="165" class="data">AI Systems Architect</text>
            <text x="0" y="190" class="data-dim">Location ...... </text><text x="140" y="190" class="data">Kerala, India</text>
            <text x="0" y="215" class="data-dim">Education ..... </text><text x="140" y="215" class="data">B.Tech CSE (AI)</text>
            <text x="0" y="240" class="data-dim">Status ........ </text><text x="140" y="240" class="data">Building Intelligent Systems</text>
        </g>

        <!-- RESEARCH DOMAINS -->
        <g id="research-panel" class="boot-layer">
            <rect x="0" y="280" width="280" height="195" fill="none" stroke="{border_color}" stroke-width="1" rx="4"/>
            <text x="20" y="310" class="label">Research Domains</text>
            <line x1="20" y1="322" x2="260" y2="322" stroke="{border_color}" stroke-width="1"/>
            
            <text x="20" y="352" class="data" fill="{secondary_accent}">&#x25B8;</text>
            <text x="35" y="352" class="data">Machine Learning</text>
            
            <text x="20" y="382" class="data" fill="{secondary_accent}">&#x25B8;</text>
            <text x="35" y="382" class="data">Computer Vision</text>
            
            <text x="20" y="412" class="data" fill="{secondary_accent}">&#x25B8;</text>
            <text x="35" y="412" class="data">Robotics</text>
            
            <text x="20" y="442" class="data" fill="{secondary_accent}">&#x25B8;</text>
            <text x="35" y="442" class="data">Multi-Agent Systems</text>
        </g>

        <!-- CURRENT PROJECTS -->
        <g id="projects-panel" class="boot-layer">
            <rect x="320" y="280" width="310" height="195" fill="none" stroke="{border_color}" stroke-width="1" rx="4"/>
            <text x="340" y="310" class="label">Featured Projects</text>
            <line x1="340" y1="322" x2="610" y2="322" stroke="{border_color}" stroke-width="1"/>
            
            <text x="340" y="352" class="data" fill="{primary_accent}">&#x25B8;</text>
            <text x="355" y="352" class="data">AgriMind AI</text>
            
            <text x="340" y="382" class="data" fill="{primary_accent}">&#x25B8;</text>
            <text x="355" y="382" class="data">DRISHTI</text>
            
            <text x="340" y="412" class="data" fill="{primary_accent}">&#x25B8;</text>
            <text x="355" y="412" class="data">Swarm Intelligence</text>
            
            <text x="340" y="442" class="data" fill="{primary_accent}">&#x25B8;</text>
            <text x="355" y="442" class="data">FlowAPI</text>
        </g>

    </g>

    <!-- LAYER 8: STATUS INDICATOR -->
    <g id="status-indicator" transform="translate({width - 150}, 40)">
        <rect x="-10" y="-15" width="130" height="26" rx="4" fill="{bg_color}" stroke="{border_color}" stroke-width="1"/>
        <circle id="status-dot" cx="0" cy="-2" r="4" fill="#10B981"/>
        <text id="status-text" x="12" y="2" class="label boot-layer" fill="#10B981">STATUS: ONLINE</text>
    </g>

    <!-- LAYER 9: DECORATIVE PARTICLES (Subtle Animations) -->
    <g id="accent-particles">
        <!-- Near portrait -->
        <rect x="35" y="80" width="2" height="2" fill="{secondary_accent}" class="particle particle-1"/>
        <rect x="410" y="520" width="2" height="2" fill="{secondary_accent}" class="particle particle-2"/>
        <rect x="30" y="510" width="2" height="2" fill="{primary_accent}" class="particle particle-1"/>
        
        <!-- Near info panel -->
        <rect x="{width - 45}" y="300" width="2" height="2" fill="{secondary_accent}" class="particle particle-2"/>
        <rect x="{left_w + 20}" y="{height - 60}" width="2" height="2" fill="{primary_accent}" class="particle particle-1"/>
    </g>

    <!-- LAYER 10: METADATA -->
    <metadata>
        <creator>Aaron George Profile Generator</creator>
        <version>1.1</version>
        <theme>{theme}</theme>
    </metadata>
</svg>"""

    output_file = f"assets/{theme}.svg"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    build_svg("dark")
    build_svg("light")
