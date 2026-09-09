import streamlit as st

from calculations.quantity_calculations import (
    calculate_floor_area,
    calculate_perimeter,
    calculate_gross_wall_area,
    calculate_opening_area,
    calculate_net_wall_area
)



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
#-----
# CALCULATE QUANTITIES
#-----


if st.button("🧮 Calculate Quantities", type="primary"):

    #Calulate floor area 
    floor_area = calculate_floor_area(length, width)

    #Calculate perimeter
    perimeter = calculate_perimeter(length, width)

    #Calculate gross wall area 
    gross_wall_area = calculate_gross_wall_area(perimeter, wall_height)

    # Standard door size
    door_area = calculate_opening_area(
        0.9,
        2.1,
        number_of_doors
    )

    # Standard window size
    window_area = calculate_opening_area(
        1.2,
        1.2,
        number_of_windows
    )

    # Calculate net wall area
    net_wall_area = calculate_net_wall_area(
        gross_wall_area,
        door_area,
        window_area
    )

    st.success("Quantities calculated successfully!")

    st.header("📊 Quantity Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Floor Area",
            f"{floor_area:.2f} m"
        )

    with col2:
        st.metric(
            "Perimeter",
            f"{perimeter:.2f} m"
        )

    with col3:
        st.metric(
            "Net Wall Area",
            f"{net_wall_area:.2f} m² "
        )



    st.divider() 

    st.subheader("Detailed Quantities") 

    st.write( f"**Gross Wall Area:** " 
              f"{gross_wall_area:.2f} m²" ) 

    st.write( f"**Door Opening Area:** " 
              f"{door_area:.2f} m²" ) 

    st.write( f"**Window Opening Area:** " 
                f"{window_area:.2f} m²" )