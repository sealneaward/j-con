import pika
import time
import sys
import argparse
from policy import Policy


if __name__ == '__main__':

    try:
        path = './data/message.json'
        while True:
            data = open(path).read()
            message = data

            # create connection and resulting new channel (option to use existing channel id)
            # crate queue from channel
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='j-con')
            channel.basic_publish(exchange='', routing_key='j-con', body=message)
            time.sleep(10)
    except KeyboardInterrupt:
        sys.exit()
