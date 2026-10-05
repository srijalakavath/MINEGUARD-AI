import streamlit as st
import base64
import os
import pandas as pd

# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Mine Operations",
    page_icon="🚜",
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
    '<div class="title">🚜 Mine Operations</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '⛏️ Track daily mining production and operations'
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# DAILY INPUT
# ==================================================

st.markdown(
    '<div class="box">',
    unsafe_allow_html=True
)

st.subheader("📋 Daily Mining Record")

col1, col2 = st.columns(2)

# ==================================================
# LEFT SIDE
# ==================================================

with col1:

    mine_date = st.date_input(
        "📅 Mining Date"
    )

    mine_area = st.selectbox(
        "📍 Mine Area",
        [
            "North Zone",
            "South Zone",
            "East Zone",
            "West Zone",
            "Underground Zone"
        ]
    )

    planned_depth = st.number_input(
        "🎯 Planned Depth (m)",
        min_value=0.0,
        value=100.0,
        step=5.0
    )

    actual_depth = st.number_input(
        "📏 Actual Depth Reached (m)",
        min_value=0.0,
        value=80.0,
        step=5.0
    )

# ==================================================
# RIGHT SIDE
# ==================================================

with col2:

    soil_removed = st.number_input(
        "🟫 Soil Removed (tonnes)",
        min_value=0.0,
        value=500.0,
        step=50.0
    )

    rock_removed = st.number_input(
        "🪨 Rock Removed (tonnes)",
        min_value=0.0,
        value=300.0,
        step=50.0
    )

    ore_extracted = st.number_input(
        "💎 Ore Extracted (tonnes)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

    material_type = st.selectbox(
        "⛏️ Main Material",
        [
            "Gold Ore",
            "Coal",
            "Iron Ore",
            "Copper Ore",
            "Bauxite",
            "Other"
        ]
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# WORKFORCE
# ==================================================

st.markdown(
    '<div class="box">',
    unsafe_allow_html=True
)

st.subheader("👷 Workforce & Equipment")

col1, col2, col3 = st.columns(3)

with col1:

    workers = st.number_input(
        "👷 Number of Workers",
        min_value=0,
        value=25,
        step=1
    )

with col2:

    working_hours = st.number_input(
        "⏱️ Working Hours",
        min_value=0.0,
        max_value=24.0,
        value=8.0,
        step=0.5
    )

with col3:

    fuel_used = st.number_input(
        "⛽ Fuel Used (litres)",
        min_value=0.0,
        value=250.0,
        step=10.0
    )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# CALCULATIONS
# ==================================================

if planned_depth > 0:

    depth_progress = (
        actual_depth / planned_depth
    ) * 100

    depth_progress = min(
        depth_progress,
        100
    )

else:

    depth_progress = 0


total_material = (
    soil_removed +
    rock_removed +
    ore_extracted
)

if total_material > 0:

    ore_percentage = (
        ore_extracted /
        total_material
    ) * 100

else:

    ore_percentage = 0

# ==================================================
# RECORD BUTTON
# ==================================================

if st.button(
    "🚜 RECORD DAILY OPERATION",
    use_container_width=True
):

    st.markdown("---")

    st.subheader("📊 Daily Production Summary")

    # ------------------------------------------------
    # METRICS
    # ------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "⛏️ Ore Extracted",
            f"{ore_extracted:,.0f} t"
        )

    with col2:

        st.metric(
            "🪨 Total Material",
            f"{total_material:,.0f} t"
        )

    with col3:

        st.metric(
            "📏 Depth Progress",
            f"{depth_progress:.1f}%"
        )

    with col4:

        st.metric(
            "💎 Ore %",
            f"{ore_percentage:.1f}%"
        )

    # ------------------------------------------------
    # DEPTH PROGRESS
    # ------------------------------------------------

    st.subheader("📏 Mining Depth Progress")

    st.progress(
        depth_progress / 100
    )

    st.write(
        f"🎯 {actual_depth:.1f} m completed "
        f"out of {planned_depth:.1f} m planned."
    )

    # ------------------------------------------------
    # PRODUCTION STATUS
    # ------------------------------------------------

    st.subheader("📦 Production Status")

    if ore_extracted >= 100:

        st.success(
            "🟢 Good production level recorded."
        )

    elif ore_extracted >= 50:

        st.warning(
            "🟡 Moderate production level recorded."
        )

    else:

        st.info(
            "🔵 Low production level recorded."
        )

    # ------------------------------------------------
    # OPERATION SUMMARY
    # ------------------------------------------------

    st.subheader("📋 Operation Summary")

    operation_data = pd.DataFrame({
        "Parameter": [
            "Date",
            "Mine Area",
            "Main Material",
            "Planned Depth",
            "Actual Depth",
            "Soil Removed",
            "Rock Removed",
            "Ore Extracted",
            "Workers",
            "Working Hours",
            "Fuel Used"
        ],

        "Value": [
            str(mine_date),
            mine_area,
            material_type,
            f"{planned_depth:.1f} m",
            f"{actual_depth:.1f} m",
            f"{soil_removed:,.0f} tonnes",
            f"{rock_removed:,.0f} tonnes",
            f"{ore_extracted:,.0f} tonnes",
            str(workers),
            f"{working_hours:.1f} hours",
            f"{fuel_used:,.0f} litres"
        ]
    })

    st.dataframe(
        operation_data,
        use_container_width=True,
        hide_index=True
    )

# ==================================================
# SESSION HISTORY
# ==================================================

if "operations" not in st.session_state:

    st.session_state.operations = []

if st.button(
    "➕ SAVE THIS DAY'S RECORD",
    use_container_width=True
):

    record = {
        "Date": str(mine_date),
        "Area": mine_area,
        "Material": material_type,
        "Ore (t)": ore_extracted,
        "Workers": workers,
        "Fuel (L)": fuel_used
    }

    st.session_state.operations.append(
        record
    )

    st.success(
        "✅ Daily mining record saved!"
    )

# ==================================================
# HISTORY
# ==================================================

if len(st.session_state.operations) > 0:

    st.markdown("---")

    st.subheader("📚 Daily Operation History")

    history = pd.DataFrame(
        st.session_state.operations
    )

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📈 Ore Production Trend")

    chart_data = history[
        ["Date", "Ore (t)"]
    ].set_index("Date")

    st.line_chart(
        chart_data
    )

# ==================================================
# CONNECTION
# ==================================================

st.markdown("---")

st.markdown("""
<div class="box">

<h3 style="color:#FFD700;">
🔗 MineGuard Connection
</h3>

<p style="color:#F5E6C8;">

⛏️ <b>OreScope</b> helps understand ore location,
grade and quantity.

<br><br>

🚜 <b>Mine Operations</b> records actual daily production.

<br><br>

💰 <b>MineBudget</b> can use production information
to understand mining revenue and expenses.

<br><br>

🌱 <b>EnvironmentWatch</b> can monitor the environmental
impact of mining activities.

</p>

</div>
""", unsafe_allow_html=True)

# ==================================================
# DEMO NOTE
# ==================================================

st.info(
    "ℹ️ This is a demonstration mining-management "
    "system. Production values shown here are example "
    "data and should not be treated as actual mine records."
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