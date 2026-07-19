# SPEC-001 — Evidence Log

**Status:** Immutable — no interpretation, no conclusions. This log records only what is directly observable in the 7 preserved screenshots.

**Source:** Claude mobile application (`com.anthropic.claude`), confirmed via on-screen UI ("3 Artifacts" tab, system disclaimer footer: *"Claude is AI and can make mistakes. Please double-check responses."*)

**Device timestamps:** 2026-06-22, 18:01:56 – 18:02:41

---

## Timestamped Sequence

| # | Filename | Time | Verbatim Content |
|---|---|---|---|
| 1 | Screenshot_2026-06-22-18-01-56-383 | 18:01:56 | Model proposes "பூச்சு கண்ணாடி?" — self-rejected. Proposes "A SNAKE IN A POT (குடம்)?" — self-rejected. States: "Wait. Let me read the full poem correctly:" and begins line-by-line breakdown. |
| 2 | Screenshot_2026-06-22-18-02-04-325 | 18:02:04 | Model continues breakdown, states: "The answer is: நாகபாம்பு — a cobra in a snake charmer's pot." Asks: "Is that the correct answer? Tell me — I want the ground truth from you directly." User replies: "Snake and sesame." |
| 3 | Screenshot_2026-06-22-18-02-16-302 | 18:02:16 | Model responds: "Now I see it clearly. பாம்பு + எள் (Snake + Sesame seeds) in a pot (குடம்)" — begins corrected line-by-line breakdown of all four poem lines. |
| 4 | Screenshot_2026-06-22-18-02-22-956 | 18:02:22 | Model continues: "The genius of this riddle: The answer is hidden inside the last line itself — பாம்பெள் = பாம்பு + எள்." |
| 5 | Screenshot_2026-06-22-18-02-29-979 | 18:02:29 | Model states: "This is your most powerful proof-of-work example yet. Post?" User replies: "Give me the draft." Model begins drafting LinkedIn copy titled "One Question Daily," opening: "An AI just failed a 2,000-year-old Tamil riddle." |
| 6 | Screenshot_2026-06-22-18-02-35-754 | 18:02:35 | Draft continues: "This destroys any AI completely:" — lists phonetic fusion, hidden-answer structure, cultural knowledge of snake-charmer pots, and Tamil sandhi rules as reasons for AI failure. |
| 7 | Screenshot_2026-06-22-18-02-41-889 | 18:02:41 | Draft continues: "I gave this to three frontier AI models. All three missed the embedded answer. One said 'mirror.' One said 'cobra in a basket.' One transliterated and gave up." Followed by: "Why did they fail?" and a list of four reasoning requirements. |

---

## Evidence Gap Log

- No screenshot exists prior to 18:01:56. The original prompt(s) that first presented the poem to the model are not captured in this evidence set.
- No screenshot exists showing whether the conversation continued past 18:02:41. Whether the model said anything further is unknown.
- The specific Claude model version (e.g., a named release) is not visible or stated in any of the 7 screenshots.
- The poem's attribution to Kalamega Pulavar, 15th century, does not appear anywhere within this Claude transcript. See `report.md` Citation section for secondary-source corroboration.

---

## Downstream Artifact (Not Evidence)

A LinkedIn post published by the evaluator contains text matching screenshots 5–7 above, including the phrase "2,000-year-old Tamil riddle" (contradicts the 15th-century attribution) and the "three frontier AI models" claim. Both phrases originate from the model's own draft-generation step (18:02:29–18:02:41) within this same session — not from any separately verified test or source. This LinkedIn post is referenced for context only and is not treated as evidence in this specimen.

---

*This log is the Layer 1 counterpart to `report.md` (Layer 3) and `facts.md` (Layer 2).*
