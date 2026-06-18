# 🤖 Perplexity AI Validation & Auto-Fix Prompt

**Use this prompt AFTER Perplexity generates a song lesson markdown.**

This prompt asks the AI to automatically validate the markdown against the checklist and fix any issues it finds.

---

## 📋 How to Use This

1. Perplexity generates the initial markdown (using PERPLEXITY_SONG_CREATION_GUIDE.md)
2. Copy your generated markdown
3. **Paste this entire validation prompt into Perplexity**
4. Perplexity will validate and auto-fix
5. Get back a corrected, validated markdown ready for conversion

---

## 🔧 Validation & Auto-Fix Prompt

**Copy everything below and paste into Perplexity after it generates the markdown:**

```
I need you to validate and auto-fix the song lesson markdown I just created.

TASK: 
1. Check the markdown against ALL requirements in SONG_MARKDOWN_VALIDATION.md
2. AUTO-FIX any issues you find
3. Return the corrected markdown

VALIDATION REQUIREMENTS:

✓ Section 1: Title
  - H1 heading with song name
  - Alternate names in parentheses

✓ Section 2: Basic Info
  - Header: ## Basic Info
  - 4 fields: Date, Status, Source, Type

✓ Section 3: Media Links
  - Header: ## Media Links
  - ### YouTube with links
  - ### Spotify section
  - Links in format: [text](url)
  - At least 3 total media sources
  - **QUALITY CHECK:** Links are to TRADITIONAL/AUTHENTIC versions ONLY
    - ✓ Traditional capoeira groups, mestres, Angola recordings
    - ✓ Educational/teaching versions
    - ✗ NO remixes, electronic versions, or pop covers
  - If any remix/non-authentic links found: REPLACE with traditional versions

✓ Section 4: Lyrics
  - Header: ## Lyrics
  - ### Full Lyrics subsection (plain text)
  - ### Line-by-line Meaning (or Line-by-Line Meaning)
  - Translation table with exactly 2 columns: Portuguese | English
  - Table separator: |---|---|
  - Every lyric has translation

✓ Section 5: Pronunciation
  - Header: ## Pronunciation
  - Table with 2 columns: Phrase | Pronunciation Help
  - Simplified pronunciation (not IPA)
  - Table separator: |---|---|

✓ Section 6: Vocabulary
  - Header: ## Vocabulary
  - Table with 3 columns: Word / Phrase | Meaning | Notes
  - Table separator: |---|---|---|
  - **CRITICAL: EVERY SINGLE WORD from lyrics included**
  - Notes specify gender for nouns, tense for verbs
  - At least 40-60 entries

✓ Section 7: Grammar
  - Header: ## Grammar Notes (or Grammar)
  - AT LEAST 6 subsections: ### 1. , ### 2. , etc.
  - Subsections 1-5 are tables
  - Subsection 6 is questions
  - Examples from actual song lyrics
  - New examples use ONLY taught vocabulary

✓ Section 8: Cultural Notes
  - Header: ## Cultural Notes
  - 3-5 bullet points with dashes
  - Covers history, significance, tradition

✓ Section 9: Repeated Expressions
  - Header: ## Repeated Expressions / Chorus
  - 3-4 repeated phrases
  - Format: **"phrase"** — explanation

✓ Section 10: Practice
  - Header: ## Practice
  - 4+ numbered exercises (1. , 2. , 3. , 4. )
  - Mix of writing, identification, recitation
  - **ONLY uses taught vocabulary**

✓ Table Format
  - All tables use pipes |
  - Proper separators: |---|---|
  - Same number of pipes per row
  - Headers in first row

✓ Overall Quality
  - File 8000-15000 bytes
  - All brackets [ ] matched
  - All parentheses ( ) matched
  - No spelling errors in headers
  - Section names exact match

VALIDATION PROCESS:
1. Go through each section
2. Check it against the requirements above
3. If ANY requirement is missing or wrong, AUTO-FIX it
4. Do NOT ask me for confirmation
5. Just fix it and provide the corrected markdown

FIXES TO MAKE (if found):

If missing ### Full Lyrics:
- Add it with the complete song lyrics

If translation table wrong:
- Ensure exactly 2 columns: Portuguese | English
- Fix table separator: |---|---|
- Add translation for every lyric line

If vocabulary incomplete:
- Add EVERY word from lyrics
- Add gender for nouns
- Add tense for verbs
- Aim for 40-60 total words

If grammar has fewer than 6 subsections:
- Add missing subsections
- Make them numbered: ### 1. , ### 2. , etc.
- Ensure subsections 1-5 are tables

If tables malformed:
- Count pipes - make sure they match per row
- Add separators if missing: |---|---|
- Remove any empty cells (use - if needed)

If file too small (<8000 bytes):
- Expand sections with more detail
- Add more cultural notes
- Add more practice exercises

If new examples use unknown vocabulary:
- Replace with examples using ONLY taught words
- Or teach the new word in-line: *word (meaning)*

OUTPUT FORMAT:

Provide:
1. A brief summary of issues found (or "No issues found ✓")
2. The COMPLETE corrected markdown file
3. Confirmation: "VALIDATION COMPLETE - Ready for conversion ✓"

START VALIDATION NOW:

[Paste your markdown below this line]
```

---

## 📤 How to Submit Your Markdown to Perplexity

### Step 1: Generate the Initial Markdown
Ask Perplexity:
```
Please create a song lesson for [SONG NAME] following the 
PERPLEXITY_SONG_CREATION_GUIDE.md completely.

[Include all requirements]
```

### Step 2: Copy the Generated Markdown
- Copy everything Perplexity provided
- Select all (Ctrl+A / Cmd+A)
- Copy (Ctrl+C / Cmd+C)

### Step 3: Ask for Validation
Paste the validation prompt above (the entire thing) into a new Perplexity message, then:
- Paste your markdown at the end

### Step 4: Let AI Auto-Fix
Perplexity will:
- ✓ Check all 10 sections
- ✓ Validate all tables
- ✓ Ensure all words in vocabulary
- ✓ Fix any issues found
- ✓ Return corrected markdown

### Step 5: Get Result
Perplexity returns:
- Summary of issues found
- Complete, corrected markdown
- "VALIDATION COMPLETE - Ready for conversion ✓"

---

## ✅ What Gets Auto-Fixed

| Issue | Auto-Fix |
|-------|----------|
| Missing section | Adds it with appropriate content |
| Wrong section name | Fixes to correct name |
| Table malformed | Fixes pipes, separators, alignment |
| Incomplete vocabulary | Adds missing words with notes |
| Few grammar subsections | Adds missing subsections |
| New examples with unknown words | Replaces with taught vocabulary |
| File too small | Expands sections with detail |
| Pronunciation in IPA | Converts to simplified format |
| Missing translations | Adds English translations |

---

## 🎯 Success Criteria

After validation, your markdown should:
- ✓ All 10 sections present
- ✓ Every word from lyrics in vocabulary
- ✓ All tables properly formatted
- ✓ Grammar has 6 subsections
- ✓ File is 8000+ bytes
- ✓ No formatting errors
- ✓ Status: "VALIDATION COMPLETE - Ready for conversion"

---

## 📝 Example Workflow

### You ask Perplexity:
```
Please create a song lesson for "Bananeira" following the 
PERPLEXITY_SONG_CREATION_GUIDE.md completely.

Type: Corrido
Lyrics: [paste full lyrics]
Cultural significance: [brief context]
```

### Perplexity generates markdown

### You paste the validation prompt:
```
I need you to validate and auto-fix the song lesson markdown...

[Full validation prompt here]

[Paste your markdown below this line]
[Your generated markdown]
```

### Perplexity auto-validates and fixes:
```
ISSUES FOUND (2):
1. Missing ### Line-by-line Meaning subsection → ADDED
2. Vocabulary missing 5 words from lyrics → ADDED

[Complete corrected markdown...]

VALIDATION COMPLETE - Ready for conversion ✓
```

### You get back:
✓ Validated markdown  
✓ All issues fixed automatically  
✓ Ready for immediate conversion  

---

## 🚀 This Eliminates Manual Validation

**No more:**
- ❌ Manual checking sections
- ❌ Manual fixing formatting
- ❌ Back-and-forth corrections
- ❌ Multiple tries to get it right

**You get:**
- ✓ One-pass creation
- ✓ Automatic validation
- ✓ Automatic fixes
- ✓ Ready-to-convert markdown

**Total time:** ~10 minutes for validated, perfect markdown!

---

## 💡 Pro Tips

### If Validation Finds Many Issues:
- Perplexity will fix them all
- Review the summary to understand what was wrong
- Use that knowledge for next songs

### If "VALIDATION COMPLETE" with Zero Issues:
- Congratulations! Perplexity nailed it
- Skip straight to local conversion

### If Validation Still Misses Something:
- Python validator on local side will catch it
- Double safety net!

---

## 🔗 Integration with Local Workflow

1. **Perplexity:** Create + Auto-validate + Fix markdown
2. **Local:** Run Python validator (catches anything missed)
3. **Local:** Convert to HTML
4. **Local:** Integrate + Deploy

Two layers of validation = perfect output!

