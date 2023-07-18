import pickle


class Human:
    def __init__(self, name):
        self.name = name
    
    def __getstate__(self) -> object:
        data = self.__dict__
        data["age"] = 10
        return data

    def __setstate__(self, value):
        # print(value.pop("age"))
        self.__dict__ = value
        # print(self.__dict__.get("age"))


human = Human("Dre")

data_str = pickle.dumps(human)

new_human = pickle.loads(data_str)

print(new_human.age)