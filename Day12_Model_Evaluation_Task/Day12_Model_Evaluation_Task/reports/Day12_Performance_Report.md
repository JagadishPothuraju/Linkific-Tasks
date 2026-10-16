# Day 12 - Model Performance Report

## Setup
- Dataset: Breast Cancer Wisconsin (educational use only)
- Split: stratified 80/20, random_state=42
- Class labels: 0 = malignant; 1 = benign
- Models: standardized Logistic Regression and Decision Tree

## Results (macro averages)

              Model  Accuracy  Precision (macro)  Recall (macro)  F1 Score (macro)
Logistic Regression    0.9825             0.9812          0.9812            0.9812
      Decision Tree    0.9123             0.9019          0.9157            0.9075

## Interpretation
Accuracy measures overall correctness. Precision measures correctness among predicted class instances, recall measures how many actual class instances are identified, and F1 balances precision and recall. Macro averages give both classes equal weight. For this medical-related practice dataset, recall for the malignant class is especially important to inspect because false negatives may be serious. These results are educational only and are not clinical evidence or a diagnostic tool.
