import sqlite3


DATABASE_NAME = "data/buildquant.db"


def get_connection():
    """
    Create a connection to the BuildQuant database.
    """
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    """
    Create the projects table if it does not already exist.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_number TEXT NOT NULL,
            location TEXT NOT NULL,
            building_type TEXT NOT NULL,
            length REAL NOT NULL,
            width REAL NOT NULL,
            wall_height REAL NOT NULL,
            number_of_doors INTEGER NOT NULL,
            number_of_windows INTEGER NOT NULL,
            floor_area REAL NOT NULL,
            perimeter REAL NOT NULL,
            gross_wall_area REAL NOT NULL,
            door_area REAL NOT NULL,
            window_area REAL NOT NULL,
            net_wall_area REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_project(
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
    net_wall_area,
):
    """
    Save a complete project to the database.
    """
    connection = get_connection()
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
            number_of_doors,
            number_of_windows,
            floor_area,
            perimeter,
            gross_wall_area,
            door_area,
            window_area,
            net_wall_area
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
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
        net_wall_area,
    ))

    connection.commit()
    connection.close()


def get_projects():
    """
    Retrieve all saved projects from the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM projects
        ORDER BY id DESC
    """)

    projects = cursor.fetchall()

    connection.close()

    return projects


def get_projects():
    """
    Retrieve all saved projects from the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM projects
        ORDER BY id DESC
    """)

    projects = cursor.fetchall()

    connection.close()

    return projects

