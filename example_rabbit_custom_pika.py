""" Scratch pad. """
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672))
channel = connection.channel()

channel.queue_declare(queue="text_queue", durable=True)

# message = {
#     "Body": {"Type": "environment", "Alias": "{{alias}}", "Properties": {}},
#     "Topic": "{{alias}}.environment.{{action}}",
#     "CallContext": {},
# }

message = "hello world"

channel.basic_publish(
    exchange="",
    routing_key="text_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
)

print(" [x] Sent %r" % message)
connection.close()

print("Chain of tasks now on the Rabbit broker.")
