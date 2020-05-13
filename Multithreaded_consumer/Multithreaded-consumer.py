import pika
import time
from concurrent.futures import ThreadPoolExecutor
# from mysql_pool import Mysql_Pool


t=ThreadPoolExecutor(10)
# 初始化三个数据库的连接池


# 创建多个线程处理写入数据库的事情
user_pwd = pika.PlainCredentials(username='cralwer', password='******')


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
        #ch.basic_ack(delivery_tag=method.delivery_tag)
        pass



def handle():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='ip', port=5672, virtual_host='/vhost', credentials=user_pwd))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()


for i in range(10):
    t1 = t.submit(handle)
t.shutdown()
