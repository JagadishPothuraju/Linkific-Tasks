# Email/SMS Spam Detection — Machine Learning Project

## Overview
Classifies a text message as `spam` or `ham` (legitimate) using TF-IDF features and Multinomial Naive Bayes.

## Dataset note
The included CSV contains 50 manually assembled examples (25 spam, 25 ham) for practice only. This is not a benchmark dataset; scores must not be generalized to real-world performance. For stronger evaluation, use the UCI SMS Spam Collection dataset, document its source, and rerun the notebook.

## Workflow
1. Inspect and clean records. 2. Split into training/testing subsets. 3. Convert text to TF-IDF features. 4. Train Multinomial Naive Bayes. 5. Evaluate accuracy, spam precision, spam recall, F1-score and confusion matrix. 6. Test example messages and save artifacts.

## Run
```bash
pip install -r requirements.txt
jupyter notebook Spam_Detection_ML_Project.ipynb
```
Run from the project root so `data/sms_spam_sample.csv` resolves correctly.

## Metrics
- Accuracy: overall fraction correct.
- Spam precision: among messages predicted spam, fraction truly spam.
- Spam recall: fraction of actual spam detected.
- F1-score: harmonic mean of spam precision and recall.

## GitHub
```bash
git init
git add .
git commit -m "Add end-to-end spam detection project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```
Replace the URL with your repository. Verify the uploaded files before marking GitHub complete. Never commit private messages or credentials.
