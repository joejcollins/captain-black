""" Scratch pad. """
import celery
from task_queuing.tasks.number import slowly_add_two_numbers
from task_queuing.tasks.text import slowly_reverse_string

task1 = slowly_reverse_string.s("qwerty")
task2 = slowly_reverse_string.s("asdfgh")
task3 = slowly_add_two_numbers.s(1, 2)
task4 = slowly_add_two_numbers.s(3, 4)

result = celery.group(task1, task2, task3, task4)()
print("test")
