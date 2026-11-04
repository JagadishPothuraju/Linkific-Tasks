# Day 26 – Responsible AI Proof of Concept

This educational Python demo shows how a keyword-based résumé scoring rule can create group-level differences, and compares it with a skills-only scoring rule.

All records are synthetic. This is not a hiring tool or a validated fairness audit.

## Run
From this folder:
`python -m src.fairness_audit`

## Tests
`python -m pip install pytest`
`python -m pytest -q`

## Files
- `src/fairness_audit.py`: synthetic fairness audit
- `tests/`: test cases
- `docs/CASE_STUDY.md`: real-world case study
- `docs/PREVENTION_RECOMMENDATIONS.md`: prevention steps
- `docs/RESPONSIBLE_AI_GUIDELINES.md`: company guidelines

Selection-rate parity in a tiny synthetic sample does not prove fairness. Real systems require representative data, suitable metrics, expert review and ongoing monitoring.
