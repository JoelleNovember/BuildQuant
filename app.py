import os
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

from calculations.cost_calculations import (
    calculate_material_cost,
    calculate_total_cost
)

from calculations.material_api import get_material_price
from reports.generate_report import generate_report


# ---------------------------------------------------------
# PAGE CONFIGURATION & DATABASE INIT
# ---------------------------------------------------------

st.set_page_config(
    page_title="BuildQuant",
    page_icon="🏗️",
    layout="wide"
)

create_tables()

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🏗️ BuildQuant")
st.write("**Residential Quantity System**")
st.divider()

# ---------------------------------------------------------
# PROJECT INFORMATION
# ---------------------------------------------------------

st.header("📋 Project Information")

project_name = st.text_input("Project Name", placeholder="e.g. Doe Residence")
project_number = st.text_input("Project Number", placeholder="e.g. PRJ_001")
location = st.text_input("Location", placeholder="e.g. Cape Town")
building_type = st.selectbox(
    "Building Type",
    ["Single-storey dwelling", "Double-storey dwelling"]
)

st.divider()

# ---------------------------------------------------------
# BUILDING DIMENSIONS & OPENINGS
# ---------------------------------------------------------

st.header("📐 Building Dimensions")
col1, col2, col3 = st.columns(3)
with col1:
    length = st.number_input("Length (m)", min_value=0.0, step=0.1)
with col2:
    width = st.number_input("Width (m)", min_value=0.0, step=0.1)
with col3:
    wall_height = st.number_input("Wall Height (m)", min_value=0.0, step=0.1)

st.divider()

st.header("🚪 Doors & Windows")
col1, col2 = st.columns(2)
with col1:
    number_of_doors = st.number_input("Number of Doors", min_value=0, step=1)
with col2:
    number_of_windows = st.number_input("Number of Windows", min_value=0, step=1)

st.divider()

# ---------------------------------------------------------
# CALCULATE QUANTITIES
# ---------------------------------------------------------

if st.button("🧮 Calculate Quantities", type="primary"):

    floor_area = calculate_floor_area(length, width)
    perimeter = calculate_perimeter(length, width)
    gross_wall_area = calculate_gross_wall_area(perimeter, wall_height)

    door_area = calculate_opening_area(0.9, 2.1, number_of_doors)
    window_area = calculate_opening_area(1.2, 1.2, number_of_windows)

    net_wall_area = calculate_net_wall_area(
        gross_wall_area, door_area, window_area
    )

    tile_quantity = calculate_quantity_with_waste(floor_area, 10)
    paint_area = calculate_quantity_with_waste(net_wall_area, 5)

    tile_data = get_material_price("tiles")
    tile_rate = tile_data["rate"]

    paint_data = get_material_price("paint")
    paint_rate = paint_data["rate"]

    tile_cost = calculate_material_cost(tile_quantity, tile_rate)
    paint_cost = calculate_material_cost(paint_area, paint_rate)
    total_cost = calculate_total_cost([tile_cost, paint_cost])

    # Store calculation outputs in session state so they persist across reruns
    st.session_state["calc_done"] = True
    st.session_state["calc_data"] = {
        "floor_area": floor_area,
        "perimeter": perimeter,
        "gross_wall_area": gross_wall_area,
        "door_area": door_area,
        "window_area": window_area,
        "net_wall_area": net_wall_area,
        "tile_quantity": tile_quantity,
        "paint_area": paint_area,
        "tile_cost": tile_cost,
        "paint_cost": paint_cost,
        "total_cost": total_cost,
    }

    save_project(
        project_name, project_number, location, building_type,
        length, width, wall_height, number_of_doors, number_of_windows,
        floor_area, perimeter, gross_wall_area, door_area, window_area, net_wall_area
    )

    st.success("Project saved successfully!")

# ---------------------------------------------------------
# DISPLAY RESULTS & GENERATE PDF
# ---------------------------------------------------------

if st.session_state.get("calc_done"):
    data = st.session_state["calc_data"]

    st.header("📊 Quantity Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Floor Area", f"{data['floor_area']:.2f} m²")
    with col2:
        st.metric("Perimeter", f"{data['perimeter']:.2f} m")
    with col3:
        st.metric("Net Wall Area", f"{data['net_wall_area']:.2f} m²")

    st.divider()

    st.subheader("Detailed Quantities")
    st.write(f"**Gross Wall Area:** {data['gross_wall_area']:.2f} m²")
    st.write(f"**Door Opening Area:** {data['door_area']:.2f} m²")
    st.write(f"**Window Opening Area:** {data['window_area']:.2f} m²")
    st.write(f"**Floor Tiles:** {data['tile_quantity']:.2f} m² (incl. 10% waste)")
    st.write(f"**Paint Area:** {data['paint_area']:.2f} m² (incl. 5% allowance)")

    st.subheader("💰 Cost Estimate")
    st.write(f"**Floor Tiles:** R{data['tile_cost']:,.2f}")
    st.write(f"**Paint:** R{data['paint_cost']:,.2f}")
    st.metric("Estimated Total", f"R{data['total_cost']:,.2f}")

    st.divider()

    pdf_path = "reports/generated/buildquant_report.pdf"
    os.makedirs("reports/generated", exist_ok=True)

    if st.button("📄 Generate PDF Report"):
        generate_report(
            pdf_path,
            project_name,
            project_number,
            location,
            data["floor_area"],
            data["net_wall_area"],
            data["tile_quantity"],
            data["paint_area"],
            data["tile_cost"],
            data["paint_cost"],
            data["total_cost"]
        )
        st.success("PDF report generated successfully!")

    # Provide direct download button when the generated file exists
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as file:
            st.download_button(
                label="⬇️ Download PDF Report",
                data=file,
                file_name=f"{project_name or 'buildquant'}_report.pdf",
                mime="application/pdf"
            )

# ---------------------------------------------------------
# BUILDQUANT DASHBOARD
# ---------------------------------------------------------

st.divider()
st.header("📊 BuildQuant Dashboard")

projects = get_projects()

if projects:
    columns = [
        "ID", "Project Name", "Project Number", "Location", "Building Type",
        "Length", "Width", "Wall Height", "Doors", "Windows", "Floor Area",
        "Perimeter", "Gross Wall Area", "Door Area", "Window Area", "Net Wall Area"
    ]

    df = pd.DataFrame(projects, columns=columns)

    st.subheader("Saved Projects")
    st.dataframe(df, use_container_width=True)

    st.subheader("Project Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Projects", len(df))
    with col2:
        st.metric("Average Floor Area", f"{df['Floor Area'].mean():.2f} m²")
    with col3:
        st.metric("Average Wall Area", f"{df['Net Wall Area'].mean():.2f} m²")

else:
    st.info("No projects have been saved yet.")