# Basic RAG — Company Documentation Q&A

## Files
- `Basic_RAG_Chunk_Size_Comparison.ipynb`: main notebook
- `data/company_handbook.txt`: synthetic sample documentation
- `RAG_Comparison_Report.md`: report template
- `response_evaluation_template.csv`: response scoring template
- `requirements.txt`: Python dependencies

## Run
1. Open the notebook in Google Colab or Jupyter.
2. Upload the `data` folder alongside the notebook (or change `doc_path`).
3. Run cells in order.
4. Inspect retrieved passages for chunk sizes 200, 500, and 1,000 characters.
5. Fill evaluation scores from actual outputs and write a conclusion based on evidence.

The main experiment measures retrieval. An optional LLM section shows how to add answer generation. Never publish secrets or confidential documents.
