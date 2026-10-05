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

st.title("🌱 EnvironmentWatch")

st.subheader(
    "🌍 Mining Environmental Monitoring System"
)

st.info(
    "EnvironmentWatch helps monitor water, air, noise and "
    "land conditions around the mining area."
)


# =====================================================
# LOCATION
# =====================================================

st.markdown("## 📍 Monitoring Area")

mine_area = st.text_input(
    "⛏️ Mine / Monitoring Area",
    "North Mining Zone"
)

monitoring_date = st.date_input(
    "📅 Monitoring Date"
)


# =====================================================
# WATER MONITORING
# =====================================================

st.markdown("## 💧 Water Quality")

col1, col2 = st.columns(2)

with col1:

    ph = st.number_input(
        "💧 Water pH",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.1
    )

with col2:

    suspended_solids = st.number_input(
        "🌊 Suspended Solids (mg/L)",
        min_value=0.0,
        value=50.0,
        step=5.0
    )


# =====================================================
# AIR MONITORING
# =====================================================

st.markdown("## 🌫️ Air Quality")

dust_level = st.number_input(
    "🌫️ Dust Level (µg/m³)",
    min_value=0.0,
    value=60.0,
    step=5.0
)


# =====================================================
# NOISE MONITORING
# =====================================================

st.markdown("## 🔊 Noise Monitoring")

noise_level = st.number_input(
    "🔊 Noise Level (dB)",
    min_value=0.0,
    value=65.0,
    step=1.0
)


# =====================================================
# LAND MONITORING
# =====================================================

st.markdown("## 🏔️ Land & Reclamation")

col1, col2 = st.columns(2)

with col1:

    disturbed_land = st.number_input(
        "🏔️ Land Disturbed (hectares)",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

with col2:

    restored_land = st.number_input(
        "🌱 Land Restored (hectares)",
        min_value=0.0,
        value=4.0,
        step=1.0
    )


# =====================================================
# RECLAMATION PERCENTAGE
# =====================================================

if disturbed_land > 0:

    reclamation_percentage = (
        restored_land / disturbed_land
    ) * 100

else:

    reclamation_percentage = 0


# =====================================================
# ENVIRONMENTAL STATUS
# =====================================================

st.markdown("## 🚨 Environmental Status")


# Demo thresholds
# These are only for demonstration and are NOT legal limits.

water_status = (
    7.0 <= ph <= 8.5
    and suspended_solids <= 100
)

air_status = dust_level <= 100

noise_status = noise_level <= 75

land_status = reclamation_percentage >= 30


# Count safe conditions

safe_count = sum([
    water_status,
    air_status,
    noise_status,
    land_status
])


# =====================================================
# OVERALL STATUS
# =====================================================

if safe_count == 4:

    overall_status = "🟢 SAFE"

elif safe_count >= 2:

    overall_status = "🟡 WARNING"

else:

    overall_status = "🔴 ALERT"


st.markdown(
    f"### Overall Environmental Status: **{overall_status}**"
)


# =====================================================
# STATUS METRICS
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    if water_status:
        st.success("💧 Water\nSAFE")
    else:
        st.error("💧 Water\nCHECK")


with col2:

    if air_status:
        st.success("🌫️ Air\nSAFE")
    else:
        st.error("🌫️ Air\nCHECK")


with col3:

    if noise_status:
        st.success("🔊 Noise\nSAFE")
    else:
        st.error("🔊 Noise\nCHECK")


with col4:

    if land_status:
        st.success("🌱 Land\nGOOD")
    else:
        st.warning("🌱 Land\nRESTORE")


# =====================================================
# ENVIRONMENTAL DATA TABLE
# =====================================================

st.markdown("## 📋 Environmental Report")

environment_data = pd.DataFrame({
    "Parameter": [
        "Water pH",
        "Suspended Solids",
        "Dust Level",
        "Noise Level",
        "Land Disturbed",
        "Land Restored"
    ],

    "Value": [
        ph,
        suspended_solids,
        dust_level,
        noise_level,
        disturbed_land,
        restored_land
    ],

    "Unit": [
        "pH",
        "mg/L",
        "µg/m³",
        "dB",
        "hectares",
        "hectares"
    ]
})

st.dataframe(
    environment_data,
    use_container_width=True,
    hide_index=True
)


# =====================================================
# RECLAMATION
# =====================================================

st.markdown("## 🌱 Land Reclamation")

st.progress(
    min(reclamation_percentage / 100, 1.0)
)

st.write(
    f"🌱 **{reclamation_percentage:.1f}%** "
    f"of disturbed land has been restored."
)


# =====================================================
# ENVIRONMENTAL CHART
# =====================================================

st.markdown("## 📊 Environmental Monitoring Chart")

chart_data = pd.DataFrame({
    "Parameter": [
        "Suspended Solids",
        "Dust",
        "Noise"
    ],

    "Measured Value": [
        suspended_solids,
        dust_level,
        noise_level
    ]
})

fig = px.bar(
    chart_data,
    x="Parameter",
    y="Measured Value",
    title="Environmental Measurements"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# =====================================================
# AI RECOMMENDATIONS
# =====================================================

st.markdown("## 🤖 EnvironmentWatch Recommendations")


if not water_status:

    st.warning(
        "💧 Water condition needs attention. "
        "Inspect drainage, wastewater and nearby water sources."
    )

if not air_status:

    st.warning(
        "🌫️ Dust level is high. "
        "Consider water spraying and dust-control measures."
    )

if not noise_status:

    st.warning(
        "🔊 Noise level is high. "
        "Check heavy machinery and worker protection measures."
    )

if not land_status:

    st.warning(
        "🌱 Land restoration is below the demo target. "
        "Increase reclamation activities where appropriate."
    )

if safe_count == 4:

    st.success(
        "✅ All monitored indicators are within the "
        "demo safety ranges."
    )


# =====================================================
# CONNECTION WITH OTHER MODULES
# =====================================================

st.markdown("## 🔗 MineGuard AI Connection")

st.info(
    """
🚜 **Mine Operations** → Provides mining activity and production information

🌱 **EnvironmentWatch** → Monitors environmental impact

💰 **MineBudget** → Helps consider environmental operating costs

🦺 **MineSafe AI** → Supports safer mining operations

⛰️ **SlopeGuard** → Monitors ground and slope conditions
"""
)


# =====================================================
# DEMO NOTE
# =====================================================

st.caption(
    "⚠️ Demo monitoring system. Thresholds shown here are "
    "illustrative only and are not legal or regulatory limits."
)


# =====================================================
# BACK BUTTON
# =====================================================

if st.button("🏠 Back to Dashboard"):

    st.switch_page("pages/1_Home.py")