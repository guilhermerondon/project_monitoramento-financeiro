def detectar_variacoes(precos_atuais, precos_anteriores, limite):
    eventos = []
    for ativo, preco in precos_atuais.items():
        if ativo in precos_anteriores:
            variacao = ((preco - precos_anteriores[ativo]) / precos_anteriores[ativo]) * 100
            if abs(variacao) >= limite:
                eventos.append({
                    "ativo": ativo,
                    "variacao": round(variacao, 2),
                    "preco": preco,
                })
    return eventos