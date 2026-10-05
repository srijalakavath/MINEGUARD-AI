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

st.title("💰 MineBudget")

st.subheader("⛏️ Mining Financial & Profit Management")

st.info(
    "MineBudget calculates mining income, expenses, "
    "profit/loss and profit margin."
)


# =====================================================
# INCOME
# =====================================================

st.markdown("## 💵 Mining Income")

col1, col2, col3 = st.columns(3)

with col1:
    ore_sold = st.number_input(
        "⛏️ Ore Sold (tonnes)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

with col2:
    selling_price = st.number_input(
        "💰 Selling Price / Tonne (₹)",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )

with col3:
    other_income = st.number_input(
        "📦 Other Income (₹)",
        min_value=0.0,
        value=0.0,
        step=1000.0
    )


# =====================================================
# INCOME CALCULATION
# =====================================================

ore_revenue = ore_sold * selling_price

total_income = ore_revenue + other_income


# =====================================================
# EXPENSES
# =====================================================

st.markdown("## 💸 Mining Expenses")

col1, col2, col3 = st.columns(3)

with col1:
    fuel = st.number_input(
        "⛽ Fuel Cost (₹)",
        min_value=0.0,
        value=25000.0,
        step=1000.0
    )

with col2:
    labour = st.number_input(
        "👷 Labour Cost (₹)",
        min_value=0.0,
        value=30000.0,
        step=1000.0
    )

with col3:
    maintenance = st.number_input(
        "🔧 Maintenance (₹)",
        min_value=0.0,
        value=15000.0,
        step=1000.0
    )


col1, col2, col3 = st.columns(3)

with col1:
    transportation = st.number_input(
        "🚚 Transportation (₹)",
        min_value=0.0,
        value=10000.0,
        step=1000.0
    )

with col2:
    other_expenses = st.number_input(
        "📦 Other Expenses (₹)",
        min_value=0.0,
        value=5000.0,
        step=1000.0
    )

with col3:
    st.write("")
    st.write("")
    st.caption("💡 Enter your estimated mining expenses.")


# =====================================================
# CALCULATIONS
# =====================================================

total_expenses = (
    fuel
    + labour
    + maintenance
    + transportation
    + other_expenses
)

profit = total_income - total_expenses

if total_income > 0:
    profit_margin = (profit / total_income) * 100
else:
    profit_margin = 0


# =====================================================
# FINANCIAL SUMMARY
# =====================================================

st.markdown("## 📊 Financial Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💵 Total Income",
        f"₹{total_income:,.0f}"
    )

with col2:
    st.metric(
        "💸 Total Expenses",
        f"₹{total_expenses:,.0f}"
    )

with col3:
    st.metric(
        "📈 Profit / Loss",
        f"₹{profit:,.0f}"
    )

with col4:
    st.metric(
        "📊 Profit Margin",
        f"{profit_margin:.1f}%"
    )


# =====================================================
# PROFIT STATUS
# =====================================================

if profit > 0:

    st.success(
        f"🟢 PROFIT — Estimated profit: ₹{profit:,.0f}"
    )

elif profit == 0:

    st.warning(
        "🟡 BREAK-EVEN — Income and expenses are equal."
    )

else:

    st.error(
        f"🔴 LOSS — Estimated loss: ₹{abs(profit):,.0f}"
    )


# =====================================================
# INCOME TABLE
# =====================================================

st.markdown("## 💵 Income Breakdown")

income_data = pd.DataFrame({
    "Income Type": [
        "Ore Revenue",
        "Other Income"
    ],
    "Amount (₹)": [
        ore_revenue,
        other_income
    ]
})

st.dataframe(
    income_data,
    use_container_width=True,
    hide_index=True
)


# =====================================================
# EXPENSE TABLE
# =====================================================

st.markdown("## 💸 Expense Breakdown")

expense_data = pd.DataFrame({
    "Expense Type": [
        "Fuel",
        "Labour",
        "Maintenance",
        "Transportation",
        "Other Expenses"
    ],
    "Amount (₹)": [
        fuel,
        labour,
        maintenance,
        transportation,
        other_expenses
    ]
})

st.dataframe(
    expense_data,
    use_container_width=True,
    hide_index=True
)


# =====================================================
# EXPENSE CHART
# =====================================================

st.markdown("## 📊 Expense Analysis")

fig = px.bar(
    expense_data,
    x="Expense Type",
    y="Amount (₹)",
    title="Mining Expense Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# =====================================================
# AI INSIGHT
# =====================================================

st.markdown("## 🤖 MineBudget AI Insight")

highest_expense = expense_data.loc[
    expense_data["Amount (₹)"].idxmax()
]

expense_name = highest_expense["Expense Type"]

expense_value = highest_expense["Amount (₹)"]


if profit_margin >= 30:

    st.success(
        f"🟢 Healthy operation.\n\n"
        f"Profit margin: {profit_margin:.1f}%\n\n"
        f"Highest expense: {expense_name} "
        f"(₹{expense_value:,.0f})"
    )

elif profit_margin >= 10:

    st.warning(
        f"🟡 Moderate profit.\n\n"
        f"Profit margin: {profit_margin:.1f}%\n\n"
        f"Consider controlling {expense_name} expenses."
    )

else:

    st.error(
        f"🔴 Financial attention required.\n\n"
        f"Profit margin: {profit_margin:.1f}%\n\n"
        f"Review {expense_name} and other operating costs."
    )


# =====================================================
# CONNECTION WITH OTHER MODULES
# =====================================================

st.markdown("## 🔗 MineGuard AI Connection")

st.info(
    """
⛏️ OreScope
→ Ore quantity and quality

🚜 Mine Operations
→ Daily mining production

💰 MineBudget
→ Income, expenses and profit

🌱 EnvironmentWatch
→ Environmental monitoring

🦺 MineSafe AI
→ Mining safety
"""
)


# =====================================================
# DEMO NOTE
# =====================================================

st.caption(
    "⚠️ Demo financial calculator. Actual mining costs, "
    "market prices, taxes and accounting rules may differ."
)


# =====================================================
# BACK TO HOME
# =====================================================

if st.button("🏠 Back to Dashboard"):

    st.switch_page("pages/1_Home.py")