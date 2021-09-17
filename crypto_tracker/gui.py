import PySimpleGUI as sg
import secrets
import os.path
from test import CryptoCurrency
from pprint import pprint as pp


# window layout of twwo colums

def gui_view():
    welcome_center_column = [
        [
            sg.Text("Welcome"),
            # sg.In(size=(25,1), enable_events=True, key="-FOLDER-")
        ]
    ]

    crypto_viewer_column = [
        [
            sg.Text("Please enter a crypto-currency symbol to get started:")
        ]
    ]

    enter_symbol_column = [
        [
            sg.In(size=(45,1), enable_events=True, key="-SYMBOL-")
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(80, 40),
                key="-CRYPTO DATA-"
            )
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

    window = sg.Window("Crypto Tracker", layout, margins=(200,50))

    # event loop
    while True:
        data = {}
        event, values = window.read()
        # End program if user closes windows or 
        # presses the OK button 
        if event == "Search" or event == sg.WIN_CLOSED:
            break
        if event == '-SYMBOL-':
            symbol = values['-SYMBOL-']
            try:
                crypto_symbol = symbol.upper()
                crypto = CryptoCurrency(secrets.API_KEY)
                instance = crypto.get_price(crypto_symbol)
                data = {
                    'name': instance[crypto_symbol]['name'],
                    'date_added': instance[crypto_symbol]['date_added'],
                    'cmc_rank': instance[crypto_symbol]['cmc_rank'],
                    'quote': instance[crypto_symbol]['quote'],
                }
            except Exception as err:
                crypto = []
                print(err)


            crypto_data = [
                data
            ]

            window['-CRYPTO DATA-'].update(crypto_data)
    window.close()

gui_view()