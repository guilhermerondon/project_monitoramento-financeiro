import pika
import json

def enviar_evento(evento):
    conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexao.channel()
    canal.queue_declare(queue='eventos_financeiros')
    canal.basic_publish(
        exchange='',
        routing_key='eventos_financeiros',
        body=json.dumps(evento)
    )
    print(f"[✔️] Evento enviado: {evento}")
    conexao.close()