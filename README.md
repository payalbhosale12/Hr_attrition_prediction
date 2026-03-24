# 🧑‍💼 HR Attrition Prediction using Logistic Regression

📌 Project Overview

-This project aims to predict employee attrition using a logistic regression model. By analyzing various HR-related factors such as job role, salary, years at the company, and work environment, the goal is to identify patterns that influence whether an employee is likely to stay or leave. This analysis helps HR departments take proactive steps to improve employee satisfaction and reduce turnover.

📁 Dataset  
The dataset includes various features related to employee demographics, job profile, and company information:

- **Age**: Employee's age  
- **DistanceFromHome**: Distance between home and workplace  
- **Education**: Education level (1-5)  
- **EmployeeCount**: Count of employees (constant value)  
- **EmployeeID**: Unique identifier for each employee  
- **JobLevel**: Job position level in the company  
- **MonthlyIncome**: Monthly salary of the employee  
- **NumCompaniesWorked**: Total companies the employee has worked for  
- **PercentSalaryHike**: Percentage increase in salary  
- **StandardHours**: Standard working hours (constant value)  
- **StockOptionLevel**: Stock options granted (0-3)  
- **TotalWorkingYears**: Total years of work experience  
- **TrainingTimesLastYear**: Training programs attended in the last year  
- **YearsAtCompany**: Years spent in the current company  
- **YearsSinceLastPromotion**: Years since last promotion  
- **YearsWithCurrManager**: Years with current manager  
- **BusinessTravel**: Frequency of business travel  
- **Department**: Department the employee works in  
- **EducationField**: Field of education  
- **Gender**: Gender of the employee  
- **JobRole**: Job title  
- **MaritalStatus**: Marital status (Single, Married, Divorced)  
- **Over18**: Whether the employee is above 18 (all values are 'Y')  

🛠️ Operations Performed

**Data Loading**  
- Loaded the dataset into a Jupyter Notebook using `pandas`.

**Exploratory Data Analysis (EDA)** 
- Dropped constant columns and unnecessary identifiers  
- Handled missing values and duplicates  
- Encoded categorical variables using label encoding and one-hot encoding


**Model Building**  
- Applied Logistic Regression for binary classification  
- Split data into training and testing sets  
- Evaluated model using accuracy, precision, recall, F1-score, and confusion matrix  

📊 Key Insights

- Employees with fewer years since last promotion were more likely to stay.  
- High job levels and better salary hikes reduced the likelihood of attrition.  
- Employees who traveled frequently for business showed higher attrition rates.  
- The “Sales Executive” role had comparatively higher turnover.

  📈 Model Performance

✅ **Accuracy Achieved**: **83.96%**
- Balanced performance between precision and recall
- Helpful in classifying employee attrition risk for early interventions 

✅ Conclusion  
The logistic regression model provides a strong baseline for predicting employee attrition, achieving a training accuracy of 83.96%. The analysis highlights key factors such as job level, business travel, promotion history, and monthly income that significantly influence employee retention. These insights can help HR professionals make data-driven decisions to improve workplace policies, design better retention strategies, and reduce turnover.

📦 Tools & Technologies Used  
- Python, Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Jupyter Notebook  
