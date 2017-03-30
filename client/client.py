import pika
from sensor import Sensor
import time
import sys
import RPi.GPIO as GPIO
import json


if __name__ == '__main__':
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(18, GPIO.IN)
		sensor = Sensor()

		# check if GPIO can detect input from sensorian
	    while GPIO.input(18):
			data = sensor.get_data()
			message = json.dumps(data)


			# create connection and resulting new channel (option to use existing channel id)
			# crate queue from channel
			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			channel = connection.channel()
			channel.queue_declare(queue='pi-con')
			channel.basic_publish(exchange='pi-con', routing_key='hello', body=message)
			time.sleep(10)
	except KeyboardInterrupt:
	    sys.exit()
