def get_average():
    with open('day9/bonus/data.txt', 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(value.strip("\n")) for value in values]

    avg = sum(values) / len(values)
    return avg

average = get_average()
print(average)