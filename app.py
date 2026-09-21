import os
import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# IMPORT DEPENDENCIES
# ---------------------------------------------------------
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
    layout="wide",
    initial_sidebar_state="expanded"
)

create_tables()

# ---------------------------------------------------------
# BUILDQUANT SIDEBAR NAVIGATION
# ---------------------------------------------------------

st.sidebar.markdown("""
# 🏗️ BUILDQUANT

### Residential Quantity System

---
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📋 New Project",
        "📐 Quantities",
        "💰 Cost Estimate",
        "📊 Analytics",
        "📄 Reports"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("""
### 🔌 Systems Integration
**Material Price API**
Connected through REST API
""")
st.sidebar.divider()
st.sidebar.caption("BuildQuant • Educational Prototype")

# ---------------------------------------------------------
# NEW PROJECT PAGE
# ---------------------------------------------------------

if page == "📋 New Project":

    st.title("📋 New Residential Project")
    st.write("Enter the information for the proposed residential project.")
    st.divider()


    st.header("📋 Project Information")
    project_name = st.text_input("Project Name", placeholder="e.g. Smith Residence", key="np_name")
    project_number = st.text_input("Project Number", placeholder="e.g. PRJ-2026-001", key="np_num")
    location = st.text_input("Location", placeholder="e.g. Cape Town", key="np_loc")
    building_type = st.selectbox(
        "Building Type",
        ["Single-storey dwelling", "Double-storey dwelling"],
        key="np_type"
    )

    st.divider()
    st.header("📐 Building Dimensions")
    col1, col2, col3 = st.columns(3)
    with col1:
        length = st.number_input("Length (m)", min_value=0.0, step=0.2, key="np_len")
    with col2:
        width = st.number_input("Width (m)", min_value=0.0, step=0.2, key="np_wid")
    with col3:
        wall_height = st.number_input("Wall Height (m)", min_value=0.0, step=0.2, key="np_hgt")

    st.divider()
    st.header("🚪 Doors & Windows")
    col1, col2 = st.columns(2)
    with col1:
        number_of_doors = st.number_input("Number of Doors", min_value=0, step=1, key="np_doors")
    with col2:
        number_of_windows = st.number_input("Number of Windows", min_value=0, step=1, key="np_wins")

    st.divider()

    if st.button("🧮 Calculate Quantities", type="primary", use_container_width=True):
        if not project_name:
            st.error("Please enter a Project Name before calculating.")
        else:
            # Perform calculations
            floor_area = calculate_floor_area(length, width)
            perimeter = calculate_perimeter(length, width)
            gross_wall_area = calculate_gross_wall_area(perimeter, wall_height)
            door_area = calculate_opening_area(0.9, 2.1, number_of_doors)
            window_area = calculate_opening_area(1.2, 1.2, number_of_windows)
            net_wall_area = calculate_net_wall_area(gross_wall_area, door_area, window_area)

            tile_quantity = calculate_quantity_with_waste(floor_area, 10)
            paint_area = calculate_quantity_with_waste(net_wall_area, 5)

            tile_data = get_material_price("tiles")
            tile_rate = tile_data.get("rate", 0.0) if isinstance(tile_data, dict) else 0.0
            
            paint_data = get_material_price("paint")
            paint_rate = paint_data.get("rate", 0.0) if isinstance(paint_data, dict) else 0.0

            tile_cost = calculate_material_cost(tile_quantity, tile_rate)
            paint_cost = calculate_material_cost(paint_area, paint_rate)
            total_cost = calculate_total_cost([tile_cost, paint_cost])

            # Persist calculation in session state
            st.session_state["calc_done"] = True
            st.session_state["calc_data"] = {
                "project_name": project_name,
                "project_number": project_number,
                "location": location,
                "building_type": building_type,
                "floor_area": floor_area,
                "perimeter": perimeter,
                "gross_wall_area": gross_wall_area,
                "door_area": door_area,
                "window_area": window_area,
                "net_wall_area": net_wall_area,
                "tile_quantity": tile_quantity,
                "paint_area": paint_area,
                "tile_rate": tile_rate,
                "paint_rate": paint_rate,
                "tile_cost": tile_cost,
                "paint_cost": paint_cost,
                "total_cost": total_cost
            }

            # Save to SQLite Database
            save_project(
                project_name, project_number, location, building_type,
                length, width, wall_height, number_of_doors, number_of_windows,
                floor_area, perimeter, gross_wall_area, door_area, window_area, net_wall_area
            )

            st.success("✅ Project calculated and saved successfully!")
            st.balloons()

# ---------------------------------------------------------
# QUANTITIES PAGE
# ---------------------------------------------------------

elif page == "📐 Quantities":

    st.title("📐 Quantity Analysis")

    if st.session_state.get("calc_done"):
        data = st.session_state["calc_data"]
        st.subheader(f"Current Project: {data['project_name']}")
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Floor Area", f"{data['floor_area']:.2f} m²")

        with col2:
            st.metric("Perimeter", f"{data['perimeter']:.2f} m")

        with col3:
            st.metric("Net Wall Area", f"{data['net_wall_area']:.2f} m²")

        st.divider()
        st.subheader("Detailed Quantities Breakdown")

        quantity_data = pd.DataFrame({
            "Item": [
                "Floor Area",
                "Perimeter",
                "Gross Wall Area",
                "Door Opening Area",
                "Window Opening Area",
                "Net Wall Area",
                "Floor Tiles",
                "Paint Area"
            ],

            "Quantity": [
                f"{data['floor_area']:.2f} m²",
                f"{data['perimeter']:.2f} m",
                f"{data['gross_wall_area']:.2f} m²",
                f"{data['door_area']:.2f} m²",
                f"{data['window_area']:.2f} m²",
                f"{data['net_wall_area']:.2f} m²",
                f"{data['tile_quantity']:.2f} m²",
                f"{data['paint_area']:.2f} m²"
            ]
        })

        st.dataframe(quantity_data, use_container_width=True, hide_index=True)
    else:
        st.info("No active calculation session. Please go to 📋 New Project and execute a calculation first.")


# ---------------------------------------------------------
# COST ESTIMATE PAGE
# ---------------------------------------------------------

elif page == "💰 Cost Estimate":

    st.title("💰 Cost Estimate")

    if st.session_state.get("calc_done"):
        data = st.session_state["calc_data"]
        st.subheader(f"Estimate — {data['project_name']}")
        st.divider()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Floor Tiles Cost",f"R{data['tile_cost']:,.2f}")
            st.caption(
                f"  {data['tile_quantity']:.2f} m² × "
                f"R{data['tile_rate']:,.2f}/m²"
            )

        with col2:
            st.metric(
                "Paint Cost",
                f"R{data['paint_cost']:,.2f}"
            )

            st.caption(
                f"{data['paint_area']:.2f} m² × "
                f"R{data['paint_rate']:,.2f}/m²"
            )

        with col3:
            st.metric(
                "Estimated Total Cost",
                f"R{data['total_cost']:,.2f}"
            )

        st.divider()
        st.subheader("Cost Allocation Chart")
        cost_df = pd.DataFrame({
            "Material": ["Floor Tiles", "Paint"],
            "Cost (ZAR)": [data["tile_cost"], data["paint_cost"]]
        })

        st.bar_chart(cost_df.set_index("Material"), color="#198754")
        st.divider()
        st.info("Material rates are live updates from the BuildQuant Material Price REST API.")
    else:
        st.info("No cost estimation available. Please go to 📋 New Project and execute a calculation first.")


# ---------------------------------------------------------
# 📊 ANALYTICS PAGE
# ---------------------------------------------------------
elif page == "📊 Analytics":

    st.title("📊 Project Analytics")
    projects = get_projects()

    if projects:
        try:
            columns = [
                "ID", "Project Name", "Project Number", "Location", "Building Type",
                "Length", "Width", "Wall Height", "Doors", "Windows",
                "Floor Area", "Perimeter", "Gross Wall Area", "Door Area", "Window Area", "Net Wall Area"
            ]
            df = pd.DataFrame(projects, columns=columns)

            col1, col2 = st.columns(2)
            with col1:
                st.write("### 📐 Floor Area Comparison (m²)")
                st.bar_chart(df[["Project Name", "Floor Area"]].set_index("Project Name"), color="#198754")
            with col2:
                st.write("### 🧱 Net Wall Area Comparison (m²)")
                st.bar_chart(df[["Project Name", "Net Wall Area"]].set_index("Project Name"), color="#0F5132")

        except Exception as e:
            st.error(f"Error structuring analytics data: {e}")
    else:
        st.info("No saved projects in the database. Run calculations in 📋 New Project to populate analytics.")


# ---------------------------------------------------------
# 📄 REPORTS PAGE
# ---------------------------------------------------------
elif page == "📄 Reports":

    st.title("📄 Project Reports")

    if st.session_state.get("calc_done"):
        data = st.session_state["calc_data"]
        st.write("Generate and download formal PDF quantity reports.")
        st.divider()

        st.subheader(f"📋 {data['project_name']}")
        st.write(f"**Project Number:** {data['project_number']}")
        st.write(f"**Location:** {data['location']}")
        st.write(f"**Estimated Total:** R{data['total_cost']:,.2f}")
        st.divider()

        pdf_dir = "reports/generated"
        pdf_path = os.path.join(pdf_dir, "buildquant_report.pdf")
        os.makedirs(pdf_dir, exist_ok=True)

        if st.button("📄 Generate PDF Report", type="primary"):
            generate_report(
                pdf_path,
                data["project_name"],
                data["project_number"],
                data["location"],
                data["floor_area"],
                data["net_wall_area"],
                data["tile_quantity"],
                data["paint_area"],
                data["tile_cost"],
                data["paint_cost"],
                data["total_cost"]
            )
            st.success("✅ PDF report generated successfully!")

        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as file:
                st.download_button(
                    label="⬇️ Download PDF Report",
                    data=file,
                    file_name=f"{data['project_name'] or 'buildquant'}_report.pdf",
                    mime="application/pdf"
                )
    else:
        st.info("Please complete a project calculation in 📋 New Project before generating reports.")


# ---------------------------------------------------------
# 🏠 DASHBOARD PAGE
# ---------------------------------------------------------
elif page == "🏠 Dashboard":

    st.markdown("""
    <style>
    .buildquant-header {
        background: linear-gradient(135deg, #0F5132, #198754);
        padding: 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 25px;
    }
    .buildquant-header h1 { margin: 0; font-size: 32px; color: #FFFFFF; }
    .buildquant-header p { margin-top: 8px; font-size: 16px; color: #E8F5E9; }
    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        border-left: 5px solid #198754;
        box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
        min-height: 120px;
    }
    .kpi-title { font-size: 14px; color: #6c757d; margin-bottom: 8px; font-weight: bold; }
    .kpi-value { font-size: 28px; font-weight: bold; color: #0F5132; }
    .kpi-description { font-size: 13px; color: #6c757d; margin-top: 5px; }
    .section-title {
        color: #0F5132;
        font-size: 22px;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .info-card {
        background-color: #F1F8F4;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #D8EBDD;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="buildquant-header">
        <h1>🏗️ BUILDQUANT</h1>
        <p>Residential Quantity Estimation & Data Engineering Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    projects = get_projects()

    if projects:
        try:
            columns = [
                "ID", "Project Name", "Project Number", "Location", "Building Type",
                "Length", "Width", "Wall Height", "Doors", "Windows",
                "Floor Area", "Perimeter", "Gross Wall Area", "Door Area", "Window Area", "Net Wall Area"
            ]
            df = pd.DataFrame(projects, columns=columns)

            total_projects = len(df)
            average_floor_area = df["Floor Area"].mean()
            average_wall_area = df["Net Wall Area"].mean()
            building_types = df["Building Type"].nunique()

            st.markdown('<div class="section-title">📊 Project Overview</div>', unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">🏗️ TOTAL PROJECTS</div>
                    <div class="kpi-value">{total_projects}</div>
                    <div class="kpi-description">Saved projects</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">📐 AVG FLOOR AREA</div>
                    <div class="kpi-value">{average_floor_area:.2f} m²</div>
                    <div class="kpi-description">Average project size</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">🧱 AVG WALL AREA</div>
                    <div class="kpi-value">{average_wall_area:.2f} m²</div>
                    <div class="kpi-description">Average net wall area</div>
                </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-title">🏠 BUILDING TYPES</div>
                    <div class="kpi-value">{building_types}</div>
                    <div class="kpi-description">Distinct types recorded</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('<div class="section-title">📋 Saved Projects Registry</div>', unsafe_allow_html=True)
            display_columns = ["Project Name", "Project Number", "Location", "Building Type", "Floor Area", "Net Wall Area"]
            st.dataframe(df[display_columns], use_container_width=True, hide_index=True)

        except Exception as e:
            st.error(f"Error loading project dashboard: {e}")
    else:
        st.markdown("""
        <div class="info-card">
            <h3>👋 Welcome to BuildQuant</h3>
            <p>No projects have been saved yet.</p>
            <p>Navigate to <b>📋 New Project</b>, enter dimensions, and click <b>Calculate Quantities</b> to populate your records.</p>
        </div>
        """, unsafe_allow_html=True)