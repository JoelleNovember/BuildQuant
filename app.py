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


#BUILDING DIMENSIONS

st.header("📐 Building Dimensions")

col1, col2, col3 = st.columns(3)

with col1:
    length = st.number_input(
        "Length (m)",
        min_value=0.0,
        step=0.1
    )

with col2:
    width = st.number_input(
        "Width (m)",
        min_value=0.0,
        step=0.1
    )

with col3:
    wall_height = st.number_input(
        "Wall Height (m)",
        min_value=0.0,
        step=0.1
    )

st.divider()

# DOORS AND WINDOWS

st.header("🚪 Doors & Windows")

col1, col2 = st.columns(2)

with col1:
    number_of_doors = st.number_input(
        "Number of Doors",
        min_value=0,
        step=1
    )

with col2:
    number_of_windows = st.number_input(
        "Number of Windows",
        min_value=0,
        step=1
    )

st.divider()


# SAVE PROJECT
if st.button("💾 Save Project", type="primary"):

    st.success("Project information captured successfully!")

    st.subheader("Project Summary")

    st.write(f"**Project:** {project_name}")
    st.write(f"**Project Number:** {project_number}")
    st.write(f"**Location:** {location}")
    st.write(f"**Building Type:** {building_type}")

    st.subheader("Building Information")

    st.write(f"**Length:** {length} m")
    st.write(f"**Width:** {width} m")
    st.write(f"**Wall Height:** {wall_height} m")

    st.subheader("Openings")

    st.write(f"**Doors:** {number_of_doors}")
    st.write(f"**Windows:** {number_of_windows}")

    