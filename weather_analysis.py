# ============================================================
# WEATHER ANALYSIS MODULE
# ============================================================


def analyze_weather(
    temperature,
    humidity,
    rainfall
):

    # --------------------------------------------------------
    # Store weather information
    # --------------------------------------------------------

    result = {
        "temperature": {},
        "humidity": {},
        "rainfall": {},
        "overall": ""
    }


    # ========================================================
    # TEMPERATURE ANALYSIS
    # ========================================================

    if temperature < 15:

        result["temperature"] = {
            "status": "Low",
            "message": "The supplied temperature is relatively low."
        }

    elif temperature <= 30:

        result["temperature"] = {
            "status": "Moderate",
            "message": "The supplied temperature is in a moderate range."
        }

    else:

        result["temperature"] = {
            "status": "High",
            "message": "The supplied temperature is relatively high."
        }


    # ========================================================
    # HUMIDITY ANALYSIS
    # ========================================================

    if humidity < 40:

        result["humidity"] = {
            "status": "Low",
            "message": "The supplied humidity is relatively low."
        }

    elif humidity <= 80:

        result["humidity"] = {
            "status": "Moderate",
            "message": "The supplied humidity is in a moderate range."
        }

    else:

        result["humidity"] = {
            "status": "High",
            "message": "The supplied humidity is relatively high."
        }


    # ========================================================
    # RAINFALL ANALYSIS
    # ========================================================

    if rainfall < 50:

        result["rainfall"] = {
            "status": "Low",
            "message": "The supplied rainfall is relatively low."
        }

    elif rainfall <= 200:

        result["rainfall"] = {
            "status": "Moderate",
            "message": "The supplied rainfall is in a moderate range."
        }

    else:

        result["rainfall"] = {
            "status": "High",
            "message": "The supplied rainfall is relatively high."
        }


    # ========================================================
    # OVERALL WEATHER ASSESSMENT
    # ========================================================

    statuses = [
        result["temperature"]["status"],
        result["humidity"]["status"],
        result["rainfall"]["status"]
    ]


    high_count = statuses.count("High")
    low_count = statuses.count("Low")


    if high_count >= 2:

        result["overall"] = (
            "Several supplied weather parameters are relatively high."
        )

    elif low_count >= 2:

        result["overall"] = (
            "Several supplied weather parameters are relatively low."
        )

    else:

        result["overall"] = (
            "The supplied weather parameters are generally moderate "
            "according to these simple thresholds."
        )


    return result