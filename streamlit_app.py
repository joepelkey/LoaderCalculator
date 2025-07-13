import streamlit as st

st.set_page_config(page_title="Production Tracker")

st.title("Production Tracker")

packages = st.number_input("Packages Processed", min_value=0)
hours = st.number_input("Hours", min_value=0.0, format="%.2f")
target = st.number_input("Plan PPH", min_value=1, value=350)

if hours > 0:
    actual_pph = packages / hours
    excess_hours = (packages / target) - hours
    st.metric("Actual PPH", f"{actual_pph:.2f}")

    if excess_hours < 0:
        st.error(f"Off Plan: {abs(excess_hours):.2f} hours")
    else:
        st.success(f"On Plan: {excess_hours:.2f} hours")
else:
    st.write("Enter hours to calculate.")


