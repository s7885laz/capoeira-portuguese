#!/usr/bin/env python3
"""
Song Markdown Validator for Capoeira Portuguese Learning

Validates song lesson .md files to ensure they're compatible with song_md_to_html_converter.py
before conversion. Helps catch formatting issues early and prevents conversion errors.

This script checks:
- Required sections and structure
- Markdown table formatting
- Heading case consistency
- Media link formatting
- Special characters and encoding
- File completeness

Usage:
    python validate_song_md.py song-name.md              # Validate single file
    python validate_song_md.py                           # Validate all song-*.md files
    python validate_song_md.py --fix song-name.md        # Auto-fix common issues
    python validate_song_md.py --report                  # Generate validation report
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple


class SongMarkdownValidator:
    """Validates song lesson markdown files for converter compatibility."""

    # Required sections in order
    REQUIRED_SECTIONS = [
        '# [Song Title]',
        '## Basic Info',
        '## Media Links',
        '## Lyrics',
        '## Pronunciation',
        '## Vocabulary',
        '## Grammar',
        '## Cultural Notes',
        '## Repeated Expressions / Chorus',
        '## Practice'
    ]

    # Required subsections within main sections
    REQUIRED_SUBSECTIONS = {
        'Lyrics': ['### Full Lyrics', '### Line-by-line Meaning'],  # Note: case-flexible now
        'Media Links': ['### YouTube', '### Spotify'],  # At least these two
        'Grammar': ['### 1. Verb Forms', '### 2. Sentence Patterns'],  # Common grammar subsections
    }

    # Common issues and patterns
    PATTERNS = {
        'heading1': re.compile(r'^# .+$', re.MULTILINE),
        'heading2': re.compile(r'^## .+$', re.MULTILINE),
        'heading3': re.compile(r'^### .+$', re.MULTILINE),
        'table': re.compile(r'^\|.+\|$', re.MULTILINE),
        'link_markdown': re.compile(r'\[([^\]]+)\]\(([^\)]+)\)'),
        'link_http': re.compile(r'https?://'),
        'media_youtube': re.compile(r'### YouTube', re.IGNORECASE),
        'media_spotify': re.compile(r'### Spotify', re.IGNORECASE),
        'media_apple': re.compile(r'### Apple', re.IGNORECASE),
        'table_separator': re.compile(r'^\|[\s\-|:]+\|$', re.MULTILINE),
    }

    def __init__(self, songs_dir=None):
        """Initialize validator with project paths."""
        if songs_dir is None:
            songs_dir = Path(__file__).parent.parent / "songs"
        self.songs_dir = Path(songs_dir)

    def validate_file(self, file_path: str) -> Tuple[bool, List[str], List[str]]:
        """
        Validate a single markdown file.

        Returns:
            (is_valid, errors, warnings)
        """
        file_path = Path(file_path)

        if not file_path.exists():
            return False, [f"File not found: {file_path}"], []

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        errors = []
        warnings = []

        # 1. Check file encoding
        try:
            content.encode('utf-8')
        except UnicodeEncodeError as e:
            errors.append(f"Encoding error: {e}")

        # 2. Check for title (H1)
        if not self.PATTERNS['heading1'].search(content):
            errors.append("Missing H1 title (# Song Title)")
        else:
            # Extract title
            match = self.PATTERNS['heading1'].search(content)
            title = match.group(0)[2:].strip()
            if len(title) < 3:
                errors.append(f"Title too short: '{title}'")

        # 3. Check required sections (flexible matching for Grammar/Grammar Notes)
        required_sections_flexible = {
            '# [Song Title]': r'^#\s+.+$',
            '## Basic Info': r'^##\s+Basic Info$',
            '## Media Links': r'^##\s+Media Links$',
            '## Lyrics': r'^##\s+Lyrics$',
            '## Pronunciation': r'^##\s+Pronunciation$',
            '## Vocabulary': r'^##\s+Vocabulary$',
            '## Grammar': r'^##\s+Grammar(?:\s+Notes)?$',  # Matches both "Grammar" and "Grammar Notes"
            '## Cultural': r'^##\s+Cultural\s+(?:Notes|Context)?$',  # Flexible
            '## Repeated': r'^##\s+Repeated\s+(?:Expressions|Phrases)\s*/\s*Chorus$',
            '## Practice': r'^##\s+Practice$'
        }

        for section_display, section_pattern in required_sections_flexible.items():
            if not re.search(section_pattern, content, re.MULTILINE | re.IGNORECASE):
                warnings.append(f"Missing or incorrectly named section: {section_display}")

        # 4. Check Basic Info subsections
        basic_info_match = re.search(
            r'## Basic Info\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )
        if basic_info_match:
            basic_info = basic_info_match.group(1)
            required_fields = ['Date added:', 'Status:', 'Source:', 'Type:']
            for field in required_fields:
                if field not in basic_info:
                    warnings.append(f"Basic Info missing field: {field}")

        # 5. Check Lyrics section structure
        lyrics_match = re.search(
            r'## Lyrics\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if lyrics_match:
            lyrics = lyrics_match.group(1)

            # Check for Full Lyrics (case insensitive)
            if not re.search(r'###\s+Full\s+(?:lyrics|Lyrics)', lyrics, re.IGNORECASE):
                errors.append("Lyrics: Missing '### Full Lyrics' subsection")

            # Check for Line-by-line/Line-by-Line Meaning (very flexible)
            if not re.search(r'###\s+(?:Line-by-line|Line-by-Line)\s+(?:Meaning|meaning)', lyrics, re.IGNORECASE):
                errors.append("Lyrics: Missing 'Line-by-line Meaning' table subsection")

            # Check for translation table (has pipes and dashes)
            if not re.search(r'\|.*\|.*\n\|[\s\-|:]+\|', lyrics):
                errors.append("Lyrics: Missing translation table (expected pipe-separated format)")

        # 6. Check Media Links
        media_match = re.search(
            r'## Media Links\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if media_match:
            media = media_match.group(1)

            # Check for YouTube (case insensitive)
            if not re.search(r'###\s+YouTube', media, re.IGNORECASE):
                warnings.append("Media Links: No '### YouTube' section found (recommended)")

            # Check for Spotify (case insensitive)
            if not re.search(r'###\s+Spotify', media, re.IGNORECASE):
                warnings.append("Media Links: No '### Spotify' section found (recommended)")

            # Check for at least some link or search instruction
            if not re.search(r'https?://|search:', media, re.IGNORECASE):
                warnings.append("Media Links: No HTTP links or search instructions found")

        # 7. Check Vocabulary table
        vocab_match = re.search(
            r'## Vocabulary\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if vocab_match:
            vocab = vocab_match.group(1)
            if '|' not in vocab:
                errors.append("Vocabulary: Missing table (expected pipe-separated format)")

            # Check table has header
            if '---|' not in vocab:
                errors.append("Vocabulary: Missing table separator (---|)")

        # 8. Check Pronunciation table
        pron_match = re.search(
            r'## Pronunciation\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if pron_match:
            pron = pron_match.group(1)
            if '|' not in pron:
                errors.append("Pronunciation: Missing table (expected pipe-separated format)")

        # 9. Check Grammar/Grammar Notes
        grammar_match = re.search(
            r'## Grammar(?:\s|Notes)?\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if grammar_match:
            grammar = grammar_match.group(1)

            # Check for subsections
            if not re.search(r'^### \d+\. ', grammar, re.MULTILINE):
                warnings.append("Grammar: No numbered subsections found (expected ### 1. , ### 2. , etc.)")

            # Check for at least one grammar table
            if '|' not in grammar:
                warnings.append("Grammar: No tables found (expected at least one grammar table)")

        # 10. Check Cultural Notes
        cultural_match = re.search(
            r'## Cultural Notes\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if not cultural_match:
            warnings.append("Missing 'Cultural Notes' section")

        # 11. Check Practice section
        practice_match = re.search(
            r'## Practice\n(.*?)(?=\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if not practice_match:
            warnings.append("Missing 'Practice' section")
        else:
            practice = practice_match.group(1)
            if not re.search(r'^\d+\.', practice, re.MULTILINE):
                warnings.append("Practice: No numbered list found (expected 1. , 2. , etc.)")

        # 12. Check for common markdown errors
        # Check for unmatched brackets
        if content.count('[') != content.count(']'):
            errors.append("Unmatched square brackets [] in content")

        if content.count('(') != content.count(')'):
            errors.append("Unmatched parentheses () in content")

        # 13. Check line ending consistency
        crlf_count = content.count('\r\n')
        lf_count = content.count('\n') - crlf_count
        if crlf_count > 0 and lf_count > 0:
            warnings.append("Mixed line endings (CRLF and LF) - may cause issues")

        # 14. Check for non-breaking spaces
        if ' ' in content:
            warnings.append("Contains non-breaking spaces (\\u00a0) - may cause issues")

        # 15. Check file size
        if len(content) < 5000:
            warnings.append(f"File seems incomplete ({len(content)} bytes - expected 8000+)")
        elif len(content) > 50000:
            warnings.append(f"File is very large ({len(content)} bytes - may be too detailed)")

        is_valid = len(errors) == 0
        return is_valid, errors, warnings

    def validate_all(self) -> dict:
        """Validate all song-*.md files in songs directory."""
        results = {}

        song_files = list(self.songs_dir.glob('song-*.md'))

        if not song_files:
            print(f"No song files found in {self.songs_dir}")
            return results

        for song_file in sorted(song_files):
            is_valid, errors, warnings = self.validate_file(song_file)
            results[song_file.name] = {
                'valid': is_valid,
                'errors': errors,
                'warnings': warnings
            }

        return results

    def print_report(self, file_path: str):
        """Print validation report for a single file."""
        is_valid, errors, warnings = self.validate_file(file_path)

        file_name = Path(file_path).name

        print(f"\n{'=' * 70}")
        print(f"Song Markdown Validation Report: {file_name}")
        print(f"{'=' * 70}\n")

        if is_valid:
            print("✓ VALID - File is compatible with HTML converter\n")
        else:
            print("✗ INVALID - File has compatibility issues\n")

        if errors:
            print(f"❌ ERRORS ({len(errors)}):")
            for i, error in enumerate(errors, 1):
                print(f"   {i}. {error}")
            print()

        if warnings:
            print(f"⚠️  WARNINGS ({len(warnings)}):")
            for i, warning in enumerate(warnings, 1):
                print(f"   {i}. {warning}")
            print()

        if not errors and not warnings:
            print("✓ All checks passed!\n")

        # Print summary
        print(f"{'=' * 70}")
        print(f"Status: {'READY FOR CONVERSION' if is_valid else 'NEEDS FIXES'}")
        print(f"{'=' * 70}\n")

        return is_valid

    def print_all_reports(self):
        """Print validation report for all files."""
        results = self.validate_all()

        print(f"\n{'=' * 70}")
        print(f"Song Markdown Validation Report — All Files")
        print(f"{'=' * 70}\n")

        valid_count = sum(1 for r in results.values() if r['valid'])
        total_count = len(results)

        for file_name, result in results.items():
            status = "✓ VALID" if result['valid'] else "✗ INVALID"
            error_count = len(result['errors'])
            warning_count = len(result['warnings'])
            print(f"{status} — {file_name}")
            if error_count > 0:
                print(f"        {error_count} error(s)")
            if warning_count > 0:
                print(f"        {warning_count} warning(s)")
            print()

        print(f"{'=' * 70}")
        print(f"Summary: {valid_count}/{total_count} files valid")
        print(f"{'=' * 70}\n")

    def generate_checklist(self) -> str:
        """Generate a checklist for Perplexity to follow when creating songs."""
        checklist = """
# ✅ Song Lesson Markdown Checklist for Perplexity

Use this checklist when generating song lesson markdown files to ensure they're compatible with the HTML converter.

## 📋 Required Sections (in order)

- [ ] **# [Song Title]** — H1 heading with song name (e.g., "# Ai, Ai, Aidê")
- [ ] **## Basic Info** with:
  - [ ] Date added: YYYY-MM-DD
  - [ ] Status: In Study / Mastered
  - [ ] Source: [Artist/Tradition]
  - [ ] Type: Corrido / Ladainha / etc.

- [ ] **## Media Links** with:
  - [ ] ### YouTube (at least one link)
  - [ ] ### Spotify (search instructions okay)
  - [ ] ### Apple Music (optional)
  - [ ] ### YouTube Music (optional)
  - Links should use markdown format: [Description](https://url)

- [ ] **## Lyrics** with:
  - [ ] ### Full Lyrics (plain text, one line per lyric)
  - [ ] ### Line-by-line Meaning (or Line-by-Line Meaning — both work!)
    - Must be a markdown table with two columns: Portuguese | English
    - Table format: | Portuguese | English | with |---|---| separator

- [ ] **## Pronunciation** with:
  - [ ] Markdown table: | Line / Phrase | Pronunciation Help |
  - [ ] Table separator: |---|---|
  - [ ] Optional: pronunciation tips after the table

- [ ] **## Vocabulary** with:
  - [ ] Markdown table: | Word / Phrase | Meaning | Notes |
  - [ ] Every word from the song included (NO exceptions)
  - [ ] Notes should include: gender (for nouns), verb form, usage context

- [ ] **## Grammar** or **## Grammar Notes** with:
  - [ ] ### 1. Verb Forms (table format)
  - [ ] ### 2. Sentence Patterns (table format)
  - [ ] ### 3. Pronouns and Subject Omission (table format)
  - [ ] ### 4. Repetition and Chorus Structure (table format)
  - [ ] ### 5. Poetic / Traditional / Informal Language (table format)
  - [ ] ### 6. Grammar Questions (bullet points or questions)

- [ ] **## Cultural Notes** (or **## Cultural Context**)
  - [ ] Bullet points or paragraphs explaining history, significance, tradition
  - [ ] At least 3-4 points

- [ ] **## Repeated Expressions / Chorus**
  - [ ] List of repeated phrases with their functions
  - [ ] Format: "**[phrase]**" — [explanation]

- [ ] **## Practice**
  - [ ] Numbered list (1. , 2. , 3. , 4. )
  - [ ] At least 4 practice exercises
  - [ ] Examples only use vocabulary already taught

---

## 📊 Table Format Requirements

### All Tables Must Have:
- [ ] Pipe characters (|) separating columns
- [ ] Header row with column names
- [ ] Separator row with dashes and pipes: |---|---|---|
- [ ] Data rows with proper column alignment
- [ ] No extra spaces that break the table (critical!)

### Example:
```markdown
| Word | Meaning | Notes |
|---|---|---|
| água | water | Feminine noun |
| maré | tide | Common in capoeira songs |
```

---

## ⚠️ Common Mistakes to AVOID

- [ ] ❌ Inconsistent heading capitalization (don't mix "Line-by-line" and "Line-by-Line")
- [ ] ❌ Missing table separators (|---|---|)
- [ ] ❌ Unmatched brackets or parentheses
- [ ] ❌ Vocabulary words not explained
- [ ] ❌ Grammar tables with missing columns
- [ ] ❌ Practice exercises using unexplained vocabulary
- [ ] ❌ CRLF line endings (use LF only)
- [ ] ❌ Non-breaking spaces instead of regular spaces
- [ ] ❌ Missing Media Links section
- [ ] ❌ Short file (< 5000 bytes usually means incomplete)

---

## 🔍 Before Submitting

Run this validation check:
```bash
python utils/validate_song_md.py song-name.md
```

✓ File should show: **READY FOR CONVERSION**
✓ All errors should be: **FIXED**
✓ Warnings can be: **REVIEWED** (not critical)

---

## 💡 Tips

- Copy an existing song file (e.g., song-ai-ai-aide.md) as a template
- Use the exact section names from this checklist
- Always include pronunciation (even if simplified)
- Grammar tables are most important — don't skip them
- Cultural context makes the lesson richer — add details!

"""
        return checklist


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate song lesson markdown files for HTML converter compatibility"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Song markdown file to validate (optional)"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate validation report for all files"
    )
    parser.add_argument(
        "--checklist",
        action="store_true",
        help="Print checklist for Perplexity"
    )
    parser.add_argument(
        "--directory",
        help="Songs directory (auto-detected if not specified)"
    )

    args = parser.parse_args()

    try:
        validator = SongMarkdownValidator(songs_dir=args.directory)

        if args.checklist:
            print(validator.generate_checklist())
        elif args.report or not args.file:
            validator.print_all_reports()
        else:
            is_valid = validator.print_report(args.file)
            sys.exit(0 if is_valid else 1)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
