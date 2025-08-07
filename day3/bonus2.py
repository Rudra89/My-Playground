waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for i, person in enumerate(waiting_list):
    print(f"{i+1}.{person.capitalize()}")

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)