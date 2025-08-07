todos = []

while True:
    user_input = input("Type add, show, edit or exit: ")
    user_input = user_input.lower().strip()
    
    match user_input:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.title())
        case 'edit':
            number = int(input("Enter the number of item you want edit:"))
            new_item = input("Enter the new item: ")
            todos[number-1] = new_item
        case 'exit':
            break
        case _:
            print("Unknown Command")

print("Bye!")