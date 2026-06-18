#!/usr/bin/env python3
"""
sync_vocab.py — Sync vocabulary from song MD files into vocab-log.json.

Scans both content/songs/ and songs/ for MD files, parses their vocabulary
tables, and merges new words into vocab-log.json.

Rules:
  - Deduplication is by normalised word (lowercased, stripped).
  - A word found in multiple songs gets source_content as an array of all
    song IDs it appears in.
  - Existing quiz stats, mastery_level, and date_learned are never overwritten.
  - source_content for existing entries is migrated to array and extended.

Usage:
  python3 utils/sync_vocab.py [--dry-run]
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
VOCAB_LOG = REPO_ROOT / "progress" / "vocab-log.json"
SONG_DIRS = [
    REPO_ROOT / "content" / "songs",
    REPO_ROOT / "songs",
]

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def song_id_from_path(path: Path) -> str:
    """Return a song ID from a file path (stem without extension)."""
    return path.stem


def parse_vocab_table(text: str) -> list[dict]:
    """
    Extract vocab rows from a Markdown table inside a ## Vocabulary section.

    Supports two column layouts:
      3-col: | Word / Phrase | Meaning | Notes |
      4-col: | Word / Phrase | Meaning | Part of Speech | Notes |

    Returns a list of dicts with keys: word, meaning, part_of_speech, notes.
    Skips header rows, separator rows, and non-vocab tables (e.g. line-by-line
    translation tables whose first column header is "Portuguese").
    """
    # Isolate the ## Vocabulary section (up to the next ## heading)
    vocab_section_match = re.search(
        r"^## Vocabulary\b.*?(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not vocab_section_match:
        return []

    section = vocab_section_match.group(0)

    # Find all markdown tables within this section
    rows = []
    current_table_cols = None  # "word_col_type": "3col" | "4col" | None

    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            current_table_cols = None
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]

        # Separator row
        if all(re.match(r"^-+$", c) for c in cells if c):
            continue

        # Header row detection
        if len(cells) >= 2:
            first = cells[0].lower()
            if first in ("word / phrase", "word/phrase", "word"):
                # Determine table type
                if len(cells) >= 4 and "part" in cells[2].lower():
                    current_table_cols = "4col"
                else:
                    current_table_cols = "3col"
                continue
            # Skip non-vocab tables (e.g. Portuguese | English translation tables)
            if first in ("portuguese", "line / phrase", "form in song",
                         "pattern", "item", "word repetition"):
                current_table_cols = None
                continue

        if current_table_cols is None:
            continue

        # Data row
        if current_table_cols == "4col" and len(cells) >= 3:
            word    = cells[0]
            meaning = cells[1]
            pos     = cells[2] if len(cells) > 2 else ""
            notes   = cells[3] if len(cells) > 3 else ""
        elif current_table_cols == "3col" and len(cells) >= 2:
            word    = cells[0]
            meaning = cells[1]
            pos     = ""
            notes   = cells[2] if len(cells) > 2 else ""
        else:
            continue

        word = word.strip()
        if not word:
            continue

        rows.append({
            "word":           word,
            "meaning":        meaning.strip(),
            "part_of_speech": pos.strip(),
            "notes":          notes.strip(),
        })

    return rows


# ---------------------------------------------------------------------------
# Vocab-log helpers
# ---------------------------------------------------------------------------

def load_vocab_log() -> list[dict]:
    if not VOCAB_LOG.exists():
        return []
    with open(VOCAB_LOG, encoding="utf-8") as f:
        return json.load(f)


def save_vocab_log(entries: list[dict], dry_run: bool) -> None:
    if dry_run:
        print(json.dumps(entries, ensure_ascii=False, indent=2))
        return
    with open(VOCAB_LOG, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
        f.write("\n")


def normalise(word: str) -> str:
    """Normalisation key for deduplication."""
    return word.lower().strip()


def entry_key(entry: dict) -> str:
    return normalise(entry["word"])


def migrate_source_to_array(entry: dict) -> None:
    """Ensure source_content is always a list (migrate legacy string entries)."""
    sc = entry.get("source_content")
    if sc is None:
        entry["source_content"] = []
    elif isinstance(sc, str):
        entry["source_content"] = [sc] if sc else []


def blank_quiz_stats() -> dict:
    return {
        "times_asked":   0,
        "times_correct": 0,
        "times_wrong":   0,
        "success_rate":  None,
    }


# ---------------------------------------------------------------------------
# Main sync logic
# ---------------------------------------------------------------------------

def collect_song_vocab() -> dict[str, dict]:
    """
    Walk all song MD files and return a dict keyed by normalised word.
    Each value: { word, meaning, part_of_speech, sources: [song_id, ...] }
    When the same word appears in multiple songs, sources grows.
    First-seen meaning/pos wins (content/songs/ scanned before songs/).
    """
    collected: dict[str, dict] = {}

    for song_dir in SONG_DIRS:
        if not song_dir.exists():
            continue
        for md_file in sorted(song_dir.glob("*.md")):
            song_id = song_id_from_path(md_file)
            text = md_file.read_text(encoding="utf-8")
            rows = parse_vocab_table(text)
            for row in rows:
                key = normalise(row["word"])
                if key not in collected:
                    collected[key] = {
                        "word":           row["word"],
                        "meaning":        row["meaning"],
                        "part_of_speech": row["part_of_speech"],
                        "sources":        [song_id],
                    }
                else:
                    # Word already seen — just add new source if not present
                    if song_id not in collected[key]["sources"]:
                        collected[key]["sources"].append(song_id)
                    # Fill in missing meaning/pos from this file if blank
                    if not collected[key]["meaning"] and row["meaning"]:
                        collected[key]["meaning"] = row["meaning"]
                    if not collected[key]["part_of_speech"] and row["part_of_speech"]:
                        collected[key]["part_of_speech"] = row["part_of_speech"]

    return collected


def sync(dry_run: bool = False) -> None:
    existing = load_vocab_log()

    # Migrate all existing entries to array source_content
    for entry in existing:
        migrate_source_to_array(entry)

    # Build lookup by normalised word
    lookup: dict[str, dict] = {entry_key(e): e for e in existing}

    song_vocab = collect_song_vocab()

    added   = 0
    updated = 0

    for key, song_entry in song_vocab.items():
        if key in lookup:
            log_entry = lookup[key]
            # Extend sources array with any new songs
            old_sources = set(log_entry["source_content"])
            new_sources = [s for s in song_entry["sources"] if s not in old_sources]
            if new_sources:
                log_entry["source_content"].extend(new_sources)
                updated += 1
                print(f"  updated sources for '{log_entry['word']}': +{new_sources}")
        else:
            # New word — create a fresh entry
            new_entry = {
                "word":           song_entry["word"],
                "meaning":        song_entry["meaning"],
                "part_of_speech": song_entry["part_of_speech"],
                "source_type":    "song",
                "source_content": song_entry["sources"],
                "date_learned":   None,
                "last_reviewed":  None,
                "quiz_stats":     blank_quiz_stats(),
                "mastery_level":  "new",
            }
            existing.append(new_entry)
            lookup[key] = new_entry
            added += 1
            sources_str = ", ".join(song_entry["sources"])
            print(f"  added '{song_entry['word']}' from [{sources_str}]")

    print(f"\nSync complete: {added} added, {updated} updated, "
          f"{len(existing)} total entries.")

    if dry_run:
        print("\n--- DRY RUN: vocab-log.json not written ---\n")
    save_vocab_log(existing, dry_run)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync song vocab into vocab-log.json")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing vocab-log.json",
    )
    args = parser.parse_args()
    sync(dry_run=args.dry_run)
