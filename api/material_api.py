from flask import Flask, jsonify

app = Flask(__name__)


MATERIALS = {
    "concrete": {
        "material": "concrete",
        "unit": "m3",
        "rate": 1500
    },

    "tiles": {
        "material": "tiles",
        "unit": "m2",
        "rate": 350
    },

    "paint": {
        "material": "paint",
        "unit": "m2",
        "rate": 120
    }
}


@app.route("/materials/<material>")
def get_material(material):

    if material not in MATERIALS:
        return jsonify({
            "error": "Material not found"
        }), 404

    return jsonify(MATERIALS[material])


if __name__ == "__main__":
    app.run(port=5000)

