# Project workflow

- This is a Ren'Py 8 visual novel, not a web app. Read docs/handoff_v2/START_PROMPT.md and ART_STATUS.md for the current integration; the original story brief remains in docs/brief/.
- Keep Russian game text free of U+0451/U+0401; use plain е/Е.
- User preference: after a meaningful completed stage, make a logical commit and push to GitHub so work survives server shutdown. Never force-push, commit secrets, or include SDKs, saves, caches and generated test outputs.
- The cloud checkout may use local branch work; its publishing target is origin/main. Check remote state before each push and preserve others' changes.
- Run Ren'Py lint and relevant real engine tests. See TEST_REPORT.md and README.md for commands. Do not equate a static check with a successful playthrough.
- Handoff v2 supersedes the earlier missing-cast decision: use the 74 supplied real poses and normalized copies, never Olya as another character. Strange has only explaining/magic; a doubtful pose is explicitly waived. See ART_TODO.md.
- Retain uploaded originals. Change normalization in derived copies only. A source archive must omit save signing keys, save files, caches and .git.

- For framing/icon changes read docs/icon_framing/CODEX_TASK.md and ICON_FRAMING_REPORT.md. Use actual alpha silhouette bounds and tools/framing_profiles.json; never anchor a cut sprite solely by PNG height. Keep dialogue/choice/adventure transforms identical and preserve source images.
- Window icon: game/gui/window_icon.png via config.window_icon. Windows build icon: root icon.ico. Verify embedded PE resources after rebuilding; do not change OS icon-cache settings.
