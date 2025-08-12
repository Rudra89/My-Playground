names = ['a','b', 'c']

feet_inches = input("Enter feet and inches: ")

def parse(feetinches):
    parts = feetinches.split(" ")
    feets = float(parts[0])
    inches = float(parts[1])
    return feets, inches

def convert(feets, inches):
    meters = feets * 0.3048 + inches * 0.0254
    print(f"{feets} feet and {inches} inches is equal to {meters} meters")
    return meters

f, i = parse(feet_inches) 
print(f, i)
result = convert(f, i)

if result < 1:
    print("Your height is too low for ride!")
else:
    print("Your height is enough for ride!")
