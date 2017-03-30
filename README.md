# pi-con
Contextually aware access control on a Raspberry Pi.

## Introduction

This application will serve as a context based access management system for communication across the RabbitMQ medium.
The access managment is largely based on whether the sensors are supplying new information to client modues.
If there has not been any updates locally, the client assumes the sensors are no longer connected,
and the RabbitMQ communication access is shut off.

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

### Raspberry Pi (Client) Setup

**This assumes that you have Raspberry Pi setup, and the sensorian firmware is installed**

1. Clone the repository

```
git clone github.com/sealneaward/pi-con
```

2. Start the client

```
sudo python client/client.py
```

3. Start the listener

```
sudo python listener.py
```

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
