import requests



URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "make":"Bill",
    "model":"Gaytes",
    "color":"population control"
}

def create_vehicle():
    make = input("Enter a make: ")
    model = input("Enter a model: ")
    color = input("Enter color: ")
    SAMPLE_VEHICLE["make"] = make
    SAMPLE_VEHICLE["model"] = model
    SAMPLE_VEHICLE["color"] = color
    response = requests.post(URL, json=SAMPLE_VEHICLE)
    if response.status_code == 204:
        print("Vehicle created.")
    else:
        print("Error while attempting to create vehicle.")

if __name__ == "__main__":
    print("CREATE VEHICLE")
    print("------------")
    create_vehicle()