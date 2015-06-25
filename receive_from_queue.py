#!/usr/bin/env python
import pika
import sys
import logging

logging.basicConfig()

credentials = pika.PlainCredentials('admin','shelter1')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = 'dctestqueuesrv1', virtual_host='/',
        credentials=credentials))

channel = connection.channel()
print "got here!"
queue_name = 'docman'
#result = channel.queue_declare(queue=queue_name)

filename = 'queuepolchg.txt'
outfile = open(filename, 'w')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body)
    print "--------------------------"
    outfile.write(body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
