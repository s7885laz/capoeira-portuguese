# 🔧 Local Workflow — Validation, Conversion, Integration & Deployment

**This workflow is for YOU (locally).** These are the steps you perform after Perplexity delivers a markdown file.

---

## 📌 Overview

```
1. RECEIVE markdown from Perplexity
   └─ Save to songs/song-name.md

2. VALIDATE (Python + Manual)
   └─ Run validation script
   └─ Check report for issues

3. CONVERT to HTML
   └─ Run conversion script
   └─ HTML generated in app/

4. INTEGRATE into app
   └─ Update landing page
   └─ Add song card with link

5. DEPLOY & BACKUP
   └─ Sync to _template/ folder
   └─ Backup complete
```

---

## Step 1: RECEIVE — Save Markdown File

### From Perplexity:
1. Copy the complete markdown from Perplexity
2. Save to file: `songs/song-name.md`
3. Use naming: `song-[lowercase-name].md`

### Example:
- Song: "Iê Maré" → filename: `song-ie-mare.md`
- Song: "Santo Antônio Quero Água" → filename: `song-santo-antonio-quero-agua.md`

---

## Step 2: VALIDATE — Check Markdown Quality

### Run Python Validation

```bash
# From project root directory
cd /Users/lazarovitsbence/workspaces/Projects/Capoeira_Portuguese_Claude

# Validate single file
python utils/validate_song_md.py songs/song-name.md

# OR validate all new songs
python utils/validate_song_md.py --report
```

### Expected Output

#### ✅ If Valid:
```
======================================================================
Song Markdown Validation Report: song-name.md
======================================================================

✓ VALID - File is compatible with HTML converter

✓ All checks passed!

======================================================================
Status: READY FOR CONVERSION
======================================================================
```

#### ❌ If Invalid:
```
======================================================================
Song Markdown Validation Report: song-name.md
======================================================================

✗ INVALID - File has compatibility issues

❌ ERRORS (3):
   1. Missing required section: ## Vocabulary
   2. Lyrics: Missing 'Line-by-line Meaning' table
   3. File too small (5000 bytes, expected 8000+)

⚠️  WARNINGS (2):
   1. Grammar section has fewer than 6 subsections
   2. Media Links: No HTTP links found

======================================================================
Status: NEEDS FIXES
======================================================================
```

### What the Validator Checks

✓ All 10 required sections present  
✓ Section names match exactly  
✓ Markdown tables properly formatted  
✓ File size adequate (8000+ bytes)  
✓ Balanced brackets and parentheses  
✓ Media links exist  
✓ Grammar has 6 subsections  
✓ UTF-8 encoding valid  

---

## Step 2b: FIX Issues (if validation failed)

### If Status = "NEEDS FIXES"

1. **Read the error messages** carefully
2. **Open the markdown file** in text editor
3. **Fix each issue:**

| Error | Solution |
|-------|----------|
| Missing section | Ask Perplexity to regenerate that section |
| Wrong section name | Use Find & Replace to fix (e.g., `## Grammer` → `## Grammar`) |
| Table formatting | Ensure all rows have same number of pipes `\|` |
| File too small | Ask Perplexity to expand/add more detail |
| Unmatched brackets | Find the typo and fix manually |

4. **Save the file**
5. **Re-run validation:** `python utils/validate_song_md.py songs/song-name.md`
6. **Repeat until:** Status = "READY FOR CONVERSION"

### Common Quick Fixes

```bash
# Before running validation, fix common issues:

# Fix case: "Line-by-Line" vs "Line-by-line"
# Open file, use Find & Replace

# Verify all sections exist:
grep "^## " songs/song-name.md

# Count table pipes (should be consistent per table):
grep "^|" songs/song-name.md | head -20
```

---

## Step 3: CONVERT — Generate HTML

### Prerequisites
- [ ] Validation status: "READY FOR CONVERSION" ✓
- [ ] No error messages from validator

### Run Conversion

```bash
# Convert specific file
python utils/song_md_to_html_converter.py --file song-name.md

# Expected output:
# Converting: song-name.md... ✓ song-name.html

# OR convert all songs
python utils/song_md_to_html_converter.py

# Expected output:
# Found 3 song files. Converting...
# Converting: song-1.md... ✓ song-1.html
# Converting: song-2.md... ✓ song-2.html
# Converting: song-3.md... ✓ song-3.html
# ✓ Successfully converted 3/3 files
```

### Verify HTML Generated

```bash
# Check that HTML file was created
ls -lh app/*.html | grep song-name

# Should show something like:
# -rw-r--r-- 1 user staff 22K Jun 17 app/song-name.html

# Open in browser to spot-check
open app/song-name.html
```

### Expected HTML Quality

The HTML should have:
- ✓ Song title and metadata
- ✓ 🎵 Listen section (Media Links with buttons)
- ✓ 📝 Lyrics (Full + English Translation table)
- ✓ 🔊 Pronunciation (table)
- ✓ 📚 Vocabulary (table with all words)
- ✓ 📖 Grammar (6 subsections with tables)
- ✓ 🌍 Cultural Context (paragraphs)
- ✓ Repeated Expressions / Chorus
- ✓ ✏️ Practice Exercises
- ✓ Navigation buttons

### File Size Check

```bash
# HTML file should be 12-25 KB
ls -lh app/song-name.html

# If much smaller, conversion may have failed
# If much larger, content may be duplicated
```

---

## Step 4: INTEGRATE — Add to Landing Page

### Edit Landing Page

File to edit: `app/poc.html`

1. Open `app/poc.html` in text editor
2. Find the section: `<div class="song-grid">`
3. Add new song card before "coming soon" cards

### Song Card Template

```html
<a href="FILENAME.html" class="song-card">
    <div class="song-title">Song Title</div>
    <div class="song-subtitle">English Subtitle</div>
    <div class="song-meta">
        <span class="song-badge">Type</span>
        <span class="song-badge">Level X</span>
    </div>
</a>
```

### Fill in Details

- **FILENAME.html** — Exact filename from conversion (e.g., `ie-mare.html`)
- **Song Title** — Portuguese name
- **English Subtitle** — English translation
- **Type** — Corrido, Ladainha, Samba, etc.
- **Level X** — Difficulty 1-5

### Example

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

### Difficulty Level Guidelines

| Level | Description | Examples |
|-------|-------------|----------|
| **1** | Beginner | Few words, simple grammar, 1-2 grammar tables |
| **2** | Beginner+ | Moderate vocabulary, common patterns, 3-4 tables |
| **3** | Intermediate | Complex structures, cultural depth, 5-6 tables |
| **4** | Advanced | Specialized vocabulary, intricate grammar |
| **5** | Expert | Very challenging, advanced nuances |

### Placement Order

Place songs in order:
1. **Level 1** songs first
2. Then Level 2, Level 3, etc.
3. "Coming soon" cards at the end

---

## Step 5: DEPLOY & BACKUP

### Backup Markdown File

```bash
# Copy to template for version control/backup
cp songs/song-name.md _template/songs/
```

### Backup HTML File

```bash
# Copy to template
cp app/song-name.html _template/app/
```

### Backup Updated Landing Page

```bash
# Copy updated landing page
cp app/poc.html _template/app/
```

### Verify All Backups

```bash
# Verify files exist in both locations
ls -la songs/song-name.md _template/songs/song-name.md
ls -la app/song-name.html _template/app/song-name.html
ls -la app/poc.html _template/app/poc.html
```

### Optional: Git Commit (if using version control)

```bash
# Stage files
git add songs/song-name.md
git add app/song-name.html
git add app/poc.html

# Commit with message
git commit -m "Add song lesson: Song Name"

# Push to remote
git push
```

---

## 📊 Complete Workflow Checklist

### Step 1: Receive
- [ ] Markdown file received from Perplexity
- [ ] Saved as: `songs/song-name.md`
- [ ] Filename format: `song-[name].md`

### Step 2: Validate
- [ ] Run: `python utils/validate_song_md.py songs/song-name.md`
- [ ] Status: "READY FOR CONVERSION" ✓
- [ ] No error messages
- [ ] Fixed any issues if needed

### Step 3: Convert
- [ ] Run: `python utils/song_md_to_html_converter.py --file song-name.md`
- [ ] HTML file generated: `app/song-name.html`
- [ ] File size: 12-25 KB
- [ ] Opened in browser — looks complete

### Step 4: Integrate
- [ ] Opened: `app/poc.html`
- [ ] Added song card with correct href
- [ ] Added title, subtitle, type, level
- [ ] Placed in correct position (by level)
- [ ] Saved file

### Step 5: Deploy
- [ ] Backed up: `songs/song-name.md` → `_template/songs/`
- [ ] Backed up: `app/song-name.html` → `_template/app/`
- [ ] Backed up: `app/poc.html` → `_template/app/`
- [ ] (Optional) Committed to Git

### Final Check
- [ ] Landing page shows new song
- [ ] Clicking song card opens lesson
- [ ] All sections display correctly
- [ ] All links work
- [ ] Grammar tables render properly
- [ ] Vocabulary table complete

---

## ⏱️ Timeline

| Step | Time | Task |
|------|------|------|
| 1. Receive | 2 min | Save file |
| 2. Validate | 1 min | Run script, check report |
| 2b. Fix (if needed) | 5-15 min | Correct issues |
| 3. Convert | 1 min | Run converter |
| 4. Integrate | 5 min | Update landing page |
| 5. Deploy | 2 min | Backup files |
| **TOTAL** | **15-25 min** | **Complete process** |

---

## 🚀 Quick Reference Commands

```bash
# All commands from project root directory:
cd /Users/lazarovitsbence/workspaces/Projects/Capoeira_Portuguese_Claude

# VALIDATE
python utils/validate_song_md.py songs/song-name.md

# CONVERT
python utils/song_md_to_html_converter.py --file song-name.md

# CONVERT ALL
python utils/song_md_to_html_converter.py

# WATCH FOR NEW SONGS (auto-convert)
python utils/song_md_to_html_converter.py --watch

# VERIFY FILES EXIST
ls -lh app/song-name.html
ls -lh songs/song-name.md
```

---

## 📂 File Organization

### After Complete Workflow:

```
Capoeira_Portuguese_Claude/
├── songs/
│   ├── song-ie-mare.md              ← Source markdown
│   ├── song-santo-antonio.md
│   └── [other songs].md
│
├── app/
│   ├── poc.html                     ← Updated landing page
│   ├── ie-mare.html                 ← Generated HTML lesson
│   ├── santo-antonio.html
│   └── [other lessons].html
│
├── _template/
│   ├── songs/
│   │   ├── song-ie-mare.md          ← Backup
│   │   └── [etc.]
│   └── app/
│       ├── poc.html                 ← Backup
│       ├── ie-mare.html             ← Backup
│       └── [etc.]
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Validation fails | Read error message, fix issue, re-run validator |
| HTML not generated | Check validation passed, check filename spelling |
| HTML looks incomplete | Check for errors in validation, regenerate |
| Song not showing on landing page | Check HTML filename matches href in poc.html |
| Links in HTML don't work | Check Media Links section in markdown |
| Tables look broken in HTML | Validate markdown table format, re-convert |

---

## ✅ Success Indicators

You've completed the workflow when:

✓ Validation status: "READY FOR CONVERSION"  
✓ HTML file created (12-25 KB)  
✓ Landing page updated with song card  
✓ Song card link works  
✓ HTML lesson displays all sections  
✓ Files backed up in _template/  
✓ All changes saved  

**Song is now live in your app!** 🥁

