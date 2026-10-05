import streamlit as st
import base64
import os


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
            rgba(8, 6, 3, 0.60),
            rgba(20, 12, 5, 0.78)
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
    max-width: 1200px;
    padding-top: 2rem;
}}

h1 {{
    color: #FFD700 !important;
    text-align: center;
}}

h2, h3 {{
    color: #FFD700 !important;
}}

p {{
    color: white !important;
}}

.stButton > button {{
    width: 100%;
    min-height: 55px;

    background-color: #7A4A21;
    color: white;

    border: 1px solid #FFD700;
    border-radius: 12px;

    font-size: 16px;
    font-weight: bold;
}}

.stButton > button:hover {{
    background-color: #D4A017;
    color: black;
}}

.card {{
    background: rgba(25, 15, 7, 0.82);
    border: 1px solid #B87333;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    min-height: 150px;
}}

.card-title {{
    color: #FFD700;
    font-size: 21px;
    font-weight: bold;
}}

.card-text {{
    color: white;
    font-size: 15px;
}}

.flow {{
    background: rgba(15, 10, 5, 0.85);
    border: 1px solid #B87333;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

st.title("⛏️ MineGuard AI")

st.markdown(
    "<h3 style='text-align:center;'>"
    "Smart Mining Management & Safety Platform"
    "</h3>",
    unsafe_allow_html=True
)

st.write(
    "A unified platform for mining safety, ore analysis, "
    "operations, financial management, environmental monitoring "
    "and employee assistance."
)


# =====================================================
# SYSTEM STATUS
# =====================================================

st.markdown("## 🟢 MineGuard System")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("🦺 Safety\nActive")

with col2:
    st.success("⛏️ Mining\nActive")

with col3:
    st.success("🌱 Environment\nActive")

with col4:
    st.success("👷 Employee Help\nActive")


# =====================================================
# MAIN MODULES
# =====================================================

st.markdown("## 🚀 MineGuard Modules")


# Row 1
col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">🦺 MineSafe AI</div>
        <div class="card-text">
        Analyze mining conditions and identify potential
        safety risks.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open MineSafe AI", key="safe"):
        st.switch_page("pages/MineSafe.py")


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">⛏️ OreScope</div>
        <div class="card-text">
        Analyze drilling information, ore grade and
        estimated ore quantity.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open OreScope", key="ore"):
        st.switch_page("pages/OreScope.py")


with col3:

    st.markdown("""
    <div class="card">
        <div class="card-title">🚜 Mine Operations</div>
        <div class="card-text">
        Record daily mining production, workers,
        depth and extracted material.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Mine Operations", key="operations"):
        st.switch_page("pages/MineYield.py")


# Row 2
col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">💰 MineBudget</div>
        <div class="card-text">
        Calculate mining income, expenses,
        profit and loss.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open MineBudget", key="budget"):
        st.switch_page("pages/MineBudget.py")


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">🌱 EnvironmentWatch</div>
        <div class="card-text">
        Monitor water, air, noise and land
        restoration conditions.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open EnvironmentWatch", key="environment"):
        st.switch_page("pages/TailingsWatch.py")


with col3:

    st.markdown("""
    <div class="card">
        <div class="card-title">⛰️ SlopeGuard</div>
        <div class="card-text">
        Monitor slope conditions, rainfall,
        ground stability and risk.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open SlopeGuard", key="slope"):
        st.switch_page("pages/SlopeGuard.py")


# Row 3
col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">❓ Employee Help</div>
        <div class="card-text">
        Help workers with safety, emergency,
        medical and workplace questions.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Employee Help", key="employee"):
        st.switch_page("pages/EmployeeHelp.py")


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">🤖 MineGuard AI</div>
        <div class="card-text">
        Connect safety, operations, environment,
        finance and employee assistance into one platform.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# HOW THE SYSTEM CONNECTS
# =====================================================

st.markdown("## 🔗 How MineGuard AI Works")

st.markdown("""
<div class="flow">

⛏️ <b>OreScope</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

🚜 <b>Mine Operations</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

💰 <b>MineBudget</b>

<br><br>

🌧️ <b>Rainfall + Ground Conditions</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

⛰️ <b>SlopeGuard</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

🦺 <b>MineSafe AI</b>

<br><br>

🚜 <b>Mine Operations</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

🌱 <b>EnvironmentWatch</b>

<br><br>

👷 <b>Employee</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

❓ <b>Employee Help</b>
&nbsp;&nbsp; → &nbsp;&nbsp;

🦺 <b>Safety / Supervisor</b>

</div>
""", unsafe_allow_html=True)


# =====================================================
# PROJECT PURPOSE
# =====================================================

st.markdown("## 🎯 What MineGuard AI Solves")

col1, col2 = st.columns(2)

with col1:

    st.info("""
    🦺 **Safety**

    • Mining risk assessment  
    • Slope monitoring  
    • Safety recommendations  
    • Employee safety guidance
    """)

with col2:

    st.info("""
    📊 **Mining Management**

    • Ore analysis  
    • Daily production  
    • Financial analysis  
    • Environmental monitoring
    """)


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    "<p style='text-align:center;'>"
    "⛏️ MineGuard AI • Smart Mining Management Platform"
    "</p>",
    unsafe_allow_html=True
)