# 🥗 VitaFuel — AI Calorie & Fitness Assistant

> **AI Calorie & Fitness Assistant — Educational Estimates, Not Medical Advice**

VitaFuel is a **Data Science and Machine Learning based wellness application** designed to help users understand their daily calorie requirements, track food intake, monitor exercise, and analyze their overall energy balance.

The application combines **Python, Streamlit, data analysis, calorie estimation formulas, and Machine Learning concepts** into an easy-to-use interactive application.

---

## 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Objectives](#-objectives)
* [Features](#-features)
* [Technologies Used](#-technologies-used)
* [How the System Works](#-how-the-system-works)
* [Calorie Calculation](#-calorie-calculation)
* [Machine Learning](#-machine-learning)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [How to Run](#-how-to-run)
* [Using the Application](#-using-the-application)
* [Data Storage](#-data-storage)
* [Model Evaluation](#-model-evaluation)
* [Limitations](#-limitations)
* [Future Improvements](#-future-improvements)
* [Disclaimer](#-disclaimer)
* [Author](#-author)

---

# 📖 Project Overview

VitaFuel helps users estimate their daily energy requirements based on personal information such as:

* Age
* Gender
* Height
* Weight
* Activity level
* Fitness goal

The application calculates:

* **BMI**
* **BMR**
* **TDEE**
* **Daily calorie target**
* **Food calorie intake**
* **Protein**
* **Carbohydrates**
* **Fat**
* **Calories burned through exercise**
* **Total exercise duration**
* **Remaining estimated calories**

Users can also add **multiple food items and multiple exercises** to their daily log.

---

# 🎯 Objectives

The main objectives of VitaFuel are:

1. To develop an interactive calorie and fitness application.
2. To estimate a user's daily calorie requirements.
3. To calculate BMI, BMR and TDEE.
4. To allow users to track their food intake.
5. To allow users to record multiple exercises.
6. To estimate calories burned during exercise.
7. To demonstrate the use of Data Science in a real-world application.
8. To integrate Machine Learning for calorie-related prediction.
9. To provide an easy-to-understand dashboard for users.

---

# ✨ Features

## 👤 Personal Profile

Users can enter:

* Age
* Gender
* Height
* Weight
* Activity level
* Fitness goal

The profile can be saved so that users do not have to enter it every time they reopen the application.

---

## ⚖️ BMI Calculator

BMI is calculated using:

$$
BMI = \frac{Weight}{Height^2}
$$

where height is measured in meters.

---

## 🔥 BMR Calculator

VitaFuel uses the **Mifflin-St Jeor equation**.

### Male

$$
BMR = 10W + 6.25H - 5A + 5
$$

### Female

$$
BMR = 10W + 6.25H - 5A - 161
$$

Where:

* `W` = Weight in kg
* `H` = Height in cm
* `A` = Age in years

---

## ⚡ TDEE Calculator

TDEE stands for **Total Daily Energy Expenditure**.

It is calculated using:

$$
TDEE = BMR \times Activity\ Factor
$$

The application uses different activity multipliers depending on the user's activity level.

| Activity Level    | Factor |
| ----------------- | -----: |
| Sedentary         |    1.2 |
| Lightly Active    |  1.375 |
| Moderately Active |   1.55 |
| Very Active       |  1.725 |
| Extremely Active  |    1.9 |

---

## 🍎 Food Tracker

Users can add multiple food items.

Each food record contains:

* Food name
* Meal
* Quantity
* Calories
* Protein
* Carbohydrates
* Fat

The application automatically calculates daily totals.

---

## 🏃 Exercise Tracker

Users can add multiple exercises such as:

* Walking
* Running
* Cycling
* Swimming
* Skipping
* Yoga
* Strength Training
* Dancing
* HIIT

The application estimates calories burned based on exercise intensity, body weight and duration.

---

## 📊 Dashboard

The dashboard provides a summary of the user's daily information.

It displays:

* Daily calorie target
* Food intake
* Calories burned
* Remaining calories
* BMI
* BMR
* TDEE
* Protein
* Carbohydrates
* Fat
* Exercise time

---

# 🤖 Machine Learning

The project can use Machine Learning to predict calorie-related values.

Since calories are numerical and continuous values, **regression algorithms** are appropriate.

### Models

The project can use:

### 1. Linear Regression

Linear Regression learns a relationship between input features and a continuous target.

Example features:

* Age
* Weight
* Height
* Exercise duration
* Activity information

Target:

* Calories burned or another calorie-related numerical value.

---

### 2. Random Forest Regression

Random Forest Regression combines multiple decision trees to make predictions.

It can model nonlinear relationships between features and calorie expenditure.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Data Preprocessing
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
Save Trained Model
   ↓
Use Model in VitaFuel
```

---

# 📏 Model Evaluation

Regression models can be evaluated using:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted values.

### Mean Squared Error (MSE)

Penalizes larger errors more heavily.

### Root Mean Squared Error (RMSE)

The square root of MSE.

### R² Score

Measures how well the model explains variation in the target variable.

A good Machine Learning project should compare multiple models and select the better-performing model based on appropriate evaluation metrics.

---

# 🛠️ Technologies Used

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| Python       | Main programming language   |
| Streamlit    | Interactive web application |
| Pandas       | Data manipulation           |
| NumPy        | Numerical computation       |
| Scikit-learn | Machine Learning            |
| Matplotlib   | Data visualization          |
| Joblib       | Model saving/loading        |
| JSON         | Local data storage          |
| HTML         | Frontend structure          |
| CSS          | Frontend styling            |
| JavaScript   | Frontend interactions       |

---

# 📂 Project Structure

```text
VitaFuel/
│
├── app.py
├── index.html
├── dataset.csv
├── calorie_model.pkl
├── vitafuel_data.json
├── requirements.txt
└── README.md
```

### File Description

**`app.py`**

Main Streamlit application.

**`index.html`**

Frontend version of the VitaFuel website.

**`dataset.csv`**

Dataset used for Data Science and Machine Learning.

**`calorie_model.pkl`**

Saved trained Machine Learning model.

**`vitafuel_data.json`**

Stores profile, food and exercise information for the local application.

**`requirements.txt`**

Contains the Python libraries required to run the project.

**`README.md`**

Project documentation.

---

# 💻 Installation

## Step 1 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then enter the project folder:

```bash
cd VitaFuel
```

---

## Step 2 — Install Required Libraries

```bash
pip install streamlit pandas numpy scikit-learn matplotlib joblib
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🖥️ Using the Application

### Step 1 — Open VitaFuel

Start the Streamlit application.

### Step 2 — Create Your Profile

Enter:

```text
Age
Gender
Height
Weight
Activity Level
Fitness Goal
```

Click:

```text
Save Profile
```

---

### Step 3 — Track Food

Go to:

```text
Nutrition
```

Select:

```text
Food
Quantity
Meal
```

Click:

```text
Add Food
```

Multiple food items can be added.

---

### Step 4 — Track Exercise

Go to:

```text
Exercise
```

Select:

```text
Exercise
Duration
```

Click:

```text
Add Exercise
```

Multiple exercises can be added.

---

### Step 5 — Check Dashboard

Open:

```text
Dashboard
```

to see the overall calorie and fitness summary.

---

# 💾 Data Storage

The current application stores user information locally using:

```text
vitafuel_data.json
```

The file can contain:

```text
Profile
Food records
Exercise records
```

This approach is suitable for a small academic prototype.

For a production application, a proper database would be recommended.

---

# 🔐 Future Database Architecture

A production version could use:

```text
User
 ↓
Authentication
 ↓
Database
 ├── Profile
 ├── Food Records
 ├── Exercise Records
 └── Prediction History
```

Possible database technologies include:

* SQLite
* MySQL
* PostgreSQL

---

# ⚠️ Limitations

The current project has some limitations:

1. Calorie values are estimates.
2. Food nutritional values can vary depending on ingredients and preparation.
3. Exercise calorie expenditure varies between individuals.
4. Local JSON storage is not suitable for a large multi-user system.
5. The basic calorie calculations are formula-based.
6. Machine Learning predictions depend on the quality and features of the training dataset.
7. The application is not intended for medical diagnosis.

---

# 🚀 Future Improvements

Future versions of VitaFuel could include:

* 🔐 User authentication
* 🗄️ Database integration
* 🤖 Fully trained Machine Learning prediction
* 📈 Personal progress charts
* 🥗 Larger food database
* 🇮🇳 Indian food database
* 📷 Food image recognition
* 📱 Mobile application
* ⌚ Smartwatch integration
* 🏃 Fitness device integration
* ☁️ Cloud deployment
* 🧠 Personalized recommendations
* 📊 Advanced analytics
* 🔔 Daily reminders

---

# 🧪 Data Science Components

The project demonstrates several Data Science concepts:

```text
Data Collection
       ↓
Data Cleaning
       ↓
Data Exploration
       ↓
Feature Engineering
       ↓
Machine Learning
       ↓
Model Evaluation
       ↓
Prediction
       ↓
Application
```

This makes VitaFuel more than a simple calorie calculator—it demonstrates how a Data Science workflow can be converted into a usable application.

---

# 🔒 Disclaimer

> **VitaFuel is an educational and general wellness project. Calorie, BMI, BMR, TDEE, nutrition and exercise values are estimates and may not be accurate for every individual. The application is not a substitute for professional medical, nutritional or fitness advice.**

---

# 👩‍💻 Author

**Bhabna Paul**

B.Sc. Data Science
Asansol Engineering College

### Project

**VitaFuel — AI Calorie & Fitness Assistant**

---

# ⭐ Project Highlights

```text
🥗 Calorie Estimation
⚖️ BMI Calculation
🔥 BMR & TDEE
🍎 Food Tracking
🏃 Multiple Exercise Tracking
📊 Dashboard
🤖 Machine Learning
📈 Data Analysis
💾 Data Persistence
🌐 Streamlit Application
```

---

## 📜 License

This project is developed for **educational and academic purposes**.
