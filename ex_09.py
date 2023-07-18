import csv


class Animal:
    def __init__(self, type, age):
        self.type = type
        self.age = age
    
animals = [Animal("Lion", 5), Animal("Wolf", 3)]

with open("animals.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["age", "type"])
    writer.writeheader()
    for animal in animals:
        writer.writerow(animal.__dict__)