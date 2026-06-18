# ✅ Song Lesson Markdown Checklist for Perplexity

**Use this checklist BEFORE submitting your song lesson markdown to ensure it will convert correctly to HTML.**

---

## 📋 Required Sections (in this order)

### 1. Title
```markdown
# Song Title (Ee Maré / Full Name)
```
- [ ] Use `#` (H1) for the song title
- [ ] Include alternate names in parentheses if applicable

### 2. Basic Info
```markdown
## Basic Info
- Date added: 2026-06-17
- Status: In Study
- Source: Traditional / Artist Name
- Type: Corrido (or Ladainha, Samba, etc.)
```
- [ ] Include all four fields (Date, Status, Source, Type)
- [ ] Use bullet points with dashes

### 3. Media Links
```markdown
## Media Links

### YouTube
- [Description](https://youtube.com/...)
- [Another link](https://youtube.com/...)

### Spotify
- Search: "Song Name capoeira"

### Apple Music
- Search: "Song Name capoeira"

### YouTube Music
- Search: "Song Name capoeira"
```
- [ ] Include YouTube section with actual links
- [ ] Include Spotify section (can be search instructions)
- [ ] Optional: Apple Music and YouTube Music sections
- [ ] Use markdown link format: `[text](url)`

### 4. Lyrics
```markdown
## Lyrics

### Full Lyrics

Ie!
Ee mare, ee da beira mar
[... rest of lyrics, one line per line ...]

### Line-by-line Meaning

| Portuguese | English |
|---|---|
| Ie! | Hey! |
| Ee mare, ee da beira mar | Hey tide, hey from shore |
| [etc.] | [etc.] |
```
- [ ] Section header: `## Lyrics`
- [ ] Subsection: `### Full Lyrics` (exactly this name)
- [ ] Subsection: `### Line-by-line Meaning` or `### Line-by-Line Meaning` (both work)
- [ ] Full lyrics as plain text (one line per lyric line)
- [ ] Translation table with pipe separators `|...|...|`
- [ ] Table separator row: `|---|---|`
- [ ] **CRITICAL:** Exactly two columns: Portuguese | English

### 5. Pronunciation
```markdown
## Pronunciation

| Phrase | Pronunciation Help |
|---|---|
| Ie | ee-EH |
| Ee mare | ee mah-REH |
| [etc.] | [etc.] |

**Optional tips:** Explain any special sounds...
```
- [ ] Section header: `## Pronunciation`
- [ ] Pronunciation table with pipe separators
- [ ] Table format: | Phrase | Pronunciation Help |
- [ ] Table separator: `|---|---|`
- [ ] Optional: Additional pronunciation tips after the table

### 6. Vocabulary
```markdown
## Vocabulary

| Word / Phrase | Meaning | Notes |
|---|---|---|
| ie | hey | Traditional Capoeira exclamation |
| mare | tide | Feminine noun |
| [etc.] | [etc.] | [etc.] |
```
- [ ] Section header: `## Vocabulary`
- [ ] Vocabulary table with three columns: Word | Meaning | Notes
- [ ] **EVERY SINGLE WORD** from the song must be included
- [ ] Include nouns, verbs, adjectives, prepositions, articles, contractions
- [ ] Notes should specify: gender (if noun), verb tense, or context
- [ ] Table separator: `|---|---|---|`

### 7. Grammar
```markdown
## Grammar Notes

### 1. Verb Forms

| Form in song | Base verb | Tense | Meaning | Notes |
|---|---|---|---|---|
| subiu | subir | Preterite | rose | 3rd person singular |
| [etc.] | [etc.] | [etc.] | [etc.] | [etc.] |

### 2. Sentence Patterns

| Pattern | Explanation | Example from song | New example |
|---|---|---|---|
| Subject + ta + adj. | Describes state | "A mare ta cheia" | "O mar ta calmo" |
| [etc.] | [etc.] | [etc.] | [etc.] |

### 3. Pronouns and Subject Omission

| Item | Explanation | Example | Notes |
|---|---|---|---|
| ella | She/It | "Ella te chama" | Refers to "a mare" |
| [etc.] | [etc.] | [etc.] | [etc.] |

### 4. Repetition and Chorus Structure

| Feature | Explanation | Example |
|---|---|---|
| Call-and-response | Lead sings, group responds | Lead: "A mare ta cheia" — Group: "Ie, mare" |
| [etc.] | [etc.] | [etc.] |

### 5. Poetic / Traditional / Informal Language

| Expression | Literal | Functional | Notes |
|---|---|---|---|
| Ie! | Hey! | Battle cry, opening shout | African-rooted |
| ta | is | Colloquial "está" | Everyday Brazilian speech |
| [etc.] | [etc.] | [etc.] | [etc.] |

### 6. Grammar Questions

- Why is "ta" used instead of "está"?
- Why does "cheia" end in "-a"?
- [etc.]
```
- [ ] Header: `## Grammar Notes` (or `## Grammar`, both work)
- [ ] At least 5 subsections numbered: `### 1.`, `### 2.`, etc.
- [ ] Most subsections should have tables (not text)
- [ ] Last subsection (6) can be questions
- [ ] Tables have proper pipe separators and headers

### 8. Cultural Notes
```markdown
## Cultural Notes

- "Ie Mare" is one of the oldest corridos in Capoeira...
- The "Ie!" exclamation is rooted in African traditions...
- [etc.]
```
- [ ] Section header: `## Cultural Notes`
- [ ] Bullet points with `-`
- [ ] At least 3-4 cultural/historical points
- [ ] Explain historical significance, spiritual meaning, or tradition

### 9. Repeated Expressions / Chorus
```markdown
## Repeated Expressions / Chorus

- **"Ee mare, ee da beira mar"** — the anchor line, most recognizable phrase
- **"Ie, mare"** — universal response after each verse
- **"Ie!"** — restart signal after the full stop
- [etc.]
```
- [ ] Section header: `## Repeated Expressions / Chorus`
- [ ] List of repeated phrases with explanations
- [ ] Format: **"phrase"** — explanation

### 10. Practice
```markdown
## Practice

1. Write 2 new sentences using "ta + gerund": e.g., "O menino ta correndo"
2. Identify the tense of "subiu" and "desceu" — why are these past?
3. Reuse "no meio do" in a new sentence
4. Recite or sing the anchor line slowly
```
- [ ] Section header: `## Practice`
- [ ] Numbered list (1., 2., 3., 4.)
- [ ] At least 4 practice exercises
- [ ] Exercises should ONLY use vocabulary already taught in the Vocabulary section
- [ ] Include: writing sentences, identifying verbs, reciting, reusing structures

---

## 📊 Table Format — CRITICAL

All tables must follow this exact format:

```markdown
| Column 1 | Column 2 | Column 3 |
|---|---|---|
| Cell | Cell | Cell |
| Cell | Cell | Cell |
```

### Rules:
- [ ] Use pipe characters `|` to separate columns
- [ ] First row is the header
- [ ] Second row is the separator: `|---|---|---|`
- [ ] Each row must have the same number of pipes
- [ ] No extra spaces that break alignment (spaces inside cells are fine)

### Common Table Mistakes to AVOID:
- ❌ Mismatched column counts per row
- ❌ Missing or malformed separator row
- ❌ Inconsistent pipe placement
- ❌ Empty cells without spacing

---

## ✨ Best Practices

1. **Copy an existing song as a template** (e.g., `song-ai-ai-aide.md`)
   - This ensures you get the exact format right
   - Modify content, keep structure

2. **Keep vocabulary complete**
   - Include EVERY word from the lyrics
   - Include articles (o, a, um, uma)
   - Include prepositions (em, de, pra, na)
   - Include contractions (tá, pra, na)
   - Include conjunctions (e, ou)

3. **Make grammar tables practical**
   - Show real examples from the song
   - Include new examples using same vocabulary
   - Explain BOTH why the grammar matters AND how it works

4. **Cultural notes should tell a story**
   - Where did this song come from?
   - Who uses it and why?
   - What does it mean spiritually/historically?
   - Why is it important in Capoeira?

5. **Practice exercises should build skills**
   - Ask learners to write sentences
   - Ask them to identify verb forms
   - Ask them to reuse patterns
   - Make them recite/sing the song

---

## 🔍 Final Checklist Before Submitting

Run this before you submit your markdown:

```bash
# Check file size (should be 8000+ bytes)
wc -c song-name.md

# Check for balanced brackets
grep -o '\[' song-name.md | wc -l  # Should match:
grep -o '\]' song-name.md | wc -l

# Count tables (should have 8+)
grep -c '|' song-name.md

# Check for all major sections
grep '## ' song-name.md
```

### Requirements:
- [ ] File is at least 8000 bytes
- [ ] All brackets match
- [ ] At least 100 pipe characters (tables)
- [ ] All 10 major sections present

---

## 📧 Submission Template for Perplexity

When asking Perplexity to generate a song lesson, use this:

```
Please create a comprehensive song lesson for [SONG TITLE] using the Song Lesson Markdown Checklist.

Follow this structure exactly:
1. H1 title with song name
2. Basic Info (Date, Status, Source, Type)
3. Media Links (YouTube, Spotify, etc.)
4. Lyrics (Full Lyrics + Line-by-line Meaning table)
5. Pronunciation table
6. Vocabulary table (INCLUDE EVERY WORD)
7. Grammar Notes with 6 subsections (mostly tables)
8. Cultural Notes (bullet points)
9. Repeated Expressions / Chorus
10. Practice exercises (4+ numbered items)

Use markdown tables (|---|---|) for all structured data.
Assume the learner knows ZERO Portuguese.
Include ONLY vocabulary already taught in examples.

Reference: [Link to checklist]
```

---

## ❌ Common Errors to Avoid

1. **Missing words in vocabulary table**
   - Every word matters, even articles and prepositions
   
2. **Wrong section names**
   - Use exact names: "Line-by-line Meaning" (not "Translation")
   - Use "## Grammar Notes" (preferred) or "## Grammar"
   
3. **Table formatting issues**
   - Mismatched pipes per row
   - Missing separator row (|---|---|)
   
4. **Incomplete grammar section**
   - Need at least 5 subsections
   - Most should include tables with examples
   
5. **Practice exercises using unknown words**
   - Only use words from vocabulary table
   - If you need new words, teach them first
   
6. **Missing cultural context**
   - Don't skip cultural notes!
   - This is what makes Capoeira songs meaningful

---

## ✅ Quality Checklist

Before submitting to conversion, verify:

- [ ] Title is clear and complete
- [ ] All 10 sections present
- [ ] All tables properly formatted
- [ ] Every word in song is in vocabulary table
- [ ] Grammar section has 5+ subsections
- [ ] Cultural notes are 3+ bullet points
- [ ] Practice has 4+ exercises
- [ ] No practice exercises use untaght vocabulary
- [ ] File is 8000+ bytes
- [ ] No spelling errors in section headers

---

## 🚀 Ready to Submit

Once you've checked everything above, the markdown file is ready to convert to HTML using:

```bash
python utils/song_md_to_html_converter.py --file song-name.md
```

The generated HTML will automatically be added to `/app/` and ready for your learning platform!

