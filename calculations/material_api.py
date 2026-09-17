import requests


API_URL = "http://localhost:5000"


def get_material_price(material):
    """
    Get a material price from the Material Price API.
    """

    response = requests.get(
        f"{API_URL}/materials/{material}"
    )

    response.raise_for_status()

    return response.json()

