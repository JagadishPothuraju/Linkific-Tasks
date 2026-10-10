# Week 1 Mini Project — Sales Data Analysis
**Prepared by:** Jagadish Pothuraju  
**Domain:** Artificial Intelligence and Machine Learning

## Objective
Load and clean a CSV, perform basic analysis, create four visualizations, and write 5–8 insights.

## Dataset
`data/sales_data.csv` is synthetic practice data bundled to make the project runnable offline. It is **not** an externally collected real-world dataset. If your assignment requires a real CSV, replace this file with a sourced dataset and record the source URL here.

## Visualizations
1. Monthly sales revenue
2. Revenue by product category
3. Estimated profit by region
4. Distribution of profit per transaction

## Project structure
- `data/sales_data.csv` — input dataset
- `notebooks/Sales_Data_Analysis.ipynb` — analysis notebook
- `outputs/cleaned_sales_data.csv` — cleaned dataset
- `outputs/insights.txt` — example insights
- `screenshots/` — four chart images
- `requirements.txt` — dependencies

## Run
```bash
python -m pip install -r requirements.txt
jupyter notebook
```
Open `notebooks/Sales_Data_Analysis.ipynb` and run all cells.

## GitHub upload
```bash
git init
git add .
git commit -m "Week 1 Mini Project - Sales Data Analysis"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

## 2–5 minute demo video plan
1. Introduce the project and objective (20–30 seconds).
2. Show the CSV and missing-data cleaning (30–45 seconds).
3. Explain the four visualizations (60–90 seconds).
4. Present the key insights (30–45 seconds).
5. Show the folder structure and GitHub repository (20–30 seconds).
