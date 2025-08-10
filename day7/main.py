# OPTIMAZIED VERSION OF DAY 6

while True:
    user_choice = input("Type add, edit, show, complete or exit: ")
    user_choice = user_choice.lower().strip()

    if "add" in user_choice:
        todo = user_choice[4:].title()

        with open('day7/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('day7/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in user_choice:
        with open('day7/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1}) {todo}")

    elif "edit" in user_choice:
        number = int(user_choice[5:])
        number = number - 1

        with open('day7/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo name: ").capitalize()
        todos[number] = new_todo.title() + "\n"

        with open('day7/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in user_choice:
        number = int(user_choice[9:])
        number = number - 1

        with open('day7/todos.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[number].strip("\n")
        todos.pop(number)

        with open('day7/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"{todo_to_remove} was removed from the list"
        print(message)

    elif "exit" in user_choice:
        break

    else:
        print('Command is not valid')

print("Bye!")