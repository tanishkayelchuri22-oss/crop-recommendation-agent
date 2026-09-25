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
    Generate crop-specific farming advice based on
    the predicted crop and current farm conditions.
    """

    advice = []

    crop_name = str(crop).lower()

    # --------------------------------------------------
    # Crop-specific advice
    # --------------------------------------------------

    crop_advice = {

        "rice": [
            "Rice generally benefits from adequate water availability "
            "and consistent soil moisture.",
            "Maintain proper field water management and avoid prolonged "
            "water stress during important growth stages."
        ],

        "maize": [
            "Maize benefits from well-drained soil and adequate moisture "
            "during germination and grain development.",
            "Avoid excessive standing water because poor drainage can "
            "affect maize root development."
        ],

        "wheat": [
            "Wheat generally performs well under cooler growing conditions "
            "with controlled irrigation.",
            "Avoid excessive irrigation, particularly near crop maturity."
        ],

        "cotton": [
            "Cotton benefits from good sunlight, suitable soil conditions "
            "and careful moisture management.",
            "Avoid excessive moisture and monitor the crop regularly "
            "during humid conditions."
        ],

        "jute": [
            "Jute generally prefers warm and humid conditions with "
            "adequate moisture.",
            "Maintain sufficient soil moisture while avoiding prolonged "
            "waterlogging where drainage is poor."
        ],

        "coffee": [
            "Coffee generally benefits from suitable moisture conditions "
            "and well-managed soil.",
            "Good drainage and suitable soil conditions are important "
            "for healthy coffee growth."
        ],

        "sugarcane": [
            "Sugarcane requires substantial water during its growth period "
            "and benefits from good soil fertility.",
            "Maintain adequate moisture while avoiding prolonged "
            "waterlogging."
        ],

        "banana": [
            "Banana generally requires regular moisture and good soil fertility.",
            "Protect the crop from prolonged dry conditions and maintain "
            "adequate drainage during heavy rainfall."
        ],

        "coconut": [
            "Coconut benefits from adequate moisture and well-drained soil.",
            "Maintain soil moisture during dry periods and monitor drainage "
            "during heavy rainfall."
        ],

        "chickpea": [
            "Chickpea generally performs well with moderate moisture "
            "and good drainage.",
            "Avoid excessive irrigation because waterlogging can affect "
            "chickpea growth."
        ],

        "kidneybeans": [
            "Kidney beans benefit from well-drained soil and moderate moisture.",
            "Avoid excessive rainfall or irrigation that may cause "
            "waterlogging."
        ],

        "lentil": [
            "Lentil generally prefers moderate moisture and good drainage.",
            "Avoid excessive irrigation and prolonged wet soil conditions."
        ],

        "blackgram": [
            "Blackgram generally benefits from moderate moisture and "
            "well-drained soil.",
            "Avoid prolonged waterlogging and monitor the crop during "
            "high-humidity conditions."
        ],

        "mungbean": [
            "Mungbean generally performs well with moderate moisture "
            "and good drainage.",
            "Avoid excessive irrigation and monitor moisture during "
            "hot weather."
        ],

        "mothbeans": [
            "Mothbeans are relatively suited to warm and comparatively "
            "dry conditions.",
            "Avoid excessive irrigation and monitor soil moisture carefully."
        ],

        "pigeonpeas": [
            "Pigeonpea generally benefits from good drainage and moderate "
            "soil moisture.",
            "Avoid prolonged waterlogging, particularly during periods "
            "of heavy rainfall."
        ],

        "groundnut": [
            "Groundnut benefits from well-drained soil and appropriate "
            "moisture during pod development.",
            "Avoid prolonged waterlogging because it can affect root and "
            "pod development."
        ],

        "soybean": [
            "Soybean generally benefits from adequate moisture and "
            "well-drained soil.",
            "Monitor drainage during heavy rainfall and avoid prolonged "
            "waterlogging."
        ],

        "grapes": [
            "Grapes benefit from good drainage and careful irrigation management.",
            "Avoid excessive moisture around the roots and monitor humidity "
            "during wet conditions."
        ],

        "apple": [
            "Apple generally benefits from suitable temperature conditions "
            "and well-drained soil.",
            "Monitor temperature and moisture conditions carefully because "
            "extreme conditions can affect fruit development."
        ],

        "mango": [
            "Mango benefits from good drainage and suitable moisture management.",
            "Avoid excessive irrigation and monitor the crop during periods "
            "of heavy rainfall."
        ],

        "orange": [
            "Orange generally benefits from well-drained soil and consistent "
            "moisture management.",
            "Avoid both prolonged drought and excessive water around the roots."
        ],

        "papaya": [
            "Papaya requires good drainage and adequate moisture.",
            "Avoid waterlogging because excessive soil moisture can damage "
            "the root system."
        ],

        "pomegranate": [
            "Pomegranate generally benefits from well-drained soil and "
            "controlled irrigation.",
            "Avoid excessive moisture and maintain appropriate irrigation "
            "during fruit development."
        ],

        "watermelon": [
            "Watermelon benefits from warm conditions and adequate moisture "
            "during early growth and fruit development.",
            "Avoid excessive waterlogging and maintain good field drainage."
        ],

        "muskmelon": [
            "Muskmelon generally benefits from warm conditions and controlled "
            "irrigation.",
            "Avoid excessive moisture because good drainage is important "
            "for healthy root development."
        ]
    }

    if crop_name in crop_advice:
        advice.extend(crop_advice[crop_name])
    else:
        advice.append(
            f"The model recommends {crop_name}. "
            "Check local agronomic recommendations before cultivation."
        )

    # --------------------------------------------------
    # Crop-specific condition checks
    # --------------------------------------------------

    if crop_name == "rice" and rainfall < 50:
        advice.append(
            "For the predicted rice crop, rainfall is relatively low. "
            "Monitor field moisture and irrigation requirements carefully."
        )

    if crop_name == "rice" and rainfall > 200:
        advice.append(
            "For the predicted rice crop, rainfall is relatively high. "
            "Monitor drainage and avoid uncontrolled water accumulation."
        )

    if crop_name in ["wheat", "chickpea", "lentil"] and temperature > 30:
        advice.append(
            f"The predicted {crop_name} may experience stress under "
            "the current high-temperature condition. Monitor the crop closely."
        )

    if crop_name in ["maize", "cotton", "sugarcane"] and temperature > 30:
        advice.append(
            f"The predicted {crop_name} is experiencing a relatively "
            "high temperature condition. Pay attention to soil moisture."
        )

    if crop_name in ["coffee", "jute"] and humidity > 80:
        advice.append(
            f"Humidity is high for the predicted {crop_name}. "
            "Monitor the crop and surrounding field for moisture-related problems."
        )

    if crop_name in [
        "chickpea",
        "lentil",
        "blackgram",
        "mungbean",
        "mothbeans",
        "kidneybeans"
    ] and rainfall > 200:
        advice.append(
            f"Rainfall is high for the predicted {crop_name}. "
            "Good drainage is especially important."
        )

    # --------------------------------------------------
    # Nitrogen advice
    # --------------------------------------------------

    if N < 40:
        advice.append(
            "Nitrogen is relatively low. Consider soil testing and "
            "appropriate nutrient management before applying fertilizer."
        )

    elif N > 100:
        advice.append(
            "Nitrogen is relatively high. Avoid unnecessary nitrogen "
            "application and monitor crop growth."
        )

    else:
        advice.append(
            "Nitrogen is within the project's normal range."
        )

    # --------------------------------------------------
    # Phosphorus advice
    # --------------------------------------------------

    if P < 30:
        advice.append(
            "Phosphorus is relatively low. Consider soil testing and "
            "appropriate phosphorus management."
        )

    elif P > 100:
        advice.append(
            "Phosphorus is relatively high. Avoid unnecessary phosphorus "
            "application."
        )

    else:
        advice.append(
            "Phosphorus is within the project's normal range."
        )

    # --------------------------------------------------
    # Potassium advice
    # --------------------------------------------------

    if K < 30:
        advice.append(
            "Potassium is relatively low. Consider appropriate potassium "
            "management based on soil testing."
        )

    elif K > 100:
        advice.append(
            "Potassium is relatively high. Avoid unnecessary potassium "
            "application."
        )

    else:
        advice.append(
            "Potassium is within the project's normal range."
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
            "Temperature is relatively high. Monitor crop and soil moisture "
            "conditions carefully."
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
            "Humidity is relatively high. Monitor the crop for "
            "moisture-related issues."
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
            "Rainfall is relatively low. Monitor soil moisture and "
            "irrigation needs."
        )

    elif rainfall > 200:
        advice.append(
            "Rainfall is relatively high. Monitor drainage and "
            "excess-water conditions."
        )

    else:
        advice.append(
            "Rainfall is within the project's moderate range."
        )

    return {
        "crop": crop_name,
        "advice": advice
    }
