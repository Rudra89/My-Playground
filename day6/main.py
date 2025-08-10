# OPTIMAZIED VERSION OF DAY 5

while True:
    user_choice = input("Type add, edit, show, complete or exit: ")
    user_choice = user_choice.lower().strip()

    match user_choice:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todo = todo.title()

            with open('day6/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('day6/todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('day6/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{index+1}) {todo}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('day6/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo name: ").capitalize()
            todos[number] = new_todo.title() + "\n"

            with open('day6/todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the todo to complete: "))
            number = number - 1

            with open('day6/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            with open('day6/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case "exit":
            break
        case _:
            print("Invalid command")

print("Bye!")