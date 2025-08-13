def get_todos(filepath="day10/todos.txt"):
    """
    Read a text file and return the list of to-do
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, filepath="day10/todos.txt"):
    """
    Write a to-do items list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)