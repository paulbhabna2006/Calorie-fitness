# AI Calorie & Fitness Assistant

## Abstract
An educational Streamlit application that estimates calorie needs, captures food and exercise, and demonstrates machine-learning calorie-burn prediction. It is not a medical diagnostic or treatment system.

## Objectives and methodology
- Calculate BMI, Mifflin–St Jeor BMR, activity-adjusted TDEE, and goal-based calorie targets.
- Log estimated food macros and MET-based activity expenditure.
- Train Linear Regression and Random Forest models on `calories.csv`; compare MAE, RMSE and R², then save the lowest-RMSE model.

## Install, train, run
```bash
cd calorie_fitness_app
python -m venv .venv
.venv\Scripts\activate   # Windows PowerShell
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

Sample profile: Female, 30 years, 165 cm, 65 kg, moderately active, general fitness. Add one serving of Rice and one Egg, then log 30 minutes of Walking to see dashboard metrics and charts.

## Results
After training, `model_metrics.json` holds the test split, metrics, best model, and values for an actual-vs-predicted chart. Results vary slightly if the dataset is changed.

## Architecture
`CSV datasets → train_model.py → Joblib model/metrics → app.py → Streamlit pages/session logs → charts`.

## Future scope
Persistent multi-day storage, verified food APIs, authentication, dietary preferences, and clinician-reviewed personalization.

## Conclusion
The project demonstrates an end-to-end beginner-friendly data-science workflow while clearly treating all values as estimates.

## Viva questions and concise answers
1. **What is BMR?** Estimated energy the body uses at rest.
2. **What is TDEE?** BMR adjusted for typical activity.
3. **Why use a train/test split?** To evaluate predictions on unseen data.
4. **What does MAE show?** Average absolute prediction error in calories.
5. **Why compare models?** Different algorithms may generalize differently.
6. **Why Random Forest?** It can model nonlinear feature relationships.
7. **Why are values estimates?** Human metabolism, preparation, and sensors vary.
8. **What is Joblib for?** Saving and loading trained Python models.
