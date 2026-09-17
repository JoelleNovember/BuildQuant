def calculate_material_cost(quantity, rate):
    """
    Calculate the esitmated cost of a material

    Formula:
    quantity X rate
    """

    return quantity * rate


def calculate_total_cost(material_costs):
    """
    Calculate the total esitmate cost.

    material_costs should be a lisy of costs.
    """
    return sum(material_costs)