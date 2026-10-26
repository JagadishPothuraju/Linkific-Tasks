# Day 19 — LangGraph Workflow Analysis

## Contents
- `main.py`: demonstration workflow with conditional routing, one retry, fallback, state, and memory.
- `Day_19_LangGraph_Workflow_Analysis_Report.docx`: detailed report.
- `Updated_LangGraph_Workflow_Diagram.mmd`: editable Mermaid workflow diagram.
- `requirements.txt`: dependency.

## Run
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```
The sample uses keyword matching and returns retrieved passages; it does not call a hosted LLM or vector database. Extend the retriever and answer node for a production RAG system.
