import pika
import urllib2
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='calvin_candy')

def manage_order(data):
    url = "http://127.0.0.1:8000/api-ordermanager/order/"
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    print 'data', data
    rea_data = json.loads(data)
    info = {
    	"token": rea_data["token"]
    }
    order = {
    	"address": rea_data["order"]["address"],
    	"status": rea_data["order"]["status"],
    }

    products = []
    for p in rea_data["order"]["products"]:
    	products.append(p)
    order["products"] = products
    info["order"] = order
    print info
    request = urllib2.Request(url, json.dumps(info))
    request.add_header("Content-Type", "application/json")
    response = opener.open(request)
    return response.read()


def on_request(ch, method, props, body):
    print("request", body)
    response = manage_order(body)
    print response
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


#Queue Basic implementation

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='calvin_candy')
#channel.basic_consume(callback, queue='calvin_candy')
print(" [x] Awaiting order request")
channel.start_consuming()