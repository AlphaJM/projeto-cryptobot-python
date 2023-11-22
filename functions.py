import requests
from binance.client import Client
from analises import validarpreco

def obter_candlesticks(client, symbol, intervalo, limite=5):
    candlesticks = client.get_klines(symbol=symbol, interval=intervalo, limit=limite)
    return candlesticks

def vender(client, symbol, quantidade, preco):
    order = client.create_order(
        symbol=symbol,
        side='SELL',
        type='LIMIT',
        timeInForce='GTC',
        quantity=quantidade,
        price=preco
    )
    return "Venda realizada com sucesso."

def comprar(client, symbol, quantidade, preco):
    order = client.create_order(
        symbol=symbol,
        side='BUY',
        type='LIMIT',
        timeInForce='GTC',
        quantity=quantidade,
        price=preco
    )
    return "Compra realizada com sucesso."

def obter_preco_atual_btcusdt():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {"symbol": "BTCUSDT"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        data = response.json()
        preco_atual = float(data["price"])
        return preco_atual
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
