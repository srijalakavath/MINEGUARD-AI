import streamlit as st
import base64
import os
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="OreScope",
    page_icon="⛏️",
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
    '<div class="title">⛏️ OreScope</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🔎 Explore ore depth, grade, quantity and value'
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# INPUT SECTION
# ==================================================

st.markdown(
    '<div class="box">',
    unsafe_allow_html=True
)

st.subheader("🔎 Drill Hole Information")

col1, col2 = st.columns(2)

with col1:

    drill_id = st.text_input(
        "🆔 Drill Hole ID",
        value="DH-001"
    )

    depth = st.number_input(
        "📏 Drilling Depth (m)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

    target_depth = st.number_input(
        "🎯 Target Depth (m)",
        min_value=1.0,
        value=150.0,
        step=10.0
    )

    ore_type = st.selectbox(
        "💎 Ore Type",
        [
            "Gold",
            "Coal",
            "Iron Ore",
            "Copper",
            "Bauxite"
        ]
    )

with col2:

    ore_grade = st.number_input(
        "📊 Ore Grade (%)",
        min_value=0.0,
        max_value=100.0,
        value=4.0,
        step=0.5
    )

    ore_quantity = st.number_input(
        "⚖️ Estimated Ore Quantity (tonnes)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    drilling_progress = (
        depth / target_depth
    ) * 100

    drilling_progress = min(
        drilling_progress,
        100
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# ORE QUALITY
# ==================================================

if ore_grade >= 5:

    quality = "🟢 HIGH"

elif ore_grade >= 2:

    quality = "🟡 MEDIUM"

else:

    quality = "🔴 LOW"

# ==================================================
# DEMO ORE PRICES
# ==================================================

prices = {
    "Gold": 60000,
    "Coal": 5000,
    "Iron Ore": 7000,
    "Copper": 25000,
    "Bauxite": 4500
}

price = prices[ore_type]

estimated_value = (
    ore_quantity * price * (ore_grade / 100)
)

# ==================================================
# ANALYZE BUTTON
# ==================================================

if st.button(
    "🔎 ANALYZE ORE",
    use_container_width=True
):

    st.markdown("---")

    st.subheader("📊 Ore Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "💎 Ore Type",
            ore_type
        )

    with col2:

        st.metric(
            "📊 Ore Grade",
            f"{ore_grade:.2f}%"
        )

    with col3:

        st.metric(
            "⚖️ Quantity",
            f"{ore_quantity:,.0f} t"
        )

    with col4:

        st.metric(
            "💰 Estimated Value",
            f"₹{estimated_value:,.0f}"
        )

    # ==================================================
    # QUALITY
    # ==================================================

    st.subheader("💎 Ore Quality")

    if quality == "🟢 HIGH":

        st.success(
            "🟢 HIGH QUALITY ORE"
        )

    elif quality == "🟡 MEDIUM":

        st.warning(
            "🟡 MEDIUM QUALITY ORE"
        )

    else:

        st.error(
            "🔴 LOW QUALITY ORE"
        )

    # ==================================================
    # DRILLING PROGRESS
    # ==================================================

    st.subheader("📏 Drilling Progress")

    st.progress(
        drilling_progress / 100
    )

    st.write(
        f"🎯 {drilling_progress:.1f}% "
        f"of target depth completed"
    )

    # ==================================================
    # RECOMMENDATION
    # ==================================================

    st.subheader("🤖 Mining Recommendation")

    if ore_grade >= 5 and drilling_progress >= 80:

        st.success(
            "🟢 Strong exploration result. "
            "Further evaluation may be considered."
        )

    elif ore_grade >= 2:

        st.info(
            "🟡 Moderate ore quality. "
            "Additional exploration data is recommended."
        )

    else:

        st.warning(
            "🔴 Low-grade result. "
            "Further investigation is recommended before decisions."
        )

    # ==================================================
    # DRILL HOLE SUMMARY
    # ==================================================

    st.subheader("📋 Drill Hole Summary")

    summary = pd.DataFrame({
        "Parameter": [
            "Drill Hole",
            "Ore Type",
            "Depth",
            "Target Depth",
            "Ore Grade",
            "Ore Quantity",
            "Quality"
        ],

        "Value": [
            drill_id,
            ore_type,
            f"{depth:.1f} m",
            f"{target_depth:.1f} m",
            f"{ore_grade:.2f}%",
            f"{ore_quantity:,.0f} tonnes",
            quality
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

# ==================================================
# SAMPLE DRILL HOLES
# ==================================================

st.markdown("---")

st.subheader("📋 Sample Drill-Hole Comparison")

sample_data = pd.DataFrame({
    "Drill Hole": [
        "DH-001",
        "DH-002",
        "DH-003",
        "DH-004",
        "DH-005"
    ],

    "Depth (m)": [
        120,
        180,
        150,
        220,
        100
    ],

    "Ore Type": [
        "Gold",
        "Coal",
        "Iron Ore",
        "Copper",
        "Bauxite"
    ],

    "Grade (%)": [
        5.2,
        3.5,
        4.1,
        2.8,
        2.2
    ],

    "Quantity (t)": [
        1200,
        3000,
        2500,
        1800,
        2100
    ]
})

st.dataframe(
    sample_data,
    use_container_width=True,
    hide_index=True
)

# ==================================================
# GRADE CHART
# ==================================================

st.subheader("📊 Ore Grade Comparison")

fig = px.bar(
    sample_data,
    x="Drill Hole",
    y="Grade (%)",
    color="Ore Type",
    title="Ore Grade by Drill Hole"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================================
# DEMO NOTE
# ==================================================

st.info(
    "ℹ️ Ore prices, grades and estimated values shown "
    "in this project are demo/example values. "
    "Real mining decisions require geological surveys, "
    "sampling and qualified professionals."
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