# The-Career-Engineered-Portfolio
Project Title: Josh Mathai IT/cybersecurity Portfolio

Live Link: (https://joshmathai.github.io/The-Career-Engineered-Portfolio/)


The Orchestration Log: The AI initially suggested adding a full framework/backend, which was unnecessary for a GitHub Pages deployment. I corrected the plan by switching to a lightweight static site (HTML/CSS) to keep hosting simple, fast, and secure while still meeting the assignment’s CTA and professionalism requirements.

## Portfolio Plan record

Updated November 10, 2026 · IS218–003 · Plan due November 12, 2026, 2:30 p.m. Eastern.

- Career research: [browsable research site](https://joshmathai.github.io/The-Career-Engineered-Portfolio/research/)
- [Repository](https://github.com/JoshMathai/The-Career-Engineered-Portfolio) · [research source](research/index.html)
- [AI/programming exploration research site](https://joshmathai.github.io/The-Career-Engineered-Portfolio/programming-research/) · [source](programming-research/index.html). This distinct URL belongs in Creative Project Plan. Both sites are cross-linked and share this repository. The museum is not being substituted for it.

This is the continuing project record, not an additional report. Public research, dates, original-source links, role criteria, three duties per role, evidence gaps, comparison, audience assumptions, two visual drafts, four stories, and a next experiment are [on the research site](research/index.html). Full career reflection, full personal role comparison, and personal eligibility circumstances belong in private Canvas.

### Decisions and scope

Research question: what evidence should an NJIT IT & Cybersecurity candidate build now for entry-level NJ/NY opportunities while exploring future AI engineering work?

Keep the existing IT Support / SOC Analyst / Security Analyst direction. The three AI employer descriptions inform longer-term learning; they do not establish entry-level fit. A local entry-level original posting remains the next research gap. The proposed troubleshooting lab is planned, with no claimed result.

Primary reader: an entry-level IT/cybersecurity recruiter; alternative: a project client. Reader needs remain hypotheses. Voice: clear, practical, accountable; brand character: Sage. Compare an evidence grid and editorial narrative using the same content. Provisionally choose the grid for scanning; have a partner validate the decision. Retain HTML/CSS, the black palette, white buttons, and GitHub Pages from AGENTS.md. Add research at `/research/` while retaining the existing portfolio. No audio or narration is used.

AI assisted research summarization, structure, HTML/CSS, and checks. Original employer text was retrieved and checked against the summaries on November 10. Palantir’s page required a direct HTTP fetch after the search reader returned 403. Unknown deadlines remain “not stated.” Palantir’s old embedded posting date is separated from the current access date. AI title novelty, universal remote work, and automatic entry-level suitability are not supported claims. Verification of the summaries does not prove the employer still accepts applications or that the candidate qualifies.

### Partner review loop

**Status: pending.** Owner confirmed no partner presentation or feedback has occurred. The public issues API returned no open issues on November 10. No peer approval, review change, or retry result is claimed.

Give a partner the [task on the site](research/index.html#review). Have them try before explaining. Record specific feedback using the [GitHub issue template](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/issues/new?template=career-review.md). As owner, accept/defer with a reason, link accepted documentation changes and actual verification, then have the same reviewer retry the affected task. Record the result before closing a resolved issue.

Issue: pending · Owner response: pending · Accepted change: pending · Verification: pending · Reviewer retry: pending.

### Verification log

- Employer sources: retrieved November 10, 2026; details and source/date limitations appear beside each role. All 17 distinct external research links returned HTTP 200; Palantir succeeded on retry after a temporary 502.
- Local HTML, fragment, and asset checks: passed November 10; reproduce with `python3 scripts/check_site.py`.
- Browser/mobile/keyboard checks: not run. Browser preview access was declined by the browser security gate. Responsive CSS, native links, headings, a skip link, and focus styles are present; these are not a substitute for an actual browser check.
- GitHub Pages: both research URLs returned HTTP 200 on November 10, and their HTML matched the pushed source byte-for-byte. [Pages deployment/check log](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/actions/runs/42889246638).
- Partner review and reviewer retry: not run.
- Cross-links: both research sites link to each other, their source, and this record.

### Canvas short update

Change: [research implementation commit](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/commit/156a06ed409374104073603fe0ca0a8633f74d5b) · Check: [reproducible checker](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/blob/156a06ed409374104073603fe0ca0a8633f74d5b/scripts/check_site.py) and [deployment log](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/actions/runs/42889246638). Peer issue/change/retry links remain pending real feedback.

Current work: [career research site](https://joshmathai.github.io/The-Career-Engineered-Portfolio/research/) · [repository](https://github.com/JoshMathai/The-Career-Engineered-Portfolio) · [same project record](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/blob/main/README.md#portfolio-plan-record). Add the actual review issue/change/check links after review; do not claim pending work is complete.

Changed / Added source-based career research, public direction comparison, and two portfolio layout drafts.

Checked / Original sources and external links, local link/fragment checks, and both published pages matching source; browser and partner checks not run.

Next / Present both sites to a partner and record feedback and retry. Coin Dash is now the owner-selected programming topic.

## Creative Project Plan record

Updated November 11, 2026 · IS218–003 · Plan due November 12, 2026, 2:30 p.m. Eastern.

[Coin Dash research site](https://joshmathai.github.io/The-Career-Engineered-Portfolio/programming-research/) · [repository/source](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/tree/main/programming-research) · [career research site](https://joshmathai.github.io/The-Career-Engineered-Portfolio/research/).

### Owner decision and Plan scope

Josh selected **Coin Dash** on November 11, replacing Synthetic Log Lab. Run to collect a coin within ten seconds; each collection resets the timer. Difficulty gradually reduces available coins from six to a minimum of two and increases placement distance. At every reset, at least one coin must be reachable with reaction time allowed, but the player chooses which to chase without a safe-coin marker. Poor choices can still lose. All initial tuning values are hypotheses.

The [browsable plan](programming-research/index.html) contains the question, rules, two game concepts, two audience/presentation approaches and first-screen sketches, Dream/Promise/Experiment, original dated sources, chosen stack and fallback, five checkable stories, and a rough account/task/data sketch. This is the same continuing record, not another report or a completed game.

**Stack decision:** Godot/GDScript for a small 3D game; Blender is optional for simple GLB character/coin assets after a primitive greybox works. Compare with a 2D Canvas/JavaScript fallback. Investigate a Django/SQLite account-and-score wrapper using maintained framework authentication. The research sites remain HTML/CSS on GitHub Pages; the eventual account app needs server hosting. Nothing has been installed or provisioned for the game/backend.

**Working promise:** account → gameplay/replay → saved score → private dashboard → edit display name/change password with current-password verification. Keep ownership server-enforced. No enemies, obstacles, multiplayer, public rankings, or complex character animation in the initial scope. Client score reporting is not cheat-proof. The optional creative experiment does not replace the full required account journey.

### Evidence and next check

AI assisted the plan and mathematical probe. Source capabilities were verified against official Godot, MDN, and Django documentation on November 11. Godot's original import guide establishes the Blender/GLB workflow. The timer, web export, asset import, and account integration still require execution in their actual stack. No human playtest or Blender work is claimed.

- **Run:** `python3 programming-research/fairness_probe.py`
- **Actual output:** [fairness-results.txt](programming-research/fairness-results.txt) · [probe source](programming-research/fairness_probe.py).
- **Assumptions:** 60×40 arena, constant speed 5 units/second, 10-second clock, 2-second reserve; a maximum 40-unit safe path. The player has no obstacles or acceleration in this model.
- **Observed November 11:** random-only placement had no reachable coin in 162/5,000 samples; guarded placement had at least one in 5,000/5,000. Bounds, minimum distance, unique positions, coin-count floor, 30 forced fallback cases, and a reachability boundary passed.
- **Limit:** a fixed-seed geometric sample, not a universal proof or human/gameplay fairness result. No timer/collision, Godot browser export, account/database, or actual gameplay checks have run.
- **Site checks:** `python3 scripts/check_site.py` passed for three HTML pages and 31 local references; unique IDs, one main heading per page, language/viewport metadata, and résumé PDF signature checked. Browser visual/mobile/keyboard checks remain unrun after the earlier preview denial.
- **Source-link check:** all eight technical/course links on the Coin Dash page returned HTTP 200 on November 11.
- **Change:** [Coin Dash implementation commit](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/commit/3421ddd) · [successful GitHub Pages deployment](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/actions/runs/43048026814). The live Coin Dash page, probe source, and result file returned HTTP 200 and matched the pushed files byte-for-byte on November 11. Peer feedback remains separate from this implementation.

**Next experiment:** make a primitive Godot arena, verify a single-thread Compatibility web export, and measure actual time to one of the last two coins. Tune distance/reserve after a short partner session. The [five stories and checks](programming-research/index.html#plan) also cover replay, score persistence, private data, and account maintenance for later work. Compare a simple spawn function with a placement-strategy interface; retain the simpler design unless the interface helps compare the two policies.

### Partner review

[Programming research feedback template](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/issues/new?template=programming-review.md).

Task: trace Timer documentation → ten-second reset rule → gameplay story; explain the reachable-coin guarantee and its limits; compare first-screen sketches. Log an actual observed problem, owner response, accepted change, verification, and the same reviewer's retry before closing the issue. Topic approval from the owner does not count as peer review.

Issue: pending · Owner response: pending · Accepted peer change: pending · Verification of peer change: pending · Reviewer retry: pending.

### Creative Project Plan — Canvas short update

Current work: [Coin Dash research site](https://joshmathai.github.io/The-Career-Engineered-Portfolio/programming-research/) · [repository](https://github.com/JoshMathai/The-Career-Engineered-Portfolio) · [same project record](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/blob/main/README.md#creative-project-plan-record) · [fairness check source](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/blob/main/programming-research/fairness_probe.py) and [actual output](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/blob/main/programming-research/fairness-results.txt). [Implementation change](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/commit/3421ddd) · [successful publication check](https://github.com/JoshMathai/The-Career-Engineered-Portfolio/actions/runs/43048026814). Add actual peer issue/change/retry links when available.

Changed / Replaced Synthetic Log Lab with Coin Dash: rules, two concepts, audience/layout options, sources, stack comparison, five stories, and account/data plan.

Checked / Original technical sources, local site references, a 5,000-layout fairness model, and published files matching source after successful Pages deployment. Engine/gameplay/account/browser and partner checks not run.

Next / Build the greybox, test the ten-second rule and browser export, and complete real partner feedback and retry.
