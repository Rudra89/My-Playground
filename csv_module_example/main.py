import csv

with open('csv_module_example/weather.csv', 'r') as file:
    data = list(csv.reader(file))

for station, temperature in data[1:]:
    print(f"Station: {station}")

city = input("Enter a city: ")
for station, temperature in data[1:]:
    if city.lower() in station.lower():
        print(f"Temperature: {temperature}°C")