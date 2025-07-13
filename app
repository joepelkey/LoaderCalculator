import streamlit as st

st.title("Live Loader Efficiency Tracker")

packages = st.number_input("Packages Loaded", min_value=0)
hours = st.number_input("Hours Loaded", min_value=0.0, format="%.2f")
target = st.number_input("Target PPH", min_value=1)

if hours > 0:
    actual_pph = packages / hours
    excess_hours = (packages / target) - hours
    st.metric("Actual PPH", f"{actual_pph:.2f}")

    if excess_hours < 0:
        st.error(f"Cost: {abs(excess_hours):.2f} hours")
    else:
        st.success(f"Saved: {excess_hours:.2f} hours")
else:
    st.write("Enter hours to calculate.")
