import time
from src import coletor, detector, eventos, config

def main():
    precos_anteriores = coletor.coletar_precos(config.ATIVOS)
    while True:
        time.sleep(config.INTERVALO_COLETA)
        precos_atuais = coletor.coletar_precos(config.ATIVOS)
        evs = detector.detectar_variacoes(precos_atuais, precos_anteriores, config.LIMITE_VARIACAO)
        for e in evs:
            eventos.enviar_evento(e)
        precos_anteriores = precos_atuais

if __name__ == "__main__":
    main()