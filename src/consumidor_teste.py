import pika
import json

def callback(ch, method, properties, body):
    evento = json.loads(body)
    print(f"📩 Evento recebido: {evento}")

# Conecta ao RabbitMQ
conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()

# Garante que a fila existe
canal.queue_declare(queue='eventos_financeiros')

# Define a função que processa as mensagens
canal.basic_consume(
    queue='eventos_financeiros',
    on_message_callback=callback,
    auto_ack=True
)

print("👂 Aguardando eventos... pressione CTRL+C para sair.")
canal.start_consuming()
