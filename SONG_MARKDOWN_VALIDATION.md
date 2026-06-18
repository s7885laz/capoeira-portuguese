# ✅ Song Markdown Validation Checklist

**Use this checklist to validate your markdown BEFORE submitting it.**

You can do this validation manually by checking each item below, or wait for the Python validator to check it automatically.

---

## 📋 Section 1: Title

- [ ] Has H1 heading (`#`)
- [ ] Includes full song name
- [ ] Includes alternate names in parentheses (if applicable)
- [ ] Example: `# Iê Maré (Ee Maré / Ee da Beira Mar)`

**Check:** Does your title look like the example above?

---

## 📋 Section 2: Basic Info

- [ ] Header is exactly `## Basic Info`
- [ ] Has 4 fields:
  - [ ] Date added: (format: YYYY-MM-DD)
  - [ ] Status: (either "In Study" or "Mastered")
  - [ ] Source: (Artist or "Traditional")
  - [ ] Type: (Corrido, Ladainha, Samba, etc.)
- [ ] Uses bullet points with dashes (`-`)
- [ ] No extra formatting

**Check:** Do you have all 4 fields listed exactly as above?

---

## 📋 Section 3: Media Links

- [ ] Header is exactly `## Media Links`
- [ ] Has `### YouTube` subsection (REQUIRED)
  - [ ] At least 1 link in format: `[Description](https://...)`
- [ ] Has `### Spotify` subsection (REQUIRED)
  - [ ] Either real link OR search instruction: `Search: "Song Name"`
- [ ] Optional: `### Apple Music` and `### YouTube Music`
- [ ] Links use proper markdown format: `[text](url)`
- [ ] At least 3 total media links/sections

**Check:** Do you have YouTube and Spotify? Are links in `[text](url)` format?

---

## 📋 Section 4: Lyrics

**Full Lyrics subsection:**
- [ ] Header is exactly `### Full Lyrics`
- [ ] Contains the complete song lyrics
- [ ] One lyric line per line (NOT in a table)
- [ ] Plain text format

**Line-by-line Meaning subsection:**
- [ ] Header is exactly `### Line-by-line Meaning` OR `### Line-by-Line Meaning`
- [ ] Is a markdown table
- [ ] Has exactly 2 columns: Portuguese | English
- [ ] Has table separator row: `|---|---|`
- [ ] Every lyric line has a translation
- [ ] Format example:
  ```
  | Portuguese | English |
  |---|---|
  | Ie! | Hey! |
  ```

**Check:** Do you have both subsections? Is the translation table properly formatted with 2 columns?

---

## 📋 Section 5: Pronunciation

- [ ] Header is exactly `## Pronunciation`
- [ ] Has markdown table with 2 columns: Phrase | Pronunciation Help
- [ ] Has table separator: `|---|---|`
- [ ] Pronunciation uses simplified format (not IPA)
  - Example: "mah-REH" NOT "mɑ̃ˈreɪ"
- [ ] Optional: Pronunciation tips after table in format: ***word** — explanation*

**Check:** Is the pronunciation table properly formatted? Is it simplified English pronunciation?

---

## 📋 Section 6: Vocabulary

- [ ] Header is exactly `## Vocabulary`
- [ ] Has markdown table with exactly 3 columns:
  - Word / Phrase | Meaning | Notes
- [ ] Has table separator: `|---|---|---|`
- [ ] **CRITICAL: Includes EVERY SINGLE WORD from the song**
  - [ ] Articles: o, a, um, uma
  - [ ] Prepositions: em, de, pra, na, no
  - [ ] Contractions: tá, pra, na
  - [ ] Conjunctions: e, ou
  - [ ] Verbs (infinitive and conjugated forms)
  - [ ] Nouns, adjectives, adverbs
- [ ] Notes include:
  - [ ] Gender for nouns (Masculine/Feminine)
  - [ ] Tense/form for verbs
  - [ ] Context or usage examples
- [ ] At least 40-60 vocabulary entries

**Check:** Does every single word from your lyrics appear in the vocabulary table? Do notes explain gender and verb tenses?

---

## 📋 Section 7: Grammar

- [ ] Header is exactly `## Grammar Notes` (or `## Grammar`)
- [ ] Has AT LEAST 5 numbered subsections: `### 1. `, `### 2. `, etc.
- [ ] Most subsections (1-5) are markdown tables
- [ ] Last subsection (6) has grammar questions

**Subsection 1: Verb Forms**
- [ ] Table with columns: Form | Base verb | Tense | Meaning | Notes
- [ ] Includes 5+ verb forms from song
- [ ] Notes explain tense and person

**Subsection 2: Sentence Patterns**
- [ ] Table with columns: Pattern | Explanation | Example from song | New example
- [ ] At least 3-4 patterns
- [ ] Examples directly from actual song
- [ ] New examples only use taught vocabulary

**Subsection 3: Pronouns and Subject Omission**
- [ ] Table with columns: Item | Explanation | Example | Notes
- [ ] Covers pronouns, subject omission
- [ ] Examples from song

**Subsection 4: Repetition and Chorus Structure**
- [ ] Table with columns: Feature | Explanation | Example
- [ ] Covers call-and-response, anchors, repeated phrases
- [ ] Examples from song

**Subsection 5: Poetic / Traditional / Informal Language**
- [ ] Table with columns: Expression | Literal | Functional | Notes
- [ ] Covers poetic/cultural language elements
- [ ] Examples from song

**Subsection 6: Grammar Questions**
- [ ] At least 3-4 questions
- [ ] Questions about grammar points in the song
- [ ] Format: `- Why...?` or `- What...?`

**Check:** Do you have 6 subsections? Are subsections 1-5 tables? Are all examples from the actual song? Do new examples only use taught vocabulary?

---

## 📋 Section 8: Cultural Notes

- [ ] Header is exactly `## Cultural Notes` (or `## Cultural Context`)
- [ ] Has 3-5 bullet points (5+ is better)
- [ ] Uses dash format: `- [content]`
- [ ] Covers:
  - [ ] Historical origin/tradition
  - [ ] Spiritual or cultural significance
  - [ ] Connection to Afro-Brazilian culture
  - [ ] Notable mestres or communities (if applicable)
  - [ ] Why this song matters in Capoeira

**Check:** Do you have 3+ bullet points? Does each explain something about the song's history or significance?

---

## 📋 Section 9: Repeated Expressions / Chorus

- [ ] Header is exactly `## Repeated Expressions / Chorus`
- [ ] Has 3-4+ repeated phrases listed
- [ ] Format: `- **"phrase"** — explanation`
- [ ] Explains function of each phrase (anchor, response, signal, etc.)

**Check:** Do you have the repeated phrases listed with explanations?

---

## 📋 Section 10: Practice

- [ ] Header is exactly `## Practice`
- [ ] Has 4+ numbered exercises: `1. `, `2. `, `3. `, `4. `
- [ ] Each exercise uses format: `[Number]. [Bold topic]: [instruction]`
  - Example: `1. **Write 2 new sentences** using "ta + gerund"`
- [ ] Exercises include mix of:
  - [ ] Writing exercises
  - [ ] Identification/analysis exercises
  - [ ] Recitation/singing exercises
- [ ] **CRITICAL: All exercises ONLY use vocabulary already taught**
  - [ ] No new words introduced
  - [ ] If new word needed, teach it: *word (meaning)*

**Check:** Do you have 4+ exercises? Do they only use taught vocabulary?

---

## 📊 Table Format Validation

Check ALL tables in your file:

For each table, verify:
- [ ] Uses pipe characters `|` to separate columns
- [ ] First row: column headers
- [ ] Second row: separator with dashes `|---|---| `
- [ ] All rows have same number of pipes
- [ ] No empty cells (use `-` if needed)
- [ ] Proper markdown format

**Example correct table:**
```markdown
| Column 1 | Column 2 |
|---|---|
| Data | Data |
| Data | Data |
```

**Check:** Count the pipes in each row — they should all match!

---

## 🔍 Overall Quality Checks

File Size:
- [ ] File is between 8,000-15,000 bytes (8-15 KB)
- [ ] Too small = incomplete
- [ ] Too large = over-detailed

Formatting:
- [ ] Brackets match: every `[` has `]`
- [ ] Parentheses match: every `(` has `)`
- [ ] No unmatched characters
- [ ] All section headers use correct format

Content:
- [ ] No spelling errors in section headers
- [ ] Section names match exactly (case-sensitive where noted)
- [ ] All tables properly formatted
- [ ] All 10 sections present

**Check:** Are all brackets/parentheses matched? Is the file the right size?

---

## ✅ Final Validation Summary

### All 10 Sections Present?
- [ ] Section 1: Title (H1)
- [ ] Section 2: Basic Info
- [ ] Section 3: Media Links
- [ ] Section 4: Lyrics
- [ ] Section 5: Pronunciation
- [ ] Section 6: Vocabulary
- [ ] Section 7: Grammar Notes
- [ ] Section 8: Cultural Notes
- [ ] Section 9: Repeated Expressions
- [ ] Section 10: Practice

### Critical Requirements Met?
- [ ] Every word from lyrics in vocabulary
- [ ] All tables properly formatted
- [ ] Grammar has 6 subsections
- [ ] File is 8000+ bytes
- [ ] All brackets/parentheses matched
- [ ] Only taught vocabulary in examples
- [ ] No formatting errors

### If ALL checks above are ✓:
**Your markdown is VALIDATED and ready for conversion!** ✅

### If ANY checks are ✗:
**Return to that section and fix the issue before submitting.**

---

## 🎯 What Happens Next

Once your markdown passes all these checks:

1. **Local Validation** — Python script automatically runs all these checks
2. **Conversion** — Markdown → HTML with all sections properly formatted
3. **Integration** — Added to landing page automatically
4. **Deployment** — Backed up and ready for use

Your validated markdown ensures perfect HTML conversion every time!

