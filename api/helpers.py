import requests
import mysecrets
from pprint import pprint as pp


class CryptoCurrency:
    # https://coinmarketcap.com/api/documentation/v1/
    def __init__(self):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": mysecrets.API_KEY,
        }
        self.session = requests.Session()
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

    def get_all_trending_latest(self):
        url = self.apiurl + "/v1/cryptocurrency/trending/latest"
        r = self.session.get(url)
        data = r.json()["data"]
        return data

    def get_limit_trending_latest(self, limit):
        '''takes an int as limit of trending cryptos to query'''
        url = self.apiurl + "/v1/cryptocurrency/trending/latest/limit"
        params = {"limit": {limit}}
        r = self.session.get(url, params)
        data = r.json()["data"]
        return data

    def get_trending_most_visited(self, limit):
        url = self.apiurl + "/v1/cryptocurrency/trending/most-visited"
        r = self.session.get(url)
        data = r.json()["data"]
        return data

