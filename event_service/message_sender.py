import pika
import json
import repository

def send_email_message(event_id, email):
    event = repository.get_event_by_id(event_id)
    if not event:
        print(f"[X] Evento {event_id} não encontrado")
        return

    event_data = {
        'id': event[0],
        'title': event[1],
        'description': event[2],
        'date': event[3]
    }

    message = {
        'email': email,
        'event': event_data
    }

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    print(f"[→] Mensagem enviada para fila com dados do evento: {message}")
    connection.close()
