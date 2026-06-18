# Song Lesson Creation Workflow

Complete workflow for creating, validating, and converting song lesson markdown files to HTML for the Capoeira Portuguese Learning app.

---

## 📋 Overview

```
1. PLAN
   └─ Choose song, gather info

2. CREATE (in Perplexity)
   └─ Generate markdown using checklist

3. VALIDATE (locally)
   └─ Check format and completeness

4. FIX (if needed)
   └─ Correct any issues

5. CONVERT
   └─ Generate HTML file

6. INTEGRATE
   └─ Add to landing page

7. DEPLOY
   └─ Sync to backup
```

---

## Step 1: PLAN — Choose Your Song

### Before you start:
- [ ] Song exists in Capoeira tradition (Angola or Regional)
- [ ] Lyrics are available and authentic
- [ ] You understand the cultural/historical context
- [ ] Song is appropriate for beginner learners

### Information to gather:
- Portuguese title and any alternate names
- English translation
- Song type (Corrido, Ladainha, etc.)
- Media sources (YouTube, Spotify links if available)
- Cultural history and significance
- 5+ media links minimum

### Good starting songs:
✓ "Santo Antônio Quero Água" — Level 1, very simple vocabulary
✓ "A Maré Tá Cheia" — Level 2, water/ocean imagery
✓ "Ai, Ai, Aidê" — Level 3, classic call-and-response
✓ "Iê Maré" — Level 3, rhythmic complexity

---

## Step 2: CREATE — Generate Markdown in Perplexity

### Preparation (5 minutes)

1. **Copy the validation checklist** to your clipboard:
   - File: `VALIDATION_CHECKLIST_FOR_PERPLEXITY.md`
   - Share with Perplexity or paste in the prompt

2. **Prepare your prompt** for Perplexity

### Perplexity Prompt Template

```
I'm creating a comprehensive Brazilian Portuguese lesson from a Capoeira song.

SONG: [Song Title]
TYPE: [Corrido/Ladainha/etc.]

Please generate a complete song lesson markdown file following this exact structure:

[PASTE OR REFERENCE: VALIDATION_CHECKLIST_FOR_PERPLEXITY.md]

ADDITIONAL REQUIREMENTS:
- Assume learner knows ZERO Portuguese
- Include EVERY SINGLE WORD from lyrics in vocabulary table
- Use only taught vocabulary in examples
- Make grammar tables practical with real examples
- Include authentic cultural context

OUTPUT FORMAT:
Save as: song-[slugified-name].md
Structure: Follow all 10 sections from checklist
Quality: Pass all quality checks from checklist
```

### Perplexity Generation Tips

✓ **Be specific** — Reference exact section names from checklist
✓ **Provide lyrics** — Paste the song lyrics so Perplexity doesn't guess
✓ **Give context** — Explain why this song matters in Capoeira
✓ **Request completeness** — Ask for EVERY WORD explained
✓ **Verify accuracy** — Ask Perplexity to double-check Portuguese accuracy

### Example Prompt:

```
Please generate a song lesson for "Iê Maré" following the Song Lesson Markdown Checklist.

Song details:
- Portuguese: Iê Maré (also: Ee Maré, Ee da Beira Mar)
- Type: Corrido (call-and-response)
- Traditional Capoeira Angola song
- Famous for its "stop and restart" technique

Lyrics:
Ie!
Ee mare, ee da beira mar
[... full lyrics ...]

Follow the checklist structure exactly:
1. H1 title
2. Basic Info (Date, Status, Source, Type)
3. Media Links (YouTube, Spotify required)
4. Lyrics section with Full Lyrics + Line-by-line Meaning table
5. Pronunciation table
6. Vocabulary table (INCLUDE EVERY WORD - no exceptions)
7. Grammar Notes (6 subsections with tables)
8. Cultural Notes (3+ bullet points on history/significance)
9. Repeated Expressions / Chorus
10. Practice (4+ numbered exercises)

Use markdown tables (|---|---|) for all structured data.
```

### Expected Output
- Markdown file with `.md` extension
- Filename: `song-[name].md`
- Size: 8000-15000 bytes
- All 10 sections complete

---

## Step 3: VALIDATE — Check Format Locally

### Setup
```bash
# Navigate to project
cd /Users/lazarovitsbence/workspaces/Projects/Capoeira_Portuguese_Claude

# Save markdown file from Perplexity
# Place in: songs/song-name.md
```

### Run Validation

```bash
# Validate single file
python utils/validate_song_md.py songs/song-name.md

# Expected output format:
# ✓ VALID - File is compatible with HTML converter
# ❌ INVALID - File has compatibility issues
```

### What Gets Checked
- ✓ All 10 required sections present
- ✓ Section names are correct
- ✓ Markdown table formatting
- ✓ Brackets and parentheses balanced
- ✓ Media links exist
- ✓ File size adequate (8000+ bytes)
- ✓ Encoding valid (UTF-8)

### Read the Report
```
STATUS: READY FOR CONVERSION ✓
  ✓ All required sections
  ✓ Tables properly formatted
  ✓ 2 media links found

WARNINGS (non-critical):
  - Consider adding more cultural context
  - Line-by-line should have more entries
```

**If Status = READY FOR CONVERSION:** → Go to Step 5 (Convert)

**If Status = NEEDS FIXES:** → Go to Step 4 (Fix)

---

## Step 4: FIX — Correct Issues (if validation failed)

### Common Issues and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Missing section | Perplexity forgot section | Add manually or ask Perplexity to regenerate |
| Table formatting broken | Mismatched pipes `\|` | Count pipes per row, add missing pipes |
| Empty columns | Bad table structure | Ensure every cell has content (use `-` if empty) |
| Unmatched brackets | Typo in link | Find `[` without `]` and fix |
| File too small | Incomplete content | Ask Perplexity to expand sections |
| Wrong section name | Typo in header | Change `## Grammer` to `## Grammar` |

### Quick Fixes via Text Editor
1. Open file: `songs/song-name.md`
2. Use Find & Replace (Ctrl+H / Cmd+H)
3. Common fixes:
   - `## Grammer` → `## Grammar`
   - `### Line-by-Line` → `### Line-by-line` (or vice versa)
   - Add missing `|` to break table rows
4. Save file
5. Re-run validation: `python utils/validate_song_md.py songs/song-name.md`

### If Issues Persist
Ask Perplexity for corrections:

```
I have a song lesson markdown that needs fixing. 

Issues found:
- [List validation errors]

Please fix these sections:
1. [Section name] — [What's wrong]
2. [Section name] — [What's wrong]

Use the exact format from the Song Lesson Markdown Checklist.
Keep the rest of the content unchanged.
```

---

## Step 5: CONVERT — Generate HTML

### Run Conversion
```bash
# Convert specific file
python utils/song_md_to_html_converter.py --file song-name.md

# Expected output:
# Converting: song-name.md... ✓ song-name.html

# OR convert all new songs
python utils/song_md_to_html_converter.py

# Expected output:
# Found 3 song files. Converting...
# Converting: song-1.md... ✓ song-1.html
# Converting: song-2.md... ✓ song-2.html
# Converting: song-3.md... ✓ song-3.html
# ✓ Successfully converted 3/3 files
```

### Verify HTML Created
```bash
# Check that HTML file exists
ls -lh app/*.html | grep song-name

# Should show:
# -rw-r--r-- 1 user group 22K Jun 17 09:30 app/song-name.html
```

### Expected HTML Sections
The generated HTML should have:
- ✓ 🎵 Listen (Media Links)
- ✓ 📝 Lyrics (Full Lyrics + English Translation table)
- ✓ 🔊 Pronunciation (table)
- ✓ 📚 Vocabulary (table with all words)
- ✓ 📖 Grammar (all subsections with tables)
- ✓ 🌍 Cultural Context
- ✓ ✏️ Practice Exercises

---

## Step 6: INTEGRATE — Add to Landing Page

### Update Landing Page
File: `app/poc.html`

1. Open in text editor
2. Find the `<div class="song-grid">` section
3. Add new song card before the "coming soon" cards:

```html
<a href="song-name-slugified.html" class="song-card">
    <div class="song-title">Song Title</div>
    <div class="song-subtitle">English Translation</div>
    <div class="song-meta">
        <span class="song-badge">Corrido</span>
        <span class="song-badge">Level 2</span>
    </div>
</a>
```

### Example:
```html
<a href="ie-mare-ee-mare-ee-da-beira-mar.html" class="song-card">
    <div class="song-title">Iê Maré</div>
    <div class="song-subtitle">From the Seashore</div>
    <div class="song-meta">
        <span class="song-badge">Corrido</span>
        <span class="song-badge">Level 3</span>
    </div>
</a>
```

### Difficulty Levels
- **Level 1** — Beginner (few words, simple grammar)
- **Level 2** — Beginner+ (moderate vocabulary, common patterns)
- **Level 3** — Intermediate (complex structures, cultural depth)
- **Level 4** — Advanced (specialized vocabulary, intricate grammar)
- **Level 5** — Expert (challenging content, advanced nuances)

### Song Types
- **Corrido** — Call-and-response, rhythmic
- **Ladainha** — Long opening song, poetic
- **Samba** — Rhythmic, often slow
- **Jogo** — Game-like, interactive

---

## Step 7: DEPLOY — Sync Backups

### Backup Files
```bash
# Copy to template for backup
cp app/song-name.html _template/app/
cp songs/song-name.md _template/songs/
cp app/poc.html _template/app/
```

### Verify Backups
```bash
# Check files exist in both locations
ls -la songs/song-name.md _template/songs/song-name.md
ls -la app/song-name.html _template/app/song-name.html
```

### Optional: Commit to Version Control (if using Git)
```bash
git add songs/song-name.md app/song-name.html app/poc.html
git commit -m "Add song lesson: [Song Name]"
git push
```

---

## 📊 Complete Workflow Checklist

### Before Creating Song
- [ ] Song is from authentic Capoeira tradition
- [ ] Lyrics are accurate and authentic
- [ ] You've gathered cultural context
- [ ] You understand the song's significance

### During Perplexity Generation
- [ ] Shared validation checklist with Perplexity
- [ ] Provided complete, accurate lyrics
- [ ] Specified all 10 required sections
- [ ] Requested every word be explained
- [ ] Asked for authentic cultural context

### After Receiving Markdown
- [ ] Saved file as `songs/song-name.md`
- [ ] Ran validation: `python utils/validate_song_md.py`
- [ ] Status shows: "READY FOR CONVERSION"
- [ ] Fixed any errors if needed

### After Conversion
- [ ] HTML file generated: `app/song-name.html`
- [ ] All sections present in HTML
- [ ] File is 12-25KB in size
- [ ] Opened HTML in browser — looks good

### After Integration
- [ ] Added card to `app/poc.html`
- [ ] Landing page shows new song
- [ ] Clicking song card opens lesson
- [ ] All links and content work

### Final Deployment
- [ ] Copied HTML to `_template/app/`
- [ ] Copied markdown to `_template/songs/`
- [ ] Copied updated `poc.html` to `_template/app/`
- [ ] Committed changes (if using Git)

---

## ⏱️ Timeline

| Step | Time | Key Action |
|------|------|-----------|
| 1. Plan | 10 min | Gather song info |
| 2. Create | 5-10 min | Ask Perplexity (wait for response) |
| 3. Validate | 2 min | Run validation script |
| 4. Fix | 5-15 min | Correct issues (if any) |
| 5. Convert | 1 min | Run converter script |
| 6. Integrate | 3 min | Update landing page |
| 7. Deploy | 2 min | Backup files |
| **TOTAL** | **~30-45 min** | **One complete song** |

---

## 🚀 Quick Reference

### Commands You'll Use Most

```bash
# Validate a song
python utils/validate_song_md.py songs/song-name.md

# Convert a song
python utils/song_md_to_html_converter.py --file song-name.md

# Convert all songs
python utils/song_md_to_html_converter.py

# Watch for new songs (auto-convert)
python utils/song_md_to_html_converter.py --watch

# View validation checklist
python utils/validate_song_md.py --checklist
```

### Key Files

| File | Purpose | Location |
|------|---------|----------|
| VALIDATION_CHECKLIST_FOR_PERPLEXITY.md | Checklist for Perplexity | Root directory |
| validate_song_md.py | Validation script | utils/ |
| song_md_to_html_converter.py | Conversion script | utils/ |
| poc.html | Landing page (edit this) | app/ |
| song-*.md | Source markdown files | songs/ |
| *.html | Generated lesson pages | app/ |

---

## 🎓 Example: Full Workflow in Action

### You want to add "Bananeira" song

**Step 1-2: Plan & Create**
```bash
# Ask Perplexity:
# "Please create a song lesson for 'Bananeira' following VALIDATION_CHECKLIST_FOR_PERPLEXITY.md
#  Type: Corrido, Difficulty: Level 1, super beginner-friendly"

# Perplexity generates: song-bananeira.md
# Save to: songs/song-bananeira.md
```

**Step 3: Validate**
```bash
$ python utils/validate_song_md.py songs/song-bananeira.md

# Output:
# ======================================================================
# Song Markdown Validation Report: song-bananeira.md
# ======================================================================
# 
# ✓ VALID - File is compatible with HTML converter
# 
# ✓ All checks passed!
# 
# ======================================================================
# Status: READY FOR CONVERSION
# ======================================================================
```

**Step 5: Convert**
```bash
$ python utils/song_md_to_html_converter.py --file song-bananeira.md

# Output:
# Converting: song-bananeira.md... ✓ bananeira.html
```

**Step 6: Integrate**
Edit `app/poc.html`, add:
```html
<a href="bananeira.html" class="song-card">
    <div class="song-title">Bananeira</div>
    <div class="song-subtitle">Banana Tree</div>
    <div class="song-meta">
        <span class="song-badge">Corrido</span>
        <span class="song-badge">Level 1</span>
    </div>
</a>
```

**Step 7: Deploy**
```bash
cp songs/song-bananeira.md _template/songs/
cp app/bananeira.html _template/app/
cp app/poc.html _template/app/
```

✓ **Done!** Song is live in your app.

---

## 📝 Notes

- Always use validation before conversion — it catches errors early
- The checklist prevents 90% of conversion issues
- Keep markdown files as source of truth (backup regularly)
- HTML files are generated — don't edit them directly
- Template folder is your backup — sync after each song

---

## 🆘 Troubleshooting

**Validation fails with "Missing section"**
→ Check section name spelling against checklist

**HTML file is generated but looks incomplete**
→ Re-run validation on markdown, fix issues, re-convert

**Landing page doesn't show new song**
→ Check that HTML filename matches href in poc.html

**Perplexity generated song but it's incomplete**
→ Ask it to regenerate, reference checklist again

---

## Next Steps

1. **Choose your next song**
2. **Prepare Perplexity prompt** (reference this workflow)
3. **Generate markdown** in Perplexity
4. **Validate** locally
5. **Convert** to HTML
6. **Integrate** into app
7. **Deploy** backups

**Happy creating! 🥁**

