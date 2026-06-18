# Quick Copy-Paste Prompts for Perplexity

Use these prompts directly in Perplexity. They include the improved download handling.

---

## Prompt A: Generate Top 10 Capoeira Songs List

Copy everything below and paste into Perplexity:

```
Using the 'Top 10 Songs List Template', generate a curated list of the 10 most popular Capoeira songs suitable for beginner Portuguese learners. 

Focus on:
- Songs that are widely taught in capoeira schools
- Culturally significant and historically important
- Linguistically accessible to complete beginners
- Mix of corridos, ladainhas, and other song types

Include for each song:
- Portuguese title
- English translation
- Song type (corrido, ladainha, samba, etc.)
- Difficulty level (1-5)
- Why it's great for beginners
- Key vocabulary (5-7 words)
- Cultural significance (1 sentence)

**CRITICAL:** At the end, create a downloadable file using this format:

**[DOWNLOAD: capoeira-top-10-songs.md]**

Then provide the complete markdown content in a code block that I can download directly from Perplexity's UI. Look for a download icon or button next to the code block in the response.
```

---

## Prompt B: Generate Lesson for Specific Song

Copy everything below, **replace [SONG TITLE]**, then paste into Perplexity:

```
Using the 'Detailed Song Lesson Template', create a comprehensive lesson file for the Capoeira song: [SONG TITLE]

Include:
1. Basic metadata (date, status, source, type)
2. Media Links (search for YouTube, Spotify, Apple Music, YouTube Music)
3. Full Portuguese lyrics
4. Line-by-line English translation
5. Pronunciation guide (simplified, not IPA)
6. Complete vocabulary list - EVERY SINGLE WORD including:
   - Nouns (with gender)
   - Verbs (with tense/mood)
   - Adjectives
   - Prepositions and articles
   - Contractions (tá, pra, na, etc.)
   - Pronouns and conjunctions
7. Grammar analysis (verb forms, sentence patterns, repetition, poetic language)
8. Cultural and historical context (origin, significance, notable mestres)
9. Practice exercises (2 new sentences, 1 grammar question, recitation)

Critical: Include EVERY word from the song in the vocabulary table. Do not leave any word unexplained.

**CRITICAL:** At the end, create a downloadable file using this format:

**[DOWNLOAD: [song-name].md]**

Then provide the complete lesson in a code block. Perplexity will show a download button or icon next to the code block that lets me download the file directly.
```

---

## Example: A Maré Tá Cheia

```
Using the 'Detailed Song Lesson Template', create a comprehensive lesson file for the Capoeira song: A Maré Tá Cheia

Include:
1. Basic metadata (date, status, source, type)
2. Media Links (search for YouTube, Spotify, Apple Music, YouTube Music)
3. Full Portuguese lyrics
4. Line-by-line English translation
5. Pronunciation guide (simplified, not IPA)
6. Complete vocabulary list - EVERY SINGLE WORD including:
   - Nouns (with gender)
   - Verbs (with tense/mood)
   - Adjectives
   - Prepositions and articles
   - Contractions (tá, pra, na, etc.)
   - Pronouns and conjunctions
7. Grammar analysis (verb forms, sentence patterns, repetition, poetic language)
8. Cultural and historical context (origin, significance, notable mestres)
9. Practice exercises (2 new sentences, 1 grammar question, recitation)

Critical: Include EVERY word from the song in the vocabulary table. Do not leave any word unexplained.

**CRITICAL:** At the end, create a downloadable file using this format:

**[DOWNLOAD: a-mare-ta-cheia.md]**

Then provide the complete lesson in a code block. Perplexity will show a download button or icon next to the code block that lets me download the file directly.
```

---

## How to Use

1. **Pick a prompt** (A or B)
2. **Copy the entire text** (Ctrl+C / Cmd+C)
3. **Go to Perplexity.ai** in your browser
4. **Paste into the chat** (Ctrl+V / Cmd+V)
5. **Press Enter** to submit
6. **Wait for response** (usually 1-3 minutes)
7. **Look for the download icon** — next to the code block in Perplexity's response
8. **Click the download button** to save the file directly to your computer
9. **Select the location** (choose your `/songs/` folder)
10. **File saves automatically** as `.md`

**Note:** The download button appears automatically when Perplexity detects a code block with a clear filename.

---

## Troubleshooting

**Q: I don't see a download button next to the code block?**
A: Perplexity may not always show a download button. If missing, try asking Perplexity: "Create a downloadable file named [filename].md" at the start of a new message. Or fall back to: right-click the code block → Copy → Paste into text editor → Save as `.md`.

**Q: The download button is there but won't work?**
A: Try: Right-click the code block → "Copy" → Paste into text editor → Save as `.md` manually.

**Q: I got partial content?**
A: Perplexity sometimes truncates long responses. Ask it: "Continue the lesson from where you left off."

**Q: My `.md` file won't open?**
A: Make sure the file extension is `.md`, not `.txt`. Check your text editor's save settings.

**Q: The response looks wrong?**
A: Regenerate the response (look for a "Regenerate" or "Try Again" button in Perplexity).

---

## Organize Your Files

After downloading, store them here:

```
/Capoeira_Portuguese_Claude/
├── songs/
│   ├── a-mare-ta-cheia.md       ← Save song lessons here
│   ├── meu-deus.md
│   └── [other songs].md
├── lists/
│   └── top-10-songs.md          ← Save top 10 lists here
├── prompts/
│   ├── perplexity-song-prompt.md
│   ├── PERPLEXITY_QUICK_PROMPTS.md
│   └── PERPLEXITY_WORKFLOW.md
```

---

## Next Steps

1. Use Prompt B to generate a lesson for **"A Maré Tá Cheia"**
2. Save it as `a-mare-ta-cheia.md`
3. Test it in your learning app
4. Generate more songs as needed

