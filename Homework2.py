class Building:

    def __init__(self,buildingType,numberOfFloors):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType)


house_1 = Building("school", 5)
house_2 = Building("shop", 3)
print(house_1 == house_2)
