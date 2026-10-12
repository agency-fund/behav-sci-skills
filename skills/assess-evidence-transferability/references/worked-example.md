# Worked example: moving the Afghanistan default-contribution finding to garment workers in Bangladesh

The program, the team's answers, and the discounted range are illustrative. The study facts are the ones recorded in the dossier for Blumenstock, Callen and Ghani (2018); nothing else about the study is asserted here.

**User's answers to Before you start.** Finding: Blumenstock, Callen & Ghani (2018), *American Economic Review*; 949 employees of one Afghan mobile-money firm (Roshan), salaries paid by mobile money; a 5% default contribution to a savings account versus a 0% default raised participation by 40 percentage points, equivalent to a 50% employer match; mechanism per the authors: present bias and the cognitive cost of deciding, not endorsement or inattention. User's case: a savings program at three garment factories in Gazipur, Bangladesh, about 6,000 workers (mostly young women, many first-generation wage earners, lower literacy) paid monthly into a mobile-money wallet introduced 18 months ago; the program would default a 5% salary deduction into a locked savings wallet, opt-out at the factory HR desk; outcome the team cares about: savings balance retained at 6 months. Implementer: factory HR with the wallet provider. Decision: a pilot in one factory, then scale to three; the current proposal quotes "a 40-point increase". Near-setting replications: none supplied. Cheap tests feasible: a short survey, interviews, and an A/B arm in the pilot.

```markdown
# Transferability assessment: Afghanistan 5% savings default (Blumenstock et al. 2018)

**Decision this informs:** a one-factory pilot, then scale to three factories; a proposal number is also at stake
**Finding:** Blumenstock, Callen & Ghani (2018), AER 108(10); 949 employees of one firm; a 5% default versus 0% raised participation by 40 points (equivalent to a 50% employer match); claimed mechanism: present bias plus the cognitive cost of deciding, not endorsement or inattention
**Near-setting replications supplied:** none supplied; treated as single-setting

## Fit, dimension by dimension

| Dimension | The study | Your case | Difference | Touches the mechanism? |
|---|---|---|---|---|
| Units (who, how many) | 949 salaried employees of one telecom firm, Afghanistan | About 6,000 garment workers, mostly young women, lower literacy, newer to formal wages | Gender, literacy, income level, familiarity with the wallet | unknown: present bias and decision cost are plausibly present in both; a lower wage makes a 5% deduction pinch more, which could raise opt-outs for reasons unrelated to the mechanism |
| Treatment (what, as delivered) | Automatic 5% contribution with opt-out through the wallet | Automatic 5% deduction with opt-out at the HR desk | Opt-out is costlier and socially visible | yes: the mechanism is decision cost; raising opt-out cost changes both the effect and whether participation reflects preference |
| Outcome (what was measured, when) | Participation (any contribution) | Balance retained at 6 months | A different construct; the study does not report retention | yes: the finding says nothing about whether money stays in the account |
| Setting (institutions, infrastructure, channel, literacy) | Payroll by mobile money already established; one employer | Wallet introduced 18 months ago; trust in it uncertain; strong remittance pressure on payday | If workers withdraw the full salary on payday to send home, a lock changes household cash flow, and opt-outs may be driven by family claims rather than present bias | yes |
| Implementer (who delivered, with what trust and capacity) | The employer, with a research team | Factory HR with the wallet provider; worker trust in HR is low in this sector | A default announced by HR may be read as a wage cut | yes: endorsement was not the study's mechanism, but distrust can drive opt-outs that the study did not face |

## Verdict
Transfers with modifications, because the decision-cost mechanism plausibly exists here but three rows (treatment, setting, implementer) change the conditions it ran under, and the outcome the team cares about was not measured in the study. The 40-point figure cannot be carried into the proposal.

## Discounted expected effect (provisional)
- Published effect: 40 percentage points on participation
- Published-to-field discount: the finding is a single-firm academic study; academic journal effects average several times the effect seen when units run the same kinds of interventions (8.7 against 1.4 points, DellaVigna and Linos 2022)
- Further discount for untested differences: HR-desk opt-out may inflate participation without reflecting preference (treatment row), so the planning range should refer to voluntary participation measured with a wallet-menu opt-out; remittance pressure (setting row) and HR distrust (implementer row) both push opt-outs up
- Range to hand to estimate-expected-effect: for participation, roughly 10 to 25 points with a wallet-menu opt-out, an illustrative judgment, not derived from a source; for balance retained at 6 months, no range from this study; provisional, not a planning number

## Assumptions to test locally
1. Workers do not withdraw the full salary on payday for remittances: one month of wallet transaction data with consent, or a five-item survey; would change the verdict if it failed? yes
2. Workers read the default as savings, not as a wage cut by HR: ten interviews before launch; yes
3. A wallet-menu opt-out keeps participation well above the 0% default arm: the pilot's A/B arm (HR-desk opt-out versus wallet-menu opt-out); no, but it changes the range
4. Participation persists as retained balance at 6 months: the pilot's own outcome, which the study cannot supply; yes, for the outcome the team cares about

## What to check before relying on this
- The setting row: payday remittance behavior is the assumption most likely to be wrong and the cheapest to check.
- Whether the decision-cost mechanism is present at all: if workers already make an active choice about every payday transfer, there is no passive default to exploit.
```

**What happened next (illustrative).** The team replaced "a 40-point increase" in the proposal with the provisional range and handed it to `estimate-expected-effect` for the planning number; assumptions 1 and 2 went into a two-week pre-pilot check before the A/B arm was designed.
