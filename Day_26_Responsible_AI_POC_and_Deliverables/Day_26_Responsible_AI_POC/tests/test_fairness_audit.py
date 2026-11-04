import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.fairness_audit import SAMPLE, biased_score, skills_only_score, selection_rates, audit


def test_biased_rule_creates_group_difference():
    rates = selection_rates(SAMPLE, biased_score)
    assert rates["Group A"] > rates["Group B"]


def test_skills_only_rule_removes_keyword_penalty():
    rates = selection_rates(SAMPLE, skills_only_score)
    assert rates["Group A"] == rates["Group B"]


def test_audit_has_both_comparisons():
    result = audit()
    assert "biased_rule_selection_rates" in result
    assert "skills_only_selection_rates" in result


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-q"]))
