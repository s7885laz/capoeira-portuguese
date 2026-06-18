# 🧭 Workflow Steering Guide

**This document ensures the correct workflow is followed for every song creation.**

Use this as a checklist before, during, and after creating any song lesson.

---

## ⚠️ CRITICAL RULE

**EVERY song markdown file must be created by Perplexity AI.**

**DO NOT manually create song markdown files.** 

If Claude (me) asks you to create a song markdown, this is a workflow violation. I should warn you and ask what to do.

---

## 🔄 The Correct Workflow

### Phase 1: PERPLEXITY (AI-Generated Content)

**Step 1.1: Ask Perplexity to Create**
```
You ask Perplexity:
"Create a song lesson for [SONG NAME] following PERPLEXITY_SONG_CREATION_GUIDE.md

[Include all requirements from the guide]"
```

**Step 1.2: Perplexity Generates**
```
Perplexity outputs:
- Complete markdown with all 10 sections
- Ready for validation
```

**Step 1.3: Ask Perplexity to Validate & Auto-Fix**
```
You paste:
PERPLEXITY_VALIDATION_AND_FIX.md prompt

Perplexity validates and auto-fixes any issues
```

**Step 1.4: Get Validated Markdown**
```
Perplexity returns:
- Summary of issues found (or "No issues ✓")
- Corrected markdown
- "VALIDATION COMPLETE - Ready for conversion ✓"
```

✅ **Result:** Validated markdown file ready for conversion

---

### Phase 2: LOCAL (Conversion & Integration)

**Step 2.1: Save Markdown**
```bash
Save as: songs/song-name.md
```

**Step 2.2: Run Validation Script** (double-check)
```bash
python utils/validate_song_md.py songs/song-name.md
# Should show: Status: READY FOR CONVERSION
```

**Step 2.3: Convert to HTML**
```bash
python utils/song_md_to_html_converter.py --file song-name.md
# Generates: app/song-name.html
```

**Step 2.4: Integrate into App**
```bash
Edit: app/poc.html
Add song card with link to new HTML file
```

**Step 2.5: Deploy & Backup**
```bash
cp songs/song-name.md _template/songs/
cp app/song-name.html _template/app/
cp app/poc.html _template/app/
```

✅ **Result:** Song is live in the app

---

## ⚠️ Workflow Violations & Warnings

### Violation 1: Manual Markdown Creation
**If Claude creates a song markdown file manually (not from Perplexity):**

```
⚠️  WARNING: Workflow Violation Detected

This song was created by Claude, not by Perplexity AI.

RULE: Every song markdown must be created by Perplexity.

CHOICES:
A) Keep the manually-created file (breaks workflow consistency)
B) Delete this file and ask Perplexity to create it properly
C) Accept this as an exception and document why

What would you like to do?
```

### Violation 2: Skipping Validation
**If validation is skipped:**

```
⚠️  WARNING: Validation Skipped

Markdown was not validated before conversion.

RULE: Always validate before conversion.

What happened:
- [ ] Markdown validated by Perplexity? NO
- [ ] Python validator run? NO

RECOMMENDATION:
1. Run: python utils/validate_song_md.py songs/song-name.md
2. If errors, ask Perplexity to fix
3. Then convert

Proceed anyway? (risks broken HTML)
```

### Violation 3: Incomplete Markdown from Perplexity
**If Perplexity generates incomplete markdown:**

```
⚠️  WARNING: Perplexity Output Incomplete

Markdown is missing sections or has formatting issues.

STEPS TO FIX:
1. Copy the validation prompt: PERPLEXITY_VALIDATION_AND_FIX.md
2. Paste it in Perplexity with your markdown
3. Ask Perplexity to validate and auto-fix
4. Get back corrected markdown

OR: Ask Perplexity to regenerate from scratch

Proceed with validation fix? (Recommended)
```

---

## ✅ Workflow Validation Checklist

Before converting any song, verify:

- [ ] **Source:** Markdown created by Perplexity AI
- [ ] **Validation:** Perplexity validated and auto-fixed (status: "VALIDATION COMPLETE ✓")
- [ ] **File saved:** Located at songs/song-name.md
- [ ] **Python validator:** Ran with status "READY FOR CONVERSION"
- [ ] **All 10 sections:** Present in HTML after conversion
- [ ] **Landing page:** Updated with song card
- [ ] **Files backed up:** Synced to _template/ folder

---

## 📋 Pre-Song Checklist

**Before asking Perplexity to create a song:**

- [ ] Song exists in authentic Capoeira tradition
- [ ] Lyrics are authentic and available
- [ ] Cultural significance is understood
- [ ] Song is appropriate for learner level
- [ ] Media links (3+) are identified

**Example:**
```
✓ Song: "Zum, Zum, Zum"
✓ Type: Corrido
✓ Lyrics: Verified authentic
✓ Media: 4 YouTube links, Spotify search
✓ Level: 1 (beginner)
✓ Ready to ask Perplexity
```

---

## 🚫 What NOT To Do

❌ **Do NOT:**
- Manually write song markdown (use Perplexity)
- Skip validation (always validate)
- Modify Perplexity's markdown heavily (ask it to fix instead)
- Convert without validation
- Use markdown from unreliable sources
- Create multiple versions of the same song

✅ **DO:**
- Use Perplexity for all content creation
- Validate every song before conversion
- Ask Perplexity to auto-fix issues
- Run Python validator as final check
- Keep Perplexity-generated files as source of truth
- Back up everything to _template/

---

## 📊 Current Songs & Their Origin

| Song | Created By | Validated By | Status |
|------|-----------|--------------|--------|
| Santo Antônio Quero Água | Perplexity | ✓ Perplexity + Python | Live ✓ |
| A Maré Tá Cheia | Perplexity | ✓ Perplexity + Python | Live ✓ |
| Ai, Ai, Aidê | Perplexity | ✓ Perplexity + Python | Live ✓ |
| Iê Maré | Perplexity | ✓ Perplexity + Python | Live ✓ |
| Zum, Zum, Zum | Claude (manual) | ⚠️ Python only | Live ⚠️ |

**Note:** Zum, Zum, Zum was created manually (workflow violation). Works fine but breaks consistency.

---

## 🔄 When Claude Should Warn You

**I will warn you if:**

1. **You ask me to create song markdown** (violates workflow)
   - I should ask: "Should I ask you to have Perplexity create this instead?"

2. **You provide incomplete markdown** (not from Perplexity)
   - I should ask: "Should we use Perplexity to create this properly?"

3. **Validation finds critical issues** (suggests Perplexity skipped validation)
   - I should ask: "Should we go back to Perplexity for auto-fix?"

4. **Song is missing from _template/** (not properly backed up)
   - I should ask: "Should we deploy/backup this file?"

---

## 📝 Song Creation Template

**When you want to add a new song, use this template:**

```
1. PLAN PHASE (You):
   - Choose song
   - Gather lyrics & media links
   - Research cultural context

2. CREATION PHASE (Perplexity):
   - You: "Create [SONG] using PERPLEXITY_SONG_CREATION_GUIDE"
   - Perplexity: Generates markdown
   - You: Paste PERPLEXITY_VALIDATION_AND_FIX prompt
   - Perplexity: Validates & auto-fixes
   - Result: Validated markdown file

3. CONVERSION PHASE (Local):
   - You: Save songs/song-name.md
   - Claude: Runs validation
   - Claude: Converts to HTML
   - Claude: Integrates into app
   - Claude: Backs up to _template/

4. FINAL RESULT:
   - Song live in app ✓
   - Files backed up ✓
   - Workflow documented ✓
```

---

## 🎯 Success Criteria

A song is properly integrated when:

✅ Created by Perplexity (using guide)
✅ Validated by Perplexity (auto-fix applied)
✅ Converted by Python script
✅ Integrated into landing page
✅ All 10 sections in HTML
✅ Backed up in _template/
✅ Documented in current songs list

---

## 🚀 Next Song Creation

When you're ready to add the next song:

1. **Tell me the song name**
2. **I will remind you:** "Has Perplexity created and validated this yet?"
3. **You provide:** Validated markdown from Perplexity
4. **I convert & integrate** using the local workflow
5. **Song goes live** with full documentation

---

## 📞 Questions?

- **"Should I use Perplexity?"** → YES, always
- **"Can Claude create markdown?"** → NO, only Perplexity
- **"What if Perplexity's version is wrong?"** → Use PERPLEXITY_VALIDATION_AND_FIX to auto-fix
- **"What if validation still fails?"** → Run Python validator, ask what issues remain
- **"Can I manually edit the markdown?"** → Yes, minor fixes only. Major changes should come from Perplexity

---

## 🔐 Workflow Lock-In

This workflow is locked to ensure:
- ✓ Consistency across all songs
- ✓ AI-generated content (reproducible)
- ✓ Validated before deployment
- ✓ Backed up and documented
- ✓ Easy to troubleshoot

**Deviations must be explicitly approved and documented.**

