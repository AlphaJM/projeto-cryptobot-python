from binance.client import Client

def vender(api_key, api_secret, symbol, quantidade, preco):
    candlesticks = obter_candlesticks(api_key, api_secret, symbol, '1m')
    if not validar_preco(candlesticks):
        print("Condição de venda atendida. Realizando venda.")
        client = Client(api_key, api_secret)
        order = client.create_order(
            symbol=symbol,
            side='SELL',
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantidade,
            price=preco
        )
        return "Venda realizada com sucesso."
    else:
        print("Condição de venda não atendida. Não realizando venda.")
        return "Condição de venda não atendida."

def obter_candlesticks(api_key, api_secret, symbol, intervalo, limite=5):
    client = Client(api_key, api_secret)
    candlesticks = client.get_klines(symbol=symbol, interval=intervalo, limit=limite)
    return candlesticks

def validar_preco(candlesticks):
    return float(candlesticks[-1][4]) > float(candlesticks[0][1])
