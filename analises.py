from binance.client import Client
    
def validarpreco(candlesticks):
    # Adicione sua lógica de validação aqui com base nos candlesticks
    # Por exemplo, comparar o preço de fechamento do último candlestick com o preço de abertura do primeiro
    if float(candlesticks[-1][4]) > float(candlesticks[0][1]):
        return 1  # Indica que você deve vender
    else:
        return 0  # Indica que você deve comprar





