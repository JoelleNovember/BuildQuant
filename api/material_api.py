from flask import Flask, jsonify

app = Flask(__name__)

# Sample material pricing database
MATERIALS = {
    "tiles": {
        "material": "Ceramic Floor Tiles",
        "rate": 180.00,
        "unit": "m²"
    },
    "paint": {
        "material": "Acrylic PVA Paint",
        "rate": 85.00,
        "unit": "litre"
    },
    "concrete": {
        "material": "Ready-mix Concrete",
        "rate": 1450.00,
        "unit": "m³"
    }
}

@app.route("/materials/<material>", methods=["GET"])
def get_material(material):
    material_key = material.lower()
    if material_key in MATERIALS:
        return jsonify(MATERIALS[material_key])
    return jsonify({"error": "Material not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)