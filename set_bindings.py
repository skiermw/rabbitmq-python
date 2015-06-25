#!/usr/bin/env python
import pika
import sys




credentials = pika.PlainCredentials('poladmin','shelter1')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = 'dctestqueuesrv1', virtual_host='directchan',
        credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='accounting', durable=True)
channel.queue_declare(queue='actuarial', durable=True)
channel.queue_declare(queue='crm', durable=True)

channel.exchange_declare(exchange='direct_channel', type='topic')

channel.queue_bind(exchange='direct_channel',
                   queue='actuarial',
                   routing_key='policy_admin.*')

channel.queue_bind(exchange='direct_channel',
                   queue='accounting',
                   routing_key='policy_admin.*')

channel.queue_bind(exchange='direct_channel',
                   queue='crm',
                   routing_key='policy_admin.quote')
                   

connection.close()
