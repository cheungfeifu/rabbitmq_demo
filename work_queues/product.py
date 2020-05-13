
import pika
import sys

user_pwd = pika.PlainCredentials(username='feihu', password='Huaxin2011')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='49.235.56.197', port=5672, virtual_host='/test', credentials=user_pwd))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()