# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 15:21
# @Author  : ZFH
# @FileName: RabbitmqHandler.py
# @Software: PyCharm
import pika

class RabbitmqHandler:
    def __init__(self,db_name):
        self.user_pwd = pika.PlainCredentials(username='cralwer', password='5C5wIYOsE1CiIgxv')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='ip',port=5672,virtual_host='/{}'.format(db_name),credentials=self.user_pwd))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)

    def send(self,msg):
        self.channel.basic_publish(exchange='', routing_key='task_queue', body=msg)
        # print(" [x] Sent %r" % msg)

    def close(self):
        self.connection.close()

