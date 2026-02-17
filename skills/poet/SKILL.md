---
name: poet
description: Create immersive data poetry visualizations. Use when (1) building new poem-style visualizations from data, (2) converting existing charts/vizs into the dark/glassmorphic poems aesthetic, (3) choosing metaphors and abstraction levels for data, or (4) creating atmospheric/mathematical data experiences.
---

# Data Poet Skill

Transform data into immersive visual experiences using the poems/ aesthetic.

## Usage

```
/geepers-poet                                    # Interactive - asks for data source and level
/geepers-poet "Census poverty data"              # Create poem from described data
/geepers-poet path/to/data.csv --level 2         # Impressionistic treatment of CSV
/geepers-poet path/to/data.json --level 3 --metaphor "erosion"  # Abstract with hint
/geepers-poet convert path/to/existing-viz.html  # Convert existing viz to poems style
```

## Arguments

| Argument | Description |
|----------|-------------|
| First positional | Data source (file path, URL, or description) |
| `--level` | Abstraction level: 1 (literal), 2 (impressionistic), 3 (abstract), 4 (atmospheric) |
| `--metaphor` | Optional metaphor hint (e.g., "erosion", "constellation", "breathing") |
| `--palette` | Color palette name from STYLE_GUIDE.md (e.g., "bioluminescent", "ember") |
| `--name` | Output directory name under poems/ |
| `convert` | Mode: convert existing visualization to poems aesthetic |

## Abstraction Levels

| Level | Name | Description | Good For |
|-------|------|-------------|----------|
| 1 | Literal | Traditional chart with poems styling | Policy, science, reference |
| 2 | Impressionistic | Data encoded in natural metaphors | Stories about people, culture |
| 3 | Abstract | Mathematical beauty driven by data | Complex multidimensional data |
| 4 | Atmospheric | Ambient environment from data | Climate, loss, meditation |

## What It Creates

A self-contained poem visualization:
```
poems/[name]/
├── index.html       # Full visualization
├── style.css        # Optional external styles
├── script.js        # Optional external logic
└── social-card.png  # OG image (placeholder)
```

Every poem includes: dark background, full-viewport canvas/SVG, glassmorphic UI, touch support, DPI scaling, social metadata.

## Routes To

- **Agent**: `geepers_poet` (primary)
- **Collaborators**: `geepers_datavis_color`, `geepers_datavis_story`, `geepers_datavis_math`, `geepers_datavis_data`

## Design Reference

All design decisions are governed by `poems/STYLE_GUIDE.md`. The agent reads this before every task.

## Examples

**New poem from data description:**
```
/geepers-poet "NOAA shipwreck data with coordinates, depth, year, and vessel type" --level 2 --metaphor "ghost fleet"
```

**Convert a bar chart:**
```
/geepers-poet convert datavis/dev/housing_crisis/index.html --level 1
```

**Abstract mathematical visualization:**
```
/geepers-poet data_trove/data/asteroids_real.json --level 3 --palette cosmic
```
