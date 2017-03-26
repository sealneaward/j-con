# pi-con
Contextually aware access control on a Raspberry Pi.

### Setup

1. Install RabbitMQ server.

```
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.8/rabbitmq-server_3.6.8-1_all.deb

sudo dpkg -i rabbitmq-server_3.6.8-1_all.deb
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
```
