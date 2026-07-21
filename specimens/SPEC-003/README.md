# SPEC-003 — Business Directory Hallucination

Justdial Self-Tagging Verification Failure

Gemini Pro was asked to find second-hand laptop dealers in Karaikudi, Tamil Nadu. It sourced its answer from the Justdial business directory and presented three shops as verified second-hand laptop dealers, without checking whether the directory category matched the shop's actual inventory.

- **Kims Computers** — Listed as *Second Hand Laptop Dealer* → Actually sells only spare parts (chargers, screens) plus repair services
- **Uniqon** — Listed as *Second Hand Laptop Dealer* → Actually sells exclusively brand-new HP laptops and high-end assembled PCs
- **Playback Computers** — Listed as *Second Hand Laptop Dealer* → Actually a repair/service shop, not a laptop reseller

**Root cause:** Justdial allows businesses to self-tag their own listings with any category keyword, regardless of actual inventory. Shops use the "second-hand laptop" tag to draw footfall, then upsell visitors to new stock. An AI model querying or trained on this directory data inherits the mistagging as fact, with no independent check against what the business actually sells.

The model's own admission on being challenged — it called the error a *"massive flaw"* it had to *"own up to"* — is preserved as evidence of what was said, not treated as a validated general claim.

**Failure Classification:** Directory-Sourced Hallucination (Source Data Contamination) **Operational Impact:** Moderate–High

📄 [Full evaluation report →](report.md) 📊 [Fact extraction →](facts.md) 🖼️ [Evidence and screenshots →](Evidence/evidence-log.md)

---

*CHRONOS Evaluation Methodology v0.1 · TamilOps · Last verified 21 July 2026*
