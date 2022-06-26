import pika, json

params = pika.URLParameters('amqps://nrlmqfuz:dpN-kI883VX-j6oW002E4sfPIoDLFrgX@cougar.rmq.cloudamqp.com/nrlmqfuz')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)