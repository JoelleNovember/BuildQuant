def validate_positive_number(value, field_name):
    """
    Check that a number is greater than zero.

    """

    if value <= 0:
        return f"{field_name} must be greater than zero."

    return None


def validate_non_negative_number(value, field_name):
    """
    Check that a number is zero or greater

    """
    if value < 0:
        return f"{field_name} cannot be negative."

    return None

def validate_project_name(project_name):
    """
    Check that a project name was entered.

    """
    if not project_name.strip():
        return "Project name is required."

    return None

def validate_project_number(project_number):
    """
    Check that a project number was entered.

    """

    if not project_number.strip():
        return "Project number is required."

    return None

