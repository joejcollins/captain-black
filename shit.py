""" Scratch pad. """
from task_queue.text import slowly_reverse_string
result = slowly_reverse_string.delay("shit")
print(result.get())