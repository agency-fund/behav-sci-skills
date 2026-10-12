# Worked example: timing a latrine-kit offer in Indonesian CLTS villages

Setting: an illustrative sanitation program ("Desa Bersih", 40 villages in East Java) that has already run community-led total sanitation (CLTS) triggering. The target behavior came from `define-key-behavior`; the lever from `select-intervention-levers`; the calendar rows from the district field team. All numbers are illustrative, not findings.

**Inputs the user gave.** Ask: households without an improved latrine buy a pour-flush pan-and-pipe kit from the local mason cooperative (illustrative price Rp 450,000, about a week of a farm laborer's earnings) and build before the rains. Lever: Enablement, BCT 12.5 Adding objects to the environment (the kit offered at the village meeting with delivery). Confirmed barriers: cash is spent before the dry season ends (present bias confirmed in interviews) and the kit is hard to transport. Natural window: construction needs the dry season. Landmarks named by the field team: the main rice harvest, the second harvest, Lebaran (Eid al-Fitr), the school year start in July, and the Independence Day village clean-up on 17 August.

```markdown
# Delivery moment plan

**The ask:** Households in triggered villages without an improved latrine buy a pour-flush kit from the mason cooperative (Rp 450,000, illustrative) at the village meeting and build it before the rains. Cost at the moment of action: a cash outlay of about one week's laborer earnings, plus a half day of digging.
**Confirmed barrier:** Cash set aside for the latrine is spent before the dry season ends; present bias is among the confirmed barriers (interviews, 2 villages). Transport of the kit is a second, physical-opportunity barrier the delivery offer addresses.

## Income and expense calendar
| Period | Cash in | Cash out | Net position | Source |
|---|---|---|---|---|
| Jan to Feb | little (rainy season, no harvest) | food purchases, debt | trough | field team |
| Mar to Apr | main rice harvest sale | repay input credit | flush | field team |
| May to Jun | wage work, remittances | Lebaran spending (date moves; field team supplies it) | trough in the Lebaran weeks, neutral otherwise | field team; Lebaran date assumed, confirm |
| Jul | some second-crop sales | school fees, uniforms | trough | field team |
| Aug to Sep | second harvest sale | village clean-up contributions | flush | field team |
| Oct to Dec | little | rains begin; construction stops by November | neutral, window closing | field team |

## Temporal landmarks
| Landmark | Date(s) | Cash position | Frame it offers | Evidence |
|---|---|---|---|---|
| Main harvest sale | late Mar to Apr | flush | "the harvest money" | Kenya post-harvest RCT (liquidity), transfers as a mechanism, not a number |
| Lebaran | lunar date, field team confirms | trough | "a clean start" | fresh-start is US archival only; untested here |
| School year start | mid-Jul | trough | none useful | n/a |
| Second harvest sale | Aug to Sep | flush | "before the rains" | liquidity, as above |
| Independence Day clean-up | 17 Aug | neutral | "the village competition" | untested here; social, not temporal |

## The behavior's natural window
Dry season, roughly May to October; pits and slabs cannot be built once the rains start in November. Nothing clinical or administrative fixes a date inside the window.

## Chosen moment
- **When:** The village meeting held within 14 days of the main harvest sale (late April), with a second offer within 14 days of the second harvest sale (early September) for households that missed the first.
- **Mechanism:** Liquidity first (harvest cash present), with the dry-season window as the reason-now. No salience landmark is claimed; Lebaran is rejected as a frame because it is a cash trough.
- **Evidence it rests on:** Duflo, Kremer and Robinson (Kenya): a small, time-limited offer right after harvest raised fertilizer use by 14 and 18 points; one field RCT, a different behavior and country, so the direction transfers, not the number.
- **Rejected moments:** at triggering (whenever the facilitator is scheduled: no cash check); Lebaran (trough); July (fees due); October (window closing, rains risk).

## Deadline rule
The cooperative price with free delivery holds for 14 days after each meeting, because present bias is a confirmed barrier and the offer is meant to catch the cash before it goes. After 14 days the kit stays available at the standard price without delivery; the September meeting repeats the offer.

## Equity check
Landless laborers paid daily have no harvest flush. Fallback: the September offer coincides with peak wage demand for harvest labor, and the cooperative accepts two installments across the two meetings (to be confirmed with the cooperative; a lock-in version would be `design-commitment-device`).

## What to test
Villages randomized to the post-harvest meeting offer versus the program's default (the offer made at the triggering meeting, whenever scheduled). Outcome: kits bought within 30 days and latrines verified built before 1 November. Run by the district team with the M&E lead; cadence of follow-up messages goes to `design-reminder-schedule`.

## What to check before relying on this
- The harvest sale dates: they vary by village irrigation status; the calendar uses the district modal dates.
- Whether 17 August's clean-up has any pull on latrine building; it is in the table as untested and is not used.
```

**Where this run stopped.** It did not write the meeting script or the SMS (that is `draft-lever-content`), did not set how many reminders follow the meeting (`design-reminder-schedule`), and did not design the installment lock (`design-commitment-device`).
