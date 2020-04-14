# Absenteeism_ML_Analysis
## Overview
The project takes a data set about employees and the amount of time they been absent from work. It performs and initial exploration analysis of the dataset and it creates a prediction about if they would be absent from work with Machine Learning Models. Finally the results are visualized in Tableau.

## Initial Data Exploration
The main goal is this section is to understand better the data set and evaluate some poddible relationships betweent the features. It also will give background information about the relevance of some of the features. It will later help with feature selection.

### Feature Data/Description
+ Categorical Data:
    * **Reason for Absence:** (Reasons 1 - 21 are registered in the International Classification of Diseases (ICD), Reasons 22 - 28 are not)
        1. Certain infectious and parasitic diseases
        1. Noeplasms

    + **Education:** level of education attained by the employee
      1. Highschool Education only
      2. Bachelor Degrees or graduate degree
      3. Some level of postgraduate
      4. Masters or PhD
+ Numerical/Quantitative
    + Continuos
        + **Transportation Expense:** cost related to business travel such as fuel, parking, and meals
        + **Distance to Work:** Measured in kilometers
        + **Daily Work Load Average:** Measured in minutes
        + **Body Mass Index**
    + Discrete
        + **Age:** years of age
        + **Pets:** number of Pets in the family
        + **Children:** number of children in the family
        + **Absenteeism Time in Hours**
        + **Date:** date of absence
+ Other Data
  + ID: Individual Identification
  
### Missing values

Vizualizations in Tableau can be find at the link bellow

https://public.tableau.com/profile/luis.antonio.coca#!/vizhome/Absenteeism_Analysis_15777401924910/TransportationExpensevsProbabilityandChildren
