"""Train and save the exercise calorie-burn prediction model."""

from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


ROOT = Path(__file__).parent


def metrics(y_true, y_pred):

    return {
        "MAE": round(mean_absolute_error(y_true, y_pred), 2),
        "RMSE": round(np.sqrt(mean_squared_error(y_true, y_pred)), 2),
        "R2": round(r2_score(y_true, y_pred), 3)
    }


def main():

    # Load dataset
    data = pd.read_csv(ROOT / "calories.csv")

    # Features
    features = [
        "Gender",
        "Age",
        "Height",
        "Weight",
        "Duration",
        "Heart_Rate",
        "Body_Temp",
        "Exercise_Type"
    ]

    X = data[features]
    y = data["Calories"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    # Categorical columns
    categorical = [
        "Gender",
        "Exercise_Type"
    ]

    # Preprocessing
    preprocess = ColumnTransformer(
        [
            (
                "categories",
                OneHotEncoder(handle_unknown="ignore"),
                categorical
            )
        ],
        remainder="passthrough"
    )

    # Models
    candidates = {

        "Linear Regression":
            LinearRegression(),

        "Random Forest":
            RandomForestRegressor(
                n_estimators=250,
                random_state=42,
                min_samples_leaf=1
            )
    }

    results = {}
    fitted = {}

    # Train models
    for name, regressor in candidates.items():

        model = Pipeline(
            [
                ("prep", preprocess),
                ("model", regressor)
            ]
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        results[name] = metrics(
            y_test,
            predictions
        )

        fitted[name] = model

    # Select best model
    best_name = min(
        results,
        key=lambda name: results[name]["RMSE"]
    )

    best = fitted[best_name]

    # Save best model
    joblib.dump(
        best,
        ROOT / "calories_model.pkl"
    )

    # Save categorical encoder
    encoder = (
        best
        .named_steps["prep"]
        .named_transformers_["categories"]
    )

    joblib.dump(
        encoder,
        ROOT / "categorical_encoder.pkl"
    )

    # Predictions
    best_predictions = best.predict(X_test)

    # Save model information
    comparison = {

        "dataset_size": len(data),

        "features": features,

        "test_size": 0.25,

        "results": results,

        "best_model": best_name,

        "actual": y_test.tolist(),

        "predicted":
            best_predictions.round(1).tolist()
    }

    # Save metrics
    (
        ROOT / "model_metrics.json"
    ).write_text(
        json.dumps(
            comparison,
            indent=2
        ),
        encoding="utf-8"
    )

    # Display results
    print("\nModel Results")
    print("=" * 40)

    for name, result in results.items():

        print("\n" + name)
        print("MAE :", result["MAE"])
        print("RMSE:", result["RMSE"])
        print("R2  :", result["R2"])

    print("\nBest Model:", best_name)

    print("\nModel saved as:")
    print("calories_model.pkl")

    print("\nTraining completed successfully!")


if __name__ == "__main__":
    main()