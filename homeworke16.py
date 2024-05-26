class House:
    def __init__(self):
        self.nombersOfFloors = 0

    def setNewNombersOfFloors(self):
        floors = input("Укажите этажность: ")
        self.nombersOfFloors = floors


house = House()
house.setNewNombersOfFloors()
print(house.nombersOfFloors)
