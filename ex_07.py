import json


class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    
    @staticmethod
    def from_json(json_str):
        print(json_str)
        return Hotel(**json_str)

hotel = Hotel("Continental", 220)

data = json.dumps(hotel.__dict__)

hotel1 = json.loads(data, object_hook=Hotel.from_json)

# hotel1 = Hotel(**hotel_json)

print(hotel1.name, hotel1.rooms)