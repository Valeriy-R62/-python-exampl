class Building:
                           # создание класса  Building, затем атрибута total = 0
    total = 0

    def __init__(self):
        Building.total += 1    # инициализация увеличения атрибута total на 1


builds = []
quantity = 40              # создание списка объектов и задание его размера
while len(builds) < 40:               # цикл создания объектов класса  Building
    new_building = Building()
    builds.append(new_building)
    print(Building.total, '-' ,new_building)