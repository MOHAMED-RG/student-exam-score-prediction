# 🎓 Student Exam Score Prediction using Machine Learning

## 📌 Overview

This project focuses on predicting **student exam scores** using Machine Learning based on academic, lifestyle, and behavioral factors.

The project follows an end-to-end Machine Learning workflow, including data cleaning, exploratory data analysis, feature engineering, preprocessing, model training, model comparison, hyperparameter tuning, evaluation, and deployment using Streamlit.

The final **Linear Regression model** achieved an **R² score of 0.897** on the test set.

---

## 🚀 Live Demo

🔗 **Streamlit App:**
https://student-exam-score-prediction-knbeeasetgdmvthtzoijfd.streamlit.app/

---

## 📊 Dataset

The dataset used in this project is the **Student Habits vs Academic Performance** dataset from Kaggle.

🔗 **Dataset:**
https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance

The dataset contains **1,000 student records** and includes academic, lifestyle, and demographic features.

### Main Features

- Age
- Gender
- Study Hours per Day
- Social Media Hours
- Netflix Hours
- Part-Time Job
- Attendance Percentage
- Sleep Hours
- Diet Quality
- Exercise Frequency
- Parental Education Level
- Internet Quality
- Mental Health Rating
- Extracurricular Participation
- Exam Score

---

## 🔍 Exploratory Data Analysis

The exploratory analysis was performed using **Python, Pandas, Matplotlib, and Seaborn**.

The analysis focused on understanding:

- Relationships between numerical features and exam scores
- Correlations between student habits and academic performance
- Distribution of important features
- The relationship between study hours and exam scores
- Potential relationships between lifestyle factors and academic performance

### Study Hours vs Exam Score

`study_hours_per_day` showed the strongest relationship with exam scores, with a correlation of approximately **0.83**.

![Study Hours vs Exam Score](study_hours_vs_exam_score.png)

### Correlation Matrix

The correlation matrix was used to examine relationships between numerical features and the target variable.

![Correlation Matrix](correlation_matrix.png)

---

## ⚙️ Feature Engineering & Preprocessing

The dataset contains both numerical and categorical features.

### Categorical Features

Categorical variables were converted into numerical format using **One-Hot Encoding**.

The categorical features include:

- Gender
- Part-Time Job
- Diet Quality
- Parental Education Level
- Internet Quality
- Extracurricular Participation

Dummy variables were created before splitting the dataset into training and testing sets.

### Numerical Features

The following numerical features were standardized using `StandardScaler`:

- Age
- Study Hours per Day
- Social Media Hours
- Netflix Hours
- Attendance Percentage
- Sleep Hours
- Exercise Frequency
- Mental Health Rating

The scaler was fitted only on the training data and then used to transform both the training and test data.

The target variable `exam_score` was not scaled.

---

## 🤖 Machine Learning Models

Several regression models were trained and evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regression
5. Random Forest Regression

The models were evaluated using:

- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**
- **R² Score**

---

## 📈 Model Comparison

| Model | MAE ↓ | RMSE ↓ | R² ↑ |
|---|---:|---:|---:|
| Linear Regression | 4.189 | 5.146 | 0.897 |
| Ridge Regression | 4.189 | 5.146 | 0.897 |
| Lasso Regression | 4.633 | 5.768 | 0.870 |
| Decision Tree | 7.427 | 9.524 | 0.646 |
| Random Forest | 4.942 | 6.205 | 0.850 |

![Model Comparison](model_comparison.png)

Linear Regression and Ridge Regression produced very similar results. Linear Regression was selected as the final model because it provided strong performance with a simpler model structure.

---

## 🔧 Hyperparameter Tuning

Hyperparameter tuning was performed using **GridSearchCV**.

### Ridge Regression

The following values of `alpha` were tested:

```text
0.01
0.1
1
10
100
```

The best value was:

```
alpha = 1
```

The performance remained almost unchanged compared with the default Ridge model.

### Random Forest

The following parameters were tuned:

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

The tuned Random Forest achieved an R² score of approximately **0.852**, compared with 0.850 before tuning.

---

## 📊 Feature Interpretation

The coefficients from the final Linear Regression model were analyzed to understand the relationship between the features and predicted exam scores.

### Main Findings

- `study_hours_per_day` had the largest positive coefficient.
- `mental_health_rating` had the second-largest positive coefficient.
- `exercise_frequency`, `sleep_hours`, and `attendance_percentage` also had positive coefficients.
- `social_media_hours` and `netflix_hours` had negative coefficients.
- The remaining features had relatively smaller coefficients.

Because the numerical features were standardized, their coefficients represent the expected change in predicted exam score associated with a one-standard-deviation increase in the feature, while holding other features constant.

The relationships identified by the model should not be interpreted as proof of causation.

---

## 📊 Final Model Evaluation

The final Linear Regression model achieved the following results on the test set:

```
MAE  = 4.19
RMSE = 5.15
R²   = 0.897
```

### Metric Interpretation

- **MAE = 4.19**: The model's predictions were off by approximately 4.19 exam-score points on average.
- **RMSE = 5.15**: Larger prediction errors have a greater effect on this metric.
- **R² = 0.897**: The model explains approximately 89.7% of the variance in exam scores in the test set.

---

## 🔄 Machine Learning Workflow

```
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Preprocessing
        ↓
Model Training
        ↓
Model Comparison
        ↓
Hyperparameter Tuning
        ↓
Final Evaluation
        ↓
Feature Interpretation
        ↓
Save Model + Scaler
        ↓
Streamlit Application
        ↓
Deployment
```

---

## 🚀 Streamlit Application

A simple Streamlit application was created to allow users to enter student information and receive a predicted exam score.

The application accepts inputs such as:

- Age
- Study Hours
- Social Media Hours
- Netflix Hours
- Attendance Percentage
- Sleep Hours
- Exercise Frequency
- Mental Health Rating
- Gender
- Part-Time Job
- Diet Quality
- Parental Education Level
- Internet Quality
- Extracurricular Participation

The input data is processed using the same preprocessing approach used during model training before being passed to the saved model.

---

## 💾 Model Deployment

The trained Linear Regression model and the fitted StandardScaler were saved using Joblib.

- `student_exam_score_model.pkl`
- `student_exam_score_scaler.pkl`

The saved model and scaler are loaded by the Streamlit application to generate predictions.

---

## 🛠️ Tools & Libraries

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

### Development Tools

- Jupyter Notebook
- Git
- GitHub

---

## 📁 Project Structure

```
student-exam-score-prediction/
│
├── Student Habits vs Academic Performance.ipynb
├── student_habits_performance.csv
├── student_exam_score_model.pkl
├── student_exam_score_scaler.pkl
├── app.py
├── README.md
├── requirements.txt
├── study_hours_vs_exam_score.png
├── correlation_matrix.png
├── model_comparison.png
└── feature_importance.png
```

---

## 📦 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/MOHAMED-RG/student-exam-score-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd student-exam-score-prediction
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Key Insights

The analysis and modeling process produced several important insights:

### 1. Study Time Showed the Strongest Relationship

`study_hours_per_day` had both the strongest correlation with exam scores (0.83) and the largest positive coefficient in the Linear Regression model.

This indicates that study time was the most prominent feature associated with exam performance in this dataset.

### 2. Mental Health Was Also Associated with Performance

`mental_health_rating` showed a positive correlation of 0.32 with exam scores and had the second-largest positive coefficient in the final model.

This suggests an association between higher mental health ratings and higher predicted exam scores within the dataset.

### 3. Lifestyle Factors Showed Smaller Relationships

Exercise and sleep had positive relationships with exam scores, while social media and Netflix usage showed negative relationships.

However, these relationships were considerably weaker than the relationship between study hours and exam scores.

### 4. Linear Models Performed Well on This Dataset

Linear Regression, Ridge Regression, and tuned Ridge Regression produced very similar results, with an R² of approximately 0.897.

This suggests that the tested linear models were able to capture much of the predictive structure present in the dataset.

### 5. Hyperparameter Tuning Produced Limited Improvement

Tuning the Random Forest model improved its R² from 0.850 to approximately 0.852.

Ridge tuning produced essentially the same performance as the default Ridge model.

This indicates that hyperparameter tuning did not substantially change the results for the tested parameter ranges.

---

## 🎯 Conclusion

This project demonstrates an end-to-end Machine Learning workflow for predicting student exam scores using academic, lifestyle, and behavioral features.

The exploratory analysis showed that `study_hours_per_day` had the strongest relationship with exam performance in this dataset, while other factors such as mental health, exercise, sleep, social media usage, and Netflix usage showed smaller relationships.

After comparing multiple regression models, Linear Regression was selected as the final model, achieving an R² of 0.897, an MAE of 4.19, and an RMSE of 5.15 on the test set.

The final model and scaler were saved using Joblib and integrated into a Streamlit application, completing the workflow from data analysis and model development to deployment.
