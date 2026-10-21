# LLM and Hugging Face Model Comparison

This project explores AI evolution and tests three NLP tasks using Hugging Face model IDs.

- Text generation: `gpt2`
- Sentiment analysis: `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
- Summarization: `facebook/bart-large-cnn`

## Setup
`pip install requests pandas jupyter`
Open `LLM_HuggingFace_Model_Comparison.ipynb`. For hosted inference, set `HF_TOKEN` as an environment variable or Colab Secret. Never commit tokens. Model/provider availability may change; check model cards.

## Evaluation
Compare generation by relevance/coherence, sentiment by label correctness, and summaries by coverage/clarity/factual consistency. Record only actual outputs.

## References
- https://huggingface.co/models
- https://huggingface.co/docs/transformers
- https://huggingface.co/docs/api-inference
