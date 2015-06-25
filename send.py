#!/usr/bin/env python
import pika
import sys




credentials = pika.PlainCredentials('poladmin','shelter1')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = 'dctestqueuesrv1', virtual_host='directchan',
        credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_channel', type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_channel',
                      routing_key=routing_key,
                      body=message)

print " [x] Sent %r %r" % (routing_key, message)

connection.close()
