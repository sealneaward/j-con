import pika
import time
import sys
import argparse
from pprint import pprint
from policy import Policy


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make requests to write messages to channel based on attributes of listener in relation to channel.')
    parser.add_argument('--device', dest='device', type=int,help='integer ID of listening device')
    parser.add_argument('--location', dest='location', type=str, help='location of listening device')
    parser.add_argument('--user', dest='user', type=str, help='name of device user')
    parser.add_argument('--policy', dest='policy', type=str, help='path to policy to enforce')

    args = parser.parse_args()
    policy = Policy(
        policy_path=args.policy,
        user=args.user,
        device=args.device,
        location=args.location,
        type='write'
    )

    # check if access is granted
    access = policy.enforce_policy()
    if access is False:
        print('Access to RabbitMQ was denied')

    try:
        path = './data/message.json'
        while access:
            data = open(path).read()
            message = data

            pprint(message)

            # create connection and resulting new channel (option to use existing channel id)
            # crate queue from channel
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='j-con')
            channel.basic_publish(exchange='', routing_key='j-con', body=message)
            time.sleep(10)
    except KeyboardInterrupt:
        sys.exit()
