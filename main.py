from binance.client import Client
from binance.spot import Spot
from functions import comprar, vender, obter_preco_atual_btcusdt, obter_candlesticks
from analises import validarpreco

api_key = '-'
api_secret = '-'

client = Client(api_key, api_secret)
spot_client = Spot(client)

preco_atual_btcusdt = obter_preco_atual_btcusdt()

candlesticks = obter_candlesticks(client, 'BTCUSDT', '1m')
resultado_analise = validarpreco(candlesticks)

if resultado_analise == 0:
    resultado_compra = comprar(client, 'BTCUSDT', 0.002, preco_atual_btcusdt)
    print(resultado_compra)
elif resultado_analise == 1:
    resultado_venda = vender(client, 'BTCUSDT', 0.002, preco_atual_btcusdt)
    print(resultado_venda)
else:
    print('Não foi possível realizar a compra e nem a venda!')


if preco_atual_btcusdt is not None:
    resultado_analise = validarpreco(preco_atual_btcusdt)
    if resultado_analise == 0:
        resultado_compra = comprar(client, 'BTCUSDT', 0.002, preco_atual_btcusdt)
        print(resultado_compra)
    elif resultado_analise == 1:
        resultado_venda = vender(client, 'BTCUSDT', 0.002, preco_atual_btcusdt)
        print(resultado_venda)
    else:
        print('Não foi possível realizar a compra e nem a venda!')
else:
    print("Não foi possível obter o preço atual do BTCUSDT.")
