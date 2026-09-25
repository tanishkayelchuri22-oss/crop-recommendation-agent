import streamlit as st

from recommendation_engine import generate_recommendation


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("🌱 AI Crop Recommendation System")

st.write(
    "Enter your soil and environmental conditions "
    "to receive a crop recommendation."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("Farm Information")

st.sidebar.write(
    "Enter the measured values from your farm."
)


# ============================================================
# SOIL INPUTS
# ============================================================

st.header("🌱 Soil Conditions")

col1, col2, col3, col4 = st.columns(4)


with col1:

    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=300.0,
        value=90.0,
        step=1.0
    )


with col2:

    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=300.0,
        value=42.0,
        step=1.0
    )


with col3:

    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=300.0,
        value=43.0,
        step=1.0
    )


with col4:

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1
    )


# ============================================================
# WEATHER INPUTS
# ============================================================

st.header("☁ Environmental Conditions")

col1, col2, col3 = st.columns(3)


with col1:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=-20.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )


with col2:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )


with col3:

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=1000.0,
        value=150.0,
        step=1.0
    )


# ============================================================
# ANALYZE BUTTON
# ============================================================

st.divider()

analyze_button = st.button(
    "🔍 Analyze Farm",
    type="primary",
    use_container_width=True
)


# ============================================================
# RUN ANALYSIS
# ============================================================

if analyze_button:

    result = generate_recommendation(
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    )

    # -----------------------------------------
    # Crop Prediction
    # -----------------------------------------

    crop_result = result["crop_prediction"]

    st.success(
        f"🌾 Recommended Crop: {crop_result['crop'].upper()}"
    )

    st.metric(
        "Model Confidence",
        f"{crop_result['confidence']:.2f}%"
    )

    # -----------------------------------------
    # Top 3 Crop Recommendations
    # -----------------------------------------

    st.subheader("🌾 Top 3 Crop Recommendations")

    top_crops = crop_result["top_crops"]

    col1, col2, col3 = st.columns(3)

    columns = [col1, col2, col3]

    for position, item in enumerate(top_crops):

        with columns[position]:

            st.metric(
                f"#{position + 1}",
                item["crop"].upper(),
                f"{item['probability']:.2f}%"
            )

    # -----------------------------------------
    # Soil Analysis
    # -----------------------------------------

    st.divider()

    st.subheader("🌱 Soil Analysis")

    soil = result["soil_analysis"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Nitrogen",
            soil["nitrogen"]["status"]
        )

    with col2:
        st.metric(
            "Phosphorus",
            soil["phosphorus"]["status"]
        )

    with col3:
        st.metric(
            "Potassium",
            soil["potassium"]["status"]
        )

    with col4:
        st.metric(
            "pH",
            soil["ph"]["status"]
        )

    st.info(soil["overall"])

    # -----------------------------------------
    # Weather Analysis
    # -----------------------------------------

    st.divider()

    st.subheader("☁ Weather Analysis")

    weather = result["weather_analysis"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Temperature",
            weather["temperature"]["status"]
        )

    with col2:
        st.metric(
            "Humidity",
            weather["humidity"]["status"]
        )

    with col3:
        st.metric(
            "Rainfall",
            weather["rainfall"]["status"]
        )

    st.info(weather["overall"])

    # -----------------------------------------
# Farming Advice
# -----------------------------------------

st.divider()

st.subheader("🌱 Farming Advice")

farming_advice = result["farming_advice"]


# -----------------------------------------
# Crop-Specific Advice
# -----------------------------------------

st.markdown("### 🌾 Crop-Specific Advice")

for number, advice_item in enumerate(
    farming_advice["crop_advice"],
    start=1
):
    st.write(
        f"**{number}.** {advice_item}"
    )


# -----------------------------------------
# Soil & Nutrient Advice
# -----------------------------------------

st.markdown("### 🧪 Soil & Nutrient Advice")

for number, advice_item in enumerate(
    farming_advice["soil_advice"],
    start=1
):
    st.write(
        f"**{number}.** {advice_item}"
    )


# -----------------------------------------
# Weather Advice
# -----------------------------------------

st.markdown("### 🌦️ Weather Advice")

for number, advice_item in enumerate(
    farming_advice["weather_advice"],
    start=1
):
    st.write(
        f"**{number}.** {advice_item}"
    )


# -----------------------------------------
# Conditions to Watch
# -----------------------------------------

st.markdown("### ⚠️ Conditions to Watch")

for number, warning in enumerate(
    farming_advice["warnings"],
    start=1
):
    st.write(
        f"**{number}.** {warning}"
    )

    # -----------------------------------------
    # Input Summary
    # -----------------------------------------

    st.divider()

    st.subheader("📋 Input Summary")

    input_data = {
        "Parameter": [
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "Soil pH",
            "Rainfall"
        ],
        "Value": [
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]
    }

    st.table(input_data)
