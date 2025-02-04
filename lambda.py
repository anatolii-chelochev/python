people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# def f(person):
#     return person["name"]

# def g(home):
#     return home["house"]

# people.sort(key=g)
people.sort(key=lambda person: person["name"])

print(people)