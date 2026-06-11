import streamlit as st

st.set_page_config(page_title="Energy Optimization Chatbot", page_icon="⚡")

st.title("⚡ Energy Optimization Chatbot")

st.write("Calculate electricity consumption and estimated monthly cost.")

appliances = {
    "Air Conditioner": {"power": 1500, "tip": "Set AC temperature to 24–26°C."},
    "Refrigerator": {"power": 150, "tip": "Defrost regularly to improve efficiency."},
    "Computer": {"power": 200, "tip": "Enable sleep mode when idle."},
    "Fan": {"power": 80, "tip": "Clean fan blades regularly."},
    "Washing Machine": {"power": 500, "tip": "Wash full loads to save energy."}
}

appliance = st.selectbox("Select Appliance", list(appliances.keys()))

hours = st.number_input(
    "Usage Hours Per Day",
    min_value=1,
    max_value=24,
    value=5
)

if st.button("Calculate"):

    power = appliances[appliance]["power"]

    daily_units = (power * hours) / 1000
    monthly_units = daily_units * 30

    rate = 6
    monthly_cost = monthly_units * rate

    st.subheader("Results")

    st.success(f"Daily Consumption: {daily_units:.2f} kWh")
    st.success(f"Monthly Consumption: {monthly_units:.2f} kWh")
    st.success(f"Estimated Monthly Bill: ₹{monthly_cost:.2f}")

    st.info(f"Energy Saving Tip: {appliances[appliance]['tip']}")

st.markdown("---")
st.write("Developed using Python and Streamlit")
