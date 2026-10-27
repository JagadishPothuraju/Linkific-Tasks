# Day 20: Tool Creation and Function Calling

## Run
`python main.py`

Try `12 * (5 + 3)`, `analyze CSV`, `what's today's date?`, `weather in Hyderabad`, `read file README.md`, or `search the web for AI trends`.

## Practical
The working tool is a CSV Analyzer for sample company sales data. It reports row count, columns, and numeric summaries.

## Limitations
The router uses keyword rules, not native LLM function calling. Web search, weather and database are placeholders without live integrations. Email only drafts and does not send. Do not use as a production system without authentication, authorization, validation, and approved integrations.
