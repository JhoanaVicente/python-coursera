genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])


car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")
print(car_makes)

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
key_list = list(host_addresses.keys())
print(key_list)

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
values_list = list(host_addresses.values())
print(values_list)
