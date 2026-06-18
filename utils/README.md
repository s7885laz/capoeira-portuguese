# Utils — Capoeira Portuguese Learning Tools

Utility scripts for managing the learning app.

---

## `song_md_to_html_converter.py`

**Purpose:** Automatically convert Markdown **song lesson** files to styled HTML pages for the web app.

⚠️ **SPECIALIZED FOR SONG LESSONS ONLY** — This converter is hardcoded for `song-*.md` files with song-specific structure. It will not work for general Markdown files.

### Why Use This?

- ✅ **Fast** — Convert 50 songs in seconds
- ✅ **Consistent** — Same styling applied to every lesson
- ✅ **Automated** — Watch folder for new songs and convert automatically
- ✅ **Preserves Content** — All vocabulary, grammar, tables, and cultural notes are preserved

### Quick Start

#### 1. Convert All Songs

```bash
cd /Users/lazarovitsbence/workspaces/Projects/Capoeira_Portuguese_Claude
python utils/song_md_to_html_converter.py
```

This will:
- Find all `song-*.md` files in the `songs/` folder
- Convert each to an HTML file in the `app/` folder
- Use the song title to generate a URL-friendly filename

#### 2. Convert a Single Song

```bash
python utils/song_md_to_html_converter.py --file song-name.md
```

Example:
```bash
python utils/song_md_to_html_converter.py --file song-ai-ai-aide.md
```

#### 3. Watch Mode (Auto-Convert)

```bash
python utils/song_md_to_html_converter.py --watch
```

This will:
- Monitor the `songs/` folder for new `.md` files
- Automatically convert any new song added
- Run continuously until you press `Ctrl+C`

**Useful for:** When you're adding songs frequently, just run this once and forget about it.

---

## File Structure

```
Capoeira_Portuguese_Claude/
├── songs/
│   ├── song-ai-ai-aide.md          ← Markdown source
│   ├── song-santo-antonio-quero-agua.md
│   └── [other songs].md
├── app/
│   ├── ai-ai-aide.html             ← Generated HTML output
│   ├── santo-antonio-quero-agua.html
│   ├── poc.html                    ← Landing page
│   └── [other lessons].html
└── utils/
    ├── md_to_html_converter.py      ← This script
    └── README.md                    ← This file
```

---

## How the Converter Works

### Input (Markdown)
```markdown
# Ai, Ai, Aidê

## Basic Info
- Date added: 2026-06-17
- Status: In Study
- Source: Traditional
- Type: Corrido

## Lyrics
### Full Lyrics
[Portuguese lyrics]

### Line-by-Line Meaning
| Portuguese | English |
|---|---|
| Line 1 | Translation 1 |

## Vocabulary
| Word | Meaning | Notes |
|---|---|---|
| ai | ah/oh | Exclamation |

[...more sections...]
```

### Output (HTML)
✨ Beautiful, styled HTML page with:
- Song title and metadata (type, difficulty, date)
- Formatted lyrics with English translation
- Pronunciation guide
- Interactive vocabulary table
- Grammar analysis with examples
- Cultural context
- Practice exercises
- Navigation buttons

### Automatic Features

1. **Title Detection** — Extracts song title from first `#` heading
2. **Metadata Extraction** — Reads date, type, status from "Basic Info" section
3. **Difficulty Estimation** — Estimates difficulty (1-5) based on content length
4. **Table Conversion** — Converts Markdown tables to styled HTML tables
5. **Section Organization** — Automatically structures all sections with proper headings
6. **Styling** — Applies consistent CSS with:
   - Purple gradient background
   - Color-coded difficulty badges
   - Responsive tables
   - Mobile-friendly layout

---

## Usage Examples

### Scenario 1: You Just Got a New Song from Perplexity

```bash
# 1. Save the song as Markdown: songs/song-new-song.md
# 2. Run the converter:
python utils/song_md_to_html_converter.py --file song-new-song.md
# 3. Check app/new-song.html ✓
```

### Scenario 2: You Have 10 New Songs to Add

```bash
# Run once for all files:
python utils/song_md_to_html_converter.py

# Output:
# Converting: song-1.md... ✓ song-1.html
# Converting: song-2.md... ✓ song-2.html
# [etc.]
# ✓ Successfully converted 10/10 files
```

### Scenario 3: You're Adding Songs Throughout the Week

```bash
# Start watch mode in background:
python utils/song_md_to_html_converter.py --watch

# Output:
# Watching /path/to/songs for new songs (Ctrl+C to stop)...
# [14:32:15] Converting: song-new.md... ✓ song-new.html
# [14:35:22] Converting: song-another.md... ✓ song-another.html
```

---

## Requirements

- **Python 3.7+** (no external dependencies required)
- Read/write access to `songs/` and `app/` folders

The script uses only Python's standard library (`os`, `re`, `sys`, `glob`, `pathlib`, `datetime`, `time`).

---

## Troubleshooting

### "No song files found"
- Check that files are named `song-*.md` (starting with `song-`)
- Verify path: files should be in `Capoeira_Portuguese_Claude/songs/`

### "File not found: filename.md"
- Use the exact filename (e.g., `song-ai-ai-aide.md`, not `ai-ai-aide.md`)

### HTML file not generated
- Check that the Markdown file has a `# Title` heading
- Ensure file is readable and contains valid sections

### Formatting looks wrong
- Verify Markdown tables use `|` separators correctly
- Check that sections use exact heading format: `## Section Name`

---

## Advanced: Customizing Output

To modify HTML styling or structure, edit these sections in `md_to_html_converter.py`:

1. **CSS Styling** — Search for `<style>` tag in `_generate_html_template()`
2. **HTML Layout** — Modify the template string after `html = f"""`
3. **Difficulty Colors** — Edit `_get_difficulty_bg()` and `_get_difficulty_text()`

---

## Next Steps

1. **Run converter:** `python utils/song_md_to_html_converter.py`
2. **Check output:** Open `app/song-name.html` in browser
3. **Update landing page:** Add link to `poc.html` if needed
4. **Use watch mode:** For continuous additions

---

## Questions?

If the script isn't working as expected:
- Check the song Markdown file format (compare with `songs/song-ai-ai-aide.md`)
- Run with a single file first: `python utils/song_md_to_html_converter.py --file song-test.md`
- Check terminal output for error messages

