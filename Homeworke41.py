class Building:

    def __init__(self):
        self.total = 0
        self.total += 1

total_building = []
builds_size = 40
while len(total_building) < builds_size:
    new_building = Building()
    total_building.append(new_building)
print(total_building)