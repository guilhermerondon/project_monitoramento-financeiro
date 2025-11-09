import random

def detectar_variacoes(precos_atuais, precos_anteriores, limite):
    eventos = []
    for ativo, preco_atual in precos_atuais.items():
        preco_anterior = precos_anteriores.get(ativo, preco_atual)
        variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100

        # 👇 Linha de teste: força um evento aleatório às vezes
        if random.random() < 0.5:
            variacao += random.uniform(limite, limite * 2)

        if abs(variacao) >= limite:
            eventos.append({
                "ativo": ativo,
                "variacao": f"{variacao:+.2f}%",
                "preco": preco_atual
            })
    return eventos
