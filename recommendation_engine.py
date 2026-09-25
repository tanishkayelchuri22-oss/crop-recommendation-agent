from predictor import predict_crop
from soil_analysis import analyze_soil
from weather_analysis import analyze_weather
from advice import generate_advice


def generate_recommendation(
    N,
    P,
    K,
    temperature,
    humidity,
    ph,
    rainfall
):

    # -----------------------------------------
    # Crop prediction
    # -----------------------------------------

    crop_result = predict_crop(
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    )

    # -----------------------------------------
    # Soil analysis
    # -----------------------------------------

    soil_result = analyze_soil(
        N,
        P,
        K,
        ph
    )

    # -----------------------------------------
    # Weather analysis
    # -----------------------------------------

    weather_result = analyze_weather(
        temperature,
        humidity,
        rainfall
    )

    # -----------------------------------------
    # Farming advice
    # -----------------------------------------

    advice_result = generate_advice(
        crop=crop_result["crop"],
        N=N,
        P=P,
        K=K,
        temperature=temperature,
        humidity=humidity,
        ph=ph,
        rainfall=rainfall
    )

    # -----------------------------------------
    # Final result
    # -----------------------------------------

    return {
        "crop_prediction": crop_result,
        "soil_analysis": soil_result,
        "weather_analysis": weather_result,
        "farming_advice": advice_result
    }