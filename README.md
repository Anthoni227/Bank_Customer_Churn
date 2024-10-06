# **Bank Customer Churn Prediction**

### **Project Overview**
This project aims to predict whether a customer will leave (churn) a bank based on various features such as customer profile, account information, and transaction history. We leverage machine learning algorithms to identify patterns and provide insights that can help banks implement retention strategies.

---

## **Table of Contents**
1. [Project Motivation](#project-motivation)
2. [Dataset Description](#dataset-description)
3. [Project Workflow](#project-workflow)
4. [Models Implemented](#models-implemented)
5. [Installation and Requirements](#installation-and-requirements)
6. [Conclusions and Future Work](#conclusions-and-future-work)

---

## **Project Motivation**
Customer churn is a critical concern for banks, as retaining customers is more cost-effective than acquiring new ones. Understanding the factors leading to customer churn and accurately predicting churn can empower banks to take preventive actions, thereby improving customer retention and maximizing profitability.

---

## **Dataset Description**
The dataset used in this project contains various features that provide insights into customer behavior. Some of the key features include:

- **Customer Age**: Age of the customer
- **Tenure**: Duration the customer has been with the bank
- **Balance**: Account balance of the customer
- **Number of Products**: Number of products subscribed by the customer
- **Credit Score**: Credit score of the customer
- **Exited**: Whether the customer churned (1 for yes, 0 for no)

**Target Variable**: The target variable is `Exited`, indicating customer churn.

---

## **Project Workflow**
### **Data Preprocessing**:
- Handling missing values
- Encoding categorical variables
- Feature scaling

### **Exploratory Data Analysis**:
- Visualizing key features
- Identifying relationships between features and customer churn

### **Model Building**:
- Implementing various machine learning models such as Logistic Regression, Decision Tree, Random Forest, XGBoost, etc.
- Tuning model parameters using GridSearchCV

### **Model Evaluation**:
- Evaluating models based on accuracy, precision, recall, F1-score, and AUC-ROC curve.

---

## **Models Implemented**
The following machine learning models were implemented to predict customer churn:

| **Model**                    | **Accuracy** |
|------------------------------|--------------|
| Logistic Regression           | 96.66%       |
| Bagging Classifier            | 93.33%       |
| Random Forest Classifier      | 96.66%       |
| XGBoost                       | 93.33%       |
| AdaBoost                      | 93.33%       |

**Logistic Regression** and **Random Forest** were the best-performing models, each with an accuracy of **96.66%**.

---

## **Installation and Requirements**

### **Prerequisites**
Make sure you have the following installed:
- Python 3.8+
- Jupyter Notebook or any other IDE

## **Conclusions and Future Work**
The models provided valuable insights into predicting bank customer churn, with **Random Forest** being the most reliable. Future work could include:

- **Feature Engineering**: Creating new features to better capture customer behavior.
- **Handling Imbalanced Data**: Applying techniques like **SMOTE** (Synthetic Minority Over-sampling Technique) or undersampling to address class imbalance.
- **Deep Learning Models**: Experimenting with neural networks or advanced models for further improvements.

