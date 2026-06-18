# Test Song Learning Session Guide

This guide walks you through a complete test session using **A Maré Tá Cheia** as the current song.

**Learner Level:** Complete Beginner  
**Song:** A Maré Tá Cheia (Traditional Capoeira Corrido)  
**Duration:** 20-30 minutes  
**Session Type:** First Introduction to Song

---

## Pre-Session Checklist

✓ Open the song file: `/content/songs/song-a-mare-ta-cheia.md`  
✓ Open vocab-log.json: `/progress/vocab-log.json` (reference)  
✓ Open content-taught-log.md: `/progress/content-taught-log.md` (for tracking)  
✓ Have a notebook or text editor ready to record session notes  
✓ Optional: Play an audio/video of the song from YouTube or Spotify

---

## Session Structure

**First Session:** Steps 1-2 are skipped (no previous vocabulary to quiz, no previous content to recap). You'll start with Step 3.

Follow these steps in order:

**Session 1 Path:** Step 3 → Step 4 → Step 5  
**Sessions 2+:** Step 1 → Step 2 → Step 3 → Step 4 → Step 5

### STEP 1: Vocabulary Quiz (5-7 minutes) — **SKIPPED FOR THIS SESSION**

**Purpose:** Assess baseline knowledge before learning new words.

**Status:** ⏭️ **SKIPPED** — No previously learned vocabulary yet.

**Why:** This is the first session. The vocabulary log is empty, so there are no words to quiz on. Future sessions will include this step to review previously learned words weighted by difficulty and performance.

**Note for Future Sessions:**
When you have vocabulary from previous songs/articles, this step will:
- Quiz on previously learned words
- Weight questions based on success rate (struggle words appear more often)
- Use varied question formats (never the same format twice)
- Include immediate feedback and explanations

**Proceed to STEP 2** →

---

### STEP 2: Recap of Last Session (2-3 minutes) — **SKIPPED FOR THIS SESSION**

**Purpose:** Reinforce previous vocabulary and grammar.

**Status:** ⏭️ **SKIPPED** — No previous content taught yet.

**Note for Future Sessions:**
In future sessions, you would:
- Review 3-5 vocabulary words from the previous song
- Recap 1 grammar point from the previous lesson
- Ask comprehension questions
- Identify words that need more reinforcement

**Proceed to STEP 3** →

---

### STEP 3: New Vocabulary (5-7 words) (5-7 minutes)

**Purpose:** Introduce core vocabulary from the current song.

**Song: A Maré Tá Cheia**

Study these 7 vocabulary words from the song:

| # | Portuguese | English | Pronunciation | Example from Song |
|---|---|---|---|---|
| 1 | maré | tide | mah-REH | A maré tá cheia |
| 2 | cheia | full / high | SHAY-ah | A maré tá cheia |
| 3 | subiu | rose / went up | soo-bee-OO | A maré subiu |
| 4 | desceu | dropped / went down | des-seh-OO | A maré desceu |
| 5 | peixe | fish | PAY-shee | O peixe pulou na maré |
| 6 | pulou | jumped | poo-LOH | O peixe pulou na maré |
| 7 | ilha | island | EE-lya | Vou pra Ilha de Maré |

**Learning Activity:**

1. **Read and repeat:** Say each word aloud 3 times, matching the pronunciation guide
2. **Contextualize:** Read the example sentence from the song and try to understand the context
3. **Write it down:** Create your own flashcards or notes with the word, pronunciation, and meaning
4. **Create sentences:** For each word, write 1-2 sentences using ONLY taught vocabulary (in English is fine for beginners)

**Example for "maré":**
- Word: maré
- Meaning: tide
- Pronunciation: mah-REH
- My sentence: "A maré subiu." (The tide rose.) ✓ Uses only taught words
- My sentence: "The tide is important for fishermen." ✗ Introduces "important" without teaching it

**IMPORTANT:** Only use vocabulary from the table above. If you need a new word to complete a sentence, ask for it to be taught first!

---

### STEP 3: New Grammar Point (1 point) (5-7 minutes)

**Purpose:** Teach 1 focused grammar concept from the song.

**Today's Grammar Topic: Preterite Tense (Simple Past)**

**Concept:**
The preterite is the simple past tense in Portuguese. It tells what happened/occurred in the past.

**Pattern:**
For regular -IR verbs: remove -ir and add -u for 3rd person singular
- subir → subiu (rose/went up)
- descer → desceu (dropped/went down)  
- pular → pulou (jumped)

**Example from Song:**
```
A maré subiu.
= The tide rose. (past tense - it rose at a specific moment)
```

**Grammar Practice:**

1. **Identify in song:** Find all preterite verbs in "A Maré Tá Cheia"
   - subiu (rose)
   - desceu (dropped)
   - pulou (jumped)

2. **Pattern recognition:** All three follow the pattern: [verb stem] + -u

3. **Practice creating:** Try to create 2 new sentences using preterite:
   - "O mestre chegou." (The master arrived.)
   - "O gato pulou na água." (The cat jumped in the water.)

**Why this matters:**
- Preterite is the most common past tense in Portuguese
- You'll see it in almost every song and story
- Understanding it helps you talk about what happened

---

### STEP 4: Session Summary & Progress Update (3-5 minutes)

**Purpose:** Consolidate learning and record progress.

**Complete this form:**

```
SESSION 1 SUMMARY - A Maré Tá Cheia
=====================================

Date: 2026-06-17
Song: A Maré Tá Cheia
Type: Corrido (traditional)

QUIZ RESULTS
────────────
Total questions: 5
Correct: X/5
Success rate: X%
Words that were hard: [List]

VOCABULARY LEARNED
───────────────────
Words introduced: 7
- maré
- cheia
- subiu
- desceu
- peixe
- pulou
- ilha

GRAMMAR POINT
──────────────
Topic: Preterite Tense (Simple Past)
Key pattern: [verb stem] + -u for 3rd person singular
Examples: subiu, desceu, pulou

CONFIDENCE LEVEL (1-5)
──────────────────────
Vocabulary: ___/5
Grammar: ___/5
Overall: ___/5

NOTES
──────
[Write any observations, challenges, or insights]

NEXT SESSION PREVIEW
────────────────────
Next song: [TBD]
Topics to review before next session:
- Preterite verb formation
- These 7 vocabulary words
```

---

## After the Session: Update Tracking Files

Once you complete the session, update these files:

### 1. Update content-taught-log.md

Add this line to the "Songs Taught" table:

```markdown
| 1 | A Maré Tá Cheia | A maré tá cheia | Corrido | 2026-06-17 | In Study | 7 | 1 | First introduction - learning core vocabulary and preterite tense |
```

### 2. Update vocab-log.json

The vocab-log.json already contains entries for the 7 words from this song. Verify all entries are present and match what you learned.

Reference the existing entries in `/progress/vocab-log.json`

### 3. Update state.json

Change the file from:
```json
{
  "content_taught": {
    "songs_taught": [],
    ...
  }
}
```

To:
```json
{
  "content_taught": {
    "songs_taught": ["song-a-mare-ta-cheia"],
    "articles_taught": [],
    "total_vocab_from_content": 7
  },
  "vocab_count": 7,
  "sessions_completed": 1,
  "last_session_date": "2026-06-17"
}
```

### 4. Save daily-session-handout.md

Fill out the `/progress/daily-session-handout.md` template with today's session details and save it with the date:
- `daily-session-handout-2026-06-17.md`

---

## How to Use Claude AI to Facilitate This Session

You can ask Claude to help with each step:

### For Quiz:
**Prompt:** "Generate 5 beginner-level Portuguese quiz questions about vocabulary from 'A Maré Tá Cheia'. Include the answers and explanations."

### For Vocabulary:
**Prompt:** "Create 3 example sentences for each of these words from 'A Maré Tá Cheia': maré, cheia, subiu, desceu, peixe, pulou, ilha. Use simple context and include English translations."

### For Grammar:
**Prompt:** "Explain the preterite tense in Portuguese for complete beginners. Use only examples from 'A Maré Tá Cheia'. Show the pattern and provide 3 new practice sentences."

### For Session Review:
**Prompt:** "Based on this session learning 'A Maré Tá Cheia', what are the 3 most important takeaways? What should I focus on before the next session?"

---

## Tips for Success

✓ **Take your time** — Don't rush through steps. Spend 5-7 minutes on each vocabulary/grammar section.

✓ **Say words aloud** — Pronunciation matters. Hear yourself say the Portuguese words.

✓ **Write everything down** — The act of writing helps retention.

✓ **Engage with the culture** — Listen to the song while studying (find it on YouTube/Spotify). Understanding the melody helps with memory.

✓ **Use the song file** — Reference `/content/songs/song-a-mare-ta-cheia.md` throughout. Read the cultural notes to understand context.

✓ **Be honest in self-assessment** — If you don't understand something, note it and ask Claude for clarification.

---

## What Happens in Session 2?

After you complete this first session, your next session (in 1-2 days) will:

1. **Quiz on these 7 words** — Assess retention and success rate
2. **Introduce 5 new vocabulary words** from the song (not covered yet)
3. **Teach another grammar point** (maybe imperative commands, which appear in chorus "Sobe maré!")
4. **Recap today's learning** and verify understanding
5. **Update progress tracking** with new data points

---

## Session Templates to Print/Save

You may want to print these files for reference during the session:

- `/content/songs/song-a-mare-ta-cheia.md` — Full song lesson
- `/progress/daily-session-handout.md` — Blank template to fill out
- This file (`TEST-SESSION.md`) — Session guide and instructions

---

**Ready to start?** Begin with STEP 1: Vocabulary Quiz and work through all 5 steps in order. Good luck! 🥁

*Last Updated: 2026-06-17*
