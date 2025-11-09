import pika
import json

# Dados de conexão (RabbitMQ está no Docker, então localhost)
conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexao.channel()

# Garante que a fila existe
canal.queue_declare(queue='eventos_financeiros')

# Cria uma mensagem de teste
mensagem = {"ativo": "AAPL", "variacao": "+3.5%", "preco": 272.10}

# Envia a mensagem
canal.basic_publish(
    exchange='',
    routing_key='eventos_financeiros',
    body=json.dumps(mensagem)
)

print("✅ Mensagem enviada com sucesso:", mensagem)

conexao.close()
