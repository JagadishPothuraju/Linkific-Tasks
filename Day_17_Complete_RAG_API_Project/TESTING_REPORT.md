# Day 17 — RAG API Robustness Testing Report

**Prepared by:** Jagadish Pothuraju  
**Roll Number:** 23WU0102153  
**Internship Domain:** Artificial Intelligence and Machine Learning  
**Task:** Complete RAG API and Robustness Testing  
**Date:** [Enter date]

## Objective
Test the FastAPI RAG service with different document types and edge cases. Record actual HTTP responses and recommend improvements.

## Test matrix
| ID | Test case | Expected behavior | Actual response / status |
|---|---|---|---|
| T1 | Valid TXT | 200; text chunked and indexed | [Fill after running] |
| T2 | Valid text-based PDF | 200; document indexed | [Fill after running] |
| T3 | Empty file | 400 with clear message | [Fill after running] |
| T4 | Unsupported DOCX/image | 415 with allowed formats | [Fill after running] |
| T5 | Corrupted PDF | 400 with readable error | [Fill after running] |
| T6 | Scanned/image-only PDF | 422; OCR note | [Fill after running] |
| T7 | File larger than limit | 413 size-limit response | [Fill after running] |
| T8 | Ask before upload | 409; upload document first | [Fill after running] |
| T9 | Valid question after upload | 200 with answer passages and sources | [Fill after running] |
| T10 | Too-short question | 422 validation response | [Fill after running] |
| T11 | top_k outside 1–10 | 422 validation response | [Fill after running] |

## How to test
1. Run `uvicorn main:app --reload`.
2. Open `http://127.0.0.1:8000/docs`.
3. Upload the sample TXT and ask a question.
4. Repeat with valid PDF and the edge cases in the table.
5. Record actual response codes and save screenshots of success and error responses.

## API response format
Upload returns a message, document ID, filename, file size, chunk count, and chunk size. Ask returns an answer made from retrieved passages, source filenames, chunk indexes, and similarity estimates. Values depend on the actual file and run.

## Improvement suggestions
- Add OCR for scanned PDFs.
- Add authentication and per-user document isolation.
- Add endpoints to list and delete documents.
- Add duplicate upload detection and indexing status.
- Add a grounded LLM answer generation layer with source citations.
- Add rate limits, structured logs, monitoring, and timeouts.
- Validate actual file content in addition to file extension.
- Add page-count and extracted-text limits for large documents.
- Add automated tests in continuous integration.
- Never commit credentials or confidential company documents.

## Conclusion
The API demonstrates document upload, processing, chunking, embeddings, ChromaDB storage, and semantic retrieval. Complete the tests and enter actual outcomes before submission.
