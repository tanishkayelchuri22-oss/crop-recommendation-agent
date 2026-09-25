def generate_advice(
    crop,
    N,
    P,
    K,
    temperature,
    humidity,
    ph,
    rainfall
):
    """
    Generate simple project-level farming advice
    based on crop prediction and farm conditions.
    """

    advice = []

    # --------------------------------------------------
    # Crop-based advice
    # --------------------------------------------------

    crop_name = str(crop).lower()

    if crop_name == "rice":
        advice.append(
            "Rice generally requires adequate water availability "
            "and suitable soil moisture during its growing period."
        )

    elif crop_name == "jute":
        advice.append(
            "Jute generally performs well in warm conditions "
            "with adequate moisture."
        )

    elif crop_name == "maize":
        advice.append(
            "Maize generally benefits from adequate soil moisture "
            "and balanced nutrient availability."
        )

    elif crop_name == "coffee":
        advice.append(
            "Coffee generally requires suitable moisture conditions "
            "and well-managed soil."
        )

    elif crop_name == "wheat":
        advice.append(
            "Wheat generally performs best under suitable temperature "
            "and moisture conditions."
        )

    elif crop_name == "cotton":
        advice.append(
            "Cotton generally requires suitable soil conditions "
            "and appropriate moisture management."
        )

    else:
        advice.append(
            f"The model recommends {crop_name}. "
            "Check local agronomic recommendations before cultivation."
        )

    # --------------------------------------------------
    # Nitrogen advice
    # --------------------------------------------------

    if N < 40:
        advice.append(
            "Nitrogen level is relatively low. "
            "Consider checking soil nutrient requirements before applying fertilizer."
        )

    elif N > 100:
        advice.append(
            "Nitrogen level is relatively high. "
            "Avoid unnecessary nitrogen application."
        )

    else:
        advice.append(
            "Nitrogen level is within the project's normal range."
        )

    # --------------------------------------------------
    # Phosphorus advice
    # --------------------------------------------------

    if P < 30:
        advice.append(
            "Phosphorus level is relatively low. "
            "Consider soil testing and appropriate nutrient management."
        )

    elif P > 100:
        advice.append(
            "Phosphorus level is relatively high. "
            "Avoid unnecessary phosphorus application."
        )

    else:
        advice.append(
            "Phosphorus level is within the project's normal range."
        )

    # --------------------------------------------------
    # Potassium advice
    # --------------------------------------------------

    if K < 30:
        advice.append(
            "Potassium level is relatively low. "
            "Consider appropriate potassium management based on soil testing."
        )

    elif K > 100:
        advice.append(
            "Potassium level is relatively high. "
            "Avoid unnecessary potassium application."
        )

    else:
        advice.append(
            "Potassium level is within the project's normal range."
        )

    # --------------------------------------------------
    # Soil pH advice
    # --------------------------------------------------

    if ph < 5.5:
        advice.append(
            "Soil is strongly acidic according to the project's thresholds. "
            "Consider professional soil-management guidance."
        )

    elif ph < 6.0:
        advice.append(
            "Soil is acidic according to the project's thresholds. "
            "Consider suitable soil-management practices."
        )

    elif ph <= 7.5:
        advice.append(
            "Soil pH is within the project's suitable range."
        )

    elif ph <= 8.5:
        advice.append(
            "Soil is alkaline according to the project's thresholds. "
            "Consider appropriate soil-management practices."
        )

    else:
        advice.append(
            "Soil is strongly alkaline according to the project's thresholds. "
            "Consider professional soil-management guidance."
        )

    # --------------------------------------------------
    # Temperature advice
    # --------------------------------------------------

    if temperature < 15:
        advice.append(
            "Temperature is relatively low according to the project's thresholds."
        )

    elif temperature > 30:
        advice.append(
            "Temperature is relatively high according to the project's thresholds. "
            "Monitor crop and soil moisture conditions."
        )

    else:
        advice.append(
            "Temperature is within the project's moderate range."
        )

    # --------------------------------------------------
    # Humidity advice
    # --------------------------------------------------

    if humidity < 40:
        advice.append(
            "Humidity is relatively low. Monitor crop moisture conditions."
        )

    elif humidity > 80:
        advice.append(
            "Humidity is relatively high. Monitor the crop for moisture-related issues."
        )

    else:
        advice.append(
            "Humidity is within the project's moderate range."
        )

    # --------------------------------------------------
    # Rainfall advice
    # --------------------------------------------------

    if rainfall < 50:
        advice.append(
            "Rainfall is relatively low. Monitor soil moisture and irrigation needs."
        )

    elif rainfall > 200:
        advice.append(
            "Rainfall is relatively high. Monitor drainage and excess-water conditions."
        )

    else:
        advice.append(
            "Rainfall is within the project's moderate range."
        )

    return {
        "crop": crop_name,
        "advice": advice
    }