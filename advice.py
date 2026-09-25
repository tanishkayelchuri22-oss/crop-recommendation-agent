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
    Generate structured farming advice based on:
    - predicted crop
    - soil nutrients
    - soil pH
    - weather conditions
    """

    crop_name = str(crop).lower()

    crop_advice = {
        "rice": [
            "Maintain adequate soil moisture throughout important growth stages.",
            "Monitor field water levels and provide proper drainage after heavy rainfall."
        ],

        "maize": [
            "Maintain adequate soil moisture during germination and grain development.",
            "Use well-drained soil and avoid prolonged standing water."
        ],

        "wheat": [
            "Maintain controlled irrigation and avoid excessive soil moisture.",
            "Monitor the crop carefully during periods of high temperature."
        ],

        "cotton": [
            "Maintain suitable soil moisture while avoiding prolonged waterlogging.",
            "Monitor the crop regularly during humid conditions."
        ],

        "jute": [
            "Maintain adequate moisture because jute generally performs well in warm and humid conditions.",
            "Avoid prolonged waterlogging where drainage is poor."
        ],

        "coffee": [
            "Maintain suitable soil moisture and good soil management.",
            "Good drainage is important for healthy coffee growth."
        ],

        "banana": [
            "Maintain regular soil moisture and adequate nutrient availability.",
            "Ensure good drainage during periods of heavy rainfall."
        ],

        "coconut": [
            "Maintain adequate soil moisture during dry periods.",
            "Ensure good drainage during periods of heavy rainfall."
        ],

        "chickpea": [
            "Maintain moderate soil moisture and good drainage.",
            "Avoid excessive irrigation and prolonged waterlogging."
        ],

        "kidneybeans": [
            "Maintain moderate soil moisture and good drainage.",
            "Avoid excessive irrigation and waterlogged soil."
        ],

        "lentil": [
            "Maintain moderate moisture and good soil drainage.",
            "Avoid excessive irrigation during the growing period."
        ],

        "blackgram": [
            "Maintain moderate soil moisture and good drainage.",
            "Monitor the crop carefully during periods of high humidity."
        ],

        "mungbean": [
            "Maintain moderate moisture and avoid excessive irrigation.",
            "Monitor soil moisture carefully during hot conditions."
        ],

        "mothbeans": [
            "Avoid excessive irrigation and monitor soil moisture carefully.",
            "Good drainage is important for healthy crop development."
        ],

        "pigeonpeas": [
            "Maintain moderate soil moisture and good drainage.",
            "Avoid prolonged waterlogging during heavy rainfall."
        ],

        "grapes": [
            "Use careful irrigation management and maintain good drainage.",
            "Avoid excessive moisture around the root zone."
        ],

        "apple": [
            "Monitor temperature and moisture conditions during crop development.",
            "Maintain suitable soil drainage."
        ],

        "mango": [
            "Maintain appropriate irrigation and good soil drainage.",
            "Avoid excessive irrigation during wet conditions."
        ],

        "orange": [
            "Maintain consistent soil moisture without excessive irrigation.",
            "Ensure good drainage around the root zone."
        ],

        "papaya": [
            "Maintain adequate moisture while ensuring excellent drainage.",
            "Avoid prolonged waterlogging around the root system."
        ],

        "pomegranate": [
            "Use controlled irrigation and maintain well-drained soil.",
            "Avoid excessive moisture around the root zone."
        ],

        "watermelon": [
            "Maintain adequate moisture during early growth and fruit development.",
            "Avoid waterlogging and maintain good field drainage."
        ],

        "muskmelon": [
            "Maintain controlled irrigation during crop development.",
            "Avoid excessive moisture and maintain good drainage."
        ]
    }

    # ==================================================
    # CROP-SPECIFIC ADVICE
    # ==================================================

    crop_messages = crop_advice.get(
        crop_name,
        [
            f"The model recommends {crop_name}.",
            "Follow local agronomic recommendations and monitor crop conditions regularly."
        ]
    )

    # ==================================================
    # SOIL & NUTRIENT ADVICE
    # ==================================================

    soil_messages = []

    if N < 40:
        soil_messages.append(
            "Nitrogen is relatively low. Consider soil testing and appropriate nutrient management."
        )
    elif N > 100:
        soil_messages.append(
            "Nitrogen is relatively high. Avoid unnecessary nitrogen application."
        )
    else:
        soil_messages.append(
            "Nitrogen is within the project's normal range."
        )

    if P < 30:
        soil_messages.append(
            "Phosphorus is relatively low. Consider soil testing and appropriate phosphorus management."
        )
    elif P > 100:
        soil_messages.append(
            "Phosphorus is relatively high. Avoid unnecessary phosphorus application."
        )
    else:
        soil_messages.append(
            "Phosphorus is within the project's normal range."
        )

    if K < 30:
        soil_messages.append(
            "Potassium is relatively low. Consider appropriate potassium management based on soil testing."
        )
    elif K > 100:
        soil_messages.append(
            "Potassium is relatively high. Avoid unnecessary potassium application."
        )
    else:
        soil_messages.append(
            "Potassium is within the project's normal range."
        )

    if ph < 5.5:
        soil_messages.append(
            "Soil is strongly acidic according to the project's thresholds. Consider professional soil-management guidance."
        )
    elif ph < 6:
        soil_messages.append(
            "Soil is acidic according to the project's thresholds. Consider suitable soil-management practices."
        )
    elif ph <= 7.5:
        soil_messages.append(
            "Soil pH is within the project's suitable range."
        )
    elif ph <= 8.5:
        soil_messages.append(
            "Soil is alkaline according to the project's thresholds. Consider suitable soil-management practices."
        )
    else:
        soil_messages.append(
            "Soil is strongly alkaline according to the project's thresholds. Consider professional soil-management guidance."
        )

    # ==================================================
    # WEATHER ADVICE
    # ==================================================

    weather_messages = []

    if temperature < 15:
        weather_messages.append(
            "Temperature is relatively low. Monitor the crop for cold-related stress."
        )
    elif temperature > 30:
        weather_messages.append(
            "Temperature is relatively high. Pay close attention to crop and soil moisture."
        )
    else:
        weather_messages.append(
            "Temperature is within the project's moderate range."
        )

    if humidity < 40:
        weather_messages.append(
            "Humidity is relatively low. Monitor crop moisture conditions."
        )
    elif humidity > 80:
        weather_messages.append(
            "Humidity is relatively high. Monitor the crop for moisture-related problems."
        )
    else:
        weather_messages.append(
            "Humidity is within the project's moderate range."
        )

    if rainfall < 50:
        weather_messages.append(
            "Rainfall is relatively low. Monitor soil moisture and irrigation requirements."
        )
    elif rainfall > 200:
        weather_messages.append(
            "Rainfall is relatively high. Monitor drainage and excess-water conditions."
        )
    else:
        weather_messages.append(
            "Rainfall is within the project's moderate range."
        )

    # ==================================================
    # IMPORTANT CONDITIONS
    # ==================================================

    warnings = []

    if N < 40:
        warnings.append(
            "Low nitrogen may require attention before cultivation."
        )

    if P < 30:
        warnings.append(
            "Low phosphorus may require attention before cultivation."
        )

    if K < 30:
        warnings.append(
            "Low potassium may require attention before cultivation."
        )

    if ph < 5.5 or ph > 8.5:
        warnings.append(
            "Soil pH is outside the project's preferred range and should be evaluated carefully."
        )

    if temperature > 30:
        warnings.append(
            "High temperature may increase crop water requirements."
        )

    if humidity > 80:
        warnings.append(
            "High humidity may increase moisture-related crop risks."
        )

    if rainfall > 200:
        warnings.append(
            "High rainfall may increase the need for drainage."
        )

    if rainfall < 50:
        warnings.append(
            "Low rainfall may increase irrigation requirements."
        )

    if not warnings:
        warnings.append(
            "No major warning conditions were detected using the project's thresholds."
        )

    # ==================================================
    # FINAL RESULT
    # ==================================================

    return {
        "crop": crop_name,

        "crop_advice": crop_messages,

        "soil_advice": soil_messages,

        "weather_advice": weather_messages,

        "warnings": warnings,

        # Keep the original combined advice as well.
        "advice": (
            crop_messages
            + soil_messages
            + weather_messages
            + warnings
        )
    }
