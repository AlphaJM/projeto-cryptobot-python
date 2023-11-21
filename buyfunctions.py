from binance.client import Client
from sellfunctions import validar_preco 

def comprar(api_key, api_secret, symbol, quantidade, preco):
    candlesticks = obter_candlesticks(api_key, api_secret, symbol, '1m')
    if validar_preco(candlesticks):
        print("Condição de compra atendida. Realizando compra.")
        client = Client(api_key, api_secret)
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

def obter_candlesticks(api_key, api_secret, symbol, intervalo, limite=5):
    client = Client(api_key, api_secret)
    candlesticks = client.get_klines(symbol=symbol, interval=intervalo, limit=limite)
    return candlesticks
