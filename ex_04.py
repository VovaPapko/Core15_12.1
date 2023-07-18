import pickle


# class Hotel:
#     # def __init__(self):
#     #     ...
    
#     def __repr__(self):
#         return F"{self.rooms}: {self.name}"

# print(globals())

with open("hotels.bin", "rb") as f:
    hotels = pickle.load(f)
    
for hotel in hotels:
    print(hotel)

# print(globals())