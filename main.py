from binance.client import Client
from buyfunctions import comprar
from sellfunctions import vender
from validarcandles import validar_preco

api_key = 'bGGhPSsx9ZzgnnS2ZYclBsVjW1l7raAmnoN7VDZ3XWhOK2qC2Ttr7djpoyJVxmEm'
api_secret = 'qAK1ZuQ2gS4XMao6psqG0NsPmsjinyFnW9M8NtmjYDtVBwoCHb2fDu6gWkTUBB5p'

client = Client(api_key, api_secret)

symbol = 'BNBUSDT'
quantidade_compra = 1
preco_compra = 500

resultado_compra = comprar(client, symbol, quantidade_compra, preco_compra)
print("Ordem de compra:", resultado_compra)

resultado_venda = vender(client, symbol, quantidade_compra, preco_compra)
print("Ordem de venda:", resultado_venda)
