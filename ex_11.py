import copy


class Animal:
    def __init__(self, type, age, areas):
        self.type = type
        self.age = age
        self.areas = areas

    # def __copy__(self):
    #     print("in copy")
    
    def __deepcopy__(self, memo):
        copy_obj = Animal(**self.__dict__)
        memo[id(self)] = copy_obj
        copy_obj.areas = copy.deepcopy(self.areas, memo)
        copy_obj.age = self.age
        copy_obj.type = self.type
        return copy_obj

animal = Animal("Duck", 2, {"rivers":["Dnipro", "Danubiy"]})

copy.copy(animal)

animal1 = copy.deepcopy(animal)

animal.areas["rivers"][0] = "Desna"

print(animal1.areas)