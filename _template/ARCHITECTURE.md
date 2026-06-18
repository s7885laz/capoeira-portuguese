# Capoeira Portuguese Learning App — Architecture & Implementation Plan

## Project Goal
An AI-powered Brazilian Portuguese learning app built around Capoeira culture (songs, vocabulary, grammar, articles). Designed as a usable POC from day one, with a clear path to a standalone web app.

---

## Guiding Principles
- No manual tracking — all progress is handled by the app
- AI generates fresh exercises every session (no pattern-tricking like Duolingo)
- Content-first: song MD files are the source of truth in v1
- Clean separation between content, logic, and UI from the start
- Beginner-friendly: assume zero prior Portuguese knowledge

---

## Folder Structure

```
capoeira-portuguese/
│
├── README.md                        # Project overview and setup instructions
├── ARCHITECTURE.md                  # This file
│
├── content/
│   ├── songs/
│   │   ├── song-a-mare-ta-cheia.md  # Processed song files (one per song)
│   │   └── inbox_songs.md           # Songs queued for processing
│   ├── articles/                    # Capoeira-related reading materials (future)
│   └── grammar/                     # Standalone grammar reference notes (future)
│
├── prompts/
│   ├── session-prompt.md            # Main session system prompt for Claude
│   ├── vocab-quiz-prompt.md         # Prompt for vocabulary quiz exercises
│   ├── grammar-prompt.md            # Prompt for grammar explanation and exercises
│   ├── song-lesson-prompt.md        # Prompt for guided song learning sessions
│   ├── article-lesson-prompt.md     # Prompt for guided article reading (future)
│   └── perplexity-song-prompt.md    # Prompt for generating new song MD files via Perplexity
│
├── progress/
│   ├── state.json                   # Current learner state (rank, points, badges, session history)
│   └── vocab-log.json               # All learned vocabulary with timestamps and review status
│
└── app/
    └── poc.html                     # POC single-file web app (Claude-powered)
```

---

## Session Flow (Daily, ~10–30 min)

```
Session Start
│
├── 1. Vocab Quiz
│      └── AI generates fresh questions on previously learned words
│              (translation, fill-in-blank variations — never the same twice)
│
├── 2. Recap
│      └── Brief review of last session: vocabulary summary + grammar point revisited
│
├── 3. New Vocabulary (5 words)
│      └── Drawn from current song or upcoming song in the queue
│              Presented with meaning, pronunciation, example sentence
│
├── 4. New Grammar Point
│      └── One focused grammar topic from current song material
│              Explained simply, with examples from Capoeira context
│
└── Session End
       └── Points calculated, progress saved, next session preview
```

## Weekly Session (Once or Twice a Week)

```
├── Option A: New Song Lesson
│      └── Work through a song from inbox_songs.md
│              Lyrics → vocabulary → grammar → cultural notes → practice
│
└── Option B: Article Reading
       └── Capoeira-related text with AI guided comprehension (future)
```

---

## Content Pipeline

### Song Workflow
```
Perplexity (generate song MD)
    → content/songs/inbox_songs.md (queued)
        → Song selected for study
            → Dedicated song file created (e.g. song-a-mare-ta-cheia.md)
                → App consumes song file for lessons
```

### Perplexity Prompt (TODO: refine)
A dedicated prompt (`prompts/perplexity-song-prompt.md`) will instruct Perplexity to generate a complete song MD file following the established template, including:
- Full lyrics
- Line-by-line translation
- Pronunciation guide
- Vocabulary table
- Grammar notes
- Cultural notes

---

## Progress & Gamification

### Rank System
| Rank | Description |
|---|---|
| Iniciante | Starting rank |
| Aprendiz | Early learner |
| Graduado | Established learner |
| Formado | Advanced learner |
| Especialista | Near-mastery |
| Mestre | Full mastery |

### Points (v1 values — adjustable)
| Action | Points |
|---|---|
| Word learned and used correctly | +10 |
| Sentence using new grammar + words | +25 |
| Complete song mastered | +100 |
| Weekly song or article session | +150 |
| Mini-project completed | +200 |

### Badges
Ginga Master, Auréa Ace, Song Scholar, Cultural Explorer, Instrument Expert, Roda Ready, Content Creator

---

## State File Format (`progress/state.json`)

```json
{
  "rank": "Iniciante",
  "points": 0,
  "badges": [],
  "current_song": "song-a-mare-ta-cheia",
  "sessions_completed": 0,
  "last_session_date": null,
  "vocab_count": 0
}
```

## Vocab Log Format (`progress/vocab-log.json`)

```json
[
  {
    "word": "maré",
    "meaning": "tide",
    "source_song": "song-a-mare-ta-cheia",
    "date_learned": "2026-06-16",
    "last_reviewed": null,
    "quiz_stats": {
      "times_asked": 0,
      "times_correct": 0,
      "times_wrong": 0,
      "success_rate": null
    }
  }
]
```

---

## Quiz Selection Algorithm

Words are not selected randomly for quizzes. Selection is weighted based on each word's performance history, so struggling words appear more often than well-known ones.

### Selection Priority (highest to lowest)
1. **Never asked** — new words always appear first in a session
2. **High failure rate** — words with success rate below 50% are prioritised
3. **Recently failed** — words wrong in the last session are repeated early
4. **Low exposure** — words asked fewer than 3 times get priority over well-practised ones
5. **Well-known words** — words with success rate above 80% appear occasionally to maintain recall

### Weight Formula (v1 — adjustable)
```
weight = (times_wrong + 1) / (times_asked + 1)
```
Higher weight = higher chance of appearing in the next quiz. This naturally deprioritises well-known words without ever dropping them entirely.

### Rules
- Every session must include at least 2 high-priority (struggling) words if they exist
- No word is permanently retired — success rate can always drop
- Once a word reaches 80%+ success rate over 10+ attempts it is marked `confident` but still reviewed occasionally

### TODO (post-POC)
- [ ] Implement proper spaced repetition intervals (e.g. SM-2 algorithm) based on quiz stats
- [ ] Add `last_wrong_date` field to vocab log to support time-based review scheduling

---

## Tech Stack

### POC (v1)
| Layer | Choice | Reason |
|---|---|---|
| UI | Single HTML file | Portable, no build step, shareable |
| AI backend | Claude API (claude-sonnet-4-6) | Powers all exercises and explanations |
| Storage | JSON files + MD files | Simple, human-readable, version-controllable |
| Hosting | Local / claude.ai artifact | POC only |

### Standalone App (future)
| Layer | Choice |
|---|---|
| Frontend | React (separate repo) |
| Backend | Node.js or Python API |
| Database | TODO — replace JSON/MD files with proper DB |
| Hosting | TBD |

---

## TODO List

### POC Phase
- [ ] Set up folder structure
- [ ] Write `prompts/session-prompt.md` (main AI system prompt)
- [ ] Write `prompts/vocab-quiz-prompt.md`
- [ ] Write `prompts/perplexity-song-prompt.md`
- [ ] Initialise `progress/state.json` and `progress/vocab-log.json`
- [ ] Build `app/poc.html` (single file Claude-powered app)
- [ ] Test first full session with `song-a-mare-ta-cheia.md`

### Post-POC
- [ ] Add article reading mode
- [ ] Add micro-session (song listening) mode
- [ ] Add spaced repetition logic to vocab review
- [ ] Design and implement database schema (replace MD/JSON storage)
- [ ] Build standalone React frontend
- [ ] Build API backend
- [ ] Deploy as hosted web app

---

## Key Design Decisions

**Why MD files for songs?**
Human-readable, easy to author with Perplexity, version-controllable with git. Swappable for a database later with minimal app changes.

**Why a single HTML POC?**
Fastest path to a usable learning tool. No build pipeline, no deployment — just open in a browser and learn.

**Why Claude API (not hardcoded exercises)?**
Prevents the Duolingo trap: fresh exercise variations every session mean the learner must actually know the material, not just recognise patterns.
