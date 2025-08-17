import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
text_field1 = sg.InputText()
button1 = sg.FilesBrowse("Choose", key="selected_files")

label2 = sg.Text("Select destination folder")
text_field2 = sg.InputText()
button2 = sg.FolderBrowse("Choose", key="selected_folder")

compress_button = sg.Button("Compress")
output_text = sg.Text(key="output_text_widget", text_color="green")

window = sg.Window("File Zipper",
                   layout=[[label1, text_field1, button1],
                           [label2, text_field2, button2],
                           [compress_button, output_text]])
while True:
    event, values = window.read()
    filepaths = values['selected_files'].split(';')
    folder = values['selected_folder']
    make_archive(filepaths, folder)
    window["output_text_widget"].update(value="Compression Completed!")

window.close()