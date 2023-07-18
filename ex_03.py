import pickle
from random import randint

from ex_02 import Hotel


file_name = "hotels.bin"
hotels = []

for i in range(10):
    hotels.append(Hotel(f"Hotel-{i}", randint(100, 500)))

with open(file_name, "wb") as f:
    pickle.dump(hotels, f)

with open(file_name, "rb") as f:
    load_hotels = pickle.load(f)
    
print(load_hotels)

for hotel in load_hotels:
    print(hotel)