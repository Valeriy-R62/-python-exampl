class Building:
    pass


total_building = 0
builds = []
while len(builds) < 40:
    new_building = Building()
    builds.append(new_building)
    total_building += 1
print(total_building)
print(builds)
