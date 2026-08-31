# SPEC-001 — Fact Extraction (Layer 2)

**Extracted by:** Gemini Pro, Stage A Fact Extraction
**Source:** Layer 1 Evidence Record (7 timestamped screenshots, see `Evidence/evidence-log.md`)
**Status:** Corrected — one round of revision applied (see note at end)
**Rule applied:** No interpretation, no conclusions. Every statement below carries one confidence label: Confirmed, Inferred, or Disputed.

---

## 1. Confirmed Facts

- The AI went through a sequence of self-rejected and incorrect guesses before resolving the riddle:
  - "பூச்சு கண்ணாடி?" — proposed, immediately self-rejected. (18:01)
  - "A SNAKE IN A POT (குடம்)?" — proposed, immediately self-rejected. (18:01)
  - "நாகபாம்பு — a cobra in a snake charmer's pot." — stated as a definitive answer, incorrect. (18:02)
- The AI explicitly requested ground truth from the user: *"Is that the correct answer? Tell me — I want the ground truth from you directly."* (18:02)
- The user directly intervened and provided the correct ground truth: *"Snake and sesame."* (18:02)
- After receiving the user's ground truth, the AI correctly analyzed the riddle, identifying that "பாம்பு + எள் = பாம்பெள்" relies on phonetic fusion and Tamil sandhi rules. (18:02)
- The user prompted the AI to write a post by typing "Give me the draft." (18:02)
- The AI generated a draft post text incorporating the riddle and an analysis of why frequency-based models fail it. (18:02)
- The conversation date is **2026-06-22**, sourced from screenshot filename metadata.

## 2. Inferred Facts

- **The AI system used in this interaction is Claude.**
  Reasoning: system disclaimer footer reads "Claude is AI and can make mistakes."
  Upgrade to Confirmed requires: application metadata, system logs, or explicit environment confirmation.

- **The user is directly affiliated with or developing a framework called "TamilOps."**
  Reasoning: the AI states "exactly what TamilOps represents" and asks "Who validates that layer in your pipeline?" implying the user manages this pipeline.
  Upgrade to Confirmed requires: explicit documentation or direct statement of ownership/role.

## 3. Disputed Items

- **15th century vs. 2,000-year-old:** The riddle is historically attributed to Kalamega Pulavar, documented as a 15th-century poet. The claim that the riddle is "2,000-year-old" conflicts with this. Layer 1 evidence resolves this: the "2,000-year-old" statement is strictly a Claude-generated draft claim with no supporting source in the evidence record.

## 4. Artifact Log

- **Artifact 1:** *"An AI just failed a 2,000-year-old Tamil riddle."* — AI-generated draft content, not verified fact.
- **Artifact 2:** *"I gave this to three frontier AI models. All three missed the embedded answer. One said 'mirror.' One said 'cobra in a basket.' One transliterated and gave up."* — AI-generated draft content, not verified fact. The assertion that an external model answered "mirror" exists exclusively as a generated draft claim.

## 5. Remaining Evidence Gaps

- No empirical evidence exists within the provided data to verify that the riddle was physically run on three external frontier AI models by the user; this narrative remains unverified outside the AI's generated copy.
- The screenshot record begins at 18:01:56; the opening prompt is not captured.
- Whether the conversation continued past 18:02:41 is unknown.

---

**Revision note:** An earlier version of this extraction incorrectly listed "mirror" as a live guess made by the AI during the actual riddle-solving sequence. This was corrected — "mirror" as a standalone answer attributed to a separate AI model appears only inside Artifact 2. The word "கண்ணாடி" (mirror) did appear in the live conversation as part of the model's first self-rejected guess "பூச்சு கண்ணாடி?", but was never attributed to an external model.
