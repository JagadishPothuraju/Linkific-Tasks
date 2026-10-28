"""Benchmark sync (v1) vs async (v2). Start the server first:
    uvicorn app.main:app --workers 1
Then:  python benchmark/bench.py
Writes benchmark/results.csv and prints a markdown table."""
import asyncio
import csv
import statistics
import time

import httpx

BASE = "http://127.0.0.1:8000"
LEVELS = (10, 50, 100)
RUNS = 3
ORDER = {"customer_email": "a@b.com", "item": "book", "quantity": 2}


async def burst(client, method, url, n, **kw):
    async def one():
        t = time.perf_counter()
        r = await client.request(method, url, **kw)
        r.raise_for_status()
        return (time.perf_counter() - t) * 1000

    t0 = time.perf_counter()
    lat = sorted(await asyncio.gather(*[one() for _ in range(n)]))
    total = time.perf_counter() - t0
    return {"avg": statistics.mean(lat), "p95": lat[max(int(.95 * n) - 1, 0)],
            "rps": n / total}


async def median_run(client, method, url, n, **kw):
    runs = [await burst(client, method, url, n, **kw) for _ in range(RUNS)]
    return {k: statistics.median(r[k] for r in runs) for k in runs[0]}


async def main():
    cases = [("GET /users/1", "GET", "/api/{v}/users/1", {}, LEVELS),
             ("POST /orders", "POST", "/api/{v}/orders", {"json": ORDER}, (50,))]
    rows = []
    limits = httpx.Limits(max_connections=300)
    async with httpx.AsyncClient(base_url=BASE, timeout=120, limits=limits) as c:
        for name, method, path, kw, levels in cases:
            for n in levels:
                s = await median_run(c, method, path.format(v="v1"), n, **kw)
                a = await median_run(c, method, path.format(v="v2"), n, **kw)
                imp = (1 - a["avg"] / s["avg"]) * 100
                rows.append([name, n, f"{s['avg']:.0f}", f"{a['avg']:.0f}",
                             f"{s['p95']:.0f}", f"{a['p95']:.0f}",
                             f"{s['rps']:.1f}", f"{a['rps']:.1f}", f"{imp:.0f}%"])
                print(rows[-1])
    head = ["Endpoint", "Concurrency", "Sync avg ms", "Async avg ms", "Sync p95",
            "Async p95", "Sync RPS", "Async RPS", "Avg latency improvement"]
    with open("benchmark/results.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(head); w.writerows(rows)
    print("\n| " + " | ".join(head) + " |")
    print("|" + "---|" * len(head))
    for r in rows:
        print("| " + " | ".join(map(str, r)) + " |")


asyncio.run(main())
