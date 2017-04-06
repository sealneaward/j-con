from __future__ import print_function

import argparse
import pika
import sys
import json
from policy import Policy
from sense_emu import SenseHat
import pandas as pd


def callback(ch, method, properties, body):
    """
    Print message
    """

    data = json.loads(body)
    print(" [x] Received %r" % str(data['message']))

def get_context(path,sensor, season):
    """
    Using several bounds defined from the data file,
    derive location context from the HAT sensors

    Parameters
    ----------
    season: str
        time of the year, used in context formation
    sensor: sense_emu.SenseHat object
        sensor emulator object that contains humidit and temp values to
        derive contxt from
    path: str
        path to data to read bounds on context values

    Returns
    -------
    location: str
        context derved from humidity and temp sensors
    """
    temp = sensor.get_temperature()
    humid = sensor.get_humidity()

    print('Temperatue: %d' % temp)
    print('Humidity: %d' % humid)

    data = pd.read_csv(path)
    data = data[data['season'] == season]

    print('Season: %s' % season)

    data = data[
        (data['temp_lower'] < temp) &
        (data['temp_upper'] > temp) &
        (data['humid_lower'] < humid) &
        (data['humid_upper'] > humid)
    ]

    if data.empty:
        return None
    else:
        location = data['location'].values[0]
        print('Location Derived: %s' % location)
        return location

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make requests to listen to channel based on attributes of listener in relation to channel.')
    parser.add_argument('--device', dest='device', type=int,help='integer ID of listening device')
    parser.add_argument('--user', dest='user', type=str,help='name of device user')
    parser.add_argument('--policy', dest='policy', type=str, help='path to policy to enforce')
    parser.add_argument('--data', dest='data', type=str, help='path to dataset containing context bounds')
    parser.add_argument('--season', dest='season', type=str, help='season of the year')

    # initiate sensor
    sense = SenseHat()

    # get args
    args = parser.parse_args()

    # printing for functional tests
    print('User: %s' % (args.user))
    print('Device ID: %d' % (args.device))

    location = get_context(path=args.data, sensor=sense, season=args.season)
    if location is None:
        print('Error in deriving context')
        sys.exit()

    policy = Policy(
        policy_path=args.policy,
        user=args.user,
        device=args.device,
        location=location
    )

    # check if access is granted
    access = policy.enforce_policy()
    if access is False:
        print('Access to RabbitMQ was denied')
        sys.exit()

    try:
        while access:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='j-con')
            channel.basic_consume(callback,queue='j-con',no_ack=True)
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
    except KeyboardInterrupt:
        sys.exit()
