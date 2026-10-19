# 2–5 Minute Project Demo

**Introduction:** I am presenting my Email/SMS Spam Detection project. The goal is to classify messages as spam or legitimate.

**Dataset and preparation:** I load a labelled sample dataset, inspect missing values and class distribution, remove duplicates, and split it into training and test sets.

**Model:** TF-IDF converts text into numeric features. Multinomial Naive Bayes learns patterns associated with spam and ham.

**Evaluation:** I demonstrate accuracy, spam precision, spam recall, F1-score, and the confusion matrix. Precision explains the reliability of spam predictions, while recall measures how much actual spam is detected. Read the exact values from the notebook.

**Prediction demo:** I enter a promotional message and an ordinary message and show the predicted labels.

**Limitations:** This is a small educational dataset; scores are not representative of real-world performance. A larger public dataset and more validation would be needed. Thank you.
