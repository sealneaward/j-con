import pika
# from sensor import Sensor
import time
import sys


if __name__ == '__main__':
	try:
	    while True:
	        # sensor = Sensor()
			# print sensor.get_data()
			message = {
				'message_text': 'some json message'
			}

			# create connection and resulting new channel (option to use existing channel id)
			# crate queue from channel
			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			channel = connection.channel()
			channel.queue_declare(queue='hello')
			channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
			time.sleep(10)
	except KeyboardInterrupt:
	    sys.exit()
