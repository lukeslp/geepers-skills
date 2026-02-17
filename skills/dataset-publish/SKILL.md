---
name: dataset-publish
description: Publish datasets to Kaggle, HuggingFace, and GitHub. Use when (1) uploading new datasets, (2) updating existing datasets, (3) checking dataset status, (4) generating metadata files, (5) validating before publish.
aliases:
  - publish-kaggle
  - publish-huggingface
  - publish-github
  - publish-all
---

# Dataset Publishing Skill

Expert-level dataset publishing across Kaggle, HuggingFace, and GitHub. Orchestrates the full team: `/humanize`, `/geepers-doublecheck`, `/geepers-readme`, and specialist agents as needed.

## MANDATORY: Full Pipeline (Every Publish)

Every publish operation runs this pipeline. No shortcuts.

```
1. /geepers-doublecheck validate <dataset-dir>    → Synthetic data scan, source verification
2. /geepers-readme <dataset-dir>                  → Professional README with badges
3. /humanize README.md HUGGINGFACE_README.md       → Kill robot voice, enforce AI ban
4. Validate metadata constraints                   → Title 6-50 chars, subtitle 20-80 chars
5. Stage + Upload                                  → Kaggle staging dir, HF API
6. Post-publish verification                       → Download test, description renders
```

Launch steps 1-3 **in parallel** — they're independent.

## The Three Data Locations (Know These)

### 1. `~/datasets/` — Packaged Published Datasets (THIS IS THE WORK)

Original analytical/integration datasets published to Kaggle/HuggingFace. Each has its own directory, often its own git repo. **This is where original value lives.**

| Dataset | What Makes It Original | Records | Platforms |
|---------|----------------------|---------|-----------|
| `accessibility-atlas/` | 42 sources integrated (Census, WHO, SSA, VA, EEOC) | ~50MB | HF, Kaggle |
| `etymology_atlas/` | 5 linguistic databases unified into graph | 269MB | Kaggle, HF |
| `language-data/` | 4-source merge by ISO 639-3 (7,130 languages) | ~43MB | Kaggle, HF |
| `us-attention-data/` | Custom time series (Wikipedia + GDELT + Google Trends) | 4.3MB | HF |
| `us-disasters-mashup/` | 4 gov databases unified (NTSB, NOAA x2, USGS) - 48,592 events | 13MB | HF, Kaggle |
| `us-housing-affordability-crisis/` | Computed metrics from 4 ACS tables | 360KB | Kaggle |
| `us-inequality-atlas/` | Multi-dimensional Census/CMS/USDA/HRSA county merge | Multi-file | HF, Kaggle |
| `us-military-veteran-analysis/` | 6-source integration with correlation analysis | 8KB | Kaggle |
| `meteorites-ufos-detection-bias/` | NASA + NUFORC side-by-side detection bias study | 1,279 | Kaggle |
| `veterans-housing-disability/` | VA + Census + HUD merge with vulnerability score | 52 states | Kaggle |
| `strange-places-mysterious-phenomena/` | 8 sources aggregated, geocoded (354K records) | 354K | Kaggle |
| `large-meteorites/` | NASA filtered to 1kg+ (4,871 specimens) | 4,871 | HF, Kaggle |
| `noaa-significant-storms/` | NOAA filtered to F3+/Cat3+/fatal/$1M+ | 14,770 | Kaggle, HF |
| `usgs-significant-earthquakes/` | USGS filtered to M4.5+ | 3,742 | Kaggle, HF |
| `witnessed-meteorite-falls/` | NASA filtered to "Fell" type only | 1,097 | Kaggle, HF |
| `world-languages/` | 4-source merge (Glottolog, Joshua Project, etc.) | ~8MB | HF |
| `bluesky_kaggle_export/` | Curated sample of Bluesky posts | ~190K | Kaggle |

**Nested git repos** (push separately): accessibility-atlas, us-inequality-atlas, us-disasters-mashup, language-data, us-attention-data, large-meteorites, noaa-significant-storms, usgs-significant-earthquakes, witnessed-meteorite-falls, world-languages, strange-places-mysterious-phenomena

### 2. `~/html/datavis/data_trove/` — Raw API Fetches for Visualizations

NOT original work — API rips from Census, USGS, NASA, NOAA, etc. used to power D3.js visualizations at dr.eamer.dev/datavis/. **Never publish these raw fetches as standalone datasets** unless you add real integration/analytical value first.

```
data_trove/
├── data/                    # Processed data organized by topic
│   ├── quirky/              # 16+ real API datasets + D3.js vizs
│   ├── wild/                # Meteorites, ghosts, shark attacks
│   ├── linguistic/          # Glottolog, WALS, PHOIBLE (nested git repo)
│   ├── accessibility/       # Census disability, sign language
│   ├── attention/           # Wikipedia pageviews, Google Trends
│   ├── policy/              # DOGE cuts, tariffs
│   ├── healthcare/          # CMS hospitals, healthcare deserts
│   └── geographic/          # FIPS county, country centroids
├── economic/                # GDP, billionaires, corporate boards
├── demographic/             # Veterans, poverty, food deserts
├── entertainment/           # Steam (1.9GB recs), movies, Onion
├── tools/fetchers/          # 24 Python fetcher scripts
├── index.html               # Web catalog at dr.eamer.dev/datavis/data_trove/
└── published/               # Mirrors of HF/Kaggle uploads (gitignored)
```

**When data_trove data becomes a dataset**: Only when you do real integration work — merge multiple sources, compute derived metrics, filter with meaningful criteria, or add analytical value. That output goes to `~/datasets/`.

### 3. `~/html/datavis/` — Visualizations (Both Published and Dev)

Where the data gets visualized. Published and in-development.

**Published visualizations** (`~/html/datavis/`):
- `interactive/atlas/` — Inequality atlas choropleth (11 layers, uses us-inequality-atlas data)
- `interactive/strange-places/` — Strange Places map (210K+ points, Canvas)
- `poems/language/` — 3 language visualizations (tree, constellation, PIE)
- `poems/` — 30+ data poetry visualizations (dark/glassmorphic aesthetic)
- `billions/`, `dowjones/`, `spending/` — Economic visualizations

**Dev visualizations** (`~/html/datavis/dev/`):
- In-progress visualizations not yet published
- `dev/airplane-crashes.html`, `dev/earthquake-pulse.html`, `dev/emoji-race.html`, etc.
- Some have their own data in `dev/data/`

**Poems dev** (`~/html/datavis/poems/dev/`):
- Data poems in progress: `cheese/`, `firewall/`, `invisible-populations/`, etc.

**Dataset → Visualization mapping** (from `~/datasets/VISUALIZATION_CROSS_REFERENCE.md`):

| Dataset | Visualization | URL |
|---------|--------------|-----|
| strange-places | Strange Places Interactive Map | dr.eamer.dev/datavis/interactive/strange-places/ |
| us-inequality-atlas | Inequality Atlas Choropleth | dr.eamer.dev/datavis/inequality-atlas/ |
| world-languages | Language Tree/Constellation/PIE | dr.eamer.dev/datavis/poems/language/ |
| accessibility-atlas | Atlas disability layer | dr.eamer.dev/datavis/interactive/atlas/ |
| us-disasters-mashup | (not yet visualized) | — |

## Credentials

| Platform | Credential | User |
|----------|-----------|------|
| **Kaggle** | `~/.kaggle/kaggle.json` (chmod 600) | `lucassteuber` |
| **HuggingFace** | `$HF_API_KEY` env var (write scope) | `lukeslp` |
| **GitHub** | `gh` CLI auth | `lukeslp` |

**Username inconsistency**: Kaggle is `lucassteuber`, everywhere else is `lukeslp`. Known issue, can't change.

---

## WORKFLOW: New Dataset Publishing

### Step 1: Validate (PARALLEL — launch all 3)

```
/geepers-doublecheck validate <dataset-dir>/
/geepers-readme <dataset-dir>/
/humanize <dataset-dir>/README.md <dataset-dir>/HUGGINGFACE_README.md --yes
```

These run in parallel. Wait for all three before proceeding.

**What doublecheck catches**: synthetic data red flags, broken source URLs, schema gaps, coordinate implausibility, license inconsistencies across platforms.

**What readme does**: adds badges (license, platform, record count), structures author block, adds JSON-LD structured data.

**What humanize catches**: "AI-powered", robot voice, press-release tone, buzzwords.

### Step 2: Prepare Directory

```
my-dataset/
├── data.json (or .csv)          # Main data file(s)
├── dataset-metadata.json         # Kaggle metadata (REQUIRED for Kaggle)
├── HUGGINGFACE_README.md         # HF dataset card with YAML frontmatter
├── README.md                     # GitHub/general documentation
├── demo_notebook.ipynb           # Usage examples (best practice)
└── CLAUDE.md                     # Agent guidance (if complex dataset)
```

**Generate missing files**:
```bash
# Notebook from template
python3 ~/datasets/generate_notebook.py <dataset-dir>/

# HuggingFace README from template
python3 ~/datasets/generate_hf_readme.py <dataset-dir>/
```

### Step 3: Kaggle Metadata

**`dataset-metadata.json`:**
```json
{
  "title": "Dataset Name (6-50 chars)",
  "id": "lucassteuber/dataset-slug",
  "licenses": [{"name": "CC0-1.0"}],
  "subtitle": "Brief description (20-80 chars required)",
  "description": "# Title\n\nFull markdown description...",
  "keywords": ["tag1", "tag2"],
  "isPrivate": true
}
```

**HARD CONSTRAINTS:**
- Title: 6-50 characters (STRICT — count them)
- Subtitle: 20-80 characters (STRICT — count them)
- ID: `lucassteuber/slug` — slug 3-50 chars, lowercase, hyphens only
- Keywords: max 5, must match existing Kaggle tags
- Licenses: exactly 1 entry
- **Always create PRIVATE first** — make public after manual review

**Kaggle description IS the page content.** There's no separate README — the `description` field in `dataset-metadata.json` renders as the Kaggle dataset page. Write Kaggle-specific markdown here.

**Description gotchas:**
- Use `>` not `&gt;` for blockquotes
- Avoid triple newlines
- Standard markdown works: headings, bold, links, tables, code blocks
- Don't copy-paste HUGGINGFACE_README.md content — write Kaggle-specific copy

### Step 4: HuggingFace Dataset Card

**`HUGGINGFACE_README.md`** (uploaded as `README.md` on HF):
```yaml
---
license: cc0-1.0
task_categories:
  - feature-extraction
language:
  - en
tags:
  - geography
  - united-states
pretty_name: Dataset Name
size_categories:
  - 10K<n<100K
dataset_info:
  features:
    - name: field_name
      dtype: string
  splits:
    - name: train
      num_examples: 1234
---

# Dataset Name

Description...
```

**Valid HF licenses:** apache-2.0, mit, cc0-1.0, cc-by-4.0, cc-by-sa-4.0, cc-by-nc-4.0, odbl, gpl-3.0, lgpl-3.0, other

**HF does NOT support `US-Government-Works`** — use `other` for government data.

**Valid size_categories:** n<1K, 1K<n<10K, 10K<n<100K, 100K<n<1M, 1M<n<10M, 10M<n<100M, 100M<n<1B, 1B<n<10B

### Step 5: Upload

**Kaggle Upload (MUST use staging directory):**

Kaggle uploads ALL files in the target directory. Never point at the source directory.

```bash
DATASET_DIR=/path/to/dataset
STAGING=/tmp/kaggle_staging/$(basename "$DATASET_DIR")
rm -rf "$STAGING" && mkdir -p "$STAGING"

# Copy ONLY data files and Kaggle metadata
cp "$DATASET_DIR"/dataset-metadata.json "$STAGING/"
cp "$DATASET_DIR"/README.md "$STAGING/" 2>/dev/null || true
for ext in json csv parquet xlsx tsv; do
  for f in "$DATASET_DIR"/*.$ext; do
    [ -f "$f" ] && [ "$(basename "$f")" != "dataset-metadata.json" ] && cp "$f" "$STAGING/"
  done
done
# Copy Python scripts if they're part of the dataset
for f in "$DATASET_DIR"/*.py; do
  [ -f "$f" ] && cp "$f" "$STAGING/"
done

# NEVER copy to staging:
# - HUGGINGFACE_README.md (shows up as data file on Kaggle)
# - .zenodo.json, KAGGLE_SETUP.md, CLAUDE.md
# - *.ipynb (upload as Kaggle kernels separately)
# - .gitattributes, .gitignore, .git/

kaggle datasets create -p "$STAGING"
```

**HuggingFace Upload:**
```python
from huggingface_hub import HfApi, create_repo
import os

token = os.environ.get('HF_API_KEY')
api = HfApi(token=token)

repo_name = "lukeslp/dataset-name"
create_repo(repo_name, repo_type="dataset", exist_ok=True, private=True, token=token)

# Upload data files
api.upload_file(
    path_or_fileobj="data.json",
    path_in_repo="data.json",
    repo_id=repo_name,
    repo_type="dataset",
    token=token
)

# Upload README (MUST be named README.md on HF)
api.upload_file(
    path_or_fileobj="HUGGINGFACE_README.md",
    path_in_repo="README.md",
    repo_id=repo_name,
    repo_type="dataset",
    token=token
)
```

**GitHub Release (for datasets with own repo):**
```bash
cd /path/to/dataset-repo
gh release create v1.0.0 data.json --title "Dataset v1.0.0" --notes "Initial release"
```

### Step 6: Post-Publish

1. **Verify upload**: Download and spot-check from the platform
2. **Check rendering**: Kaggle description and HF README render correctly
3. **Update data_trove index**: If the dataset feeds a visualization, update `data_trove/EXTERNAL_PLATFORM_LINKS.csv`
4. **Update VISUALIZATION_CROSS_REFERENCE.md** in `~/datasets/` if there's a viz link
5. **Update datasets/CLAUDE.md** table with the new dataset

---

## WORKFLOW: Update Existing Dataset

### Kaggle Version Update

**ALWAYS use staging directory.** Never `kaggle datasets version -p .` on the source dir.

```bash
DATASET_DIR=/path/to/dataset
STAGING=/tmp/kaggle_staging/$(basename "$DATASET_DIR")
rm -rf "$STAGING" && mkdir -p "$STAGING"

cp "$DATASET_DIR"/dataset-metadata.json "$STAGING/"
cp "$DATASET_DIR"/README.md "$STAGING/" 2>/dev/null || true
for ext in json csv parquet xlsx tsv py; do
  for f in "$DATASET_DIR"/*.$ext; do
    [ -f "$f" ] && [ "$(basename "$f")" != "dataset-metadata.json" ] && cp "$f" "$STAGING/"
  done
done

kaggle datasets version -p "$STAGING" -m "Added X records, fixed Y"
```

### Kaggle Metadata-Only Update

The download command returns **double-JSON-encoded** data. Parse twice:

```python
import json
with open('/tmp/dataset-metadata.json') as f:
    data = json.loads(json.loads(f.read()))
data['isPrivate'] = False
with open('/tmp/dataset-metadata.json', 'w') as f:
    f.write(json.dumps(json.dumps(data)))
```

```bash
kaggle datasets metadata lucassteuber/dataset-name -p /tmp
# Edit /tmp/dataset-metadata.json
kaggle datasets metadata lucassteuber/dataset-name --update -p /tmp
```

### HuggingFace Update

Same upload code — `upload_file()` overwrites existing files.

---

## WORKFLOW: Check Status

```bash
# Kaggle
kaggle datasets status lucassteuber/dataset-name
kaggle datasets list --mine

# HuggingFace
huggingface-cli repo info lukeslp/dataset-name --repo-type dataset

# GitHub
gh repo view lukeslp/dataset-name
```

---

## WORKFLOW: Make Public

Datasets start PRIVATE. After manual review:

### Kaggle
```bash
kaggle datasets metadata lucassteuber/dataset-name -p /tmp
# Parse double-JSON, set "isPrivate": false, write back
kaggle datasets metadata lucassteuber/dataset-name --update -p /tmp
```

### HuggingFace
```python
from huggingface_hub import HfApi
api = HfApi(token=token)
api.update_repo_visibility("lukeslp/dataset-name", private=False, repo_type="dataset")
```

---

## Current Cross-Platform Inventory

| Dataset | GitHub | HuggingFace | Kaggle |
|---------|--------|-------------|--------|
| accessibility-atlas | public | public | public |
| etymology-atlas | — | public | public |
| joshua-project-data | public | public | — |
| language-data | — | **private** | public |
| large-meteorites | — | **private** | public |
| meteorites-ufos-detection-bias | — | — | public |
| noaa-significant-storms | — | public | public |
| strange-places | public | public | public |
| us-attention-data | public | public | public |
| us-disasters-mashup | public | public | public |
| us-housing-affordability-crisis | — | public | public |
| us-inequality-atlas | public | public | public |
| us-military-veteran-analysis | — | **private** | public |
| usgs-significant-earthquakes | — | public | public |
| veterans-housing-disability | — | — | public |
| waterfalls-worldwide | — | — | public |
| witnessed-meteorite-falls | — | **private** | public |
| world-languages | — | public | public |
| bluesky-social | — | — | public |
| temperature-anomalies | — | — | public |

**Gaps to close**: 4 HF datasets still private, 2 Kaggle-only datasets missing from HF.

---

## Kaggle Reference

### Valid License Names

`CC0-1.0`, `CC-BY-4.0`, `CC-BY-SA-4.0`, `CC-BY-SA-3.0`, `CC-BY-NC-4.0`, `CC-BY-NC-SA-4.0`,
`CC-BY-3.0`, `CC-BY-ND-4.0`, `CC-BY-NC-ND-4.0`, `GPL-2.0`, `GPL-3.0`, `LGPL-3.0`, `AGPL-3.0`,
`ODbL-1.0`, `DbCL-1.0`, `ODC-BY-1.0`, `PDDL`, `CDLA-Permissive-1.0`, `CDLA-Sharing-1.0`,
`apache-2.0`, `FDL-1.3`, `US-Government-Works`, `copyright-authors`, `other`, `unknown`

### vs HuggingFace vs GitHub

| Content | Kaggle | HuggingFace | GitHub |
|---------|--------|-------------|--------|
| Description | `dataset-metadata.json` `description` field | `README.md` (YAML frontmatter + markdown) | `README.md` |
| Metadata | `dataset-metadata.json` | YAML frontmatter in README.md | None |
| Data files | Upload via staging dir | `upload_file()` or git push | Releases or git LFS |
| License | `licenses[0].name` | `license:` in YAML | LICENSE file |
| Tags | `keywords` (max 5, must exist) | `tags:` (unlimited) | GitHub topics |

### Platform Limits

| Platform | Max File | Max Total | Notes |
|----------|----------|-----------|-------|
| Kaggle | 20 GB | 100 GB | Rate limit on rapid API calls |
| HuggingFace | 50 GB (LFS) | Unlimited | Generous rate limits |
| GitHub Releases | 2 GB | — | Use for data, not repo |

---

## Team Orchestration

This skill calls other skills and agents. Here's when:

| Task | Tool | When |
|------|------|------|
| `/humanize` | **Every publish** | Strips robot voice, enforces AI ban |
| `/geepers-doublecheck` | **Every publish** | Validates data quality, citations, synthetic detection |
| `/geepers-readme` | **Every publish** | Professional README with badges |
| `@geepers_data` | On validation failure | Deep data quality analysis |
| `@geepers_citations` | Broken source URLs | Verify and fix citations |
| `@geepers_docs` | Missing documentation | Generate dataset cards |
| `@geepers_fetcher` | Source verification | Fetch and compare against sources |
| `@geepers_links` | Link validation | Check all URLs resolve |

---

## Common Issues

### Kaggle 401 Unauthorized
Regenerate at kaggle.com/settings. Replace `~/.kaggle/kaggle.json`. `chmod 600`.

### HuggingFace 403 Forbidden
Token needs **Write** permission. Create at huggingface.co/settings/tokens.

### Kaggle Title/Subtitle Errors
Count characters. Title: exactly 6-50. Subtitle: exactly 20-80. No exceptions.

### HuggingFace License Error
Use exact IDs: `odbl` not `ODbL-1.0`, `cc-by-4.0` not `CC-BY-4.0`, `other` for gov works.

### Kaggle Metadata 400 Error
Keywords must exist in Kaggle's tag list. Some fields only changeable via web UI.

### Nested Git Repo Push
Many datasets have their own `.git/`. Push from inside the dataset dir, not from `~/datasets/`.

```bash
cd ~/datasets/us-disasters-mashup
git add -A && git commit -m "update data"
git push origin master
```

### accessibility-atlas Remote
Remote is named `master` not `origin`. Use `git push master master`.

---

## Quick Reference

| Action | Kaggle | HuggingFace | GitHub |
|--------|--------|-------------|--------|
| Create | `kaggle datasets create -p <staging>` | `create_repo()` + `upload_file()` | `gh release create` |
| Update | `kaggle datasets version -p <staging> -m "msg"` | `upload_file()` (overwrites) | `gh release upload --clobber` |
| Status | `kaggle datasets status lucassteuber/name` | `huggingface-cli repo info lukeslp/name --repo-type dataset` | `gh repo view lukeslp/name` |
| Public | Metadata update: `isPrivate: false` | `api.update_repo_visibility()` | Already public |
| Delete | Web UI only | `api.delete_repo()` | `gh release delete` |
