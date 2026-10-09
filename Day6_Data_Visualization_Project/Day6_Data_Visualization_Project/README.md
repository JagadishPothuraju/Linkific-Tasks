# Day 6 — Data Visualization with Python
**Prepared by:** Jagadish Pothuraju

## Objective
Create four meaningful charts and write observations.

## Project files
- `Day6_Data_Visualization.ipynb` — notebook and charts code
- `day5_dataset.csv` — sample dataset; replace with your actual Day 5 dataset
- `requirements.txt` — required packages

## Charts
1. Bar chart — total sales by category
2. Line chart — sales over time
3. Histogram — distribution of sales
4. Pie chart — share of sales by category

## Run
```bash
python -m pip install -r requirements.txt
jupyter notebook
```
Open the notebook and select **Run All**.

## Dataset note
The actual Day 5 dataset was not attached, so a sample dataset is included. The notebook expects `Date`, `Category`, and `Sales` columns. Adjust the code if your Day 5 dataset uses different column names.

## Push to GitHub
```bash
git init
git add .
git commit -m "Day 6 - Data Visualization with Matplotlib and Seaborn"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
