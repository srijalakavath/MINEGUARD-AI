import streamlit as st
import base64
import os

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="MineGuard AI",
    page_icon="⛏️",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------

image_path = "mine.jpg"

if os.path.exists(image_path):

    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode()

    background_image = f"data:image/jpeg;base64,{image_data}"

else:
    background_image = ""


# ---------------- CSS ----------------

st.markdown(f"""
<style>

.stApp {{
    background-image:
        linear-gradient(
            rgba(10, 7, 3, 0.65),
            rgba(20, 12, 5, 0.80)
        ),
        url("{background_image}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Hide sidebar */
[data-testid="stSidebar"] {{
    display: none;
}}

/* Hide menu */
#MainMenu {{
    visibility: hidden;
}}

/* Hide footer */
footer {{
    visibility: hidden;
}}

/* Main title */
.title {{
    text-align: center;
    color: #FFD700;
    font-size: 50px;
    font-weight: bold;
    text-shadow: 0 0 20px #8B6508;
    margin-top: 35px;
}}

/* Subtitle */
.subtitle {{
    text-align: center;
    color: #F5E6C8;
    font-size: 19px;
    margin-bottom: 25px;
}}

/* Login box */
.login-box {{
    background: rgba(20, 12, 5, 0.92);
    border: 2px solid #D4AF37;
    border-radius: 22px;
    padding: 35px;
    box-shadow: 0 0 35px rgba(212, 175, 55, 0.40);
}}

/* Input labels */
label {{
    color: #F5E6C8 !important;
}}

/* Login button */
.stButton > button {{
    background: linear-gradient(90deg, #B8860B, #FFD700);
    color: #1a1208;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    height: 50px;
    font-size: 17px;
}}

.stButton > button:hover {{
    background: linear-gradient(90deg, #FFD700, #B8860B);
    color: black;
}}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">⛏️ MineGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🦺 Mining Smarter • Working Safer • Protecting Tomorrow 🌱'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- LOGIN BOX ----------------

col1, col2, col3 = st.columns([1, 1.5, 1])

with col2:

    st.markdown(
        '<div class="login-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center;color:#FFD700;'>"
        "🔐 Welcome Back"
        "</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#E8D8B0;'>"
        "⛏️ Access your MineGuard dashboard"
        "</p>",
        unsafe_allow_html=True
    )

    # Employee Name
    name = st.text_input(
        "👤 Employee Name"
    )

    # Employee ID
    email = st.text_input(
        "📧 Email / Employee ID"
    )

    # Password
    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    st.write("")

    # Login button
    if st.button(
        "⛏️ LOGIN TO MINEGUARD",
        use_container_width=True
    ):

        if name and email and password:

            st.success("✅ Login successful!")

            st.switch_page(
                "pages/1_Home.py"
            )

        else:

            st.warning(
                "⚠️ Please fill all the details."
            )

    st.markdown(
        "<p style='text-align:center;color:#BFA76F;margin-top:20px;'>"
        "🛡️ Safety First &nbsp; • &nbsp; "
        "⛏️ Smart Mining &nbsp; • &nbsp; "
        "🌱 Green Mining"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )