# System Explanation

## Architecture
LangGraph StateGraph coordinates five nodes: Coordinator, Research Agent, Writer, Error Handler, and Finalize. The Coordinator is the entry point. Conditional edges route valid requests to research and failures to the Error Handler.

## Agent roles
- Coordinator: accepts request, creates plan, validates final output.
- Research Agent: selects relevant paragraphs from the local knowledge base.
- Writer: converts notes into a structured response.
- Error Handler: reports errors and ends failed workflows safely.
- Finalize: stores the final answer and returns it to the user.

## State management
The TypedDict state contains request, plan, research notes, draft, final answer, communication log, errors, and status.

## Error handling
Empty input, missing knowledge-base file, missing research notes, and node exceptions are caught and routed to Error Handler. The workflow does not mark failed execution as completed.

## Limitation
The workflow is LangGraph-based but uses deterministic local retrieval and templated writing. It is not connected to a live LLM or web search.
