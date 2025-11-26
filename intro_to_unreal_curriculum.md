# Introduction to Unreal Engine 5 Curriculum

## Course Overview

**Course Title:** Introduction to Unreal Engine 5  
**Target Audience:** Beginners with basic computer skills; no prior game development experience required  
**Estimated Duration:** 40-50 hours (self-paced)  
**Software Required:** Unreal Engine 5.4+ (free via Epic Games Launcher)  
**Hardware Requirements:** Windows 10/11 64-bit, 8GB RAM minimum (16GB recommended), DirectX 12 compatible GPU with 4GB VRAM minimum

---

## Learning Outcomes

By the end of this course, students will be able to:

1. Navigate the Unreal Engine interface confidently and customize their workspace
2. Understand the core concepts of real-time 3D environments and game engines
3. Build and design 3D levels using BSP geometry and static meshes
4. Apply materials and textures to create visually appealing environments
5. Implement basic lighting setups including static, stationary, and dynamic lights
6. Create interactive gameplay using Blueprints visual scripting
7. Design user interfaces with UMG (Unreal Motion Graphics)
8. Understand the basics of character movement and player input
9. Package and export a playable project
10. Apply industry-standard workflows and best practices

---

## Module 1: Getting Started with Unreal Engine

### Lesson 1.1: What is Unreal Engine?
- History of Unreal Engine and Epic Games
- Real-time rendering vs. pre-rendered graphics
- Use cases: games, film/TV, architecture, simulation, automotive
- Comparison with other engines (Unity, Godot)
- The Unreal ecosystem: Marketplace, documentation, community

### Lesson 1.2: Installation and Setup
- Creating an Epic Games account
- Installing the Epic Games Launcher
- Downloading Unreal Engine 5
- Understanding engine versions and project compatibility
- System requirements and performance optimization
- Configuring initial preferences

### Lesson 1.3: Your First Project
- Project templates overview (Blank, First Person, Third Person, etc.)
- Blueprint vs. C++ project differences
- Project settings and configuration
- Understanding the project folder structure
- Starter Content: when to use it
- **Hands-On:** Create your first Blank project

### Lesson 1.4: The Unreal Editor Interface
- Main viewport and navigation controls (WASD, mouse)
- The Outliner panel: scene hierarchy
- The Details panel: properties and settings
- The Content Browser: asset management
- Toolbar and mode switching
- Customizing layouts and saving workspaces
- **Hands-On:** Practice viewport navigation in a sample level

---

## Module 2: Working with Levels and Actors

### Lesson 2.1: Understanding Levels
- What is a Level in Unreal?
- Persistent levels vs. streaming levels
- Level organization strategies
- The World Settings panel
- Creating and saving new levels
- **Hands-On:** Create a new empty level

### Lesson 2.2: Actors and Components
- What is an Actor?
- The Actor-Component model explained
- Static Mesh Actors vs. other actor types
- Transform properties: Location, Rotation, Scale
- Pivot points and transform gizmos
- Duplicating, grouping, and organizing actors
- **Hands-On:** Place and manipulate basic actors

### Lesson 2.3: BSP Geometry (Brush Modeling)
- What is BSP and when to use it
- Additive vs. Subtractive brushes
- Creating rooms, corridors, and basic architecture
- BSP limitations and performance considerations
- Converting BSP to Static Mesh
- **Hands-On:** Build a simple room using BSP brushes

### Lesson 2.4: Working with Static Meshes
- Importing static meshes (FBX workflow)
- Mesh LODs (Level of Detail) explained
- Collision: simple vs. complex
- Static Mesh Editor basics
- Organizing meshes in the Content Browser
- **Hands-On:** Import and place external 3D assets

### Lesson 2.5: The Modeling Tools
- Introduction to Unreal's built-in modeling mode
- PolyEdit: vertices, edges, faces
- Creating and modifying geometry in-engine
- When to model in Unreal vs. external DCC tools
- **Hands-On:** Create a simple prop using modeling tools

---

## Module 3: Materials and Textures

### Lesson 3.1: Material Fundamentals
- What is a material in Unreal?
- Physically Based Rendering (PBR) overview
- Base Color, Metallic, Roughness, Normal maps
- The Material Editor interface
- Material Instances: why they matter
- **Hands-On:** Create your first simple material

### Lesson 3.2: Texture Basics
- Supported texture formats
- Importing textures properly
- Texture settings: compression, mipmaps, sRGB
- UV mapping fundamentals
- Texture coordinates and tiling
- **Hands-On:** Apply textures to a material

### Lesson 3.3: Building Complex Materials
- Using math nodes for effects
- Lerp, Multiply, Add operations
- Creating material functions for reusability
- Texture blending techniques
- World-aligned textures
- **Hands-On:** Create a terrain blend material

### Lesson 3.4: Material Instances and Parameters
- Creating Material Instances
- Scalar and Vector parameters
- Texture parameters
- Dynamic material changes at runtime (preview)
- Organizing material libraries
- **Hands-On:** Build a customizable material with parameters

### Lesson 3.5: Special Material Types
- Translucent and masked materials
- Emissive materials (glow effects)
- Decals: adding detail without geometry
- Landscape materials introduction
- **Hands-On:** Create a glowing emissive material

---

## Module 4: Lighting Your World

### Lesson 4.1: Lighting Fundamentals
- How lighting works in real-time engines
- Direct vs. indirect lighting
- Light types overview: Directional, Point, Spot, Rect
- Light mobility: Static, Stationary, Movable
- Performance implications of each type

### Lesson 4.2: The Directional Light and Sky
- Creating a sun with Directional Light
- Sky Atmosphere component
- Exponential Height Fog
- SkyLight for ambient illumination
- Time-of-day setups
- **Hands-On:** Set up an outdoor daytime sky

### Lesson 4.3: Interior Lighting
- Point lights for room illumination
- Spot lights for focused lighting
- Rect lights for realistic area lighting
- IES profiles for realistic light falloff
- Light functions for effects
- **Hands-On:** Light an interior room

### Lesson 4.4: Lumen Global Illumination
- What is Lumen and how it works
- Lumen vs. baked lighting comparison
- Software vs. Hardware Ray Tracing
- Lumen settings and optimization
- When to use Lumen vs. traditional methods
- **Hands-On:** Enable and configure Lumen

### Lesson 4.5: Post-Process Effects
- Post Process Volumes explained
- Exposure and auto-exposure
- Color grading and LUTs
- Bloom, lens flares, and vignette
- Ambient Occlusion settings
- **Hands-On:** Create a cinematic post-process look

---

## Module 5: Introduction to Blueprints

### Lesson 5.1: What are Blueprints?
- Visual scripting explained
- Blueprints vs. C++: pros and cons
- Types of Blueprints: Actor, Level, Widget, etc.
- The Blueprint Editor interface
- Event Graph, Construction Script, Functions

### Lesson 5.2: Blueprint Fundamentals
- Nodes, pins, and wires
- Execution flow (white pins)
- Data flow (colored pins)
- Variables: creating and using
- Data types: Boolean, Integer, Float, String, Vector
- **Hands-On:** Create your first Blueprint variable

### Lesson 5.3: Events and Functions
- Event BeginPlay and Event Tick
- Custom events and dispatchers
- Creating functions for reusability
- Input vs. Output parameters
- Pure vs. Impure functions
- **Hands-On:** Create a Blueprint that prints to screen

### Lesson 5.4: Flow Control
- Branch nodes (if/else logic)
- Switch statements
- For loops and While loops
- Sequence and timing nodes
- Delay and timers
- **Hands-On:** Create a countdown timer Blueprint

### Lesson 5.5: Working with Actors in Blueprints
- Spawning and destroying actors
- Getting references to other actors
- Casting explained
- Actor communication patterns
- The "Get All Actors of Class" node
- **Hands-On:** Create a spawner Blueprint

---

## Module 6: Player Interaction and Input

### Lesson 6.1: Player Controllers and Pawns
- The Player Controller explained
- Pawns vs. Characters
- Possession and player input routing
- Default Pawn class settings
- Game Mode basics
- **Hands-On:** Examine the default player setup

### Lesson 6.2: Enhanced Input System
- Input Actions and Input Mapping Contexts
- Binding input to Blueprint events
- Axis vs. Digital inputs
- Input modifiers and triggers
- Multiple input devices
- **Hands-On:** Set up WASD movement input

### Lesson 6.3: Character Movement
- The Character Movement Component
- Walking, jumping, flying modes
- Movement settings: speed, acceleration, friction
- Custom movement abilities
- **Hands-On:** Customize character movement parameters

### Lesson 6.4: Collision and Physics Interaction
- Collision channels and presets
- Overlap vs. Block vs. Ignore
- Collision events in Blueprints
- Physics simulation basics
- Trigger volumes
- **Hands-On:** Create a trigger zone that detects the player

### Lesson 6.5: Interactable Objects
- Line traces (raycasting) for detection
- Creating interactable actor Blueprints
- Interface-based interaction systems
- Visual feedback for interactables
- **Hands-On:** Build a simple door that opens on interaction

---

## Module 7: User Interface with UMG

### Lesson 7.1: UMG Fundamentals
- What is Unreal Motion Graphics?
- Widget Blueprints explained
- The UMG Designer interface
- Canvas Panel and layout
- Anchors and alignment

### Lesson 7.2: Common UI Widgets
- Text and Text Block widgets
- Images and borders
- Buttons and click events
- Progress bars and sliders
- Horizontal/Vertical boxes
- **Hands-On:** Create a simple title screen

### Lesson 7.3: Displaying UI at Runtime
- Creating and adding widgets to viewport
- Widget visibility and input modes
- Removing widgets from screen
- HUD vs. Menu UI patterns
- **Hands-On:** Display health bar on screen

### Lesson 7.4: UI Data Binding
- Binding text to variables
- Binding visibility and colors
- Property binding vs. event-driven updates
- Formatting bound values
- **Hands-On:** Create a score display that updates

### Lesson 7.5: Menu Systems
- Creating navigable menus
- Button focus and gamepad support
- Pause menu implementation
- Main menu and level loading
- **Hands-On:** Build a functional pause menu

---

## Module 8: Audio Basics

### Lesson 8.1: Sound in Unreal
- Supported audio formats
- Importing sound files
- Sound Cues vs. MetaSounds introduction
- 2D vs. 3D spatialized audio
- Sound classes and mix settings

### Lesson 8.2: Playing Sounds
- Play Sound 2D node
- Play Sound at Location
- Audio Components on Actors
- Triggering sounds from Blueprints
- **Hands-On:** Add sound effects to interactions

### Lesson 8.3: Ambient Audio
- Ambient Sound actors
- Sound attenuation settings
- Audio volumes and reverb
- Background music implementation
- **Hands-On:** Set up ambient sounds in a level

---

## Module 9: Particles and Visual Effects

### Lesson 9.1: Niagara Overview
- What is Niagara?
- Niagara vs. Cascade (legacy system)
- Emitters, Systems, and Modules
- The Niagara Editor interface

### Lesson 9.2: Creating Basic Effects
- Starting from templates
- Particle spawn rate and lifetime
- Velocity and forces
- Sprite rendering basics
- **Hands-On:** Create a simple spark effect

### Lesson 9.3: Using Effects in Levels
- Placing Niagara Systems in levels
- Triggering effects from Blueprints
- Effect pooling for performance
- **Hands-On:** Trigger a particle effect on collision

---

## Module 10: Packaging and Publishing

### Lesson 10.1: Preparing Your Project
- Content audit and cleanup
- Removing unused assets
- Fixing errors and warnings
- Map Check and asset validation
- Redirect fixup

### Lesson 10.2: Project Settings for Packaging
- Target platform configuration
- Quality settings and scalability
- Default maps and game mode
- Packaging settings overview
- Build configurations: Development vs. Shipping

### Lesson 10.3: Building and Packaging
- Cooking content explained
- Packaging for Windows
- Understanding the build process
- Common packaging errors and solutions
- **Hands-On:** Package your project

### Lesson 10.4: Distribution Basics
- Creating installers (overview)
- File size optimization
- Platform-specific considerations
- What's next: Steam, Epic Games Store, itch.io

---

## Capstone Project: Mini Game Experience

### Project Requirements
Students will create a small, playable experience that demonstrates:

1. **Environment:** A designed level with at least two distinct areas using BSP and/or static meshes
2. **Materials:** At least three custom materials applied appropriately
3. **Lighting:** Complete lighting setup with proper mood/atmosphere
4. **Blueprints:** At least one interactive element (door, pickup, switch, etc.)
5. **UI:** A simple HUD displaying at least one gameplay variable
6. **Audio:** Background ambient sound and at least one triggered sound effect
7. **Polish:** Functioning start screen and win/lose condition
8. **Packaging:** Successfully packaged as a standalone executable

### Suggested Project Ideas
- Escape Room: Find keys to unlock doors and escape
- Collectathon: Gather items scattered through an environment
- Simple Shooter Gallery: Hit targets to score points
- Walking Simulator: Explore an environment with triggered narration
- Puzzle Room: Solve simple physics or logic puzzles

---

## Appendices

### Appendix A: Keyboard Shortcuts Reference
| Action | Shortcut |
|--------|----------|
| Focus on Selection | F |
| Duplicate | Ctrl+W |
| Save All | Ctrl+Shift+S |
| Play in Editor | Alt+P |
| Compile Blueprint | F7 |
| Toggle Game View | G |
| Snap to Floor | End |
| Pilot Camera | Ctrl+Shift+P |

### Appendix B: Recommended Resources
- **Official Documentation:** docs.unrealengine.com
- **Unreal Learning Portal:** dev.epicgames.com/community/learning
- **YouTube:** Unreal Engine official channel
- **Community:** Unreal Slackers Discord, r/unrealengine

### Appendix C: Glossary
- **Actor:** Any object that can be placed in a level
- **Blueprint:** Visual scripting system in Unreal
- **BSP:** Binary Space Partitioning; brush-based geometry
- **Component:** Modular functionality attached to Actors
- **LOD:** Level of Detail; mesh optimization technique
- **Lumen:** Real-time global illumination system in UE5
- **Nanite:** Virtualized geometry system in UE5
- **PBR:** Physically Based Rendering
- **UMG:** Unreal Motion Graphics; the UI system

---

## Course Maintenance Notes

**Version:** 1.0  
**Engine Version Target:** Unreal Engine 5.4+  
**Last Updated:** November 2025  
**Author:** [Instructor Name]

### Future Expansion Considerations
- Advanced Blueprint patterns (interfaces, components)
- Animation and Animation Blueprints
- AI and Behavior Trees
- Multiplayer basics
- Landscape and terrain tools
- Cinematics with Sequencer
- C++ integration fundamentals
