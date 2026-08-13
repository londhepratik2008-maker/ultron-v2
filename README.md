# Ultron A.I. v2

A voice-reactive 3D neural blob desktop app inspired by Ultron.

## Live Demo

**[Click here to view](https://londhepratik2008-maker.github.io/ultron-v2/index.html)**

## Features

### 3D Neural Blob
- Animated icosahedron with 6 subdivision levels for smooth organic motion
- Custom GLSL vertex & fragment shaders with 3D simplex noise displacement
- Triple-layered noise (low, mid, high frequency) for realistic surface deformation
- Fresnel-based edge glow with dynamic color mixing
- Audio-reactive — blob pulses and deforms with your voice
- Click anywhere on the blob to trigger ripple wave effects

### Core & Wireframes
- Glowing inner core sphere with point light source
- 3 nested wireframe icosahedron layers rotating at different speeds
- Core pulses with audio bass frequencies
- Wireframe opacity reacts to voice volume

### Particle Systems
- **5000+ streaming particles** — emit outward from blob surface with lifecycle management
- **Secondary particle layer** — 40% additional particles moving in opposite direction
- **700 ring particles** — orbit around the blob in tilted paths
- **6 orbital rings** — torus geometries with different tilts, speeds, and colors
- All particles respond to audio volume and configurable speed

### Neural Web
- 100 floating data nodes in spherical distribution
- Dynamic connection lines between nearby nodes (distance-based)
- Nodes pulse and drift with time-based animation
- Line opacity fades with distance for depth effect

### Voice & Audio
- **Speech Recognition** — Web Speech API with continuous listening mode
- **Text-to-Speech** — Ultron responds with voice (Microsoft Zira / Google UK English Female)
- **20+ pre-programmed responses** — reacts to greetings, questions, jokes, insults, time, date, and more
- **Audio frequency analysis** — splits mic input into low/mid/high bands for reactive visuals
- **MP3 voice playback** — bundled Ultron voice asset for responses

### Themes
- **Ultraviolet** — Pink/magenta palette (default)
- **Cyberpunk** — Neon pink + purple
- **Matrix** — Classic green on black
- **Fire & Ice** — Orange flames + ice blue accents
- Full CSS variable system — every color updates across blob, particles, UI, and grid

### Camera System
- **8 camera presets** — Front, Orbit Right, Orbit Left, Top Down, Low Angle, Cinematic, Close Up, Wide
- Smooth lerp transitions between angles
- Auto-orbit that speeds up with audio volume
- Mouse wheel zoom with min/max bounds
- Parallax effect on mouse movement

### Settings Panel
- **Blob** — Noise Intensity, Wireframe Opacity, Core Glow
- **Particles** — Density (500–10000), Speed
- **Post-Processing** — Bloom Intensity, Bloom Radius
- **Audio** — Volume, Voice Rate
- All settings persist via localStorage

### UI
- Custom draggable titlebar with minimize/maximize/close
- Slide-out chat history panel with timestamps
- Audio meter showing real-time mic levels
- Zoom controls (+, -, camera angle cycle)
- Toast notifications for camera & settings changes
- Error banner for missing assets

### Tech Stack
- **Backend** — Python + pywebview (desktop window)
- **3D Engine** — Three.js r164 with EffectComposer
- **Shaders** — Custom GLSL (simplex noise, fresnel, grid, particles)
- **Post-Processing** — UnrealBloomPass for glow effects
- **Build** — PyInstaller for standalone .exe
