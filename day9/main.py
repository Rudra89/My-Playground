# OPTIMAZIED & BUGS VERSION OF DAY 8
def get_todos(filepath="day9/todos.txt"):
    """
    Read a text file and return the list of to-do
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, filepath="day9/todos.txt"):
    """
    Write a to-do items list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)


while True:
    user_choice = input("Type add, edit, show, complete or exit: ")
    user_choice = user_choice.lower().strip()

    if user_choice.startswith("add"):
        todo = user_choice[4:].title()

        todos = get_todos()
        todos.append(todo + "\n")

        write_todos(todos, 'day9/todos.txt')

    elif user_choice.startswith("show"):
        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1}) {todo}")

    elif user_choice.startswith("edit"):
        try: 
            number = int(user_choice[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo name: ").capitalize()
            todos[number] = new_todo.title() + "\n"
            write_todos(todos, 'day9/todos.txt')

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])
            number = number - 1

            todos = get_todos()
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)

            write_todos(todos, 'day9/todos.txt')

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