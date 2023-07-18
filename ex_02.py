import pickle

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
    
    def __repr__(self):
        return f"{self.name} - {self.rooms}"


if __name__ == "__main__":

    continental = Hotel(250)

    with open("hotels.bin", "wb") as f:
        pickle.dump(continental, f)
