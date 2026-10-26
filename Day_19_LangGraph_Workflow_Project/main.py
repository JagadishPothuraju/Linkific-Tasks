from typing import TypedDict, List, Optional
from langgraph.graph import StateGraph, START, END

class RAGState(TypedDict, total=False):
    question: str
    documents: List[str]
    answer: str
    memory: List[str]
    attempts: int
    error: Optional[str]

KNOWLEDGE = [
    "Planned leave should be requested at least five working days in advance.",
    "IT support tickets should include a short description, device name, and error message.",
    "Expense claims with receipts should be submitted within 30 days of purchase."
]

def retrieve(state: RAGState) -> RAGState:
    # Demonstration keyword retriever; replace with ChromaDB/FAISS in a full project.
    q = state.get("question", "").lower()
    matches = [d for d in KNOWLEDGE if any(w in d.lower() for w in q.split() if len(w) > 3)]
    attempts = state.get("attempts", 0) + 1
    return {"documents": matches, "attempts": attempts,
            "error": None if matches else "No relevant passages found."}

def route(state: RAGState) -> str:
    if state.get("documents"):
        return "answer"
    if state.get("attempts", 0) < 2:
        return "retry"
    return "fallback"

def retry(state: RAGState) -> RAGState:
    # A simple query refinement for demonstration.
    return {"question": state.get("question", "") + " policy information"}

def answer(state: RAGState) -> RAGState:
    # Replace with an LLM call grounded only in retrieved documents.
    return {"answer": "\\n".join(state.get("documents", [])), "error": None}

def fallback(state: RAGState) -> RAGState:
    return {"answer": "I could not find reliable information in the available documents. Please rephrase your question or provide a relevant document.",
            "error": state.get("error") or "Retrieval returned no results."}

def update_memory(state: RAGState) -> RAGState:
    history = list(state.get("memory", []))
    history.append(f"Q: {state.get('question','')} | A: {state.get('answer','')}")
    return {"memory": history[-10:]}

builder = StateGraph(RAGState)
builder.add_node("retrieve", retrieve)
builder.add_node("retry", retry)
builder.add_node("answer", answer)
builder.add_node("fallback", fallback)
builder.add_node("memory", update_memory)
builder.add_edge(START, "retrieve")
builder.add_conditional_edges("retrieve", route, {
    "answer": "answer", "retry": "retry", "fallback": "fallback"
})
builder.add_edge("retry", "retrieve")
builder.add_edge("answer", "memory")
builder.add_edge("fallback", "memory")
builder.add_edge("memory", END)
graph = builder.compile()

if __name__ == "__main__":
    q = input("Ask a company-policy question: ").strip()
    if not q:
        q = "How many days in advance should planned leave be requested?"
    result = graph.invoke({"question": q, "documents": [], "answer": "", "memory": [], "attempts": 0, "error": None})
    print("\\nANSWER:\\n", result.get("answer", ""))
    print("\\nDOCUMENTS:\\n", result.get("documents", []))
    print("\\nATTEMPTS:", result.get("attempts", 0))
    print("\\nERROR:", result.get("error"))
    print("\\nMEMORY:", result.get("memory", []))
