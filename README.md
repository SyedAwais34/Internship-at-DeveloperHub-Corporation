# Internship-at-DeveloperHub-Corporation
Remote internship in Data Science and Analytics at DeveloperHub Corporation.

# Data Analytics & Machine Learning Projects

## 📌 Overview
This repository contains three data science tasks focused on data exploration, visualization, and machine learning modeling using real-world datasets. The main goal is to build foundational skills in data analysis, classification, and regression.

---

## 🧪 Task 1: Exploring and Visualizing a Simple Dataset

### 🎯 Objective
Understand how to read, summarize, and visualize a dataset using basic data analysis techniques.

### 📊 Dataset
Iris Dataset (available via seaborn or CSV sources)

### ⚙️ Approach
- Loaded dataset using **pandas**
- Explored structure using:
  - `.shape`
  - `.columns`
  - `.head()`
- Performed Exploratory Data Analysis (EDA)
- Created visualizations using **matplotlib** and **seaborn**:
  - Scatter plots (feature relationships)
  - Histograms (data distribution)
  - Box plots (outliers and spread)

### 🔍 Results & Insights
- Clear separation observed between different Iris species
- Petal features showed stronger class distinction than sepal features
- No significant outliers detected in most variables

---

## 🧪 Task 2: Credit Risk Prediction

### 🎯 Objective
Predict whether a loan applicant will default on a loan (binary classification problem).

### 📊 Dataset
Loan Prediction Dataset (Kaggle)

### ⚙️ Approach
- Handled missing values using appropriate imputation techniques
- Performed feature visualization (income, education, loan amount)
- Encoded categorical variables
- Trained classification models:
  - Logistic Regression
  - Decision Tree
- Evaluated models using:
  - Accuracy score
  - Confusion matrix

### 🔍 Results & Insights
- Income and credit history were key indicators of loan approval
- Logistic Regression provided stable baseline performance
- Decision Tree captured non-linear patterns but risked overfitting

---

## 🧪 Task 4: Predicting Insurance Claim Amounts

### 🎯 Objective
Predict medical insurance charges using regression techniques.

### 📊 Dataset
Medical Cost Personal Dataset

### ⚙️ Approach
- Applied **Linear Regression model**
- Analyzed relationships between:
  - Age
  - BMI
  - Smoking status
- Used visualization to understand feature impact
- Evaluated model using:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

### 🔍 Results & Insights
- Smoking status had the strongest impact on insurance charges
- Higher BMI and age generally increased claim amounts
- Model showed reasonable prediction accuracy with moderate error levels

---

## 🛠️ Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📌 Conclusion
These tasks helped build a strong foundation in:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Classification models
- Regression models
- Model evaluation techniques

---

Task NO 2

📌 Overview

This repository contains three data science and analytics projects completed as part of an internship at DeveloperHub Corporation.

The projects focus on:

Machine Learning (Classification & Clustering)
Explainable AI (XAI)
Business Intelligence Dashboarding
Data Visualization & Insights

The main goal is to build strong practical skills in real-world data science applications.

🧪 Task 1: Term Deposit Subscription Prediction (Bank Marketing)
🎯 Objective

Predict whether a bank customer will subscribe to a term deposit based on marketing campaign data.

📊 Dataset

Bank Marketing Dataset (UCI Machine Learning Repository)

⚙️ Approach
Loaded and explored dataset using pandas
Performed data cleaning and preprocessing
Encoded categorical variables (Label Encoding / One-Hot Encoding)
Split data into training and testing sets
Trained classification models:
Logistic Regression
Random Forest Classifier
Evaluated models using:
Confusion Matrix
F1-Score
ROC Curve
Applied Explainable AI (XAI) using:
SHAP / LIME (explained at least 5 predictions)
🔍 Results & Insights
Customer demographics strongly influence subscription behavior
Random Forest performed better than Logistic Regression in most cases
Marketing success depends heavily on previous campaign outcomes
Model explanations helped identify key decision factors per customer
🧠 Skills Gained
Classification modeling
Feature encoding
Model evaluation
Explainable AI (SHAP / LIME)
Customer behavior analysis
🧪 Task 2: Customer Segmentation Using K-Means Clustering
🎯 Objective

Segment customers based on spending behavior and income to design targeted marketing strategies.

📊 Dataset

Mall Customers Dataset

⚙️ Approach
Conducted Exploratory Data Analysis (EDA)
Selected key features:
Age
Annual Income
Spending Score
Applied feature scaling (StandardScaler)
Used K-Means Clustering for segmentation
Determined optimal number of clusters using Elbow Method
Reduced dimensions using:
PCA / t-SNE for visualization
Analyzed cluster patterns and behavior
🔍 Results & Insights
Distinct customer groups identified based on spending habits
High-income high-spending customers identified as premium segment
Low-income high-spending customers indicate impulsive buyers
Clear cluster separation observed after dimensionality reduction
Each segment requires different marketing strategies
🧠 Skills Gained
Unsupervised learning (K-Means)
Customer segmentation
PCA / t-SNE visualization
Data-driven marketing strategy design
🧪 Task 3: Interactive Business Dashboard (Streamlit)
🎯 Objective

Build an interactive dashboard to analyze sales, profit, and customer performance.

📊 Dataset

Global Superstore Dataset

⚙️ Approach
Cleaned and preprocessed dataset
Converted date columns into datetime format
Built interactive filters:
Region
Category
Sub-Category
Created KPIs:
Total Sales
Total Profit
Top 5 Customers by Sales
Built visualizations using:
Bar charts
Pie charts
KPI metrics
📊 Key Insights
A small number of customers contribute major sales
Certain product categories generate higher profit
Some sub-categories show low profitability
Sales patterns vary across regions and segments
🧠 Skills Gained
Business Intelligence (BI) dashboarding
Data storytelling
Streamlit interactivity
KPI-based analysis
🛠️ Tools & Technologies
Python 🐍
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
SHAP / LIME
Streamlit
Jupyter Notebook
📌 Conclusion

These projects helped develop strong hands-on skills in:

✔ Machine Learning (Classification & Clustering)
✔ Explainable AI (XAI)
✔ Data Preprocessing & Feature Engineering
✔ Business Intelligence Dashboards
✔ Data Visualization & Insight Generation
✔ Real-world Problem Solving
