import time
import csv
from datetime import datetime
from src import coletor, detector, eventos, config

def main():
    print("Iniciando monitoramento de preços...")
    precos_anteriores = coletor.coletar_precos(config.ATIVOS)


    while True:
        print("Coletando preços...")
        time.sleep(config.INTERVALO_COLETA)

        precos_atuais = coletor.coletar_precos(config.ATIVOS)

        print("Preços atuais:")
        for ativo, preco in precos_atuais.items():
            print(f"{ativo}: {preco}")

        
        with open("precos_log.csv", "a", newline="", encoding="UTF-8") as f:
            writer = csv.writer(f)
            for ativo, preco in precos_atuais.items():
                writer.writerow([datetime.now().isoformat(), ativo, preco])


        evs = detector.detectar_variacoes(
            precos_atuais, precos_anteriores, config.LIMITE_VARIACAO
        )

        for e in evs:
            print(f"🚨 Variação detectada: {e}")
            eventos.enviar_evento(e)

        precos_anteriores = precos_atuais

if __name__ == "__main__":
    main()