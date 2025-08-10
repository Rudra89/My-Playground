password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
     result["length"] = False

isDigit = False
isUpper = False

for i in password:
    if isDigit and isUpper:
        break
    elif i.isdigit():
        isDigit = True
    elif i.isupper():
        isUpper = True

result['digits'] = isDigit
result['upper'] = isUpper

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
        