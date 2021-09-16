import PySimpleGUI as sg
import os.path


# window layout of twwo colums

welcome_center_column = [
    [
        sg.Text("Welcome"),
        # sg.In(size=(25,1), enable_events=True, key="-FOLDER-")
    ]
]

crypto_viewer_column = [
    [
        sg.Text("Please enter a crypto-currency symbol to get started:")
    ],
    # [
    #     sg.Text(size=(100,50), key="-TOUT-")
    # ]
]

enter_symbol_column = [
    [
        sg.In(size=(45,1), enable_events=True, key="-STRING-")
    ]
]

layout = [
    [
        sg.Column(welcome_center_column),
        sg.VSeparator(),
        sg.Column(crypto_viewer_column),
    ],
    [
        sg.Column(enter_symbol_column),
        sg.Button("Search")
        
    ]
]

window = sg.Window("Demo", layout, margins=(400,300))

# event loop
while True:
    event, values = window.read()
    # End program if user closes windows or 
    # presses the OK button 
    if event == "Search" or event == sg.WIN_CLOSED:
        break
window.close()