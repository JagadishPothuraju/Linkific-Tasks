# Day 9 – Exploratory Data Analysis (EDA) using Python

## Objective
Explore the cleaned dataset from Day 8 using descriptive statistics, visualizations, and evidence-based insights.

## Project structure
- `data/cleaned_student_data.csv` – cleaned Day 8 dataset
- `notebooks/Day9_Exploratory_Data_Analysis.ipynb` – full EDA notebook
- `visualizations/` – five generated charts
- `reports/descriptive_statistics.csv` – descriptive statistics table
- `reports/business_insights.md` – five insights and limitations

## Requirements and run
Python 3.9+ recommended. From this folder run:
```bash
pip install -r requirements.txt
jupyter notebook
```
Open `notebooks/Day9_Exploratory_Data_Analysis.ipynb` and run all cells. If running from the notebook directory, the notebook includes a fallback path for the dataset.

## Methods
- Dataset shape, data types, duplicates, and missing-value checks
- Descriptive statistics for numeric and categorical columns
- Five visualizations: average marks by department, marks histogram, attendance vs marks, average attendance by department, and marks spread by department
- Five academic/business insights

## Important limitation
The Day 8 cleaned practice dataset contains only eight records. Results are illustrative and should not be generalized. Use a larger representative dataset for real institutional decisions.

## GitHub upload
From your internship repository, copy this folder into `Day 9/`, then run:
```bash
git add "Day 9"
git commit -m "Add Day 9 EDA project"
git push origin main
```
