import PySimpleGUI as sg
import secrets
import os.path
from test import CryptoCurrency
from pprint import pprint as pp


# window layout of twwo colums


def gui_view():
    welcome_center_column = [
        [sg.Text("Welcome:"), sg.In(size=(20, 1), enable_events=True, key="-SYMBOL-")]
    ]

    crypto_viewer_column = [
        [sg.Text("Please enter a crypto-currency symbol to get started:")]
    ]

    enter_symbol_column = [
        [],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(80, 10), key="-CRYPTO NAME DATA-"
            )
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(80, 10), key="-CRYPTO DATE DATA-"
            )
        ],
                [
            sg.Listbox(
                values=[], enable_events=True, size=(80, 10), key="-CRYPTO RANK DATA-"
            )
        ],
                [
            sg.Listbox(
                values=[], enable_events=True, size=(80, 10), key="-CRYPTO QUOTE DATA-"
            )
        ],
    ]

    layout = [
        [
            sg.Column(welcome_center_column),
            sg.VSeparator(),
            sg.Column(crypto_viewer_column),
            sg.Button("NEXT", size=(3, 1)),
        ],
        [
            sg.Column(enter_symbol_column),
        ],
        [sg.Button("EXIT", size=36), sg.Button("Profile", size=36)],
    ]

    window = sg.Window("Crypto Tracker", layout, margins=(500, 200))

    # event loop
    while True:
        data = {}
        event, values = window.read()
        # End program if user closes windows or
        # presses the OK button
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
        if event == "-SYMBOL-":
            symbol = values["-SYMBOL-"]
            try:
                crypto_symbol = symbol.upper()
                crypto = CryptoCurrency(secrets.API_KEY)
                instance = crypto.get_price(crypto_symbol)
                data = {
                    "name": instance[crypto_symbol]["name"],
                    "date_added": instance[crypto_symbol]["date_added"],
                    "cmc_rank": instance[crypto_symbol]["cmc_rank"],
                    "quote": instance[crypto_symbol]["quote"],
                }
            except Exception as err:
                crypto = []
                print(err)

            # crypto_data = [data]

            window["-CRYPTO NAME DATA-"].update(data)
            window["-CRYPTO DATE DATA-"].update(data)
            window["-CRYPTO RANK DATA-"].update(data)
            window["-CRYPTO QUOTE DATA-"].update(data)
            print(data['name'])
    window.close()


gui_view()
