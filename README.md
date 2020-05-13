# rabbitmq_demo
rabbitmq测试代码
最简单的测试

###工作队列

1.一个队列的消息，可以使用轮询的方式发送给多个消费者，
2.假如rabbitmq没有收到消费者的消息确认，则会把这条消息发送给其他消费者，
,假如收到，则会在内存中删除该记录

3.消息持久化：创建队列需要申明durable=True，
生产者的消息也需要持久化：
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
                      
4.

