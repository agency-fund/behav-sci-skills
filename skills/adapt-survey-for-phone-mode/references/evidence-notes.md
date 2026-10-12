# Evidence notes: adapt-survey-for-phone-mode

Every source below comes from `docs/plan/2026-10-skill-expansion-dossier.md` (compiled 2026-10-12). Verification tags are carried over as the dossier gives them; nothing has been upgraded or added from memory. Numbers appear only as the dossier writes them.

## Anchor sources

### Hoogeveen, J., Dabalen, A., et al. (2016). *Mobile Phone Panel Surveys in Developing Countries: A Practical Guide for Microdata Collection* [verified-crossref]
World Bank. https://doi.org/10.1596/978-1-4648-0904-0.
- The practitioner manual for running panel surveys by mobile phone in developing countries. The dossier records no numbers from it.
- The dossier does not say which specific practices the guide covers, so this skill attributes to it only its subject (mobile phone panel surveys in LMICs), not any particular rule.

### Gourlay, S., et al. (2021). Viewpoint: High-frequency phone surveys on COVID-19: Good practices, open questions [verified-crossref]
*Food Policy*, 105, 102153. https://doi.org/10.1016/j.foodpol.2021.102153.
- Good practices and open questions from the high-frequency phone surveys run during COVID-19; the dossier ties both anchor sources to the LSMS high-frequency phone surveys. No numbers recorded.

### J-PAL. *Resources for conducting remote surveys* [verified-fetch: https://www.povertyactionlab.org/resource/resources-conducting-remote-surveys]
- Quoted: "surveys should be kept to a 30 minute call at most". This is the only verified number for this skill.
- Covers survey length, respondent tracking, and call scheduling.
- Does not cover mode effects or IVR. The dossier instructs drafters not to attribute mode-effect or IVR guidance to this page, and this skill does not.
- The research report's "shorten to about 15–20 minutes" is [unverified, author to confirm]; the dossier says do not quote it. This skill names it only to say it is unverified.

### World Bank LSMS and DIME Wiki pages [unverified, author to confirm]
- Returned 403 in the research session; nothing from them is used.

## The dossier's boundary conditions (not attributed to a single source)
- Replace showcards with verbal unfolding scales.
- Plan the call protocol (scheduling, recording attempts, replacing respondents, matching surveyors by language) and incentives.
- Test for mode effects against a face-to-face subsample.

These three lines are the dossier's summary for the entry. This skill applies them as its procedure and does not pin any of them to a page in the anchor sources.

## What this skill adds beyond the dossier (practitioner judgment, author to confirm)
- The gender and wealth check on who owns, and who answers, a shared phone.
- The privacy check before sensitive items and the default to drop them on a shared phone.
- The IVR guidance in step 3 (one idea per prompt, a keypad mapping read aloud, a repeat option, pilot the option count). No cited source was confirmed to cover IVR.
- The pre-specified decision rule in the mode-effect check.

## Non-WEIRD evidence
- Both anchor sources are LMIC-native: developing-country panel surveys (World Bank guide) and the LSMS high-frequency COVID-19 phone surveys (Gourlay et al.). The dossier records no response rates, attrition figures, or mode-effect estimates from them.

## Replication status
- Procedural. The one finding the dossier states for this entry is that phone samples skew toward phone owners. Whether answers differ by mode is an open question in the sources, hence the mode-effect check rather than an assumption of comparability.

## Known corrections and cautions (from the dossier)
- The 30-minute ceiling is verified; "15–20 minutes" is not.
- Do not attribute mode-effect or IVR guidance to J-PAL's page.
- The plan assigned no io types to this skill; it uses `survey-items` for both consumes and produces, per the drafting brief, because it transforms an instrument into an instrument.

## What to check locally
- Phone ownership and sharing by gender and wealth in the actual frame, not in national statistics.
- Network coverage and the times of day people can be reached (work hours, electricity for charging).
- Whether airtime incentives can be delivered to the number types in the frame, and the going amount.
- Which items are sensitive here, including ones that are not sensitive elsewhere.
- Whether a face-to-face subsample is feasible; if not, which earlier face-to-face round overlaps enough for a comparison.
- Enumerator language match against the respondent pool, including dialects.
