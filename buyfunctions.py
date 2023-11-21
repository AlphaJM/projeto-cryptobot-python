from binance.client import Client
from sellfunctions import validar_preco

def comprar(client, symbol, quantidade, preco):
    candlesticks = obter_candlesticks(client, symbol, '1m')
    if validar_preco(candlesticks):
        print("Condição de compra atendida. Realizando compra.")
        order = client.create_order(
            symbol=symbol,
            side='BUY',
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantidade,
            price=preco
        )
        return "Compra realizada com sucesso."
    else:
        print("Condição de compra não atendida. Não realizando compra.")
        return "Condição de compra não atendida."

def obter_candlesticks(client, symbol, intervalo, limite=5):
    candlesticks = client.get_klines(symbol=symbol, interval=intervalo, limit=limite)
    return candlesticks
