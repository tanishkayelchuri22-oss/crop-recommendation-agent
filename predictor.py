import os
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "crop_recommendation_rf.pkl"
)

CSV_PATH = os.path.join(
    BASE_DIR,
    "Crop_recommendation.csv"
)


# ---------------------------------------------------------
# Load trained model
# ---------------------------------------------------------

model = joblib.load(
    MODEL_PATH
)


# ---------------------------------------------------------
# Create crop-name encoder
# ---------------------------------------------------------

df = pd.read_csv(
    CSV_PATH
)

crop_encoder = LabelEncoder()

crop_encoder.fit(
    df["label"]
)


# ---------------------------------------------------------
# Crop prediction function
# ---------------------------------------------------------

def predict_crop(
    N,
    P,
    K,
    temperature,
    humidity,
    ph,
    rainfall
):

    input_data = pd.DataFrame({
        "N": [N],
        "P": [P],
        "K": [K],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })


    # Predict encoded crop class
    prediction = model.predict(
        input_data
    )


    predicted_class = int(
        prediction[0]
    )


    # Convert class number to crop name
    crop_name = crop_encoder.inverse_transform(
        [predicted_class]
    )[0]


    # Prediction probabilities
    probabilities = model.predict_proba(
        input_data
    )[0]


    confidence = (
        probabilities.max() * 100
    )


    # Top 3 predictions
    top_indices = np.argsort(
        probabilities
    )[-3:][::-1]


    top_crops = []


    for index in top_indices:

        crop = crop_encoder.inverse_transform(
            [int(index)]
        )[0]


        probability = (
            probabilities[index] * 100
        )


        top_crops.append({
            "crop": str(crop),
            "probability": round(
                probability,
                2
            )
        })


    return {
        "crop": str(crop_name),
        "confidence": round(
            confidence,
            2
        ),
        "top_crops": top_crops
    }