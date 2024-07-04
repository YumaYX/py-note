import json

fender_jazz_bass = {
    "model": "Fender Jazz Bass",
    "type": "Electric Bass",
    "specifications": {
        "body": {
            "material": "Alder",
            "finish": "Gloss Polyurethane",
            "shape": "Jazz Bass"
        },
        "neck": {
            "material": "Maple",
            "finish": "Satin Urethane",
            "shape": "Modern 'C'"
        },
        "fingerboard": {
            "material": "Rosewood",
            "radius": "9.5 inches",
            "frets": 20,
            "scale_length": "34 inches",
            "nut_material": "Synthetic Bone",
            "nut_width": "1.5 inches"
        },
        "electronics": {
            "pickups": {
                "neck": "Single-Coil Jazz Bass",
                "bridge": "Single-Coil Jazz Bass"
            },
            "controls": {
                "volume": 2,
                "tone": 1
            }
        },
        "hardware": {
            "bridge": "4-Saddle Standard",
            "tuners": "Standard Open-Gear",
            "pickguard": "3-Ply"
        },
        "colors": ["Sunburst", "Black", "Olympic White", "Candy Apple Red"]
    },
    "price": {
        "currency": "USD",
        "amount": 749.99
    },
    "availability": "In Stock",
    "features": [
        "Classic Fender tone and styling",
        "Comfortable neck profile",
        "Versatile sound suitable for various genres"
    ]
}


with open('output.json', 'w') as f:
    print(f)
    json.dump(fender_jazz_bass, f)