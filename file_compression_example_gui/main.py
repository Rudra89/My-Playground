import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
text_field1 = sg.InputText()
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
text_field2 = sg.InputText()
button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Zipper",
                   layout=[[label1, text_field1, button1],
                           [label2, text_field2, button2],
                           [compress_button]])
window.read()
window.close()