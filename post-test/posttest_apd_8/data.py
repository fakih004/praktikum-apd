import json

def simpan_user(data):
    with open("user.json", "w") as f:
        json.dump(data, f, indent=4)

def input_user():
    try:
        with open("user.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def simpan_pasien(data):
    with open("pasien.json", "w") as f:
        json.dump(data, f, indent=4)

def input_pasien():
    try:
        with open("pasien.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
