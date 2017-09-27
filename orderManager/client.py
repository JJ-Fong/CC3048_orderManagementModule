#!/usr/bin/env python
import pika
import uuid

class FibonacciRpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
        

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='calvin_candy',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)


fibonacci_rpc = FibonacciRpcClient()
print fibonacci_rpc 
print("send request to order")
response = fibonacci_rpc.call("{\"token\":\"a8a43c1a-6caa-41c9-a5d5-4284f7f84ea7\",\"order\":{\"address\": \"A101\",\"status\": \"RECEIVED\",\"products\": [{\"product\": \"Cocacola\",\"qty\": 1},{\"product\": \"Hamburguesa\",\"qty\": 1}]}}")
print(" [.] Got %r" % response)