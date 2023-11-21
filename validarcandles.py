from binance.client import Client
from buyfunctions import comprar
from sellfunctions import vender

def validar_preco(candlesticks):
    if(candlesticks[-1][4]) > float(candlesticks[0][1]):
        return 1
    else:
        return 0
    #return float(candlesticks[-1][4]) > float(candlesticks[0][1])
