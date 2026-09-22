import requests

API_URL = "http://localhost:5000"

def get_material_price(material):
    try:
        response = requests.get(
            f"{API_URL}/materials/{material}",
            timeout=5
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Unable to connect to the Material Price API. "
            "Please make sure the Flask API is running."
        )

    except requests.exceptions.Timeout:
        raise RuntimeError(
            "The Material Price API took too long to respond."
        )

    except requests.exceptions.HTTPError:
        raise RuntimeError(
            f"The Material Price API returned an error "
            f"for material: {material}"
        )