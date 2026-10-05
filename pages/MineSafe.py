import streamlit as st
import base64
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="MineSafe AI",
    page_icon="🦺",
    layout="wide"
)

# ==================================================
# LOAD BACKGROUND IMAGE
# ==================================================

image_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "mine_background.png"
)

if os.path.exists(image_path):

    with open(image_path, "rb") as file:
        image_data = base64.b64encode(
            file.read()
        ).decode()

    background_image = (
        "data:image/png;base64," + image_data
    )

else:
    background_image = ""

# ==================================================
# CSS
# ==================================================

st.markdown(f"""
<style>

.stApp {{
    background-image:
        linear-gradient(
            rgba(10, 7, 3, 0.55),
            rgba(20, 12, 5, 0.72)
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

.title {{
    text-align: center;
    color: #FFD700;
    font-size: 48px;
    font-weight: bold;
    text-shadow: 0 0 20px black;
}}

.subtitle {{
    text-align: center;
    color: #F5E6C8;
    font-size: 18px;
    margin-bottom: 25px;
}}

.box {{
    background: rgba(15, 10, 5, 0.90);
    border: 1px solid #B8860B;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 20px;
}}

.stButton > button {{
    background: linear-gradient(
        90deg,
        #9A6B0A,
        #FFD700
    );

    color: #1a1208;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    height: 48px;
}}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="title">🦺 MineSafe AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '⛏️ Smart Mining Safety Risk Assessment'
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# SAMPLE TRAINING DATA
# ==================================================

data = pd.DataFrame({
    "experience": [
        1, 2, 3, 5, 7, 10,
        1, 4, 6, 8, 2, 9
    ],

    "rainfall": [
        90, 80, 70, 30, 20, 10,
        100, 60, 25, 15, 85, 5
    ],

    "water": [
        90, 80, 70, 30, 20, 10,
        95, 60, 25, 15, 85, 5
    ],

    "accidents": [
        3, 2, 2, 0, 0, 0,
        4, 1, 0, 0, 3, 0
    ],

    "shift": [
        1, 1, 0, 0, 0, 0,
        1, 1, 0, 0, 1, 0
    ],

    "risk": [
        2, 2, 2, 1, 0, 0,
        2, 2, 0, 0, 2, 0
    ]
})

X = data[
    [
        "experience",
        "rainfall",
        "water",
        "accidents",
        "shift"
    ]
]

y = data["risk"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# ==================================================
# INPUT SECTION
# ==================================================

st.markdown(
    '<div class="box">',
    unsafe_allow_html=True
)

st.subheader("👷 Worker & Mine Conditions")

col1, col2 = st.columns(2)

# --------------------------------------------------
# LEFT
# --------------------------------------------------

with col1:

    experience = st.slider(
        "👷 Worker Experience (Years)",
        0,
        20,
        3
    )

    rainfall = st.slider(
        "🌧️ Rainfall Level",
        0,
        100,
        40
    )

    water = st.slider(
        "💧 Underground Water Condition",
        0,
        100,
        30
    )

# --------------------------------------------------
# RIGHT
# --------------------------------------------------

with col2:

    accidents = st.slider(
        "⚠️ Previous Accidents",
        0,
        10,
        0
    )

    shift = st.selectbox(
        "🌙 Work Shift",
        [
            "Day Shift",
            "Night Shift"
        ]
    )

    area = st.selectbox(
        "⛏️ Mine Area",
        [
            "Open Cast",
            "Underground",
            "Processing Area"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# PREDICTION
# ==================================================

shift_value = 1 if shift == "Night Shift" else 0

input_data = pd.DataFrame({
    "experience": [experience],
    "rainfall": [rainfall],
    "water": [water],
    "accidents": [accidents],
    "shift": [shift_value]
})

# ==================================================
# ASSESS RISK
# ==================================================

if st.button(
    "🦺 ASSESS SAFETY RISK",
    use_container_width=True
):

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(
        input_data
    )[0]

    confidence = max(probabilities) * 100

    # ----------------------------------------------
    # RISK LEVEL
    # ----------------------------------------------

    if prediction == 2:

        risk = "🔴 HIGH RISK"

        message = (
            "Immediate safety attention is recommended."
        )

    elif prediction == 1:

        risk = "🟡 MEDIUM RISK"

        message = (
            "Additional safety precautions are recommended."
        )

    else:

        risk = "🟢 LOW RISK"

        message = (
            "Current conditions appear relatively safer."
        )

    st.markdown("---")

    st.subheader("📊 Safety Assessment")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Risk Level",
            risk
        )

    with col2:

        st.metric(
            "AI Confidence",
            f"{confidence:.1f}%"
        )

    with col3:

        st.metric(
            "Mine Area",
            area
        )

    # ==================================================
    # MESSAGE
    # ==================================================

    if prediction == 2:

        st.error(
            f"🚨 {risk}\n\n{message}"
        )

    elif prediction == 1:

        st.warning(
            f"⚠️ {risk}\n\n{message}"
        )

    else:

        st.success(
            f"✅ {risk}\n\n{message}"
        )

    # ==================================================
    # RISK FACTORS
    # ==================================================

    st.subheader("🔎 Important Risk Factors")

    factors = []

    if rainfall >= 70:
        factors.append("🌧️ High rainfall")

    if water >= 70:
        factors.append("💧 High underground water")

    if accidents >= 2:
        factors.append("⚠️ Previous accident history")

    if experience < 2:
        factors.append("👷 Low worker experience")

    if shift == "Night Shift":
        factors.append("🌙 Night shift")

    if len(factors) == 0:

        st.info(
            "✅ No major risk factor detected "
            "in this demo assessment."
        )

    else:

        for factor in factors:
            st.warning(factor)

    # ==================================================
    # SAFETY RECOMMENDATIONS
    # ==================================================

    st.subheader("🛡️ Safety Recommendations")

    recommendations = [
        "🪖 Ensure required PPE is worn.",
        "🔦 Check lighting and visibility.",
        "📢 Report unsafe conditions immediately.",
        "🚧 Keep workers away from restricted areas.",
        "📋 Follow the mine's approved safety procedures."
    ]

    for recommendation in recommendations:
        st.write(recommendation)

    # ==================================================
    # SUMMARY
    # ==================================================

    st.subheader("📋 Assessment Summary")

    st.markdown(f"""
    <div class="box">

    <p style="color:#F5E6C8;">

    👷 <b>Experience:</b> {experience} years
    <br><br>

    🌧️ <b>Rainfall Level:</b> {rainfall}
    <br><br>

    💧 <b>Water Condition:</b> {water}
    <br><br>

    ⚠️ <b>Previous Accidents:</b> {accidents}
    <br><br>

    🌙 <b>Shift:</b> {shift}
    <br><br>

    ⛏️ <b>Mine Area:</b> {area}

    </p>

    </div>
    """, unsafe_allow_html=True)

# ==================================================
# DISCLAIMER
# ==================================================

st.markdown("---")

st.warning(
    "⚠️ Demo decision-support system only. "
    "This AI assessment is not a certified mine-safety "
    "system and must not replace official safety procedures "
    "or qualified safety personnel."
)

# ==================================================
# BACK BUTTON
# ==================================================

if st.button(
    "🏠 Back to Dashboard",
    use_container_width=True
):

    st.switch_page(
        "pages/1_Home.py"
    )