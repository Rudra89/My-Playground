import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkGrey')

clock = sg.Text('',key='clock',text_color='white')
label = sg.Text('Type a to-do')
label_input_box = sg.InputText(tooltip='Type a to-do', key='todo_input')
add_button = sg.Button('Add')
todos_list = sg.Listbox(values=functions.get_todos(), key='todos_list',
                        enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [label_input_box,add_button],
                           [todos_list, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 18))

while True:
    events, values = window.read(timeout=900)
    window['clock'].update(value=f"{time.strftime("%b %d, %Y %H:%M:%S")}")

    match events:
        case 'Add':
            if values['todo_input'] == '':
                sg.popup('You need to enter a to-do')
            else:
                todos = functions.get_todos()
                new_todo = values['todo_input'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)

                window['todos_list'].update(values=todos)

        case 'Edit':
            try :
                selected_todo = values['todos_list'][0]
                new_todo = values['todo_input'] + "\n"

                todos = functions.get_todos()
                # Getting index of selected index so we can update it in list
                selected_todo_index = todos.index(selected_todo)
                todos[selected_todo_index] = new_todo
                functions.write_todos(todos)

                # To update the list of todos with the new value after edit
                window['todos_list'].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do")

        case 'Complete':
            try:
                todo_to_complete = values['todos_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)

                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
                window['todo_input'].update(value="")
            except IndexError:
                sg.popup("Please select a to-do")

        case 'Exit':
            break

        case 'todos_list':
            window['todo_input'].update(value=values['todos_list'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()