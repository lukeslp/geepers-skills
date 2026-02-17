#!/usr/bin/env python3
"""
Dataset Publishing Tool

Publish datasets to Kaggle, HuggingFace, and GitHub.

Usage:
    python publish.py kaggle /path/to/dataset
    python publish.py huggingface /path/to/dataset
    python publish.py github /path/to/dataset
    python publish.py all /path/to/dataset

Subcommands:
    python publish.py kaggle check /path/to/dataset
    python publish.py kaggle generate /path/to/dataset
    python publish.py kaggle update /path/to/dataset --message "Update"
    python publish.py kaggle status username/dataset
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def check_kaggle_auth():
    """Check if Kaggle credentials exist."""
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_json.exists():
        return False, "~/.kaggle/kaggle.json not found"
    try:
        with open(kaggle_json) as f:
            creds = json.load(f)
        if "username" in creds and "key" in creds:
            return True, creds["username"]
    except:
        pass
    return False, "Invalid kaggle.json format"


def check_hf_auth():
    """Check if HuggingFace token exists."""
    token = os.environ.get("HF_TOKEN") or os.environ.get("HF_API_KEY")
    if token:
        return True, "Token found in environment"
    token_file = Path.home() / ".cache" / "huggingface" / "token"
    if token_file.exists():
        return True, "Token found in cache"
    return False, "No HF_TOKEN or cached token found"


def check_gh_auth():
    """Check if GitHub CLI is authenticated."""
    result = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    if result.returncode == 0:
        return True, "Authenticated"
    return False, "Run: gh auth login"


def validate_kaggle_metadata(path: Path):
    """Validate Kaggle dataset-metadata.json."""
    meta_file = path / "dataset-metadata.json"
    if not meta_file.exists():
        return False, "dataset-metadata.json not found"

    try:
        with open(meta_file) as f:
            meta = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"

    errors = []

    # Required fields
    if "title" not in meta:
        errors.append("Missing 'title'")
    elif not (6 <= len(meta["title"]) <= 50):
        errors.append(f"Title must be 6-50 chars (got {len(meta['title'])})")

    if "id" not in meta:
        errors.append("Missing 'id' (format: username/dataset-slug)")

    if "subtitle" in meta and not (20 <= len(meta["subtitle"]) <= 80):
        errors.append(f"Subtitle must be 20-80 chars (got {len(meta['subtitle'])})")

    if errors:
        return False, "; ".join(errors)
    return True, "Valid"


def validate_hf_readme(path: Path):
    """Validate HuggingFace README with YAML frontmatter."""
    readme = path / "HUGGINGFACE_README.md"
    if not readme.exists():
        readme = path / "README.md"
    if not readme.exists():
        return False, "README.md or HUGGINGFACE_README.md not found"

    with open(readme) as f:
        content = f.read()

    if not content.startswith("---"):
        return False, "Missing YAML frontmatter (must start with ---)"

    # Check for license
    if "license:" not in content:
        return False, "Missing 'license' in frontmatter"

    return True, "Valid"


def find_data_files(path: Path):
    """Find data files in directory."""
    extensions = {".json", ".csv", ".parquet", ".jsonl", ".tsv", ".xlsx"}
    files = []
    for f in path.iterdir():
        if f.is_file() and f.suffix.lower() in extensions:
            size_mb = f.stat().st_size / (1024 * 1024)
            files.append((f.name, size_mb))
    return files


def cmd_check(args):
    """Validate dataset before publishing."""
    path = Path(args.path).resolve()

    print(f"\n📋 Validating: {path}\n")

    # Check data files
    files = find_data_files(path)
    if not files:
        print("❌ No data files found (.json, .csv, .parquet)")
        return 1
    print(f"✅ Found {len(files)} data file(s):")
    for name, size in files:
        print(f"   - {name} ({size:.1f} MB)")

    # Check platform-specific
    if args.platform in ("kaggle", "all"):
        print("\n🔷 Kaggle:")
        auth_ok, auth_msg = check_kaggle_auth()
        print(f"   Auth: {'✅' if auth_ok else '❌'} {auth_msg}")
        meta_ok, meta_msg = validate_kaggle_metadata(path)
        print(f"   Metadata: {'✅' if meta_ok else '❌'} {meta_msg}")

    if args.platform in ("huggingface", "hf", "all"):
        print("\n🤗 HuggingFace:")
        auth_ok, auth_msg = check_hf_auth()
        print(f"   Auth: {'✅' if auth_ok else '❌'} {auth_msg}")
        readme_ok, readme_msg = validate_hf_readme(path)
        print(f"   README: {'✅' if readme_ok else '❌'} {readme_msg}")

    if args.platform in ("github", "gh", "all"):
        print("\n🐙 GitHub:")
        auth_ok, auth_msg = check_gh_auth()
        print(f"   Auth: {'✅' if auth_ok else '❌'} {auth_msg}")

    print()
    return 0


def cmd_generate(args):
    """Generate metadata files for a dataset."""
    path = Path(args.path).resolve()

    print(f"\n📝 Generating metadata for: {path}\n")

    # Detect dataset info
    files = find_data_files(path)
    if not files:
        print("❌ No data files found")
        return 1

    # Get basic info
    dataset_name = path.name.replace("_", "-").replace(" ", "-").lower()

    # Try to count records in JSON files
    record_count = 0
    for name, _ in files:
        if name.endswith(".json"):
            try:
                with open(path / name) as f:
                    data = json.load(f)
                if isinstance(data, list):
                    record_count = len(data)
                    break
            except:
                pass

    # Generate Kaggle metadata
    kaggle_meta = {
        "title": dataset_name[:50],
        "id": f"USERNAME/{dataset_name}",
        "licenses": [{"name": "CC-BY-4.0"}],
        "subtitle": f"{record_count:,} records" if record_count else "Dataset description (20-80 chars)",
        "description": f"# {dataset_name}\n\nDescription here...",
        "keywords": ["data"],
        "isPrivate": False
    }

    meta_path = path / "dataset-metadata.json"
    if not meta_path.exists():
        with open(meta_path, "w") as f:
            json.dump(kaggle_meta, f, indent=2)
        print(f"✅ Created: dataset-metadata.json")
    else:
        print(f"⏭️  Skipped: dataset-metadata.json (exists)")

    # Generate HuggingFace README
    hf_readme = f"""---
license: cc-by-4.0
task_categories:
  - feature-extraction
language:
  - en
tags:
  - data
pretty_name: {dataset_name}
size_categories:
  - {"1K<n<10K" if record_count < 10000 else "10K<n<100K" if record_count < 100000 else "100K<n<1M"}
---

# {dataset_name}

Description here...

## Dataset Contents

- **Total Records**: {record_count:,}
- **Format**: JSON

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("USERNAME/{dataset_name}")
```

## License

CC-BY-4.0
"""

    hf_path = path / "HUGGINGFACE_README.md"
    if not hf_path.exists():
        with open(hf_path, "w") as f:
            f.write(hf_readme)
        print(f"✅ Created: HUGGINGFACE_README.md")
    else:
        print(f"⏭️  Skipped: HUGGINGFACE_README.md (exists)")

    # Generate setup checklist
    setup_md = f"""# Platform Setup Checklist

Complete after API upload. Delete this file when done.

## Kaggle (kaggle.com/datasets/USERNAME/{dataset_name}/settings)

- [ ] Cover image (1200x630px)
- [ ] Provenance/data sources
- [ ] File descriptions
- [ ] Update frequency
- [ ] Verify license

## HuggingFace (huggingface.co/datasets/USERNAME/{dataset_name})

- [ ] Dataset card preview
- [ ] Viewer configuration

Generated: {datetime.now().strftime("%Y-%m-%d")}
"""

    setup_path = path / "KAGGLE_SETUP.md"
    if not setup_path.exists():
        with open(setup_path, "w") as f:
            f.write(setup_md)
        print(f"✅ Created: KAGGLE_SETUP.md")
    else:
        print(f"⏭️  Skipped: KAGGLE_SETUP.md (exists)")

    print(f"\n⚠️  Update USERNAME in generated files before publishing.\n")
    return 0


def cmd_status(args):
    """Check status of a dataset."""
    if args.platform == "kaggle":
        result = subprocess.run(
            ["kaggle", "datasets", "status", args.dataset],
            capture_output=True, text=True
        )
        print(result.stdout or result.stderr)
    elif args.platform in ("huggingface", "hf"):
        print("Use: huggingface-cli repo info --repo-type dataset USERNAME/DATASET")
    return 0


def cmd_publish(args):
    """Publish dataset to platform(s)."""
    path = Path(args.path).resolve()

    if args.platform in ("kaggle", "all"):
        print("\n🔷 Publishing to Kaggle...")
        result = subprocess.run(
            ["kaggle", "datasets", "create", "-p", str(path)],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print("✅ Kaggle upload complete")
        else:
            print(f"❌ Kaggle error: {result.stderr}")

    if args.platform in ("huggingface", "hf", "all"):
        print("\n🤗 Publishing to HuggingFace...")
        # This would need the full HF upload logic
        print("   Use the HuggingFace Hub Python API for uploads")

    if args.platform in ("github", "gh", "all"):
        print("\n🐙 Publishing to GitHub...")
        print("   Use: gh release create v1.0.0 datafile.json")

    return 0


def main():
    parser = argparse.ArgumentParser(description="Dataset Publishing Tool")
    parser.add_argument("platform", choices=["kaggle", "huggingface", "hf", "github", "gh", "all"])
    parser.add_argument("command", nargs="?", default="publish",
                        choices=["publish", "check", "generate", "update", "status"])
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--message", "-m", help="Update message")
    parser.add_argument("--dataset", help="Dataset ID for status command")

    args = parser.parse_args()

    if args.command == "check":
        return cmd_check(args)
    elif args.command == "generate":
        return cmd_generate(args)
    elif args.command == "status":
        if not args.dataset:
            args.dataset = args.path  # Use path as dataset ID
        return cmd_status(args)
    else:
        return cmd_publish(args)


if __name__ == "__main__":
    sys.exit(main())
