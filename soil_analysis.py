# ============================================================
# SOIL ANALYSIS MODULE
# ============================================================


def analyze_soil(N, P, K, ph):

    # --------------------------------------------------------
    # Store soil information
    # --------------------------------------------------------

    result = {
        "nitrogen": {},
        "phosphorus": {},
        "potassium": {},
        "ph": {},
        "overall": ""
    }


    # ========================================================
    # NITROGEN ANALYSIS
    # ========================================================

    if N < 40:

        result["nitrogen"] = {
            "status": "Low",
            "message": "Nitrogen level is low."
        }

    elif N <= 100:

        result["nitrogen"] = {
            "status": "Normal",
            "message": "Nitrogen level is within a commonly observed range."
        }

    else:

        result["nitrogen"] = {
            "status": "High",
            "message": "Nitrogen level is high."
        }


    # ========================================================
    # PHOSPHORUS ANALYSIS
    # ========================================================

    if P < 30:

        result["phosphorus"] = {
            "status": "Low",
            "message": "Phosphorus level is low."
        }

    elif P <= 100:

        result["phosphorus"] = {
            "status": "Normal",
            "message": "Phosphorus level is within a commonly observed range."
        }

    else:

        result["phosphorus"] = {
            "status": "High",
            "message": "Phosphorus level is high."
        }


    # ========================================================
    # POTASSIUM ANALYSIS
    # ========================================================

    if K < 30:

        result["potassium"] = {
            "status": "Low",
            "message": "Potassium level is low."
        }

    elif K <= 100:

        result["potassium"] = {
            "status": "Normal",
            "message": "Potassium level is within a commonly observed range."
        }

    else:

        result["potassium"] = {
            "status": "High",
            "message": "Potassium level is high."
        }


    # ========================================================
    # SOIL pH ANALYSIS
    # ========================================================

    if ph < 5.5:

        result["ph"] = {
            "status": "Strongly acidic",
            "message": "The soil is strongly acidic."
        }

    elif ph < 6.0:

        result["ph"] = {
            "status": "Acidic",
            "message": "The soil is acidic."
        }

    elif ph <= 7.5:

        result["ph"] = {
            "status": "Suitable",
            "message": "The soil pH is in a generally suitable range for many crops."
        }

    elif ph <= 8.5:

        result["ph"] = {
            "status": "Alkaline",
            "message": "The soil is alkaline."
        }

    else:

        result["ph"] = {
            "status": "Strongly alkaline",
            "message": "The soil is strongly alkaline."
        }


    # ========================================================
    # OVERALL SOIL ASSESSMENT
    # ========================================================

    statuses = [
        result["nitrogen"]["status"],
        result["phosphorus"]["status"],
        result["potassium"]["status"],
        result["ph"]["status"]
    ]


    low_count = sum(
        1
        for status in statuses
        if status in ["Low", "Strongly acidic", "Strongly alkaline"]
    )


    if low_count == 0:

        result["overall"] = (
            "The supplied soil parameters do not show a "
            "major issue according to these simple thresholds."
        )

    else:

        result["overall"] = (
            "Some supplied soil parameters may require attention. "
            "Consider soil testing and appropriate agronomic guidance."
        )


    return result