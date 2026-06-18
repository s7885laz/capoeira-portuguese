# Capoeira Portuguese 🇧🇷

A personal Brazilian Portuguese learning app built around Capoeira songs, vocabulary, and culture.

## What it is

An interactive web app for learning Portuguese through the music and traditions of Capoeira. Instead of generic vocabulary lists, every word and grammar point comes from real Capoeira songs — so you learn the language in the context where you'll actually use it.

## Features

- **Vocabulary quiz** — multiple choice, weighted by past performance (words you struggle with appear more often)
- **Blind mode** — hear the word spoken aloud without seeing it written, configurable by percentage
- **Google TTS pronunciation** — authentic Brazilian Portuguese audio on every quiz question, with a replay button
- **Song lessons** — annotated song pages with lyrics, translations, vocabulary, and grammar notes
- **Progress tracking** — quiz stats and mastery levels saved in `progress/vocab-log.json`

## Songs covered

| Song | Theme |
|------|-------|
| A Maré Tá Cheia | The tide, nature imagery |
| Iê Maré | Call-and-response, sea |
| Ai Ai Aidê | Classic ladainha |
| Santo Antônio Quero Água | Saints, water |
| Zum Zum Zum | Rhythm, the roda |

## Project structure

```
app/              # Web app (served via GitHub Pages)
  index.html      # Home / song selector
  vocab-quiz.html # Interactive vocabulary quiz
  *.html          # Individual song lesson pages

songs/            # Song source files (Markdown)
content/          # Grammar notes, articles, additional content
progress/         # vocab-log.json — vocab data and quiz stats
exploration/      # Pronunciation player experiments
prompts/          # AI tutor session prompts
```

## Running locally

Open via a local server (required for the vocab fetch to work):

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000/app/`.

## Deployment

Hosted on GitHub Pages from the `/app` folder.

---

*Built as a personal learning project. Capoeira é luta, dança e arte.*
