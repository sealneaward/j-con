from __future__ import print_function

import argparse
import pika
import sys
import json
from policy import Policy


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(" [x] Received %r" % str(data['message']))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make requests to listen to channel based on attributes of listener in relation to channel.')
    parser.add_argument('--device', dest='device', type=int,help='integer ID of listening device')
    parser.add_argument('--location', dest='location',help='location of listening device')
    parser.add_argument('--user', dest='user',help='name of device user')
    parser.add_argument('--policy', dest='policy',help='path to policy to enforce')

    args = parser.parse_args()
    policy = Policy(
        policy_path=args.policy,
        user=args.user,
        device=args.device,
        location=args.location,
        type='listen'
    )

    # check if access is granted
    access = policy.enforce_policy()
    if access is False:
        print('Access to RabbitMQ was denied')

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
