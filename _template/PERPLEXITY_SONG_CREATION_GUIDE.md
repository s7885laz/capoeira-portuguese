# 🎵 Perplexity Song Lesson Creation Guide

**This guide is FOR Perplexity.** Follow these steps to create high-quality, conversion-ready song lesson markdown files.

---

## 📌 Your Task

Create a comprehensive Brazilian Portuguese song lesson markdown file for a Capoeira song that:
1. ✅ Follows the exact structure in the checklist
2. ✅ Includes every word from the song in vocabulary
3. ✅ Passes the validation checklist
4. ✅ Is ready for automatic HTML conversion

**Goal:** Generate markdown that converts perfectly to HTML with zero errors.

---

## ✅ Pre-Generation Checklist

Before you start writing, confirm:
- [ ] You have the authentic Portuguese lyrics for the song
- [ ] You understand the song's cultural/historical significance
- [ ] You know the song type (Corrido, Ladainha, etc.)
- [ ] You can find 3+ media links (YouTube, Spotify, etc.)
- [ ] You understand basic Portuguese grammar

---

## 📋 Required Structure (Follow Exactly)

Your markdown file MUST have these 10 sections in this exact order:

### Section 1: Title
```markdown
# Song Title (Alternate Names)
```
**Requirements:**
- Use H1 heading (`#`)
- Include full/alternate names in parentheses
- Example: `# Iê Maré (Ee Maré / Ee da Beira Mar)`

---

### Section 2: Basic Info
```markdown
## Basic Info
- Date added: 2026-06-17
- Status: In Study
- Source: Traditional / Artist Name
- Type: Corrido
```
**Requirements:**
- Header: `## Basic Info` (exactly this)
- Four fields with dashes: Date, Status, Source, Type
- Status options: "In Study" or "Mastered"
- Type options: Corrido, Ladainha, Samba, etc.

---

### Section 3: Media Links
```markdown
## Media Links

### YouTube
- [Basic Capoeira Songs: Ai Ai Aidê (teaching version)](https://www.youtube.com/watch?v=...)
- [Song Name – Performance](https://www.youtube.com/watch?v=...)

### Spotify
- Search: "Song Name capoeira"

### Apple Music
- Search: "Song Name capoeira"

### YouTube Music
- Search: "Song Name capoeira"
```
**Requirements:**
- Header: `## Media Links` (exactly this)
- Subsections: `### YouTube` and `### Spotify` (REQUIRED, minimum)
- Optional: Apple Music, YouTube Music
- Format: `[Description](URL)` for actual links
- Or: "Search: ..." for search instructions
- **IMPORTANT:** Links should be to TRADITIONAL/AUTHENTIC performances ONLY
  - ✓ Include: Traditional capoeira groups, mestre performances, Angola recordings
  - ✓ Include: Educational/teaching versions
  - ✗ Exclude: Remixes, electronic versions, non-capoeira artists
  - ✗ Exclude: Pop/commercial versions
- Focus on links that preserve the original song's cultural authenticity

---

### Section 4: Lyrics
```markdown
## Lyrics

### Full Lyrics

Ie!
Ee mare, ee da beira mar
Oi de mare, mare

Mare subiu, mare desceu
Mare da beira mar

[... rest of lyrics ...]

### Line-by-line Meaning

| Portuguese | English |
|---|---|
| Ie! | Hey! (traditional Capoeira exclamation) |
| Ee mare, ee da beira mar | Hey tide, hey from the shore |
| Oi de mare, mare | Oh the tide, the tide |
| [etc.] | [etc.] |
```
**Requirements:**
- Header: `## Lyrics` (exactly this)
- Subsection 1: `### Full Lyrics` (exactly this name)
  - Plain text, one lyric line per line
  - Do NOT put these in a table
- Subsection 2: `### Line-by-line Meaning` OR `### Line-by-Line Meaning` (both work)
  - Must be a markdown table
  - Exactly 2 columns: Portuguese | English
  - Table separator: `|---|---|`
  - Every lyric line gets a translation
  - Translations should be natural English (not word-for-word)

---

### Section 5: Pronunciation
```markdown
## Pronunciation

| Line / Phrase | Pronunciation Help |
|---|---|
| Ie | ee-EH (short, sharp, like a shout) |
| Ee mare | ee mah-REH |
| da beira mar | dah BAY-rah mah |
| Oi de mare | oy jee mah-REH |
| [etc.] | [etc.] |

**Pronunciation tips for beginners:**
- *Final "o" sounds like "oo"* — mah-REH-noo
- *"ã" is nasalized* — say through your nose slightly
```
**Requirements:**
- Header: `## Pronunciation` (exactly this)
- Markdown table with 2 columns: Phrase | Pronunciation Help
- Table separator: `|---|---|`
- Simplified pronunciation (NOT IPA)
- Use English syllables: "mah-REH", "BAY-rah", etc.
- Optional: Add pronunciation tips after table
- Tips in format: ***word** — explanation*

---

### Section 6: Vocabulary
```markdown
## Vocabulary

| Word / Phrase | Meaning | Notes |
|---|---|---|
| ie / ee | hey | Traditional Capoeira exclamation — African origin |
| mare | tide | Feminine noun: "a mare" |
| beira | shore / edge | "Beira mar" = seashore |
| mar | sea | Masculine noun: "o mar" |
| subiu | rose / went up | Past tense of "subir" (to go up) — 3rd person singular |
| [etc.] | [etc.] | [etc.] |
```
**Requirements:**
- Header: `## Vocabulary` (exactly this)
- Markdown table with 3 columns: Word / Phrase | Meaning | Notes
- Table separator: `|---|---|---|`
- **CRITICAL: INCLUDE EVERY SINGLE WORD FROM THE SONG**
  - Articles: o, a, um, uma
  - Prepositions: em, de, pra, na, no
  - Contractions: tá, pra, na, no
  - Conjunctions: e, ou, mas
  - Verbs: in infinitive AND conjugated form
  - Nouns, adjectives, adverbs
- Notes should include:
  - Gender (for nouns): "Feminine noun" or "Masculine noun"
  - Verb info: tense, person, or form
  - Context: where/how it's used
  - Etymology: if relevant

---

### Section 7: Grammar
```markdown
## Grammar Notes

### 1. Verb Forms

| Form in song | Base verb | Tense / Mood | Meaning | Notes |
|---|---|---|---|---|
| subiu | subir | Preterite (past) | rose / went up | 3rd person singular |
| desceu | descer | Preterite (past) | fell / went down | 3rd person singular |
| chama | chamar | Present indicative | calls | 3rd person singular |
| quer | querer | Present indicative | wants | 3rd person singular; irregular verb |
| ta | estar | Present indicative (colloquial) | is | Contraction of "está" |
| vazando | vazar | Present gerund | is ebbing | Used with "ta" — ta vazando |

### 2. Sentence Patterns

| Pattern | Explanation | Example from song | New example |
|---|---|---|---|
| Subject + ta + adjective | Describes a current state | "A mare ta cheia" | "O mar ta calmo" |
| Subject + ta + gerund | Describes ongoing action | "A mare ta vazando" | "O barco ta chegando" |
| Subject + verb + object pronoun | Action directed at someone | "Ela te chama" | "Ela te espera" |

### 3. Pronouns and Subject Omission

| Item | Explanation | Example from song | Notes |
|---|---|---|---|
| ella | She / It | "Ella te chama" | Refers to "a mare" — the tide is personified |
| te | you (object) | "Ella te quer" | Clitic object pronoun placed between subject and verb |
| meu | my (masculine) | "Meu barquinho" | Agrees in gender with the noun |

### 4. Repetition and Chorus Structure

| Feature | Explanation | Example |
|---|---|---|
| Call-and-response | Lead sings a line, group responds | Lead: "A mare ta cheia" — Group: "Ie, mare" |
| Anchor refrain | Core line that anchors every section | "Mare da beira mar" repeated throughout |
| Stop-and-restart | Song pauses completely, resumes on a signal | Full silence — then "Ie! Ee mare..." |

### 5. Poetic / Traditional / Informal Language

| Expression | Literal meaning | Functional meaning | Notes |
|---|---|---|---|
| Ie! | No literal meaning | Battle cry, call to attention, opening shout | African-rooted exclamation; marks start of roda |
| ta | is | Colloquial present tense of "estar" | "Esta" is formal, "ta" is everyday spoken Brazilian Portuguese |
| barquinho | little boat | Term of smallness or endearment | Diminutive suffix "-inho" softens or endears the noun |
| ella te quer | she wants you | The tide calls / pulls you | Personification of the tide as a feminine, calling force |

### 6. Grammar Questions

- Why is "ta" used instead of "está"? (Colloquial contraction — essential for understanding real Brazilian speech)
- Why does "cheia" end in "-a"? (Feminine adjective agreeing with "mare," a feminine noun)
- What does "te" mean in "ella te chama"? (Object pronoun "you" — the tide is calling YOU)
- What is "Ie" grammatically? (A non-lexical vocalization — culturally and musically functional, not a standard word)
```
**Requirements:**
- Header: `## Grammar Notes` (or `## Grammar`, both work)
- Must have AT LEAST 5 subsections, numbered: `### 1. `, `### 2. `, etc.
- Most subsections should be markdown tables with headers and data
- Last subsection (6) can be questions instead of a table
- Tables should have 4-5 columns
- Include examples DIRECTLY from the song
- Include new examples using ONLY vocabulary already taught
- Explain WHY the grammar matters AND HOW it works

---

### Section 8: Cultural Notes
```markdown
## Cultural Notes

- **Iê Maré** is one of the oldest and most widespread corridos in Capoeira, present in both Angola and Regional traditions
- The **"Ie!" exclamation** is rooted in African linguistic traditions brought to Brazil during the slave trade; it signals the start of a game, a challenge, or a section transition
- **Sea and tide imagery** (mare, beira mar, barco, mar) connects to Afro-Brazilian spiritual traditions — Iemanja, the orixa of the sea, is invoked through this water symbolism
- **"Ella te chama, ella te quer"** — the tide is personified as a feminine, calling force, possibly referencing both the sea and Iemanja herself
- The **stop-and-restart technique** in this song is used by mestres as a test of presence: students who keep moving or talking during the pause have failed the test of attention
- **"Beira mar"** also refers to a style of Capoeira Regional from the coastal cities of Bahia
```
**Requirements:**
- Header: `## Cultural Notes` (or `## Cultural Context`, both work)
- Bullet points with dashes: `- [content]`
- At least 3-4 bullet points (5+ is better)
- Cover: historical origin, spiritual significance, cultural importance, notable traditions
- Make connections to Afro-Brazilian culture, spirituality, history
- Explain why the song matters in Capoeira

---

### Section 9: Repeated Expressions / Chorus
```markdown
## Repeated Expressions / Chorus

- **"Ee mare, ee da beira mar"** — the anchor line; the most recognizable phrase of the song
- **"Ie, mare"** — universal response line after each lead verse
- **"Oi de mare, mare"** — secondary refrain building rhythm and intensity
- **"Ie!"** — the restart signal after the full stop; the entire roda listens for this one word
```
**Requirements:**
- Header: `## Repeated Expressions / Chorus` (exactly this)
- Bullet points with dashes
- Format: **"phrase"** — explanation
- At least 3-4 repeated phrases
- Explain the function of each (anchor, response, signal, etc.)
- Bold the actual phrase text

---

### Section 10: Practice
```markdown
## Practice

1. **Write 2 new sentences using "ta + gerund":** e.g., "O menino ta correndo" / "A musica ta tocando"
2. **Reuse "no meio do" in a new sentence:** e.g., "Ella ficou no meio do grupo" (She stayed in the middle of the group)
3. **Identify the tense of "subiu" and "desceu"** — why are these in the past while other verbs are in the present?
4. **Recite or sing the anchor line slowly:** "Ee mare, ee da beira mar" — clap, stop at the pause, re-enter on "Ie!"
```
**Requirements:**
- Header: `## Practice` (exactly this)
- Numbered list: `1. `, `2. `, `3. `, `4. ` (at least 4 exercises)
- At least one writing exercise
- At least one identification/analysis exercise
- At least one recitation/singing exercise
- **CRITICAL:** All exercises should ONLY use vocabulary already taught in Section 6
- If you introduce a new word in an example, teach it on-the-fly: *word (meaning)*

---

## 📊 Markdown Table Requirements

All tables in your file MUST follow this exact format:

### Correct Table Format:
```markdown
| Column 1 | Column 2 | Column 3 |
|---|---|---|
| Cell | Cell | Cell |
| Cell | Cell | Cell |
```

### Rules (CRITICAL):
- ✓ Use pipe characters `|` to separate columns
- ✓ First row contains headers
- ✓ Second row is the separator: `|---|---|---|`
- ✓ Every data row must have the same number of pipes
- ✓ Spaces inside cells are fine (e.g., `| hello world |`)
- ✓ Each cell should have content (use `-` if a cell is empty)

### Common Mistakes to AVOID:
- ❌ Different number of pipes per row (critical error!)
- ❌ Missing or malformed separator row
- ❌ Headers in data rows
- ❌ Extra pipes at the beginning/end

---

## 🔍 Self-Validation Checklist

Before you submit your markdown, verify:

- [ ] **Title (Section 1)**
  - [ ] Uses `#` for H1
  - [ ] Includes alternate names
  - [ ] Clear and complete

- [ ] **Basic Info (Section 2)**
  - [ ] Has `## Basic Info` header
  - [ ] 4 fields: Date, Status, Source, Type
  - [ ] Uses bullet points with dashes
  - [ ] Dates are in YYYY-MM-DD format

- [ ] **Media Links (Section 3)**
  - [ ] Has `## Media Links` header
  - [ ] Has `### YouTube` with at least 1 link
  - [ ] Has `### Spotify` (link or search)
  - [ ] Links use markdown format: `[text](url)`
  - [ ] At least 3 total media links/sections

- [ ] **Lyrics (Section 4)**
  - [ ] Has `## Lyrics` header
  - [ ] Has `### Full Lyrics` subsection
  - [ ] Has `### Line-by-line Meaning` OR `### Line-by-Line Meaning`
  - [ ] Translation table has exactly 2 columns
  - [ ] Translation table has separator row: `|---|---|`
  - [ ] Every lyric line has a translation

- [ ] **Pronunciation (Section 5)**
  - [ ] Has `## Pronunciation` header
  - [ ] Has pronunciation table with 2 columns
  - [ ] Pronunciation is simplified (not IPA)
  - [ ] Examples use English syllables: "mah-REH"

- [ ] **Vocabulary (Section 6)**
  - [ ] Has `## Vocabulary` header
  - [ ] Has table with exactly 3 columns
  - [ ] **INCLUDES EVERY WORD FROM THE SONG** (critical!)
  - [ ] Notes include gender for nouns
  - [ ] Notes include tense/form for verbs
  - [ ] At least 40-60 vocabulary entries

- [ ] **Grammar (Section 7)**
  - [ ] Has `## Grammar Notes` (or `## Grammar`)
  - [ ] Has AT LEAST 5 subsections (### 1., ### 2., etc.)
  - [ ] Most subsections are tables (not text)
  - [ ] Examples are from the actual song
  - [ ] New examples only use taught vocabulary
  - [ ] Final subsection has at least 3-4 grammar questions

- [ ] **Cultural Notes (Section 8)**
  - [ ] Has correct header
  - [ ] 3-5 bullet points
  - [ ] Covers history, significance, tradition
  - [ ] Makes Afro-Brazilian/Capoeira connections

- [ ] **Repeated Expressions (Section 9)**
  - [ ] Has `## Repeated Expressions / Chorus` header
  - [ ] 3-4 repeated phrases listed
  - [ ] Format: **"phrase"** — explanation
  - [ ] Explains function of each phrase

- [ ] **Practice (Section 10)**
  - [ ] Has `## Practice` header
  - [ ] 4+ numbered exercises
  - [ ] Only uses taught vocabulary
  - [ ] Mix of writing, identification, recitation

- [ ] **Overall Quality**
  - [ ] File is 8000-15000 bytes (8-15KB)
  - [ ] No unmatched brackets or parentheses
  - [ ] All tables properly formatted
  - [ ] No spelling errors in headers
  - [ ] Section names match exactly

---

## 💡 Quality Tips

### For Vocabulary Section:
- Don't leave any word unexplained
- Include: nouns, verbs, adjectives, prepositions, articles, contractions, pronouns
- For nouns: specify masculine/feminine
- For verbs: specify tense and person
- For contractions: show the full form (e.g., "tá = está")

### For Grammar Section:
- Use actual song lyrics as primary examples
- Create new examples using ONLY taught vocabulary
- Explain not just HOW but WHY (why this tense, why this structure)
- Grammar tables should have 4-5 columns for clarity

### For Cultural Notes:
- Connect to real history (slavery, quilombos, African traditions)
- Mention spiritual significance (orixás, Afro-Brazilian religion)
- Reference notable mestres or communities if applicable
- Explain why this song is taught and valued

### For Practice:
- Include variety: writing, identifying, reciting, analyzing
- Make exercises progressively more challenging
- Always relate back to the song itself

---

## 📤 Final Output

When you're done, provide:

1. **The complete markdown file** — copy the entire content
2. **Filename suggestion** — e.g., `song-ie-mare.md`
3. **Self-validation confirmation** — "All checks passed ✓"
4. **Alternate names** (if any) — for reference

### Format:
```markdown
# COMPLETE MARKDOWN FILE

[All 10 sections with all content]

---

**Filename:** song-name.md
**Validation:** All 10 sections complete ✓
**Alternate names:** Song Name (Ee Mare / Full Title)
```

---

## 🎯 Success Criteria

Your markdown is ready for conversion when:
- ✅ All 10 sections are present and complete
- ✅ Every word from the lyrics is in vocabulary
- ✅ All tables are properly formatted
- ✅ Grammar section has 5+ subsections
- ✅ File is 8000+ bytes
- ✅ No formatting errors
- ✅ Translations are natural (not word-for-word)
- ✅ Examples only use taught vocabulary
- ✅ Cultural context is meaningful and accurate

---

## 🚀 Go Create!

You now have everything you need to create high-quality song lessons that:
- Convert perfectly to HTML
- Pass validation automatically
- Provide complete learning resources
- Respect Capoeira culture and history

**Follow this guide exactly, and your markdown will be conversion-ready on the first try!**

🥁 **Ready? Create an amazing song lesson!** 🥁

