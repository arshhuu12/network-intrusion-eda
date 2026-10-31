# ============================================================
# Network Intrusion Analytics
# M14.1 — Batch Prediction Engine
# ============================================================

from pathlib import Path
import json

import joblib
import numpy as np
import pandas as pd


# ------------------------------------------------------------
# 1. Project paths
# ------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    PROJECT_DIR
    / "models"
    / "unsw_random_forest_pipeline.joblib"
)

METADATA_PATH = (
    PROJECT_DIR
    / "models"
    / "unsw_model_metadata.json"
)


# ------------------------------------------------------------
# 2. Load saved model and metadata
# ------------------------------------------------------------

def load_model():

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    if not METADATA_PATH.exists():
        raise FileNotFoundError(
            f"Metadata file not found: {METADATA_PATH}"
        )

    pipeline = joblib.load(MODEL_PATH)

    with open(
        METADATA_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        metadata = json.load(file)

    return pipeline, metadata


# ------------------------------------------------------------
# 3. Validate uploaded data
# ------------------------------------------------------------

def validate_input(df, metadata):

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    if df.empty:
        raise ValueError(
            "Uploaded CSV contains no records."
        )

    # Check for duplicate column names.
    duplicate_columns = (
        df.columns[df.columns.duplicated()].tolist()
    )

    if duplicate_columns:
        raise ValueError(
            "Duplicate column names detected: "
            + ", ".join(map(str, duplicate_columns))
        )

    required_features = metadata["feature_columns"]

    missing_features = [
        column
        for column in required_features
        if column not in df.columns
    ]

    if missing_features:
        raise ValueError(
            "Missing required feature columns: "
            + ", ".join(missing_features)
        )

    # Preserve training feature order.
    X = df.loc[:, required_features].copy()

    categorical_features = [
        "proto",
        "service",
        "state"
    ]

    numerical_features = [
        column
        for column in required_features
        if column not in categorical_features
    ]

    # Validate numerical features.
    for column in numerical_features:

        converted = pd.to_numeric(
            X[column],
            errors="coerce"
        )

        invalid_values = (
            X[column].notna()
            & converted.isna()
        )

        if invalid_values.any():
            raise ValueError(
                f"Invalid numeric values in column "
                f"'{column}'."
            )

        # Reject infinity and negative infinity.
        if not np.isfinite(
            converted.dropna().to_numpy(dtype=float)
        ).all():
            raise ValueError(
                f"Non-finite numeric values "
                f"detected in column '{column}'."
            )

        X[column] = converted

    # Validate categorical features.
    for column in categorical_features:

        invalid_values = (
            X[column].notna()
            & X[column].astype(str).str.strip().eq("")
        )

        if invalid_values.any():
            raise ValueError(
                f"Empty categorical values "
                f"detected in column '{column}'."
            )

    return X

# ------------------------------------------------------------
# 4. Generate batch predictions
# ------------------------------------------------------------

def predict_batch(df, pipeline, metadata):

    X = validate_input(df, metadata)

    threshold = float(metadata["threshold"])

    probabilities = pipeline.predict_proba(X)[:, 1]

    predicted_labels = (
        probabilities >= threshold
    ).astype(int)

    results = df.copy()

    results["attack_probability"] = probabilities

    results["predicted_label"] = predicted_labels

    results["prediction"] = np.where(
        predicted_labels == 1,
        "Attack",
        "Normal"
    )

    return results


# ------------------------------------------------------------
# 5. Summarize predictions
# ------------------------------------------------------------

def get_prediction_summary(results):

    total_records = len(results)

    attack_count = int(
        (results["predicted_label"] == 1).sum()
    )

    normal_count = int(
        (results["predicted_label"] == 0).sum()
    )

    attack_percentage = (
        attack_count / total_records * 100
    )

    return {
        "total_records": total_records,
        "attack_count": attack_count,
        "normal_count": normal_count,
        "attack_percentage": attack_percentage
    }