import functions
import FreeSimpleGUI as sg

label = sg.Text('Type a to-do')
label_input_box = sg.InputText(tooltip='Type a to-do', key='todo_input')
add_button = sg.Button('Add')

window = sg.Window("My To-Do App",
                   layout=[[label], [label_input_box,add_button]],
                   font=('Helvetica', 18))

while True:
    events, values = window.read()
    print(events)
    print(values)
    match events:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo_input'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()