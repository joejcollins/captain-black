# Unit Testing Celery Tasks

1. install redis
1. pipenv install
1. pipenv shell
    1. python test-harness.py
    1. python test-unittest.py
    1. python test-pytest.py
    1. celery -A tasks worker -l info
    1. python run.py
