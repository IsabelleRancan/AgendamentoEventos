import pika
import json
from email_sender import send_email

def callback(ch, method, properties, body):
    data = json.loads(body)
    email = data['email']
    event = data['event']

    subject = f"Confirmação de inscrição: {event['title']}"
    body = (
        f"Olá!\n\n"
        f"Você foi inscrito com sucesso no evento:\n\n"
        f"📌 Título: {event['title']}\n"
        f"🗓 Data: {event['date']}\n"
        f"📝 Descrição: {event['description']}\n\n"
        f"Nos vemos lá! 😊"
    )

    send_email(email, subject, body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='email_queue', on_message_callback=callback)

    print("[*] Aguardando mensagens. Pressione CTRL+C para sair.")
    channel.start_consuming()

if __name__ == '__main__':
    main()
