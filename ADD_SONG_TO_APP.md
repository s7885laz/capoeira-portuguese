# Adding a Song to the App — Claude's Checklist

This is the step-by-step process Claude follows every time a new song lesson is added to the app. Run all 4 steps in order, every time, no exceptions.

**Prerequisite:** The song markdown file already exists in `songs/song-[name].md` before starting.

---

## Step 1: Validate the Song Markdown

Read the song markdown file and check it against the requirements in `SONG_MARKDOWN_VALIDATION.md`.

**Required sections (all 10 must be present):**
- `# Title`
- `## Basic Info`
- `## Media Links` (with `### YouTube` and `### Spotify` subsections)
- `## Lyrics` (with `### Full Lyrics` and `### Line-by-line Meaning`)
- `## Pronunciation`
- `## Vocabulary`
- `## Grammar Notes` (with 6 numbered subsections)
- `## Cultural Notes`
- `## Repeated Expressions`
- `## Practice`

**Critical quality checks:**
- File is 8,000–15,000 bytes
- Vocabulary table has at least 10 entries (aim for every word + key phrases)
- Grammar has exactly 6 subsections (last one must be grammar questions)
- No garbage rows in vocabulary (e.g. `| and | - |`)
- All markdown tables have matching pipe counts per row

**Fix any issues before proceeding to Step 2.**

---

## Step 2: Create the HTML Lesson Page

Create `app/[song-slug].html` by following the structure of an existing song page (e.g. `app/zum-zum-zum.html`).

**Filename convention:** `[song-slug].html` — use the same slug as the markdown file minus the `song-` prefix.
- `song-manda-leco-cajueiro.md` → `manda-leco-cajueiro.html`
- `song-zum-zum-zum.md` → `zum-zum-zum.html`

**The HTML page must include all of these sections:**
1. Header with song title and English subtitle
2. Meta bar: Type, Difficulty (1–5), Status, Date Added
3. 🎵 Listen — YouTube and Spotify links
4. 📝 Lyrics — full lyrics block + translation table
5. 🔊 Pronunciation — table + tips box
6. 📚 Vocabulary — full table from markdown
7. 📖 Grammar — all 6 subsections with tables; subsection 6 as a bullet list of questions
8. 🌍 Cultural Context — cultural notes as paragraphs
9. 🔁 Repeated Expressions — refrain box with bullet list
10. ✏️ Practice Exercises — numbered list
11. Navigation: ← Back to Home | Take Quiz →

**Style:** Copy the CSS from `zum-zum-zum.html` verbatim — do not invent new styles.

---

## Step 3: Add the Song Card to index.html

Open `app/index.html` and add a new `<a>` card inside the `<div class="song-grid">` section, before the "coming soon" placeholder card.

```html
<a href="[song-slug].html" class="song-card">
    <div class="song-title">[Portuguese Title]</div>
    <div class="song-subtitle">[English Translation]</div>
    <div class="song-meta">
        <span class="song-badge">[Type]</span>
        <span class="song-badge">Level [N]</span>
    </div>
</a>
```

**Difficulty levels:**
- Level 1 — very few unique words, simple repeating structure
- Level 2 — moderate vocabulary, common grammar patterns
- Level 3 — more complex structures or cultural depth
- Level 4 — advanced vocabulary, intricate grammar
- Level 5 — expert-level content

---

## Step 4: Update vocab-log.json

Open `progress/vocab-log.json` and add entries for words that are new to the log.

**Rules:**
- Add one entry per unique word (no duplicates)
- If the word already exists in the log, add the new song to its `source_content` array — do not create a second entry
- Only add words that genuinely teach something (skip pure chant syllables like *iê* or *ô* unless they have meaning worth teaching)
- Phrases count as entries if they appear as fixed units (e.g. `vou mandar`, `como vai`)

**Entry format:**
```json
{
  "word": "[Portuguese word or phrase]",
  "meaning": "[English meaning]",
  "part_of_speech": "[noun/verb/adjective/interjection/etc.]",
  "source_type": "song",
  "source_content": ["song-[name]"],
  "date_learned": null,
  "last_reviewed": null,
  "quiz_stats": {
    "times_asked": 0,
    "times_correct": 0,
    "times_wrong": 0,
    "success_rate": null
  },
  "mastery_level": "new"
}
```

**After updating**, confirm the total entry count increased by the expected number of new words.

---

## Completion Checklist

Before reporting done, verify:

- [ ] Markdown validated — all 10 sections present, no formatting errors
- [ ] `app/[song-slug].html` created with all 10 sections
- [ ] `app/index.html` updated — new song card visible in grid
- [ ] `progress/vocab-log.json` updated — new words added, existing words updated with new source
- [ ] HTML filename matches the `href` in the index card exactly

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---|---|
| Skipping vocab-log update | Always do Step 4 — the quiz system depends on it |
| Duplicate vocab entries | Check existing words before adding; update `source_content` instead |
| HTML slug doesn't match index href | Double-check both use the exact same filename |
| Referencing `poc.html` | The landing page is `index.html` — `poc.html` is outdated |
| Editing HTML directly without reading first | Always read the file before using Edit tool |
