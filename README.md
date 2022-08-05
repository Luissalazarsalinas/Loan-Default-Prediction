# **Loan Default Prediction**

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](http://www.pytorch.org/news.html)
![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)

An end-to-end Machine Learning Project to predict Loan Default.

## **Problem Statement**
Small Business Administration(SBA) is an agency of the Federal Government that exists to serve, support, and protect the interests of small businesses. One way SBA assist these small business enterprises is through a loan guarantee program which is designed to encourage the bank to grant loans to small business. But, since SBA loans only guarantee a portion of the entire loan balance, banks will incur some losses if a small business defaults on its SBA-guaranteed loan. Therefore, banks are still faced with a difficult choice as to whether they should grant such a loan because of the high risk of default. One way to uniform their decision-making is through analyzing relevant historical data.

This Streamlit App utilizes a Machine Learning model in order to predict if a loan will be paid in full or no,  based on the following criteria: type of industry, number of business employees, amount disbursed by the bank, Gross Amount of Loan Approved by Bank, SBA's Guaranteed Amount of Approved Loan and Loan term in months. 

The App can be viewed through this ![link]()

## **Data Preparation**
The original data set is from the U.S.SBA loan database, which includes historical data from 1987 through 2014 (899,164 observations) with 27 variables. The data set includes information on whether the loan was paid off in full or if the SBA had to charge off any amount and how much that amount was. 

According to Li, Mickel, & Taylor 2018, the project filtered the  original dataset to California State and  add the following new variables:

- New
- Portion 
- RealEstate
- Recession
- Default(Target)


![Dataset link](https://amstat.tandfonline.com/doi/full/10.1080/10691898.2018.1434342)

## **Modelling**

In this project 3 different classification algorithms were tested namely:
- Logistic Regression (Base Line)
- Random Forest
- Extra Tree
- XGBoots

