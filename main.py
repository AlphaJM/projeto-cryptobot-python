from binance.client import Client

api_key = 'sH8CDtuxmE0QglKJS2u6tVBFtR9klENOhJKUrQrrBqs2xKF4OXfXx70ogKnzNKqTJ'
api_secret = 'OUHWLgmoqxGLqK2LJotcMOb8OKKfIVEypEbEjLRDX2sMZXcItJR0F6zUuaTl9jPP'

client = Client(api_key, api_secret)

from buyfunctions import comprar
from sellfunctions import vender

api_key = 'sH8CDtuxmE0QglKJS2u6tVBFtR9klENOhJKUrQrrBqs2xKF4OXfXx70ogKnzNKqTJ'
api_secret = 'OUHWLgmoqxGLqK2LJotcMOb8OKKfIVEypEbEjLRDX2sMZXcItJR0F6zUuaTl9jPP'
symbol = 'BNBUSDT'
quantidade_compra = 1
preco_compra = 500

resultado_compra = comprar(api_key, api_secret, symbol, quantidade_compra, preco_compra)
print("Ordem de compra:", resultado_compra)

resultado_venda = vender(api_key, api_secret, symbol, quantidade_compra, preco_compra)
print("Ordem de venda:", resultado_venda)
