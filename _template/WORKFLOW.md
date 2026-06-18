# Learning App Workflow

This document outlines the complete workflow for teaching content, tracking progress, and managing vocabulary.

---

## Overview

The learning app maintains three interconnected tracking systems:

1. **state.json** — Overall learner progress (rank, points, sessions)
2. **content-taught-log.md** — Record of all songs/articles taught
3. **vocab-log.json** — Complete vocabulary database with source tracking

When you teach a new song or article, all three files must be updated.

---

## Teaching a New Song

### Step 1: Confirm the Song File Exists

✓ Check that `content/songs/song-[name].md` is complete with:
- Full lyrics
- Line-by-line translations
- Pronunciation guide
- Vocabulary table
- Grammar notes
- Cultural notes

**File location:** `/content/songs/`

### Step 2: Run a Daily Session

Follow the project instructions:
1. Vocabulary quiz (weighted by performance)
2. Recap of last session
3. 5 new vocabulary words
4. 1 new grammar point
5. Update progress

### Step 3: Update content-taught-log.md

After teaching the song, add an entry to the **Songs Taught** table:

| Field | Value |
|---|---|
| Song Title | [Portuguese name] |
| Type | [corrido/ladainha/samba/etc.] |
| Date First Taught | [Today's date] |
| Status | In Study |
| Vocab Words Added | [Count of words] |
| Grammar Points | [Count of grammar patterns] |
| Notes | [Any relevant context] |

### Step 4: Update vocab-log.json

For each vocabulary word from the song, add a JSON entry:

```json
{
  "word": "[Portuguese word]",
  "meaning": "[English meaning]",
  "part_of_speech": "[noun/verb/adjective/etc.]",
  "source_type": "song",
  "source_content": "song-[name]",
  "date_learned": "[Today's date]",
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

**Fields to include:**
- **word**: The Portuguese word
- **meaning**: English translation
- **part_of_speech**: Grammar category
- **source_type**: "song" (or "article")
- **source_content**: Exact filename (e.g., "song-a-mare-ta-cheia")
- **date_learned**: When it was first taught
- **mastery_level**: Always "new" for newly taught words

### Step 5: Update state.json

Update the following fields:

```json
{
  "content_taught": {
    "songs_taught": ["song-a-mare-ta-cheia", "song-new-name"],
    "articles_taught": [],
    "total_vocab_from_content": 7
  },
  "vocab_count": 7,
  "sessions_completed": 1,
  "last_session_date": "2026-06-17"
}
```

---

## Teaching a New Article

### Step 1: Confirm the Article File Exists

✓ Check that the article lesson file is complete with:
- Full Portuguese text (or substantial excerpt)
- English summary
- Difficulty level (1-5)
- Vocabulary glossary
- Grammar analysis
- Cultural context
- Comprehension questions
- Practice exercises

**File location:** `content/articles/article-[name].md` (file naming: `article-[topic-slug].md`)

### Step 2: Run a Reading Session

Adapt the daily session structure for articles:
1. Pre-reading vocabulary introduction
2. Guided comprehension
3. Vocabulary quiz on new words
4. Grammar pattern review
5. Discussion/reflection questions

### Step 3: Update content-taught-log.md

Add an entry to the **Articles Taught** table:

| Field | Value |
|---|---|
| Article Title | [Title] |
| Difficulty | [1-5] |
| Date First Taught | [Today's date] |
| Status | In Study |
| Vocab Words Added | [Count] |
| Grammar Points | [Count] |
| Content Type | [history/biography/cultural/etc.] |
| Notes | [Relevant context] |

### Step 4: Update vocab-log.json

For each vocabulary word from the article, add a JSON entry:

```json
{
  "word": "[Portuguese word]",
  "meaning": "[English meaning]",
  "part_of_speech": "[noun/verb/adjective/etc.]",
  "source_type": "article",
  "source_content": "article-[name]",
  "date_learned": "[Today's date]",
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

### Step 5: Update state.json

Increment the article count and total vocabulary:

```json
{
  "content_taught": {
    "songs_taught": ["song-a-mare-ta-cheia"],
    "articles_taught": ["article-[name]"],
    "total_vocab_from_content": [X]
  },
  "vocab_count": [X]
}
```

---

## Reviewing Previously Taught Content

### When Re-teaching a Song

1. **Update status in content-taught-log.md:**
   - Change Status from "In Study" to "Review" or "Mastered"

2. **Mark vocabulary in vocab-log.json:**
   - Update `last_reviewed` date
   - Update quiz stats based on session performance
   - If success rate > 80%, change `mastery_level` to "confident"

3. **Update state.json:**
   - Record the review session

### Example: After Second Session with "A Maré Tá Cheia"

**In content-taught-log.md:**
```
| A Maré Tá Cheia | Corrido | 2026-06-17 | Review | 7 | 6 | Second session - reinforcing vocabulary |
```

**In vocab-log.json (for each word):**
```json
{
  "word": "maré",
  ...
  "last_reviewed": "2026-06-24",
  "quiz_stats": {
    "times_asked": 5,
    "times_correct": 4,
    "times_wrong": 1,
    "success_rate": 80
  },
  "mastery_level": "confident"
}
```

---

## Vocabulary Sharing Between Content

If the same word appears in multiple songs or articles:

1. **Add only once to vocab-log.json** (one entry per unique word)
2. **Update source tracking:**
   ```json
   "sources": ["song-a-mare-ta-cheia", "article-history-of-capoeira"],
   "reinforcement_count": 2
   ```
3. **Note in content-taught-log.md:** Record shared vocabulary in the "Song-Article Connections" section

**Example:**
- Word "mestre" learned from Song 1
- Appears again in Article 1
- Update vocab-log entry for "mestre" to show it's been reinforced
- This counts as valuable reinforcement, not a new word

---

## Monthly Review & Summary

At the end of each month:

1. **Review content-taught-log.md:**
   - Update status of songs/articles (In Study → Review → Mastered)
   - Note total words taught
   - Identify patterns in teaching pace

2. **Analyze vocab-log.json:**
   - Count words by mastery level
   - Calculate overall success rates
   - Identify struggling words (success_rate < 50%)

3. **Update state.json:**
   - Reflect cumulative progress
   - Verify vocab_count accuracy

---

## File Structure Quick Reference

```
progress/
├── state.json                 ← Overall learner state (update after each session)
├── vocab-log.json             ← Vocabulary database (add/update words taught)
├── content-taught-log.md      ← Record of all content taught (update after each lesson)
└── daily-session-handout.md   ← Template for printable session records

content/
├── songs/
│   ├── song-a-mare-ta-cheia.md
│   └── [other song files]
└── articles/
    └── [article files - one per topic]
```

---

## Data Flow Diagram

```
New Song/Article Selected
    ↓
Run Daily/Reading Session
    ↓
Extract Vocabulary
    ↓
Update vocab-log.json
(Add/update word entries)
    ↓
Update content-taught-log.md
(Record that content was taught)
    ↓
Update state.json
(Increment content taught, vocab count, sessions)
    ↓
Generate daily-session-handout.md
(For learner review/printing)
```

---

## Tips for Accurate Tracking

✓ **Always use consistent filenames** — Match filenames exactly in all references (state.json, vocab-log.json, content-taught-log.md)

✓ **Update immediately after teaching** — Don't wait to batch updates; do it while session details are fresh

✓ **Record all vocabulary** — Even words that seem "obvious"; future quizzes should be comprehensive

✓ **Note source content precisely** — Include exact song/article name in each vocab entry

✓ **Review monthly** — Check for duplicates, inconsistencies, or missing entries

✓ **Use mastery_level field** — Track progression: new → reviewed → confident → mastered

---

**Last Updated:** 2026-06-17  
**Version:** 1.0
