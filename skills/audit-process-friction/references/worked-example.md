# Worked example: HIV self-test kit collection, Lagos, Nigeria

An illustrative run, not a real audit. The program, counts, prices, and times are invented to show the shape of the output. The target behavior came from `define-key-behavior`; the Opportunity (physical) hypothesis came from `decompose-comb-barriers`.

**Input summary (illustrative):** a Lagos HIV self-testing program sends an SMS with a collection code to men aged 18 to 30 who registered at outreach events. About 3,000 codes a month go out; partner pharmacies log about 400 kits collected; about 90 results come back by USSD. A field officer will walk the process at three pharmacies; until then, times are estimates from staff.

```markdown
# Process friction audit

**Behavior:** Men aged 18 to 30 in Lagos who receive the program's SMS collect a free HIV self-test kit from a partner pharmacy within two weeks and report the result by USSD.
**Process:** From the first SMS (the collection code) to a result recorded by the USSD system.
**How this was audited:** Reconstructed from staff and documents; a field officer walks it at three pharmacies next week, after which the time cells become observations.

## Step log
| # | Step | Where | Time incl. waiting | Money | Documents | Decision demanded | Who controls | Tag | Why this tag | Completion loss |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Read SMS with code; read second SMS listing 25 pharmacies | Phone | 2 min (estimate) | 0 | None | Which pharmacy is nearest and open (no map, no hours) | Program | movable | The program can pick the nearest pharmacy from the registration area, or let him reply with his area | 3,000 in; no data |
| 2 | Travel to the pharmacy | Street | 35 min each way (estimate) | NGN 400 transport (illustrative) plus lost earnings | None | When to go, given work hours | Program (choice of partners) | movable | Could be a community distributor or delivery; biggest change, needs partners | no data |
| 3 | Queue at the pharmacy counter | Pharmacy | 10 to 25 min (estimate) | 0 | None | None | Pharmacy | movable | A dedicated counter or pre-announced slot removes the wait | no data |
| 4 | Show the code and a photo ID | Pharmacy | 2 min | 0 | Photo ID | None | Program | removable | The ID exists to prevent duplicate collection; the code plus phone number already does that; the ID screens out men without one and signals surveillance | no data |
| 5 | Fill the form: phone, age, address | Pharmacy | 5 min | 0 | None | Supply an address he may not want to give | Program | removable (address), movable (phone, age pre-filled from registration) | Address is not used downstream; phone and age are already held | about 400 collected |
| 6 | Pharmacist explains the kit | Pharmacy | 5 min | 0 | None | None | Pharmacy | necessary | Correct use and what to do with a positive result are safety content | no data |
| 7 | Take the kit home; find 20 private minutes; use it | Home | 20 min plus finding privacy | 0 | Instructions (English only) | When and where he can be alone | Program (instructions), user | necessary (use), movable (language) | The test itself cannot go; a Yoruba or Pidgin leaflet moves the reading burden | no data |
| 8 | Dial USSD; enter result; enter 12-digit kit serial | Phone | 5 min; retries if the session times out | 0 | The kit box (for the serial) | Find and type a 12-digit number | Program | removable (serial), movable (reporting) | The pharmacist can link the serial to the code at collection; a one-key SMS reply replaces the USSD chain | about 90 reported |

**Totals for one person:** 1 trip (2 legs), about 2 hours, NGN 400 plus lost earnings, 1 document, 4 decisions.

## Removable list, smallest first
1. Drop the address field; pre-fill phone and age from registration (program; this week); targets the form step; evidence: EAST "Make it easy".
2. Drop the 12-digit serial from USSD; the pharmacist records serial against code at collection (program; this month); targets the 400 to 90 loss; evidence: FAFSA, removing the burdensome part of a form is the assistance that worked.
3. Drop the photo ID; rely on the code and the registered phone number (program, with partner pharmacies' agreement); targets collection; evidence: Sunstein on sludge that screens selectively.
4. Replace "choose a pharmacy" with the nearest pharmacy named in the SMS, with opening hours (program); targets the SMS-to-collection loss.
5. Replace USSD with a one-key SMS reply (program plus telecom partner).
6. Dedicated counter or slot at pharmacies (pharmacy); targets the queue.
7. Community distributors or delivery (program plus new partners); biggest, last.
8. A clearer SMS (program); listed last because information alone did not move completion in the FAFSA experiment.

## Steps kept, and why
- Step 6, the pharmacist's explanation: safety content, including what to do after a positive result.
- Step 7, the test itself: it is the behavior.

## Expected effect, stated cautiously
Removals 1 to 4 target the collection step (3,000 to about 400) and removal 2 the reporting step (about 400 to 90). The nearest evidence is United States assistance-versus-information (FAFSA: 28% to 36% with help, nothing from information alone) and two LMIC experiments that removed one hassle each (Kenya fertilizer, Rajasthan camps). Applying the DellaVigna and Linos discount (academic 8.7 points versus unit 1.4), the honest statement is that program-controlled removals should raise collection and reporting, that reporting is the more likely to move because the serial entry is the single heaviest step, and that no number can be promised until the field walk and a two-week tally exist. A clearer SMS alone is not expected to move either loss.

## Barrier diagnosis (input to select-intervention-levers)
- Opportunity, physical: collection requires a trip, a queue, an ID, and an address, and reporting requires typing a 12-digit serial into a USSD session; walk-through evidence pending, staff reconstruction attached; removable list above.

## What to check before relying on this
- Every time cell is a staff estimate until the field officer's walk at three pharmacies.
- Partner pharmacies must agree to drop the ID check and to record serials; the telecom partner must agree to SMS reporting.
- Whether men who do not collect differ from those who do (no ID, working hours, distance); a two-week tally at the pharmacies would show it.
```
