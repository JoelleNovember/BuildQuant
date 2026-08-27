import streamlit as st


#Page Configuration
st.set_page_config(
    page_title = "BuildQuant",
    page_icon = "🏗️",
    layout="wide"
)


#Title
st.title("🏗️ BuildQuant")
st.title("Residential Quantity System")

st.divider()


#PROJECT INFORMATION
st.header("📋 Project Information")

project_name = st.text_input(
    "Project Name",
    placeholder="e.g Doe Residence"
)

project_number = st.text_input(
    "Project Number",
    placeholder="e.g PRJ_001"
)

location = st.text_input(
    "Location",
    placeholder="e.g Cape Town"
)

building_type = st.selectbox(
    "Building Type",
    [
        "Single-storey dwelling",
        "Double-storey dewlling"
    ]
)

st.divider()


