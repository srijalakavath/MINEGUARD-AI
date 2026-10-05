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
            rgba(10, 7, 3, 0.58),
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
    max-width: 1000px;
    padding-top: 2rem;
}}

h1, h2, h3 {{
    color: #FFD700 !important;
}}

p, label {{
    color: white !important;
}}

.stButton > button {{
    background-color: #8B5A2B;
    color: white;
    border: 1px solid #FFD700;
    border-radius: 10px;
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

st.title("❓ Employee Help")

st.markdown(
    """
    <h3 style="text-align:center;">
    🤖 MineGuard Employee Assistant
    </h3>
    """,
    unsafe_allow_html=True
)

st.info(
    "👷 Ask me anything about mining safety, emergencies, "
    "PPE, equipment, medical help, environment and workplace rules."
)


# =====================================================
# CHATBOT KNOWLEDGE
# =====================================================

def get_bot_answer(question):

    q = question.lower().strip()

    # -------------------------------
    # GREETING
    # -------------------------------

    if any(word in q for word in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening"
    ]):

        return """
👋 **Hello!**

I am the **MineGuard Employee Assistant**.

You can ask me about:

🦺 Safety  
🚨 Emergency  
🏥 Medical help  
⛑️ PPE  
🚜 Equipment  
⛰️ Mine areas  
🌱 Environment  
📢 Reporting problems
"""


    # -------------------------------
    # SAFETY
    # -------------------------------

    if (
        "safety" in q
        or "safe" in q
        or "unsafe" in q
        or "danger" in q
        or "hazard" in q
    ):

        return """
🦺 **Mining Safety**

Always follow the mine's approved safety procedures.

Before starting work:

• Wear the required PPE.
• Check your work area.
• Inspect equipment before use.
• Follow supervisor instructions.
• Report unsafe conditions immediately.

⚠️ Never ignore a dangerous condition.
"""


    # -------------------------------
    # PPE
    # -------------------------------

    if (
        "ppe" in q
        or "helmet" in q
        or "safety shoes" in q
        or "gloves" in q
        or "protective" in q
    ):

        return """
⛑️ **Personal Protective Equipment**

Depending on the task and site rules, PPE may include:

• Safety helmet
• Safety shoes
• Safety glasses
• Gloves
• High-visibility clothing
• Hearing protection
• Respiratory protection

Always use the PPE required for your specific work area.
"""


    # -------------------------------
    # EMERGENCY
    # -------------------------------

    if (
        "emergency" in q
        or "accident" in q
        or "fire" in q
        or "explosion" in q
        or "dangerous situation" in q
    ):

        return """
🚨 **Emergency Procedure**

If there is an emergency:

1. Move away from immediate danger if safe.
2. Inform the mine emergency/control team.
3. Alert nearby workers when appropriate.
4. Follow the site's emergency procedure.
5. Go to the designated assembly point.
6. Do not return until authorized.

🚨 For a real emergency, contact the site's official emergency team immediately.
"""


    # -------------------------------
    # MEDICAL
    # -------------------------------

    if (
        "medical" in q
        or "doctor" in q
        or "injury" in q
        or "injured" in q
        or "hospital" in q
        or "first aid" in q
    ):

        return """
🏥 **Medical Assistance**

If you are injured or become unwell:

1. Stop work if it is safe.
2. Inform your supervisor.
3. Contact the site's medical team.
4. Get first aid or medical attention.
5. Report the incident according to site procedure.

For serious injuries, seek emergency medical assistance immediately.
"""


    # -------------------------------
    # EQUIPMENT
    # -------------------------------

    if (
        "equipment" in q
        or "machine" in q
        or "vehicle" in q
        or "excavator" in q
        or "truck" in q
    ):

        return """
🚜 **Mining Equipment**

Before operating equipment:

• Make sure you are trained and authorized.
• Inspect the equipment.
• Check for visible damage.
• Follow operating procedures.
• Wear required PPE.

If equipment is damaged or unsafe:

🛑 Do not operate it.

Report it to the responsible supervisor or maintenance team.
"""


    # -------------------------------
    # RESTRICTED AREA
    # -------------------------------

    if (
        "restricted" in q
        or "permission" in q
        or "authorized" in q
        or "enter" in q
    ):

        return """
🚧 **Restricted Areas**

Do not enter a restricted area unless you are authorized.

Please confirm access with:

👷 Your supervisor  
🦺 Safety officer  
🏢 Site control team

MineGuard AI cannot grant real-world access permission.
"""


    # -------------------------------
    # ENVIRONMENT
    # -------------------------------

    if (
        "environment" in q
        or "pollution" in q
        or "dust" in q
        or "water pollution" in q
        or "waste" in q
    ):

        return """
🌱 **Environmental Protection**

If you notice:

🌫️ Excessive dust  
💧 Water pollution  
🛢️ Leakage  
🗑️ Improper waste  
🌳 Land damage

Report it to the supervisor or environmental team.

Give the approximate location and time of the incident.
"""


    # -------------------------------
    # SLOPE
    # -------------------------------

    if (
        "slope" in q
        or "landslide" in q
        or "crack" in q
        or "ground movement" in q
        or "ground" in q
    ):

        return """
⛰️ **Slope Safety**

If you notice:

• New cracks
• Rock movement
• Ground movement
• Water appearing from a slope
• Falling rocks
• Unusual slope changes

🛑 Stay away from the area.

Immediately inform your supervisor or site safety team.

Do not enter an unstable area without authorization.
"""


    # -------------------------------
    # REPORTING
    # -------------------------------

    if (
        "report" in q
        or "complaint" in q
        or "problem" in q
        or "issue" in q
    ):

        return """
📢 **Report a Workplace Issue**

You can report:

🦺 Safety problems  
🚜 Equipment problems  
🌱 Environmental problems  
🏥 Injuries  
🚧 Restricted-area concerns

Inform your supervisor or the appropriate site team and
follow the mine's official reporting procedure.
"""


    # -------------------------------
    # WORK
    # -------------------------------

    if (
        "work" in q
        or "shift" in q
        or "job" in q
        or "start work" in q
    ):

        return """
⛏️ **Before Starting Work**

Before beginning your shift:

1. Attend required safety briefing.
2. Wear the required PPE.
3. Understand your assigned work area.
4. Check equipment and tools.
5. Follow supervisor instructions.
6. Report anything unsafe.
"""


    # -------------------------------
    # LOCATION
    # -------------------------------

    if (
        "where" in q
        or "location" in q
        or "medical room" in q
        or "office" in q
        or "assembly point" in q
    ):

        return """
📍 **Location Information**

MineGuard AI does not know your mine's real-time site map.

For the correct location of:

🏥 Medical room  
🚨 Emergency assembly point  
🏢 Main office  
🚧 Restricted areas

please check the site's signs, map or contact site control.
"""


    # -------------------------------
    # DEFAULT ANSWER
    # -------------------------------

    return """
🤖 **MineGuard Assistant**

I don't have enough information to answer that specific question.

Try asking something like:

• What PPE should I wear?
• What should I do during an emergency?
• What should I do if I see an unsafe condition?
• How do I report damaged equipment?
• What should I do if I see a slope crack?
• How can I report environmental pollution?

For site-specific instructions, always confirm with your supervisor.
"""


# =====================================================
# CHAT HISTORY
# =====================================================

if "employee_messages" not in st.session_state:

    st.session_state.employee_messages = [
        {
            "role": "assistant",
            "content":
            "👋 Hello! I am MineGuard Employee Assistant. "
            "How can I help you today?"
        }
    ]


# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for message in st.session_state.employee_messages:

    with st.chat_message(
        message["role"],
        avatar="👷" if message["role"] == "user" else "🤖"
    ):

        st.markdown(message["content"])


# =====================================================
# CHAT INPUT
# =====================================================

user_question = st.chat_input(
    "💬 Ask your mining-related question..."
)


# =====================================================
# PROCESS QUESTION
# =====================================================

if user_question:

    # Show user message
    with st.chat_message(
        "user",
        avatar="👷"
    ):

        st.markdown(user_question)

    # Save user message
    st.session_state.employee_messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    # Generate answer
    answer = get_bot_answer(user_question)


    # Show bot answer
    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        st.markdown(answer)


    # Save bot answer
    st.session_state.employee_messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# =====================================================
# QUICK QUESTIONS
# =====================================================

st.markdown("## 💡 Try asking")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        "🦺 **What PPE should I wear?**"
    )

with col2:

    st.markdown(
        "🚨 **What should I do during an emergency?**"
    )

with col3:

    st.markdown(
        "⛰️ **What if I see a slope crack?**"
    )


# =====================================================
# CLEAR CHAT
# =====================================================

if st.button("🗑️ Clear Chat"):

    st.session_state.employee_messages = [
        {
            "role": "assistant",
            "content":
            "👋 Hello! I am MineGuard Employee Assistant. "
            "How can I help you today?"
        }
    ]

    st.rerun()


# =====================================================
# IMPORTANT NOTICE
# =====================================================

st.warning(
    "⚠️ This chatbot provides general guidance for the project demo. "
    "For real emergencies, medical situations, access permissions, "
    "or mine-specific procedures, follow official site instructions "
    "and contact authorized personnel."
)


# =====================================================
# BACK BUTTON
# =====================================================

if st.button("🏠 Back to Dashboard"):

    st.switch_page("pages/1_Home.py")