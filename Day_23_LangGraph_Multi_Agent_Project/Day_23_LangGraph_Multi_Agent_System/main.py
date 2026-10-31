from typing import TypedDict, List, Dict
from pathlib import Path
from datetime import datetime
import json, re, sys

try:
    from langgraph.graph import StateGraph, END
except ImportError:
    print("Install LangGraph first: python -m pip install -r requirements.txt")
    sys.exit(1)

BASE=Path(__file__).parent
KB=BASE/"data"/"knowledge_base.txt"
OUT=BASE/"outputs"
OUT.mkdir(exist_ok=True)

class State(TypedDict, total=False):
    user_request:str
    plan:List[str]
    research_notes:List[str]
    draft:str
    final_answer:str
    communication_log:List[Dict[str,str]]
    errors:List[str]
    status:str

def log(s, sender, receiver, message):
    entries=list(s.get("communication_log",[]))
    entries.append({"timestamp":datetime.now().isoformat(timespec="seconds"),
                    "sender":sender,"receiver":receiver,"message":message})
    return entries

def coordinator(s):
    request=s.get("user_request","").strip()
    if not request:
        return {"errors":["The user request is empty."],"status":"error",
                "communication_log":log(s,"Coordinator","Error Handler","Empty request; handle error.")}
    return {"plan":["Research Agent retrieves relevant notes","Writer prepares a response","Coordinator validates and returns the answer"],
            "status":"coordinating",
            "communication_log":log(s,"Coordinator","Research Agent","Research this request: "+request)}

def research(s):
    try:
        if not KB.exists(): raise FileNotFoundError("Knowledge base file is missing.")
        paras=[x.strip() for x in KB.read_text(encoding="utf-8").splitlines() if x.strip()]
        terms=set(w.lower() for w in re.findall(r"[A-Za-z0-9-]+",s["user_request"]) if len(w)>2)
        ranked=sorted(paras,key=lambda p:sum(w in set(re.findall(r"[A-Za-z0-9-]+",p.lower())) for w in terms),reverse=True)
        notes=[p for p in ranked if any(w in p.lower() for w in terms)][:5] or paras[:3]
        return {"research_notes":notes,"status":"researched",
                "communication_log":log(s,"Research Agent","Writer",f"Shared {len(notes)} research notes.")}
    except Exception as e:
        return {"errors":list(s.get("errors",[]))+["Research Agent: "+str(e)],"status":"error",
                "communication_log":log(s,"Research Agent","Error Handler","Research failed: "+str(e))}

def writer(s):
    try:
        notes=s.get("research_notes",[])
        if not notes: raise ValueError("No research notes received.")
        draft="# Research Response\n\n## User Request\n"+s["user_request"]+"\n\n## Research Notes\n"
        draft+="\n".join("- "+n for n in notes)
        draft+="\n\n## Summary\nThe notes provide a starting point for the request. Verify details with trusted, current sources before applying them to company decisions.\n\n## Limitation\nThis demonstration uses a local knowledge base, not live web search or a hosted LLM."
        return {"draft":draft,"status":"written",
                "communication_log":log(s,"Writer","Coordinator","Draft response prepared.")}
    except Exception as e:
        return {"errors":list(s.get("errors",[]))+["Writer: "+str(e)],"status":"error",
                "communication_log":log(s,"Writer","Error Handler","Writing failed: "+str(e))}

def error_handler(s):
    answer="The workflow could not complete.\n\n"+ "\n".join("- "+e for e in s.get("errors",["Unknown error"]))
    return {"final_answer":answer,"status":"failed",
            "communication_log":log(s,"Error Handler","Coordinator","Failure summary prepared; stopping safely.")}

def finalize(s):
    return {"final_answer":s.get("draft","No draft created."),"status":"completed",
            "communication_log":log(s,"Coordinator","User","Validated and returned final response.")}

def after_coord(s): return "error_handler" if s.get("status")=="error" else "research"
def after_research(s): return "error_handler" if s.get("status")=="error" else "writer"
def after_writer(s): return "error_handler" if s.get("status")=="error" else "finalize"

def build_graph():
    g=StateGraph(State)
    for name,fn in [("coordinator",coordinator),("research",research),("writer",writer),
                    ("error_handler",error_handler),("finalize",finalize)]:
        g.add_node(name,fn)
    g.set_entry_point("coordinator")
    g.add_conditional_edges("coordinator",after_coord,{"research":"research","error_handler":"error_handler"})
    g.add_conditional_edges("research",after_research,{"writer":"writer","error_handler":"error_handler"})
    g.add_conditional_edges("writer",after_writer,{"finalize":"finalize","error_handler":"error_handler"})
    g.add_edge("finalize",END); g.add_edge("error_handler",END)
    return g.compile()

def main():
    print("DAY 23 | LANGGRAPH MULTI-AGENT RESEARCH ASSISTANT")
    print("Coordinator -> Research Agent -> Writer -> Finalize")
    request=input("Enter your company project request: ").strip()
    initial={"user_request":request,"communication_log":[],"errors":[],"status":"started"}
    result=build_graph().invoke(initial)
    safe=re.sub(r"[^A-Za-z0-9_-]+","_",request).strip("_")[:40] or "empty_request"
    (OUT/f"response_{safe}.md").write_text(result.get("final_answer",""),encoding="utf-8")
    (OUT/f"communication_log_{safe}.json").write_text(json.dumps({
        "request":request,"plan":result.get("plan",[]),"status":result.get("status"),
        "errors":result.get("errors",[]),"communication_log":result.get("communication_log",[])
    },indent=2),encoding="utf-8")
    print("\nSTATUS:",result.get("status"))
    print("\nFINAL RESPONSE\n",result.get("final_answer",""))
    print("\nCOMMUNICATION LOG")
    for m in result.get("communication_log",[]): print(f"[{m['sender']} -> {m['receiver']}] {m['message']}")
    print("\nFiles saved in outputs/")

if __name__=="__main__": main()
