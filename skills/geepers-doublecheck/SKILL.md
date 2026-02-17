---
name: geepers-doublecheck
description: Dataset validation, synthetic data detection, citation checking, and cross-platform publishing consistency. Use when (1) validating datasets before publication, (2) detecting synthetic/fake data, (3) auditing published datasets across HuggingFace/Kaggle/GitHub, (4) generating data cards, or (5) syncing the data trove index.
---

# Dataset Validator Skill

Validate datasets for authenticity, citations, and publication readiness.

## Usage

```
/geepers-doublecheck validate path/to/dataset/       # Full pre-publication validation
/geepers-doublecheck detect-synthetic path/to/data.csv  # Synthetic data scan
/geepers-doublecheck audit huggingface:lukeslp/dataset  # Post-publication audit
/geepers-doublecheck consistency                      # Cross-platform sync check
/geepers-doublecheck publish path/to/dataset/         # Validate + publish + update index
/geepers-doublecheck cards path/to/dataset/           # Generate data cards only
```

## Modes

### validate (default)
Full pre-publication checklist:
- Scan for synthetic data red flags
- Verify all source URLs resolve
- Check schema completeness
- Validate geographic coordinates
- Cross-reference entity names against real databases
- Generate quality report

### detect-synthetic
Focused synthetic data scan:
- Timestamp uniformity analysis
- Name pattern detection (generic sequences)
- Coordinate plausibility checking
- Distribution analysis (suspiciously uniform?)
- Provenance chain verification
- Confidence-rated findings (high/medium/low)

### audit
Post-publication health check:
- Fetch from HuggingFace, Kaggle, and/or GitHub
- Compare against local source of truth
- Report discrepancies (missing files, schema drift, stale descriptions)
- Check download counts and community feedback
- Verify direct download links work

### consistency
Cross-platform sync:
- Compare file checksums across all platforms
- Verify record counts match
- Check schema descriptions are consistent
- Ensure version numbers are synchronized
- Confirm license is the same everywhere

### publish
End-to-end workflow:
1. Run full validation
2. Fix any issues found
3. Delegate to `/dataset-publish` for actual API uploads
4. Update `data_trove/index.html` with new/updated entries

### cards
Generate data cards for one or more platforms:
- HuggingFace: `README.md` with YAML frontmatter
- Kaggle: `dataset-metadata.json`
- GitHub: `DATACARD.md`

## Red Flags It Catches

| Red Flag | Confidence | Example |
|----------|-----------|---------|
| Identical timestamps across files | High | All files created `2026-01-18 21:58` |
| Generic sequential names | High | "Ruins 1", "Vessel 2" |
| No source URL in metadata | High | Missing provenance |
| Impossible coordinates | High | Land species at ocean coordinates |
| Suspiciously round record counts | Medium | Exactly 1000, 5000 |
| Uniform distributions | Medium | Even spread where skew expected |
| Poetic metadata titles | Low | "Stone Chronicles" |

## Routes To

- **Agent**: `geepers_doublecheck`
- **Delegates**: `/dataset-publish` skill for actual API uploads
- **Collaborates**: `geepers_citations` (URL checking), `geepers_data` (quality), `geepers_fetcher` (source verification)
- **Updates**: `data_trove/index.html` after publish operations

## Publishing Credentials

Delegates to `/dataset-publish` which uses:
- **Kaggle**: `~/.kaggle/kaggle.json`
- **HuggingFace**: `$HF_API_KEY`, user: `lukeslp`
- **GitHub**: `gh` CLI (authenticated)
