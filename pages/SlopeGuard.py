import streamlit as st
import base64
import os
import pandas as pd
import plotly.express as px


# =====================================================
# BACKGROUND IMAGE
# =====================================================

image_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "mine_background.png"
)

if os.path.exists(image_path):
    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode()

    background_image = "data:image/png;base64," + image_data
else:
    background_image = ""


# =====================================================
# PAGE STYLE
# =====================================================

st.markdown(f"""
<style>

.stApp {{
    background-image:
        linear-gradient(
            rgba(10, 7, 3, 0.55),
            rgba(20, 12, 5, 0.75)
        ),
        url("{background_image}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stSidebar"] {{
    display: none;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

.block-container {{
    max-width: 1100px;
    padding-top: 2rem;
}}

h1, h2, h3 {{
    color: #FFD700 !important;
}}

p, label {{
    color: white !important;
}}

.stButton > button {{
    background-color: #B87333;
    color: white;
    border-radius: 10px;
    border: 1px solid #FFD700;
    font-weight: bold;
}}

.stButton > button:hover {{
    background-color: #D4A017;
    color: black;
}}

</style>
""", unsafe_allow_html=True)


# =====================================================
# TITLE
# =====================================================

st.title("⛰️ SlopeGuard")

st.subheader(
    "🪨 Mine Slope Stability & Risk Monitoring"
)

st.info(
    "SlopeGuard analyzes basic slope and ground conditions "
    "to provide a demonstration risk assessment."
)


# =====================================================
# LOCATION
# =====================================================

st.markdown("## 📍 Slope Monitoring Area")

mine_area = st.text_input(
    "⛏️ Mine Area",
    "Open Pit - North Wall"
)

monitoring_date = st.date_input(
    "📅 Monitoring Date"
)


# =====================================================
# SLOPE INPUTS
# =====================================================

st.markdown("## ⛰️ Slope Conditions")

col1, col2, col3 = st.columns(3)

with col1:

    slope_angle = st.number_input(
        "📐 Slope Angle (°)",
        min_value=0.0,
        max_value=90.0,
        value=35.0,
        step=1.0
    )

with col2:

    rainfall = st.number_input(
        "🌧️ Rainfall (mm)",
        min_value=0.0,
        value=20.0,
        step=5.0
    )

with col3:

    soil_strength = st.number_input(
        "🪨 Soil Strength (kPa)",
        min_value=1.0,
        value=150.0,
        step=10.0
    )


# =====================================================
# GROUND CONDITION
# =====================================================

st.markdown("## 🌍 Ground Condition")

ground_condition = st.selectbox(
    "Select current ground condition",
    [
        "Stable",
        "Minor Cracks",
        "Wet / Saturated",
        "Loose / Unstable",
        "Visible Movement"
    ]
)


# =====================================================
# WATER CONDITION
# =====================================================

water_condition = st.selectbox(
    "💧 Ground Water Condition",
    [
        "Low",
        "Moderate",
        "High"
    ]
)


# =====================================================
# RISK SCORE
# =====================================================

risk_score = 0


# Slope angle
if slope_angle > 45:
    risk_score += 3

elif slope_angle > 35:
    risk_score += 2

else:
    risk_score += 1


# Rainfall
if rainfall > 100:
    risk_score += 3

elif rainfall > 50:
    risk_score += 2

else:
    risk_score += 1


# Soil strength
if soil_strength < 75:
    risk_score += 3

elif soil_strength < 120:
    risk_score += 2

else:
    risk_score += 1


# Ground condition
ground_scores = {
    "Stable": 0,
    "Minor Cracks": 1,
    "Wet / Saturated": 2,
    "Loose / Unstable": 3,
    "Visible Movement": 4
}

risk_score += ground_scores[ground_condition]


# Ground water
water_scores = {
    "Low": 0,
    "Moderate": 1,
    "High": 2
}

risk_score += water_scores[water_condition]


# =====================================================
# FACTOR OF SAFETY - DEMO ESTIMATE
# =====================================================

# This is a simplified educational calculation.
# It is NOT a real engineering slope-stability calculation.

base_fos = 2.2

angle_effect = max(0, slope_angle - 30) * 0.018

rain_effect = min(rainfall / 1000, 0.25)

soil_effect = max(
    0,
    (150 - soil_strength) / 1000
)

ground_effect = {
    "Stable": 0.0,
    "Minor Cracks": 0.10,
    "Wet / Saturated": 0.20,
    "Loose / Unstable": 0.35,
    "Visible Movement": 0.50
}

water_effect = {
    "Low": 0.0,
    "Moderate": 0.10,
    "High": 0.20
}

factor_of_safety = (
    base_fos
    - angle_effect
    - rain_effect
    - soil_effect
    - ground_effect[ground_condition]
    - water_effect[water_condition]
)

factor_of_safety = max(0.5, factor_of_safety)


# =====================================================
# RISK LEVEL
# =====================================================

if risk_score <= 5 and factor_of_safety >= 1.5:

    risk_level = "🟢 LOW RISK"

elif risk_score <= 9 and factor_of_safety >= 1.2:

    risk_level = "🟡 MEDIUM RISK"

else:

    risk_level = "🔴 HIGH RISK"


# =====================================================
# MAIN RESULT
# =====================================================

st.markdown("## 🚨 SlopeGuard Assessment")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📊 Risk Score",
        risk_score
    )

with col2:
    st.metric(
        "⛰️ Factor of Safety",
        f"{factor_of_safety:.2f}"
    )

with col3:
    st.metric(
        "🚨 Risk Level",
        risk_level
    )


# =====================================================
# STATUS MESSAGE
# =====================================================

if risk_level == "🟢 LOW RISK":

    st.success(
        "🟢 Slope conditions appear relatively stable "
        "under this demonstration model."
    )

elif risk_level == "🟡 MEDIUM RISK":

    st.warning(
        "🟡 Some conditions require attention. "
        "Increase monitoring and inspect the slope."
    )

else:

    st.error(
        "🔴 HIGH RISK CONDITIONS DETECTED. "
        "Stop relying on this demo calculation and "
        "request qualified site inspection."
    )


# =====================================================
# RISK FACTORS
# =====================================================

st.markdown("## 🔎 Important Risk Factors")

risk_factors = []

if slope_angle > 35:
    risk_factors.append(
        f"📐 High slope angle: {slope_angle}°"
    )

if rainfall > 50:
    risk_factors.append(
        f"🌧️ Significant rainfall: {rainfall} mm"
    )

if soil_strength < 120:
    risk_factors.append(
        f"🪨 Lower soil strength: {soil_strength} kPa"
    )

if ground_condition != "Stable":
    risk_factors.append(
        f"🌍 Ground condition: {ground_condition}"
    )

if water_condition != "Low":
    risk_factors.append(
        f"💧 Ground water condition: {water_condition}"
    )

if len(risk_factors) == 0:

    st.success(
        "✅ No major risk factors detected by this demo model."
    )

else:

    for factor in risk_factors:
        st.write("• " + factor)


# =====================================================
# RECOMMENDATIONS
# =====================================================

st.markdown("## 🦺 Safety Recommendations")

if slope_angle > 45:

    st.warning(
        "📐 Closely inspect steep slope sections."
    )

if rainfall > 50:

    st.warning(
        "🌧️ Increase monitoring after rainfall."
    )

if soil_strength < 120:

    st.warning(
        "🪨 Inspect areas with weaker ground material."
    )

if ground_condition in [
    "Loose / Unstable",
    "Visible Movement"
]:

    st.error(
        "🚨 Visible instability requires immediate "
        "qualified site assessment."
    )

if water_condition == "High":

    st.warning(
        "💧 Check drainage and groundwater conditions."
    )

if (
    slope_angle <= 35
    and rainfall <= 50
    and soil_strength >= 120
    and ground_condition == "Stable"
    and water_condition == "Low"
):

    st.success(
        "✅ Continue routine slope monitoring."
    )


# =====================================================
# DAILY REPORT
# =====================================================

st.markdown("## 📋 Slope Monitoring Report")

slope_report = pd.DataFrame({
    "Parameter": [
        "Mine Area",
        "Slope Angle",
        "Rainfall",
        "Soil Strength",
        "Ground Condition",
        "Ground Water",
        "Factor of Safety",
        "Risk Level"
    ],

    "Value": [
        mine_area,
        f"{slope_angle}°",
        f"{rainfall} mm",
        f"{soil_strength} kPa",
        ground_condition,
        water_condition,
        f"{factor_of_safety:.2f}",
        risk_level
    ]
})

st.dataframe(
    slope_report,
    use_container_width=True,
    hide_index=True
)


# =====================================================
# RISK VISUALIZATION
# =====================================================

st.markdown("## 📊 Risk Factor Visualization")

visual_data = pd.DataFrame({
    "Factor": [
        "Slope Angle",
        "Rainfall",
        "Soil Weakness",
        "Ground Condition",
        "Water Condition"
    ],

    "Risk Contribution": [
        max(0, risk_score if slope_angle > 35 else 1),
        3 if rainfall > 100 else 2 if rainfall > 50 else 1,
        3 if soil_strength < 75 else 2 if soil_strength < 120 else 1,
        ground_scores[ground_condition],
        water_scores[water_condition]
    ]
})

fig = px.bar(
    visual_data,
    x="Factor",
    y="Risk Contribution",
    title="Slope Risk Factors"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# =====================================================
# CONNECTION
# =====================================================

st.markdown("## 🔗 MineGuard AI Connection")

st.info(
    """
🌧️ **Rainfall + Ground Conditions**
        ↓
⛰️ **SlopeGuard**
        ↓
🚨 **Risk Assessment**
        ↓
🦺 **MineSafe AI**
        ↓
⚠️ **Safety Action**

🚜 Mine Operations → provides mining activity context

🌱 EnvironmentWatch → monitors environmental conditions
"""
)


# =====================================================
# IMPORTANT DISCLAIMER
# =====================================================

st.warning(
    "⚠️ IMPORTANT: Factor of Safety and risk calculations "
    "in this application are simplified educational/demo "
    "calculations. They must NOT be used as a substitute "
    "for a qualified mining/geotechnical engineer, "
    "site inspection, or approved engineering analysis."
)


# =====================================================
# BACK BUTTON
# =====================================================

if st.button("🏠 Back to Dashboard"):

    st.switch_page("pages/1_Home.py")