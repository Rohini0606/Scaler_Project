# Scaler_Project

Insurance Price Prediction

Objective
The objective of this project is to develop a predictive model that estimates the premium prices for health insurance policies based on customer demographics and health-related features. This model aims to help the insurance company accurately price their products, ensuring competitiveness while maintaining profitability.
Background
Insurance companies often rely on a variety of factors to determine the premium price for health insurance policies. These factors can include age, medical history, lifestyle habits, and more. Accurate pricing is crucial as it affects customer satisfaction and the company’s bottom line. Underpricing can lead to financial losses, while overpricing can drive potential customers away.
Data Description
The dataset contains historical records of health insurance policyholders, with the following features:
The dataset comprises the following 11 attributes:
1.	Age: Numeric, ranging from 18 to 66 years.
2.	Diabetes: Binary (0 or 1), where 1 indicates the presence of diabetes.
3.	BloodPressureProblems: Binary (0 or 1), indicating the presence of blood pressure-related issues.
4.	AnyTransplants: Binary (0 or 1), where 1 indicates the person has had a transplant.
5.	AnyChronicDiseases: Binary (0 or 1), indicating the presence of any chronic diseases.
6.	Height: Numeric, measured in centimeters, ranging from 145 cm to 188 cm.
7.	Weight: Numeric, measured in kilograms, ranging from 51 kg to 132 kg.
8.	KnownAllergies: Binary (0 or 1), where 1 indicates known allergies.
9.	HistoryOfCancerInFamily: Binary (0 or 1), indicating a family history of cancer.
10.	NumberOfMajorSurgeries: Numeric, counting the number of major surgeries, ranging from 0 to 3 surgeries.
11.	PremiumPrice: Numeric, representing the premium price in currency, ranging from 15,000 to 40,000.


Step 1 : Tableau Visualization

Data imported to Tableau. 
Created new parameters, Calculated fields and measured variation of Premium Price with Age, Height, Weight and other health conditions.
Here is the link for Tableau Public:
https://public.tableau.com/views/ScalerProject_InsuracePremiumPrediction/SummaryStatisticsDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Step 2: EDA and Hypothesis Testing for Insurance Cost Prediction
Basic checking of data is done using Python in Google Colab editor.
Effect of Age and different health condition on Premium price payment is studied using Graphs.
Hypothesis testing is done to prove that the visualization is matching with actual results.
Here is the link for EDA and Hypothesis testing:
https://colab.research.google.com/drive/1GGZS9N0tA9VJiOC4-Q3_k7gqlgDxiW-L?usp=sharing

Step 3: ML Modeling
It is found that the target ‘Premium Price’ is not Gaussian. Hence, Logarithm of target price is taken as Target variable.
Different algorithms are applied and model performance is checked.
Best performance was seen using Linear Regression.
Here is the link for ML Modeling:
https://colab.research.google.com/drive/1F7EXvrYTanFtWVUk8oBrlKxyS88HnVWw?usp=sharing

Step 4: Web-Based Calculator for Estimating Insurance Premiums
Created a project in Pycharm Editor.
Installed StreamLit, Python packages.
Written the code to deploy ML model in web. The web app is designed such that it accepts all input features values and predicts the output (target variable) with the ML model.

 
