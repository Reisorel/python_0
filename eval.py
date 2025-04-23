drilling_machine_two = {
  "machine_id": "DM-2",
  "name": "Land Rover 200",
  "location": {
    "latitude": 37.7749,
    "longitude": -107.9090,
    "region": "San Juan Basin",
    "country": "USA"
  },
  "status": "Under Maintenance",
  "specifications": {
    "type": "Onshore",
    "depth_capacity_miles": 7,
    "drilling_speed_miles_per_day": 0.3,
    "crew_size": 25,
    "power_source": "Electric"
  },
  "last_maintenance_date": "2024-07-15",
  "next_maintenance_due": "2025-01-15"
}


specifications = drilling_machine_two["specifications"]
# Transform the depth capacity from miles to kilometers and meters
depth_capacity_miles = specifications["depth_capacity_miles"]

depth_capacity_kilometers = depth_capacity_miles * 1.60934
depth_capacity_meters = depth_capacity_kilometers * 1000

drilling_machine_two["specifications"]["depth_capacity_meters"] = depth_capacity_meters
del drilling_machine_two["specifications"]["depth_capacity_miles"]

# Transform the drilling speed from miles to kilometers and meters
drilling_speed_miles = specifications["drilling_speed_miles_per_day"]
drilling_speed_meters = drilling_speed_miles * 1.60934 * 1000
drilling_machine_two["specifications"]["drilling_speed_meters_per_day"] = drilling_speed_meters
del drilling_machine_two["specifications"]["drilling_speed_miles_per_day"]
print(specifications)


# Modification de la date de maintenance
date = drilling_machine_two["last_maintenance_date"]

# Étape 1: Convertir les tirets en slashes et stocker le résultat
date = date.replace("-", "/")

# Étape 2: Inverser l'ordre des parties de la date
date_parts = date.split("/")
date_parts.reverse()
date = "/".join(date_parts)

print(date)  # Affichera "15/07/2024"


contact_dict = {
    "operator": "John Doe",
    "contact_person": "+1-555-1234",
    "email": None,
    "phone": None,
}

drilling_machine_two["contact_information"] = contact_dict

machine_id = drilling_machine_two["machine_id"]

id_letters, id_number = machine_id.split("-")
id_number_zfilled = id_number.zfill(3)
machine_id = f"{id_letters}-{id_number_zfilled}"
print(machine_id)
drilling_machine_two["machine_id"] = machine_id
print(drilling_machine_two)
