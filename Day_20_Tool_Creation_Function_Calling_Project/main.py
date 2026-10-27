import ast, csv, datetime as dt, operator, re
from pathlib import Path
ROOT=Path(__file__).parent
def calculator(expr):
    ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow,ast.Mod:operator.mod,ast.USub:operator.neg}
    def ev(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)): return n.value
        if isinstance(n,ast.BinOp) and type(n.op) in ops: return ops[type(n.op)](ev(n.left),ev(n.right))
        if isinstance(n,ast.UnaryOp) and type(n.op) in ops: return ops[type(n.op)](ev(n.operand))
        raise ValueError("Only basic arithmetic is supported")
    try: return f"Result: {ev(ast.parse(expr,mode='eval').body)}"
    except Exception as e: return f"Calculator error: {e}"
def date_tool(): return "Today's date: "+dt.date.today().isoformat()
def file_reader(name):
    p=(ROOT/name).resolve()
    if ROOT not in p.parents: return "File error: access outside project folder is not allowed"
    try: return p.read_text(encoding="utf-8")[:3000]
    except Exception as e: return f"File error: {e}"
def data_analyzer(name="data/company_sales.csv"):
    p=(ROOT/name).resolve()
    if ROOT not in p.parents: return "Analyzer error: path not allowed"
    try:
        with p.open(newline="",encoding="utf-8-sig") as f: rows=list(csv.DictReader(f))
        if not rows: return "CSV has no data rows"
        out=[f"Rows: {len(rows)}", "Columns: "+", ".join(rows[0])]
        for col in rows[0]:
            vals=[]
            for row in rows:
                try: vals.append(float(row[col]))
                except (ValueError,TypeError): pass
            if vals: out.append(f"{col}: sum={sum(vals):.2f}, average={sum(vals)/len(vals):.2f}, min={min(vals):.2f}, max={max(vals):.2f}")
        return "\\n".join(out)
    except Exception as e: return f"Analyzer error: {e}"
def database_tool(q): return f"Database demo only; no live database configured. Request: {q}"
def web_search(q): return f"Web search demo only; connect a search API for live results. Request: {q}"
def weather_tool(city): return f"Weather demo only; connect a weather API for live conditions. City: {city}"
def email_tool(to,subject,body): return f"Email draft (not sent)\\nTo: {to}\\nSubject: {subject}\\n{body}"
def choose_tool(q):
    s=q.strip(); l=s.lower()
    if not s: return "Please enter a request."
    if any(k in l for k in ["weather","temperature","forecast"]):
        m=re.search(r"(?:in|for|at)\\s+([A-Za-z .'-]+)$",s,re.I); return weather_tool(m.group(1) if m else "unspecified city")
    if "email" in l: return email_tool("recipient@example.com","Follow-up","Demo draft; review before sending.")
    if any(k in l for k in ["today's date","current date","date today","what date"]): return date_tool()
    if any(k in l for k in ["analyze csv","sales data","average sales","analyze data"]): return data_analyzer()
    if any(k in l for k in ["read file","read the file","open file"]):
        m=re.search(r"(?:read file|read the file|open file)\\s+(.+)",s,re.I); return file_reader(m.group(1).strip() if m else "README.md")
    if any(k in l for k in ["database","employee record","customer record","query the db"]): return database_tool(s)
    if any(k in l for k in ["search the web","web search","search online","latest information"]): return web_search(s)
    expr=re.sub(r"^(calculate|compute|what is)\\s+","",s,flags=re.I).rstrip("? ")
    if re.fullmatch(r"[\\d\\s.+\\-*/()%]+",expr): return calculator(expr)
    return "No matching tool. Rephrase or choose calculator, date, CSV analyzer, file reader, database, web search, weather, or email."
def main():
    print("Day 20 Tool Calling Demo. Try: 12 * (5 + 3) | analyze CSV | what's today's date? | weather in Hyderabad")
    print("Type exit to stop.")
    while True:
        q=input("\\nYour request: ").strip()
        if q.lower() in ("exit","quit"): break
        print("\\n"+choose_tool(q))
if __name__=="__main__": main()
