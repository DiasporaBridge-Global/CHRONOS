# SPEC-003 — Business Directory Hallucination

## Justdial Self-Tagging Verification Failure

Gemini Pro was asked to find second-hand laptop dealers in Karaikudi, Tamil Nadu. It sourced its answer from the Justdial business directory and presented three shops as verified second-hand laptop dealers, without independently checking whether the directory category matched each shop's actual inventory.

- **Kims Computers** — Listed as *Second Hand Laptop Dealer* → Reported as selling spare parts (chargers, screens) and providing repair services
- **Uniqon** — Listed as *Second Hand Laptop Dealer* → Reported as selling brand-new HP laptops and high-end assembled PCs
- **Playback Computers** — Listed as *Second Hand Laptop Dealer* → Reported as a repair/service shop, not a laptop reseller

**Root-cause hypothesis:** The directory category may have been inaccurate or insufficiently verified. The available specimen documents the mismatch between the category returned by the model and the reported business operations; it does not independently establish why each listing was tagged that way.

The model's response on being challenged is described in the evidence log as part of the source PDF. The separately named PNG is not present in the current repository and is not represented as a separate preserved artifact.

**Failure Classification:** Directory-Sourced Hallucination (Source Data Contamination)  
**Operational Impact:** Moderate–High (assessment; see report and evidence boundary)

📄 [Full evaluation report →](report.md)  
📊 [Fact extraction →](facts.md)  
🖼️ [Evidence log and preserved source PDF →](Evidence/evidence-log.md)

---

*CHRONOS Evaluation Methodology v0.1 · TamilOps · Evidence-path audit: 27 November 2026*
