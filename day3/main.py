todos = []

while True:
    user_input = input("Type add, show, edit, complete or exit: ")
    user_input = user_input.lower().strip()
    
    match user_input:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index+1}) {item.capitalize()}")
        case 'edit':
            number = int(input("Enter the number of todo you want edit: "))
            new_item = input("Enter the new todo: ")
            todos[number - 1] = new_item
        case 'complete':
            number = int(input("Enter the number of todo you want complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Unknown Command")

print("Bye!")