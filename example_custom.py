"""Post a message to the custom queue."""
from datetime import datetime

import celery
from kombu import Exchange, Queue

import task_queuing.celery_app as app


def send_to_shit(producer=None):
    """Send a custom message as per Scott's instructions."""
    my_queue = Queue('custom_queue', Exchange('custom_queue'), 'custom_queue')
    eta = str(datetime.now())
    id = celery.uuid()
    # headers = {"task": "task_queuing.tasks.custom.shit", "id": id}
    # body = {"text": "Secret text to encode", "Time": current_time}

    message = {
        'task': 'task_queuing.tasks.custom.shit',
        'id': id,
        'args': [id],
        "kwargs": {},
        "retries": 0,
        "eta": eta
    }

    with app.queue_broker.producer_or_acquire(producer) as producer:
        producer.publish(
            message,
            serializer="json",
            exchange=my_queue.exchange,
            routing_key="custom_queue",
            declare=[my_queue],
            retry=True,
        )
        return id


def send_to_reverse_text(producer=None):
    """Send a custom message as per Scott's instructions."""
    # For Celery the queue and routing key should match.
    my_queue = Queue(name='text_queue', routing_key='text_queue')
    eta = str(datetime.now())
    id = celery.uuid()
    # headers = {"task": "task_queuing.tasks.custom.shit", "id": id}
    # body = {"text": "Secret text to encode", "Time": current_time}

    message = {
        'task': 'task_queuing.tasks.text.slowly_reverse_string',
        'id': id,
        'args': [id],
        "kwargs": {},
        "retries": 0,
        "eta": eta
    }

    with app.queue_broker.producer_or_acquire(producer) as producer:
        producer.publish(
            message,
            serializer="json",
            exchange=my_queue.exchange,
            routing_key="custom_queue",
            declare=[my_queue],
            retry=True,
        )
        return id


if __name__ == "__main__":
    id = send_to_shit()
    print(f"task {id} on queue")
    
