# SoulCrafter

Forge Your Fantasy

SoulCrafter is a lightweight Python fantasy prototype focused on XML-driven characters, modular core systems, and portable project structure. The current foundation keeps game data separate from code so NPCs, items, and future content can grow through structured files instead of hard-coded logic.

## Current Prototype Features

- Core `Body` data model.
- Core `Player` class with save/load support.
- Core `NPC` class for XML-loaded character data.
- XML NPC loader foundation.
- JSON player save system.
- First XML test NPC: Frostara.
- Local custom update log format.

## Folder Structure

```text
SoulCrafter/
|-- Main.py
|-- Core/
|   |-- Body.py
|   |-- Player.py
|   |-- NPC.py
|   |-- XMLLoader.py
|   `-- SaveSystem.py
|-- Data/
|   |-- NPC/
|   |   `-- Frostara.xml
|   `-- Saves/
`-- LOG/
    `-- Update.LOG
```

## Recommended First Commit Roadmap

- Initial Project Structure
- Add .gitignore
- Core Body / Player / NPC Classes
- XML Loader
- Save System
- First Frostara XML Test NPC
- README / Project Notes

## Suggested Early Commit Names

- Initial SoulCrafter Repository Setup
- Added Core Character Framework
- Implemented XML NPC Loader
- Added Save/Load System
- Added Frostara Test NPC

## Basic Run Instructions

Install Python 3, then run the prototype from the project root:

```powershell
python Main.py
```

The first run creates a generated player save in `Data/Saves/` and loads NPC data from `Data/NPC/Frostara.xml`.
