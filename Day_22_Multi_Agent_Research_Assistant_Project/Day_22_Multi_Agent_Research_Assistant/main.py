from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import json, re

ROOT = Path(__file__).parent
KB = ROOT / "data" / "knowledge_base.txt"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

@dataclass
class SharedState:
    topic: str
    plan: list = field(default_factory=list)
    research_notes: list = field(default_factory=list)
    analysis: dict = field(default_factory=dict)
    critique: dict = field(default_factory=dict)
    draft: str = ""
    messages: list = field(default_factory=list)
    status: str = "started"
    def send(self, sender, receiver, message):
        self.messages.append({"time": datetime.now().isoformat(timespec="seconds"),
                              "from": sender, "to": receiver, "message": message})

class Coordinator:
    name = "Coordinator"
    def plan(self, s):
        s.plan = ["Research Agent gathers notes", "Analyzer identifies themes and gaps",
                  "Critic reviews quality", "Writer drafts report", "Coordinator validates outputs"]
        s.send(self.name, "Research Agent", "Research topic: " + s.topic)
        s.status = "planned"
    def validate(self, s):
        s.status = "reviewed" if s.research_notes and s.analysis and s.critique and s.draft else "needs_attention"

class ResearchAgent:
    def run(self, s):
        paragraphs = [x.strip() for x in KB.read_text(encoding="utf-8").splitlines() if x.strip()]
        terms = set(w.lower() for w in re.findall(r"[A-Za-z0-9-]+", s.topic) if len(w) > 2)
        ranked = sorted(paragraphs, key=lambda p: sum(w in set(re.findall(r"[A-Za-z0-9-]+", p.lower())) for w in terms), reverse=True)
        s.research_notes = ranked[:6]
        s.send("Research Agent", "Analyzer", f"Shared {len(s.research_notes)} research notes.")
        s.send("Research Agent", "Coordinator", "Research phase complete.")

class Analyzer:
    def run(self, s):
        text = " ".join(s.research_notes).lower()
        words = ["data", "risk", "quality", "customer", "process", "evidence", "security", "review"]
        themes = [w for w in words if re.search(r"\\b"+w+r"\\b", text)]
        s.analysis = {"note_count": len(s.research_notes), "themes": themes,
                      "gaps": ["Local knowledge may be incomplete or outdated.",
                               "Verify important claims against trusted sources."],
                      "recommendations": ["Separate facts from assumptions.",
                                          "Record source names and dates.",
                                          "Use a review step before publishing."]}
        s.send("Analyzer", "Critic", "Analysis and evidence gaps are ready.")
        s.send("Analyzer", "Writer", "Use themes and recommendations in the report.")

class Critic:
    def run(self, s):
        issues = []
        if len(s.research_notes) < 2: issues.append("Limited evidence; add more sources.")
        if not s.analysis.get("themes"): issues.append("No clear themes detected.")
        issues.append("Verify facts and citations before external use.")
        s.critique = {"checks": ["Notes exist", "Themes checked", "Limitations stated"],
                      "issues": issues, "decision": "review_required" if len(issues)>1 else "approved_with_caveats"}
        s.send("Critic", "Writer", "Review feedback: " + "; ".join(issues))
        s.send("Critic", "Coordinator", "Critique completed.")

class Writer:
    def run(self, s):
        notes = "\\n".join("- " + n for n in s.research_notes)
        themes = ", ".join(s.analysis.get("themes", [])) or "No dominant themes detected"
        recs = "\\n".join("- " + x for x in s.analysis.get("recommendations", []))
        issues = "\\n".join("- " + x for x in s.critique.get("issues", []))
        s.draft = f"""# Research Assistant Report: {s.topic}

## Executive Summary
This report was prepared by a simulated multi-agent workflow. Research gathered local notes, Analyzer identified themes, Critic reviewed evidence limitations, and Writer assembled the report.

## Research Notes
{notes}

## Analysis
- Notes reviewed: {s.analysis.get('note_count', 0)}
- Themes: {themes}

## Recommendations
{recs}

## Critic Review and Limitations
{issues}

## Conclusion
Use this report as a starting point. Add verified sources and expert review before important decisions.
"""
        s.send("Writer", "Coordinator", "Draft report is ready.")

def main():
    print("DAY 22 | MULTI-AGENT RESEARCH ASSISTANT")
    print("Coordinator -> Research Agent -> Analyzer -> Critic -> Writer")
    topic = input("Enter your company project/topic: ").strip() or "Company project research"
    s = SharedState(topic)
    c = Coordinator(); c.plan(s)
    ResearchAgent().run(s); Analyzer().run(s); Critic().run(s); Writer().run(s); c.validate(s)
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", topic).strip("_")[:45] or "research"
    (OUT/f"research_report_{safe}.md").write_text(s.draft, encoding="utf-8")
    (OUT/f"workflow_state_{safe}.json").write_text(json.dumps({
        "topic": s.topic, "plan": s.plan, "analysis": s.analysis,
        "critique": s.critique, "status": s.status, "messages": s.messages
    }, indent=2), encoding="utf-8")
    print("\\nWorkflow status:", s.status)
    print("Report and shared-state JSON saved in outputs/")
    print("\\n--- REPORT PREVIEW ---\\n", s.draft[:1200])
    print("\\n--- COMMUNICATION LOG ---")
    for m in s.messages: print(f"[{m['from']} -> {m['to']}] {m['message']}")

if __name__ == "__main__": main()
