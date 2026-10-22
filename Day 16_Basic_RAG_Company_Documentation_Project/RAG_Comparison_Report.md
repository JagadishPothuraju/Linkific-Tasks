# RAG Retrieval Performance Comparison Report

**Project:** Company Documentation Q&A using RAG  
**Name:** [Your Name]  
**Date:** [Date]

## Objective
Build a basic Retrieval-Augmented Generation (RAG) pipeline and compare chunk sizes to understand their effect on retrieval and answer quality.

## Technologies
Python, Jupyter Notebook, Sentence Transformers, ChromaDB, LangChain text splitters, Pandas, and an optional LLM provider.

## Workflow
1. Load the company documentation.
2. Split it into 200, 500, and 1,000 character chunks with overlap.
3. Convert chunks and questions into embeddings.
4. Retrieve the top three semantically similar chunks.
5. Inspect the retrieved context and evaluate the answer.
6. Compare relevance, completeness, and groundedness.

## Evaluation rubric
- Relevance (1–5): Does the response answer the question?
- Completeness (1–5): Does it include the necessary information?
- Groundedness (1–5): Is it supported by the source document?
- Cosine similarity is a retrieval signal, not a direct answer-quality score.

## Results — fill after running the notebook
| Chunk size | Average relevance / 5 | Average completeness / 5 | Average groundedness / 5 | Observations |
|---|---:|---:|---:|---|
| 200 characters | [fill] | [fill] | [fill] | [fill] |
| 500 characters | [fill] | [fill] | [fill] | [fill] |
| 1,000 characters | [fill] | [fill] | [fill] | [fill] |

## Discussion
Smaller chunks may provide precise matches but can split related information. Larger chunks preserve more context but may include irrelevant text. Medium chunks can be a compromise, but the best size depends on the document and question set.

## Conclusion
In this experiment, chunk size **[fill after evaluation]** performed best because **[cite actual results]**. Do not claim a winner until you have run the experiment and inspected the outputs.

## Screenshots to include
1. Document loaded in notebook.
2. Chunking/retrieval output.
3. ChromaDB semantic search result.
4. Completed evaluation table.
5. GitHub repository after pushing the files.
