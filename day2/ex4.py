name = input("what is you name")
names = []

while name != "stop":
    names.append(name.capitalize())
    print(names)
    name = input("what is you name")