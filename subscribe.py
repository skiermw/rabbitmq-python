#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('poladmin','shelter1')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = 'dctestqueuesrv1', virtual_host='directchan',
        credentials=credentials))

channel = connection.channel()
queue_name ='accounting'
#channel.exchange_declare(exchange='direct_channel', type='topic')

result = channel.queue_declare(queue=queue_name)

    
print ' [*] Waiting for events. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
