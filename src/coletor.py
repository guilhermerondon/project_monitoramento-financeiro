import yfinance as yf

def coletar_precos(ativos):
    dados = {}
    for ativo in ativos:
        print(f"Coletando preço para {ativo}...")
        try:
            ticker = yf.Ticker(ativo)
            preco = ticker.history(period="1d")["Close"].iloc[-1]
            dados[ativo] = preco
            print(f"Preço coletado para {ativo}: {preco}")
        except Exception as e:
            print(f"Erro ao coletar preço para {ativo}: {e}")
    return dados