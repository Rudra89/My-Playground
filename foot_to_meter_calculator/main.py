import FreeSimpleGUI as sg


feet_label = sg.Text("Enter feet:")
feet_input = sg.InputText(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
meter_label = sg.Text(key="meter")

window = sg.Window("Convertor", layout=[[feet_label, feet_input],
                                        [inches_label, inches_input],
                                        [convert_button, meter_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            foot_to_meter = float(values["feet"]) * 0.3048
            inches_to_meter = float(values["inches"]) * 0.0254
            to_meter = foot_to_meter + inches_to_meter
            window["meter"].update(value = f"{to_meter}m")

window.close()