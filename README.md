# 🧑‍💼 HR Attrition Prediction using Logistic Regression

## 📌 Project Overview

This project aims to predict employee attrition using a logistic regression model. By analyzing various HR-related factors such as job role, salary, years at the company, and work environment, the goal is to identify patterns that influence whether an employee is likely to stay or leave.

This analysis helps HR departments take proactive steps to improve employee satisfaction and reduce turnover.

---

## 🚀 Live Application (Deployed on Streamlit)

🔗 **Try the App Here:**  
https://hrattritionprediction-rcvljoaescyt9sjnmsf3of.streamlit.app/

👉 This project is deployed using **Streamlit**, where users can enter employee details and get real-time predictions.

---

## 📁 Dataset

The dataset includes various features related to employee demographics, job profile, and company information:

- Age: Employee's age  
- DistanceFromHome: Distance between home and workplace  
- Education: Education level (1–5)  
- EmployeeCount: Count of employees (constant value)  
- EmployeeID: Unique identifier for each employee  
- JobLevel: Job position level in the company  
- MonthlyIncome: Monthly salary of the employee  
- NumCompaniesWorked: Total companies the employee has worked for  
- PercentSalaryHike: Percentage increase in salary  
- StandardHours: Standard working hours (constant value)  
- StockOptionLevel: Stock options granted (0–3)  
- TotalWorkingYears: Total years of work experience  
- TrainingTimesLastYear: Training programs attended in the last year  
- YearsAtCompany: Years spent in the current company  
- YearsSinceLastPromotion: Years since last promotion  
- YearsWithCurrManager: Years with current manager  
- BusinessTravel: Frequency of business travel  
- Department: Department the employee works in  
- EducationField: Field of education  
- Gender: Gender of the employee  
- JobRole: Job title  
- MaritalStatus: Marital status (Single, Married, Divorced)  
- Over18: Whether the employee is above 18 (all values are 'Y')  

---

## 🛠️ Operations Performed

### 📊 Data Loading
- Loaded dataset using pandas  

### 🔍 Exploratory Data Analysis (EDA)
- Dropped constant and unnecessary columns  
- Handled missing values and duplicates  
- Encoded categorical variables using label encoding and one-hot encoding  

### 🤖 Model Building
- Applied Logistic Regression for binary classification  
- Split data into training and testing sets  
- Evaluated using accuracy, precision, recall, F1-score, and confusion matrix  

---

## 📊 Key Insights

- Employees with fewer years since last promotion were more likely to stay  
- Higher job levels and salary hikes reduced attrition  
- Frequent business travel increased attrition risk  
- Sales Executive role had higher turnover  

---

## 📈 Model Performance

✅ Accuracy Achieved: **83.96%**

- Balanced precision and recall  
- Useful for early identification of attrition risk  

---

## ✅ Conclusion

The logistic regression model provides a strong baseline for predicting employee attrition.

Key influencing factors:
- Job level  
- Business travel  
- Promotion history  
- Monthly income  

This helps organizations:
- Improve HR policies  
- Increase employee satisfaction  
- Reduce turnover  

---

## 📦 Tools & Technologies Used

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Jupyter Notebook  
- Streamlit (Deployment)  

---

## 🙌 Author

**Payal Bhosale**  
MCA Student | Aspiring Data Analyst / Software Developer 🚀
