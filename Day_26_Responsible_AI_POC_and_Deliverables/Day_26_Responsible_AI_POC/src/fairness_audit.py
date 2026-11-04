from collections import defaultdict

# Synthetic teaching data only. Never use this demo to assess real applicants.
SAMPLE = [
    {"id": "A1", "group": "Group A", "skills": ["python", "sql", "ml"], "club": "coding club"},
    {"id": "A2", "group": "Group A", "skills": ["python", "sql"], "club": "robotics club"},
    {"id": "B1", "group": "Group B", "skills": ["python", "sql", "ml"], "club": "women's coding club"},
    {"id": "B2", "group": "Group B", "skills": ["python", "sql"], "club": "women's robotics club"},
]


def biased_score(r):
    club_name = (r.get("club") or "").lower()
    skills = r.get("skills") or []
    return len(skills) - (1 if "women" in club_name else 0)


def skills_only_score(r):
    return len(r.get("skills") or [])


def selection_rates(records, scorer, threshold=2):
    total, selected = defaultdict(int), defaultdict(int)

    for record in records:
        if not isinstance(record, dict):
            continue

        group = record.get("group") or "Unknown"
        total[group] += 1

        if scorer(record) >= threshold:
            selected[group] += 1

    return {
        group: (selected[group] / count if count else 0.0)
        for group, count in total.items()
    }


def audit(sample=None):
    records = SAMPLE if sample is None else sample
    return {
        "warning": "Synthetic demonstration only; not a validated fairness audit.",
        "biased_rule_selection_rates": selection_rates(records, biased_score),
        "skills_only_selection_rates": selection_rates(records, skills_only_score),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(audit(), indent=2))
