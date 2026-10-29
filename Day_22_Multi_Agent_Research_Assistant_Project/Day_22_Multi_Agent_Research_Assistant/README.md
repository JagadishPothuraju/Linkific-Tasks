# Day 22 — Multi-Agent Research Assistant

## Agents
- **Research Agent:** selects relevant notes from a local knowledge base.
- **Analyzer:** identifies themes, gaps, and recommendations.
- **Critic:** reviews completeness and flags limitations.
- **Writer:** creates a structured Markdown report.
- **Coordinator:** plans the workflow, logs hand-offs, validates outputs.

## Run
Requires Python 3.9+; no external packages or API keys are needed.

```bash
python main.py
```

Enter a topic such as `data quality and security`.

## Outputs
The program creates a Markdown research report and a JSON workflow-state/communication log inside `outputs/`.

## Limitation
This is a rule-based educational simulation, not a real LLM or live-web research system. Verify facts and add trusted sources before real-world use.
