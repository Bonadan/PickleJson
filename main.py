import pickle
import json
class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def to_dict(self):
        return{
            "brand":self.brand,
            "model":self.model,
            "year":self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["brand"], data["model"], data["year"])

    def pack_json(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def unpack_json(cls, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return cls.from_dict(data)


    def pack_pickle(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def unpack_pickle(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)

car = Car("VW", "Golf", 2008)

car.pack_json("car.json")
car.pack_pickle("car.pickle")


unpacked_car_json = Car.unpack_json("car.json")
print(unpacked_car_json)

unpacked_car_pickle = Car.unpack_pickle("car.pickle")
print(unpacked_car_pickle)