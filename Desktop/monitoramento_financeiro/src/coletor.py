import yfinance as yf

def coletar_precos(ativos):
    dados = {}
    for ativo in ativos:
        ticker = yf.Ticker(ativo)
        preco = ticker.history(period="1d")["Close"].iloc[-1]
        dados[ativo] = preco
    return dados