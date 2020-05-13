import pika
import sys

user_pwd = pika.PlainCredentials(username='feihu', password='')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='49.235.56.197', port=5672, virtual_host='/test', credentials=user_pwd))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
