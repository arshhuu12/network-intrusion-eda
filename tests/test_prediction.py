import unittest

import numpy as np
import pandas as pd

from app.utils.prediction import (
    load_model,
    validate_input,
    predict_batch,
    get_prediction_summary,
)


class TestPredictionEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load the saved model once for all tests."""

        cls.pipeline, cls.metadata = load_model()

        # Create a small, valid synthetic dataset.
        # No raw benchmark files are required.
        feature_columns = cls.metadata["feature_columns"]

        categorical = {
            "proto": "tcp",
            "service": "http",
            "state": "FIN",
        }

        row = {
            column: categorical.get(column, 0.0)
            for column in feature_columns
        }

        cls.sample = pd.DataFrame([row, row.copy()])

    def test_01_valid_input(self):
        """Valid input should contain 42 model features."""

        result = validate_input(
            self.sample,
            self.metadata
        )

        self.assertEqual(result.shape, (2, 42))

    def test_02_missing_feature(self):
        """Missing required features must be rejected."""

        invalid = self.sample.drop(columns=["dur"])

        with self.assertRaisesRegex(
            ValueError,
            "Missing required feature"
        ):
            validate_input(invalid, self.metadata)

    def test_03_invalid_numeric_value(self):
        """Text in a numeric feature must be rejected."""

        invalid = self.sample.copy()

        invalid["dur"] = invalid["dur"].astype(object)
        invalid.loc[0, "dur"] = "hello"

        with self.assertRaisesRegex(
            ValueError,
            "Invalid numeric values"
        ):
            validate_input(invalid, self.metadata)

    def test_04_infinite_numeric_value(self):
        """Infinite numerical values must be rejected."""

        invalid = self.sample.copy()

        invalid.loc[0, "dur"] = np.inf

        with self.assertRaisesRegex(
            ValueError,
            "Non-finite numeric values"
        ):
            validate_input(invalid, self.metadata)

    def test_05_empty_categorical_value(self):
        """Whitespace-only categories must be rejected."""

        invalid = self.sample.copy()

        invalid.loc[0, "proto"] = " "

        with self.assertRaisesRegex(
            ValueError,
            "Empty categorical values"
        ):
            validate_input(invalid, self.metadata)

    def test_06_empty_dataframe(self):
        """Empty input must be rejected."""

        invalid = self.sample.iloc[0:0].copy()

        with self.assertRaisesRegex(
            ValueError,
            "no records"
        ):
            validate_input(invalid, self.metadata)

    def test_07_duplicate_columns(self):
        """Duplicate feature names must be rejected."""

        invalid = self.sample.copy()

        invalid["dur_copy"] = invalid["dur"]

        columns = list(invalid.columns)
        columns[-1] = "dur"

        invalid.columns = columns

        with self.assertRaisesRegex(
            ValueError,
            "Duplicate column names"
        ):
            validate_input(invalid, self.metadata)

    def test_08_prediction_output(self):
        """Predictions must contain the expected output fields."""

        result = predict_batch(
            self.sample,
            self.pipeline,
            self.metadata
        )

        self.assertEqual(len(result), 2)

        self.assertIn(
            "attack_probability",
            result.columns
        )

        self.assertIn(
            "predicted_label",
            result.columns
        )

        self.assertIn(
            "prediction",
            result.columns
        )

        self.assertTrue(
            result["attack_probability"].between(0, 1).all()
        )

        self.assertTrue(
            result["predicted_label"].isin([0, 1]).all()
        )

    def test_09_prediction_threshold(self):
        """Predicted labels must follow the saved threshold."""

        result = predict_batch(
            self.sample,
            self.pipeline,
            self.metadata
        )

        threshold = self.metadata["threshold"]

        expected_labels = (
            result["attack_probability"] >= threshold
        ).astype(int)

        np.testing.assert_array_equal(
            result["predicted_label"].to_numpy(),
            expected_labels.to_numpy()
        )

    def test_10_prediction_summary(self):
        """Prediction summary should count all records."""

        result = predict_batch(
            self.sample,
            self.pipeline,
            self.metadata
        )

        summary = get_prediction_summary(result)

        print("\nPrediction summary:", summary)

        self.assertIsInstance(summary, dict)


if __name__ == "__main__":
    unittest.main()