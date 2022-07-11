import webbrowser

import PySimpleGUI as sg

sg.theme("DarkBlue")

first_row = [[sg.Text("Span Mail Detector Program", text_color="white", font=("Arial", 28))], [sg.Text("UserName:")],
             [sg.InputText(key='username', size=(35, 35))],
             [sg.Text("Password")], [sg.InputText(key="password", password_char="*", size=(35, 35))],
             [sg.Button("OK", button_color="blue", mouseover_colors='red', size=(8, 1))]]
url = {'pop': 'https://support.google.com/mail/answer/7104828?hl=en&visit_id=637931350162462803-658575470&rd=2'}
second_row = [[sg.Text("Instructions", font=("Calibri", 30))], [sg.Text("Please Input Username and password of gmail")]
    , [sg.Text("Please enable POP support in gmail.")], [sg.Text("Click Here", tooltip=url['pop'], enable_events=True,key=f'URL {url["pop"]}')],
              [sg.Text("", enable_events=True)], [sg.Text("----------- program by N.K.Rahul -----------")]]

layout = [[sg.Column(first_row), sg.VSeparator(), sg.Column(second_row)]]
# Create the window
window = sg.Window("Program", layout, size=(810, 260))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    elif event.startswith("URL "):
        url = event.split(' ')
        webbrowser.open("'https://support.google.com/mail/answer/7104828?hl=en&visit_id=637931350162462803-658575470&rd=2'")

def get_user_pass():
    username = values['username']
    password = values['password']
    return username, password


window.close()
