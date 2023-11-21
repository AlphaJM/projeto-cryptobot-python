from binance.client import Client

def vender(client, symbol, quantidade, preco):
    candlesticks = obter_candlesticks(client, symbol, '1m')
    if not validar_preco(candlesticks):
        print("Condição de venda atendida. Realizando venda.")
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

def obter_candlesticks(client, symbol, intervalo, limite=5):
    candlesticks = client.get_klines(symbol=symbol, interval=intervalo, limit=limite)
    return candlesticks


