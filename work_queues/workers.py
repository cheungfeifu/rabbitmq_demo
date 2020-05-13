###使用多线程模拟多个worker

import pika
import time
from concurrent.futures import ThreadPoolExecutor

# from mysql_pool import Mysql_Pool


t = ThreadPoolExecutor(3)

user_pwd = pika.PlainCredentials(username='feihu', password='Huaxin2011')


def callback(ch, method, properties, body):
    try:
        msg = str(body, encoding="utf-8")
        print(msg)
        '''
        do somesing....
        '''
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print('err reason:{}'.format(e))
        # ch.basic_ack(delivery_tag=method.delivery_tag)
        pass


def handle():
    user_pwd = pika.PlainCredentials(username='feihu', password='Huaxin2011')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='49.235.56.197', port=5672, virtual_host='/test', credentials=user_pwd))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()


for i in range(3):
    t1 = t.submit(handle)
t.shutdown()
