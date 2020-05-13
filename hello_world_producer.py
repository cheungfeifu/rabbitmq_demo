import pika
import sys

user_pwd = pika.PlainCredentials(username='feihu', password='')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='49.235.56.197', port=5672, virtual_host='/test', credentials=user_pwd))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()