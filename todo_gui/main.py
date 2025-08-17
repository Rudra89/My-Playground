import functions
import FreeSimpleGUI as sg

label = sg.Text('Type a to-do')
label_input_box = sg.InputText(tooltip='Type a to-do')
add_button = sg.Button('Add')

window = sg.Window("My To-Do App", layout=[[label], [label_input_box,add_button]])
window.read()
window.close()