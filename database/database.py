import sqlite3

DATABASE = "data/buildquant.db"

# ---------------------------------------------------------
# CREATE DATABASE TABLE
# ---------------------------------------------------------

def create_tables():
    """
    Create the projects table if it does not already exist.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT,
            project_number TEXT,
            location TEXT,
            building_type TEXT,
            length REAL,
            width REAL,
            wall_height REAL,
            doors INTEGER,
            windows INTEGER,
            floor_area REAL,
            perimeter REAL,
            gross_wall_area REAL,
            door_area REAL,
            window_area REAL,
            net_wall_area REAL,
            tile_quantity REAL,
            paint_area REAL,
            tile_rate REAL,
            paint_rate REAL,
            tile_cost REAL,
            paint_cost REAL,
            total_cost REAL
        )
    """)

    connection.commit()
    connection.close()

# ---------------------------------------------------------
# SAVE PROJECT
# ---------------------------------------------------------
def save_project(
    project_name,
    project_number,
    location,
    building_type,
    length,
    width,
    wall_height,
    doors,
    windows,
    floor_area,
    perimeter,
    gross_wall_area,
    door_area,
    window_area,
    net_wall_area,
    tile_quantity,
    paint_area,
    tile_rate,
    paint_rate,
    tile_cost,
    paint_cost,
    total_cost
):
    """
    Save a complete project to the database.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO projects (
            project_name,
            project_number,
            location,
            building_type,
            length,
            width,
            wall_height,
            doors,
            windows,
            floor_area,
            perimeter,
            gross_wall_area,
            door_area,
            window_area,
            net_wall_area,
            tile_quantity,
            paint_area,
            tile_rate,
            paint_rate,
            tile_cost,
            paint_cost,
            total_cost
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        project_name,
        project_number,
        location,
        building_type,
        length,
        width,
        wall_height,
        doors,
        windows,
        floor_area,
        perimeter,
        gross_wall_area,
        door_area,
        window_area,
        net_wall_area,
        tile_quantity,
        paint_area,
        tile_rate,
        paint_rate,
        tile_cost,
        paint_cost,
        total_cost
    ))

    connection.commit()
    connection.close()


# ---------------------------------------------------------
# GET ALL PROJECTS
# ---------------------------------------------------------

def get_projects():
    """
    Retrieve all saved projects from the database.
    """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            project_name,
            project_number,
            location,
            building_type,
            length,
            width,
            wall_height,
            doors,
            windows,
            floor_area,
            perimeter,
            gross_wall_area,
            door_area,
            window_area,
            net_wall_area,
            tile_quantity,
            paint_area,
            tile_rate,
            paint_rate,
            tile_cost,
            paint_cost,
            total_cost
        FROM projects
        ORDER BY id DESC
    """)

    projects = cursor.fetchall()
    connection.close()

    return projects  