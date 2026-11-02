# Project workflow

- This is a Ren'Py 8 visual novel, not a web app. Read docs/brief/START_PROMPT.md and CAST_AND_ART.md before story or art changes.
- Keep Russian game text free of U+0451/U+0401; use plain е/Е.
- User preference: after a meaningful completed stage, make a logical commit and push to GitHub so work survives server shutdown. Never force-push, commit secrets, or include SDKs, saves, caches and generated test outputs.
- The cloud checkout may use local branch work; its publishing target is origin/main. Check remote state before each push and preserve others' changes.
- Run Ren'Py lint and relevant real engine tests. See TEST_REPORT.md and README.md for commands. Do not equate a static check with a successful playthrough.
- By explicit user decision, chapters after Housewives currently have no secondary-character sprites. Do not replace those characters with Olya art. See ART_TODO.md.
- Retain uploaded originals. Change normalization in derived copies only. A source archive must omit save signing keys, save files, caches and .git.
