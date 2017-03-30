from __future__ import print_function

import pika
import sys
import RPi.GPIO as GPIO
import json

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(" [x] Received %r" % body)

if __name__ == '__main__':
    try:
        while True:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='hello')
            channel.basic_consume(callback,queue='hello',no_ack=True)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
    except KeyboardInterrupt:
        sys.exit()
