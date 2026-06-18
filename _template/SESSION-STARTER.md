# Interactive Session Starter

This file enables you to start a Portuguese learning session with natural language. Simply type your request below and follow the prompts.

---

## How It Works

When you write something like:
- "I want to start a Portuguese lesson now"
- "Let's do a Capoeira Portuguese session"
- "Start my daily learning session"
- "I'm ready to learn Portuguese"

The system will:

1. **Check your current vocabulary** (`progress/vocab-log.json`)
2. **Determine session type:**
   - If vocab is empty → Start with NEW VOCABULARY step
   - If vocab exists → Start with QUIZ step
3. **Run the appropriate session flow**
4. **Guide you through all steps**
5. **Track your progress**

---

## Session Starter Prompts

Copy and paste any of these prompts to Claude, or write your own version:

### Quick Start Prompts

**Prompt 1 (Simplest):**
```
Start a Portuguese lesson now using "A Maré Tá Cheia"
```

**Prompt 2 (With details):**
```
I want to start a Capoeira Portuguese learning session. 
Use the song "A Maré Tá Cheia" and guide me through all steps.
```

**Prompt 3 (Natural conversation):**
```
I'm ready for my daily Portuguese lesson. Let's go!
```

**Prompt 4 (Check my status first):**
```
Check my learning progress, then start today's Portuguese lesson.
What's my current vocabulary count?
```

---

## What Claude Should Do When You Ask

When you ask Claude to start a session, Claude should:

### Step 1: Check Your Progress Files

Read these files to understand your current state:
- `progress/vocab-log.json` — How many words you've learned
- `progress/state.json` — Your overall progress (rank, points, sessions completed)
- `progress/content-taught-log.md` — Which content you've studied

### Step 2: Determine Session Type

**If `vocab-log.json` is empty or has 0 entries:**
```
→ This is Session 1
→ Skip vocabulary quiz (no previous words)
→ Skip recap (no previous content)
→ Start with Step 3: Learn new vocabulary
```

**If `vocab-log.json` has entries:**
```
→ This is a subsequent session
→ Start with Step 1: Vocabulary quiz
→ Include Step 2: Recap previous session
→ Then Step 3: New vocabulary
→ Then Step 4: New grammar point
→ Then Step 5: Summary & tracking
```

### Step 3: Guide the Learner

Run through the appropriate session steps:
- **Quiz** (if applicable): Generate fresh questions on previously learned words
- **Recap** (if applicable): Brief review of last session
- **Vocabulary**: Introduce 5-7 new words from current song
- **Grammar**: Teach 1 focused grammar point
- **Summary**: Help learner complete session summary

### Step 4: Interactive Feedback

After each step:
- Ask "Ready for next step?"
- Provide immediate feedback on answers
- Explain why answers are right/wrong
- Encourage the learner

### Step 5: Update Progress

At the end of the session:
- Ask Claude to help update the tracking files
- Save a dated session handout
- Preview the next session

---

## Example Session Flow (What Claude Will Do)

When you write: **"I want to start a Portuguese lesson now"**

Claude responds with something like:

```
📚 Portuguese Learning Session Started

Let me check your progress...
✓ Checking vocab-log.json... (7 words from A Maré Tá Cheia)
✓ Checking state.json... (0 sessions completed)
✓ Checking content-taught-log.md... (0 content taught yet)

🎯 Session Type: FIRST SESSION
Current vocabulary: 7 words available
Session duration: ~25 minutes

Since this is your first session, here's what we'll do:
⏭️ Skip: Vocabulary Quiz (no previous words to quiz)
⏭️ Skip: Recap (no previous content)
✅ Start: Learn 7 new vocabulary words from "A Maré Tá Cheia"
✅ Teach: Preterite tense (simple past)
✅ Complete: Session summary & confidence check

---

## STEP 3: Learn New Vocabulary

Let's learn 7 core words from "A Maré Tá Cheia":

**Word 1: maré**
- Meaning: tide
- Pronunciation: mah-REH
- Example: "A maré tá cheia" (The tide is full)

[... continues with all 7 words ...]

Ready to move to the next step?
```

---

## Files Claude Needs Access To

When you ask Claude to start a session, make sure Claude can:

1. **Read** these files:
   - `/progress/vocab-log.json`
   - `/progress/state.json`
   - `/progress/content-taught-log.md`
   - `/content/songs/song-a-mare-ta-cheia.md` (or current song)

2. **Help you fill out**:
   - `/progress/daily-session-handout.md`

3. **Guide you to update**:
   - `vocab-log.json` (add new words)
   - `content-taught-log.md` (record content taught)
   - `state.json` (increment sessions, update vocab count)

---

## Sample Natural Language Requests

Here are various ways you can ask to start a session:

```
"Let's start a Portuguese lesson"
"I'm ready for Portuguese learning"
"Begin my daily Capoeira Portuguese session"
"Start where we left off"
"Quiz me on Portuguese"
"Teach me Portuguese today"
"I want to learn Capoeira Portuguese"
"Let's do some Portuguese learning"
"Check my progress and start a new session"
"Run a learning session for me"
```

---

## Tips for Best Results

✓ **Be conversational** — You don't need exact wording. Natural language works.

✓ **Specify if you want** — "Start a lesson focused on grammar" or "I want to practice vocabulary"

✓ **Ask for help** — "Start the session and help me fill out the progress files after"

✓ **Set expectations** — "I have 20 minutes for a lesson" or "Quick 10-minute session"

✓ **Reference context** — "I studied yesterday, so start with a quiz on those words"

---

## What Happens After the Session

Claude should:

1. **Generate a session summary** using the daily-session-handout.md template
2. **Help you update tracking files:**
   - Add words to vocab-log.json
   - Update content-taught-log.md
   - Modify state.json
3. **Save your session** with the date (e.g., `daily-session-2026-06-17.md`)
4. **Preview next session** and what to review

---

## Ready to Start?

**Just type something like:**

> "I want to start a Portuguese lesson now"

Then follow Claude's guidance through the session!

---

*Last Updated: 2026-06-17*
