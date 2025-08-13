import functions
# from functions import get_todos, write_todos

while True:
    user_choice = input("Type add, edit, show, complete or exit: ")
    user_choice = user_choice.lower().strip()

    if user_choice.startswith("add"):
        todo = user_choice[4:].title()

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos, 'day10/todos.txt')

    elif user_choice.startswith("show"):
        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1}) {todo}")

    elif user_choice.startswith("edit"):
        try: 
            number = int(user_choice[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo name: ").capitalize()
            todos[number] = new_todo.title() + "\n"
            functions.write_todos(todos, 'day10/todos.txt')

        except ValueError: 
            print("Your command is not valid")
            continue

    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])
            number = number - 1

            todos = functions.get_todos()
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            functions.write_todos(todos, 'day10/todos.txt')

            message = f"{todo_to_remove} was removed from the list"
            print(message)
            
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_choice.startswith("exit"):
        break

    else:
        print('Command is not valid')

print("Bye!")