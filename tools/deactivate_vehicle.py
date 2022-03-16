import requests
from pprint import pprint


URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "make":"Ford",
    "model":"Escort",
    "color":"Color Shift"
}

def get_vehicle():
    vehicle_id = input("Type in the desired vehicle id: ")
    url = "%s%s"  % (URL, vehicle_id)
    response = requests.get(url)
    vehicle = {}
    if response.status_code == 200:
        response_json = response.json()
        vehicle = response_json["vehicle"][0]
        print("Vehicle: ")
        pprint(vehicle)
    else:
        print("Errors while trying to retrieve vehicle")
    return vehicle.get("id")

def deactivate_vehicle(vehicle_id):
    
    url = "%s%s" %(URL, vehicle_id)
    response = requests.delete(url)
    if response.status_code == 200 or 204:
        print("Vehicle deactivated")
    else:
        print("Error while trying to deactivate vehicle")


if __name__ == "__main__":
    print("DEACTIVATE VEHICLE")
    print("---------")
    vehicle_id = get_vehicle()
    deactivate_vehicle(vehicle_id)