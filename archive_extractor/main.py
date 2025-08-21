import FreeSimpleGUI as sg
import zip_extractor

sg.theme('DarkGrey')

label1 = sg.Text("Select Archive")
input1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select Destination")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="destination")

button3 = sg.Button("Extract")
output_label = sg.Text(text_color="green", key="output_label")

window = sg.Window('Archive Extractor',
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [button3, output_label]])

while True:
    event, values = window.read()
    archive = values['archive']
    destination = values['destination']
    zip_extractor.extract_zip(archive, destination)
    window['output_label'].update("Extraction Completed!!")

window.close()