import streamlit as st
import pandas as pd


from database.database import (
    create_tables,
    save_project,
    get_projects,
)

from calculations.quantity_calculations import (
    calculate_floor_area,
    calculate_perimeter,
    calculate_gross_wall_area,
    calculate_opening_area,
    calculate_net_wall_area,
    calculate_quantity_with_waste
)

from calculations.cost_calculations import(
    calculate_material_cost,
    calculate_total_cost
)


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="BuildQuant",
    page_icon="🏗️",
    layout="wide"
)


# ---------------------------------------------------------
# DATABASE INITIALIZATION
# ---------------------------------------------------------

create_tables()


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🏗️ BuildQuant")
st.title("Residential Quantity System")

st.divider()


# ---------------------------------------------------------
# PROJECT INFORMATION
# ---------------------------------------------------------

st.header("📋 Project Information")

project_name = st.text_input(
    "Project Name",
    placeholder="e.g. Doe Residence"
)

project_number = st.text_input(
    "Project Number",
    placeholder="e.g. PRJ_001"
)

location = st.text_input(
    "Location",
    placeholder="e.g. Cape Town"
)

building_type = st.selectbox(
    "Building Type",
    [
        "Single-storey dwelling",
        "Double-storey dwelling"
    ]
)

st.divider()


# ---------------------------------------------------------
# BUILDING DIMENSIONS
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# DOORS AND WINDOWS
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# CALCULATE QUANTITIES
# ---------------------------------------------------------

if st.button("🧮 Calculate Quantities", type="primary"):

    # -----------------------------------------------------
    # Calculate Floor Area
    # -----------------------------------------------------

    floor_area = calculate_floor_area(
        length,
        width
    )


    # -----------------------------------------------------
    # Calculate Perimeter
    # -----------------------------------------------------

    perimeter = calculate_perimeter(
        length,
        width
    )


    # -----------------------------------------------------
    # Calculate Gross Wall Area
    # -----------------------------------------------------

    gross_wall_area = calculate_gross_wall_area(
        perimeter,
        wall_height
    )


    # -----------------------------------------------------
    # Calculate Door Opening Area
    # Standard door size: 0.9m x 2.1m
    # -----------------------------------------------------

    door_area = calculate_opening_area(
        0.9,
        2.1,
        number_of_doors
    )


    # -----------------------------------------------------
    # Calculate Window Opening Area
    # Standard window size: 1.2m x 1.2m
    # -----------------------------------------------------

    window_area = calculate_opening_area(
        1.2,
        1.2,
        number_of_windows
    )


    # -----------------------------------------------------
    # Calculate Net Wall Area
    # -----------------------------------------------------

    net_wall_area = calculate_net_wall_area(
        gross_wall_area,
        door_area,
        window_area
    )


    # -----------------------------------------------------
    # Calculate Floor Tile Quantity
    # 10% waste allowance
    # -----------------------------------------------------

    tile_quantity = calculate_quantity_with_waste(
        floor_area,
        10
    )


    # -----------------------------------------------------
    # Calculate Paint Area
    # 5% allowance
    # -----------------------------------------------------

    paint_area = calculate_quantity_with_waste(
        net_wall_area,
        5
    )


    # -----------------------------------------------------
    # Calculate Cost Calculations
    # -----------------------------------------------------

    material_rates = {
        "Floor tiles": 350,
        "Paint": 120
    }

    tile_rate = material_rates["Floor tiles"]
    tile_cost = calculate_material_cost(
        tile_quantity,
        tile_rate
        )

    paint_rate = material_rates["Paint"]

    paint_cost = calculate_material_cost(
        paint_area,
        paint_rate
        )

    total_cost = calculate_total_cost([
        tile_cost,
        paint_cost
        ])




    # -----------------------------------------------------
    # SAVE PROJECT
    # -----------------------------------------------------

    save_project(
        project_name,
        project_number,
        location,
        building_type,
        length,
        width,
        wall_height,
        number_of_doors,
        number_of_windows,
        floor_area,
        perimeter,
        gross_wall_area,
        door_area,
        window_area,
        net_wall_area
    )

    st.success("Project saved successfully!")


    # -----------------------------------------------------
    # QUANTITY SUMMARY
    # -----------------------------------------------------

    st.header("📊 Quantity Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Floor Area",
            f"{floor_area:.2f} m²"
        )

    with col2:
        st.metric(
            "Perimeter",
            f"{perimeter:.2f} m"
        )

    with col3:
        st.metric(
            "Net Wall Area",
            f"{net_wall_area:.2f} m²"
        )


    # -----------------------------------------------------
    # DETAILED QUANTITIES
    # -----------------------------------------------------

    st.divider()

    st.subheader("Detailed Quantities")

    st.write(
        f"**Gross Wall Area:** "
        f"{gross_wall_area:.2f} m²"
    )

    st.write(
        f"**Door Opening Area:** "
        f"{door_area:.2f} m²"
    )

    st.write(
        f"**Window Opening Area:** "
        f"{window_area:.2f} m²"
    )

    st.write(
        f"**Floor Tiles:** "
        f"{tile_quantity:.2f} m² "
        f"including 10% waste"
    )

    st.write(
        f"**Paint Area:** "
        f"{paint_area:.2f} m² "
        f"including 5% allowance"
    )

    st.subheader("💰 Cost Estimate")

    st.write(
        f"**Floor Tiles:** "
        f"R{tile_cost:,.2f}"
    )

    st.write(
        f"**Paint:** "
        f"R{paint_cost:,.2f}"
    )

    st.metric(
        "Estimated Total",
        f"R{total_cost:,.2f}"
    )


# ---------------------------------------------------------
# BUILDQUANT DASHBOARD
# Display saved projects and project statistics
# ---------------------------------------------------------

st.divider()

st.header("📊 BuildQuant Dashboard")

projects = get_projects()

if projects:

    columns = [
        "ID",
        "Project Name",
        "Project Number",
        "Location",
        "Building Type",
        "Length",
        "Width",
        "Wall Height",
        "Doors",
        "Windows",
        "Floor Area",
        "Perimeter",
        "Gross Wall Area",
        "Door Area",
        "Window Area",
        "Net Wall Area"
    ]

    df = pd.DataFrame(
        projects,
        columns=columns
    )

    st.subheader("Saved Projects")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Project Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Projects",
            len(df)
        )

    with col2:
        st.metric(
            "Average Floor Area",
            f"{df['Floor Area'].mean():.2f} m²"
        )

    with col3:
        st.metric(
            "Average Wall Area",
            f"{df['Net Wall Area'].mean():.2f} m²"
        )

else:

    st.info(
        "No projects have been saved yet."
    )

