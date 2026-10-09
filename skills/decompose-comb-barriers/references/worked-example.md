# Worked example: Nairobi market vendors and the M-Pesa savings deposit

This example continues the running case used across the skills ported from Joe Speed's prototype. The target behavior came from `define-key-behavior`; the context came from `map-audience-context`. It is illustrative, not a real diagnosis.

**Target behavior (from `define-key-behavior`):** "Female stall vendors in Gikomba and Toi markets deposit that day's net cash surplus into an M-Pesa savings wallet before leaving the market, each trading day."

```markdown
# COM-B barrier hypotheses

**Target behavior:** Female stall vendors in Gikomba and Toi markets deposit that day's net cash surplus into an M-Pesa savings wallet before leaving the market, each trading day.

## Capability
### Physical
- **Hypothesis:** Lacks fluency with the specific M-Pesa savings-lock menu sequence (distinct from ordinary send-money use, which vendors already do daily).
  **Persistence test:** Would persist even with full information and access; this is a specific-skill gap, not an access gap. Capability confirmed.
  **Diagnostic question:** Can the vendor complete a savings-lock deposit unassisted when asked to demonstrate it?
  **Discriminates because:** An Opportunity-only barrier would predict success once handed a working phone or agent; this predicts failure even then.
### Psychological
- **Hypothesis:** Can't reliably estimate "net cash surplus" without formal bookkeeping, so has nothing confident to deposit.
  **Persistence test:** Would persist even with full market access and no social cost; this is a calculation-capability gap. Capability confirmed.
  **Diagnostic question:** Given a day's sales and costs verbally, can the vendor state a surplus figure within a plausible range?
  **Discriminates because:** A Motivation barrier would predict the vendor could state a figure but chooses not to act on it; this predicts she cannot state one confidently at all.

## Opportunity
### Physical
- **Hypothesis:** The M-Pesa agent queue at closing time is long enough that depositing costs stall-minding time vendors won't spend.
  **Diagnostic question:** What is the average agent wait time at closing hour versus mid-day?
  **Discriminates because:** If wait time is short, this barrier is ruled out regardless of what vendors say about "not having time".
### Social
- **Hypothesis:** Visible cash-counting or depositing at closing invites informal borrowing requests from neighboring vendors (named in the audience and context brief).
  **Diagnostic question:** Do vendors report changing behavior (timing, location) specifically to avoid being seen with cash?
  **Discriminates because:** A purely physical-Opportunity barrier would not predict vendors actively concealing the act itself.

## Motivation
### Reflective
- **Hypothesis:** Doesn't trust mobile-money savings products to hold value as reliably as cash in hand or a *chama*.
  **Diagnostic question:** Asked directly, does the vendor rank M-Pesa savings below *chama* or cash at home for trustworthiness?
  **Discriminates because:** A Capability or Opportunity barrier would not produce a stated trust ranking; only a Motivation barrier would.
### Automatic
- **Hypothesis:** Habitual full hand-over of the day's cash to a spouse or household member at home crowds out any deposit step beforehand.
  **Diagnostic question:** Does the vendor report the hand-over happening "automatically", without a decision point, on most days?
  **Discriminates because:** A reflective-Motivation barrier would involve a considered choice each day; this predicts no decision point at all.

## Most likely barrier(s), pending diagnostic answers

| Hypothesis | Context support | Field cost |
|---|---|---|
| Opportunity/Social: visible cash invites borrowing requests | High: directly named in the audience and context brief's environmental constraints | Low: one round of vendor interviews |
| Motivation/Automatic: habitual full hand-over at home | Medium: plausible given context, not yet directly observed | Low: same interview round |
| Capability/Psychological: can't estimate surplus | Medium: informal bookkeeping is common in this sector generally | Medium: needs a short verbal-estimation exercise, not just a question |

The Opportunity/Social hypothesis is the top provisional candidate: it is both the most directly supported by existing context data and the cheapest to confirm. This remains provisional until the diagnostic questions above are actually run in the field.
```
