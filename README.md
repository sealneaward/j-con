# j-con
Contextually aware access control using context information stored in JSON documents.

## Introduction

This application will serve as a context based access management system for communication across the RabbitMQ medium.
The access managment is largely based on whether the devices requesting access follow the policy document created before hand.
If the request device does not contain the correct context in regards to the defined places, people, and device identification,
then no access is granted.

### RabbitMQ Server Setup

1. Install RabbitMQ server.

```
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.8/rabbitmq-server_3.6.8-1_all.deb

sudo dpkg -i rabbitmq-server_3.6.8-1_all.deb
sudo apt-get update
sudo apt-get -y install socat erlang-nox=1:19.0-1
```

2. Enable RabbitMQ management console

```
sudo rabbitmq-plugins enable rabbitmq_management
```

3. Go to console

```
http://localhost:15672

user: guest
password: guest
```

#### Server Management

```
To start, stop, restart and check the application status on Ubuntu and Debian, use the following:

# To start the service:
service rabbitmq-server start

# To stop the service:
service rabbitmq-server stop

# To restart the service:
service rabbitmq-server restart

# To check the status:
service rabbitmq-server status

# View queues
sudo rabbitmqctl list_queues
```

### Client Setup

1. Clone the repository

```
git clone github.com/sealneaward/j-con
```

2. Start the client

```
python client/client.py

usage: client.py [-h] [--device DEVICE] [--location LOCATION] [--user USER]
                 [--policy POLICY]

Make requests to write messages to channel based on attributes of listener in
relation to channel.

optional arguments:
  -h, --help           show this help message and exit
  --device DEVICE      integer ID of listening device
  --location LOCATION  location of listening device
  --user USER          name of device user
  --policy POLICY      path to policy to enforce
```

Example: `python client.py --device 4 --location inside --user Steve --policy ./policy/policy_example.json`


3. Start the listener

```

python listener.py

usage: listener.py [-h] [--device DEVICE] [--location LOCATION] [--user USER]
                   [--policy POLICY]

Make requests to listen to channel based on attributes of listener in relation
to channel.

optional arguments:
  -h, --help           show this help message and exit
  --device DEVICE      integer ID of listening device
  --location LOCATION  location of listening device
  --user USER          name of device user
  --policy POLICY      path to policy to enforce
```

Example `python listener.py --device 1 --location inside --user Henry --policy ./policy/policy_example.json`

4. To end the application, either press `CTRL + C` or remove the sensorian sheild.

### Common Errors

```
dpkg: dependency problems prevent configuration of rabbitmq-server:
 rabbitmq-server depends on erlang-nox (>= 1:16.b.3) | esl-erlang; however:
  Package erlang-nox is not installed.
  Package esl-erlang is not installed.
 rabbitmq-server depends on socat; however:
  Package socat is not installed.
```

**FIX**

```
sudo apt-get -f install
sudo apt-get update
```

- Then re-install rabbitmq server
