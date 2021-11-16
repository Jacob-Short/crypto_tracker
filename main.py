import requests
from requests import Session
from api import mysecrets
import sys
import argparse
import logging
import signal
import time
from datetime import datetime
import os
from pprint import pprint as pp


def create_parse():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Gives information on crypto currencies"
    )

    parser.add_argument("symbol", help="symbol of crypto to search for")

    return parser


def main(args):

    parser = create_parse()
    ns = parser.parse_args(args)
    # print(ns)

    symbol = ns.symbol

    if not ns:
        parser.print_usage()

    class CryptoCurrency:
        # https://coinmarketcap.com/api/documentation/v1/
        def __init__(self, token):
            self.apiurl = "https://pro-api.coinmarketcap.com"
            self.headers = headers = {
                "Accepts": "application/json",
                "X-CMC_PRO_API_KEY": token,
            }
            self.session = Session()
            self.session.headers.update(self.headers)

        def get_all_coins(self):
            url = self.apiurl + "/v1/cryptocurrency/map"
            r = self.session.get(url)
            data = r.json()["data"]
            return data

        def get_price(self, symbol):
            url = self.apiurl + "/v1/cryptocurrency/quotes/latest"
            params = {"symbol": symbol}
            r = self.session.get(url, params=params)
            data = r.json()["data"]
            return data

    def command_line(args):
        crypto = CryptoCurrency(mysecrets.API_KEY)
        args_upper = args.upper()
        instance = crypto.get_price(args_upper)
        # pp(instance)
        data = {
            "name": instance[args_upper]["name"],
            "date_added": instance[args_upper]["date_added"],
            "cmc_rank": instance[args_upper]["cmc_rank"],
            "quote": instance[args_upper]["quote"],
        }
        pp(data)
        print(data["name"])

    if symbol:
        command_line(symbol)


if __name__ == "__main__":
    main(sys.argv[1:])
