# **Loan Default Prediction**

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)

An end-to-end Machine Learning Project to predict Loan Default.

## **Problem Statement**
Small Business Administration(SBA) is an agency of the Federal Government that exists to serve, support, and protect the interests of small businesses. One way SBA assist these small business enterprises is through a loan guarantee program which is designed to encourage the bank to grant loans to small business. But, since SBA loans only guarantee a portion of the entire loan balance, banks will incur some losses if a small business defaults on its SBA-guaranteed loan. Therefore, banks are still faced with a difficult choice as to whether they should grant such a loan because of the high risk of default. One way to uniform their decision-making is through analyzing relevant historical data.

This Streamlit App utilizes a Machine Learning model to predict if a loan will be paid in full or not, based on the following criteria: type of industry, number of business employees, the amount disbursed by the bank, Gross Amount of Loan Approved by Bank, SBA's Guaranteed Amount of Approved Loan and Loan term in months. 

The App can be viewed through this [link](https://loan-default-app.herokuapp.com/)

## **Data Preparation**
The original data set is from the U.S.SBA loan database, which includes historical data from 1987 through 2014 (899,164 observations) with 27 variables. The data set includes information on whether the loan was paid off in full or if the SBA had to charge off any amount and how much that amount was. 

According to Li, Mickel, & Taylor 2018, the project filtered the  original dataset to California State and  add the following new variables:

- New
- Portion 
- RealEstate
- Recession
- Default(Target)


[Dataset link](https://amstat.tandfonline.com/doi/full/10.1080/10691898.2018.1434342)

## Modelling 
Machine Learning Algorithms that were tested:
 - LogisticRegression - Baseline
 - Random Forest 
 - Extra Tree
 - XGBoost

Xgboost was the model with better performance with the validation set:
 - Accuracy: 0.95
 - F1-Score: 0.90
 - ROC-AUC: 0.93
 
Xgboost was chosen as the final model, and its hyperparameters were optimized using hyperopt(library) with a Bayesian optimization as search strategy.

Final model performance with the test set:
 - Accuracy: 0.96
 - F1-Score: 0.91
 - ROC-AUC: 0.94
 
 Feature importance
 ![image](https://github.com/Luissalazarsalinas/Loan-Default-Prediction/blob/master/img/Feature_importance.png)
The variables that contribute most to the XGBoost final model were:
 - RealState
 - Term
 - Recession
These variables could be good predictors to detect fraud in credit card transactions.

## Deployment
The API was deployed using docker container on Heroku and the Streamlit App was deployed on Streamlit Cloud

<details> 
  <summary><b>💻 Deploying the API</b></summary>

1. Heroku logging 

```
Heroku login
```

2. Create a heroku app

```
heroku create <app-name> 
```

3. Set the heroku cli git remote to that app

``` 
heroku git:remote <app-name>
```

4. Set the heroku stack setting to container

```
heroku stack:set container
```

5. Push to herokuPush to heroku
 
```
git push heroku branch <master/main>
```
</details>

