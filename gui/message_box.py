
import PySimpleGUI as sg

# sg.theme('Material1')

def message_box(message, sign="pass"):
    layout = [[sg.Text("" + message)], [sg.Button("OK")]]

    # Create the window
    window = sg.Window(sign, layout, size=(500, 100), element_justification='c',resizable=True)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()
