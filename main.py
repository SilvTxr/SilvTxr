#Basic imports
import os 
import random 
import time 
from time import *

import requests
from requests import Request, Session
from requests import ConnectionError, Timeout, TooManyRedirects 

from bs4 import BeautifulSoup

import lxml


#Scrapping the cryptocurrency price from the coinmarketcap website
def get_crypto_price(url):
    session = Session()
    response = session.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    price = soup.find(class_="priceValue").text
    return price 

#Asking the client which cryptocurrency price he/she wants 
crypto_price = input("Bienvenue. Rentrez le symbole de la crypto que vous recherchez. \n Bitcoin = BTC \n Etherum = ETH \n")

#Running the get_crypto_price function with the righy cryptocurrency 
if crypto_price == 'BTC': 
    print(get_crypto_price('https://coinmarketcap.com/currencies/bitcoin/'))
if crypto_price == 'ETH': 
    print(get_crypto_price('https://coinmarketcap.com/currencies/etherum/'))

sleep(5)


