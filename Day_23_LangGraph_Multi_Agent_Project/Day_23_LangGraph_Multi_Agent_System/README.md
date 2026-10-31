# Day 23 — LangGraph Multi-Agent Research Assistant

Install (Python 3.9+):
```bash
python -m pip install -r requirements.txt
python main.py
```
Enter a company project request. The graph uses Coordinator → Research Agent → Writer → Finalize. Failures are routed to Error Handler.

Outputs in `outputs/`:
- `response_<request>.md`
- `communication_log_<request>.json`

This is a LangGraph-orchestrated educational prototype using a local knowledge base and deterministic Python logic. It does not call a hosted LLM or live web search.
