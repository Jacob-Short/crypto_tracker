import requests
from requests import Session
import secrets
import sys
import argparse
import logging
import signal
import time
import datetime
import os
from pprint import pprint as pp

class CryptoCurrency:
    #https://coinmarketcap.com/api/documentation/v1/
        def __init__(self, token):
            self.apiurl = "https://pro-api.coinmarketcap.com"
            self.headers = headers = {
                "Accepts": "application/json",
                "X-CMC_PRO_API_KEY": token,
            }
            self.session = Session()
            self.session.headers.update(self.headers)

        def get_all_coins(self):
            url = self.apiurl + '/v1/cryptocurrency/map'
            r = self.session.get(url)
            data = r.json()['data']
            return data

        def get_price(self, symbol):
            url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
            params = {'symbol': symbol}
            r = self.session.get(url, params=params)
            data = r.json()['data']
            return data

