while True:
    user_choice = input("Type add, edit, show, complete or exit: ")
    user_choice = user_choice.lower().strip()

    match user_choice:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todo = todo.capitalize()

            file = open("day4/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("day4/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("day4/todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, todo in enumerate(todos):
                print(f"{index+1}) {todo}", end="")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo name: ").capitalize()
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case "exit":
            break
        case _:
            print("Invalid command")

print("Bye!")