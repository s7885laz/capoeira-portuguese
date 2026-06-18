# Perplexity Song Script Workflow Guide

## Problem Solved
Files saved to `/root/output` in Perplexity aren't directly downloadable from the UI. This guide provides **three methods** to get your files.

---

## Method 1: Copy-Paste from Code Block (Easiest)

### Steps:
1. Ask Perplexity for a lesson using the prompt from `perplexity-song-prompt.md`
2. Perplexity will output the content in a markdown code block
3. **Right-click the code block** → **Select "Copy"**
4. Open a text editor (VS Code, Notepad, etc.)
5. **Paste** the content
6. **Save as:** `song-name.md` in your desired folder

### Pros:
- No technical setup needed
- Works from any device
- Direct, simple process

### Cons:
- Manual copy-paste each time

---

## Method 2: Use Perplexity's Artifact Feature (If Available)

If Perplexity supports artifacts/inline rendering:

1. Ask Perplexity to render the output as an **interactive artifact**
2. Look for a **Download button** in the artifact interface
3. Click to download directly as `.md`

### Pros:
- One-click download
- Built into Perplexity UI

### Cons:
- Only works if Perplexity has this feature enabled

---

## Method 3: Use Python Script to Access `/root/output` (Advanced)

If you have SSH/CLI access to Perplexity's backend (unlikely, but possible):

```bash
# List files in /root/output
ls -la /root/output/

# Copy to accessible location
cp /root/output/song-name.md ~/Downloads/song-name.md

# Or via SSH if remote:
scp user@perplexity-server:/root/output/song-name.md ~/Downloads/
```

### Cons:
- Requires backend access (not standard Perplexity feature)
- Adds complexity

---

## Recommended Workflow

**Use Method 1 (Copy-Paste) as your default:**

### Your process:
1. Open Perplexity in browser
2. Paste the prompt from `perplexity-song-prompt.md`
3. Specify: `[Song Title]` (e.g., "A Maré Tá Cheia")
4. Wait for response
5. Right-click code block → Copy
6. Paste into text editor
7. Save to `/Users/lazarovitsbence/workspaces/Projects/Capoeira_Portuguese_Claude/songs/`
8. Use the `.md` file in your learning app

---

## Improved Prompt Setup

The updated `perplexity-song-prompt.md` now includes:

✅ **Explicit download instructions** for Perplexity to follow  
✅ **Code block formatting** so content is easy to copy  
✅ **Clear filenames** (e.g., `capoeira-top-10-songs.md`)  

---

## Next Steps

1. **Test the workflow:**
   - Go to Perplexity
   - Use the prompt from `perplexity-song-prompt.md`
   - Ask for a lesson on any Capoeira song
   - Copy the code block output
   - Verify the `.md` file works in your app

2. **If Perplexity adds native file download support** in the future:
   - Update this guide with the new process
   - You can skip the manual copy-paste

3. **Store organized files:**
   ```
   /Capoeira_Portuguese_Claude/
   ├── songs/
   │   ├── a-mare-ta-cheia.md
   │   ├── meu-deus.md
   │   └── ...
   ├── top-10-songs.md
   └── prompts/
       └── perplexity-song-prompt.md
   ```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Code block won't copy | Try: Select all text manually → Ctrl+C |
| File won't open after saving | Check file extension is `.md` not `.txt` |
| Content looks corrupted | Re-copy; some special chars may not paste. Retype manually or use UTF-8 text editor |
| Perplexity shows error | Check prompt syntax; regenerate the response |

---

## Your Updated Prompt Examples

### Option A (Top 10 Songs):
```
Using the 'Top 10 Songs List Template' from the Perplexity Song Generation Prompt, 
generate a curated list of the 10 most popular Capoeira songs suitable for beginner 
Portuguese learners. Focus on songs that are widely taught, culturally significant, 
and linguistically accessible.

IMPORTANT: Wrap your complete list in a markdown code block with download instructions.
```

### Option B (Specific Song):
```
Using the 'Detailed Song Lesson Template' from the Perplexity Song Generation Prompt, 
create a comprehensive lesson file for the Capoeira song: A Maré Tá Cheia

Include all metadata, media links, authentic Portuguese lyrics, English translations, 
pronunciation guide, vocabulary, detailed grammar analysis, cultural context, and 
practice exercises.

IMPORTANT: Wrap your complete lesson in a markdown code block with download instructions.
```

---

## Why This Works

- ✅ Bypasses `/root/output` file system issue
- ✅ Uses Perplexity's UI natively (no hacks needed)
- ✅ Creates files directly on your computer
- ✅ Integrates with your workflow immediately
- ✅ Scalable for multiple songs

