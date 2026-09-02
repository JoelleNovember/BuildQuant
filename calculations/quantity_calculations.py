#Calculate floor area 

def calculate_floor_area(length, width):
    """
    Calculate the floor area of a rectangular dwelling.

    Formula: length × width
    """

    return length * width


def calculate_perimeter(length, width):
    """
    Calculate the perimeter of a rectangular dwelling.

    Formula: 2 × (length + width)
    """
    return 2 * (length + width)


def calculate_gross_wall_area(perimeter, wall_height):
    """
    Calculate the gross external wall area.

    Formula:
    perimeter x wall height
    """
    return perimeter * wall_height


def calculate_opening_area(width, height, quantity):
    """
    Calculate the total area of amn opening

    Formula:
    width x height x quantity

    """
    return width * height * quantity

def calculate_net_wall_area(gross_wall_area, door_area, window_area):
    """
    Calculate the wall area after deducting doors and windows. 
    Formula: gross wall area - door area - window area
    """
    return gross_wall_area - door_area - window_area 