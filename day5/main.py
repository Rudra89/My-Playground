while True:
    user_choice = input("Type add, edit, show, complete or exit: ")
    user_choice = user_choice.lower().strip()

    match user_choice:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todo = todo.capitalize()

            file = open("day5/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("day5/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("day5/todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]
            # or
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index+1}) {todo}")
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