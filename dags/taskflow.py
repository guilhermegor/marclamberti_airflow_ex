from airflow.decorators import dag, task
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['taskflow']
)

def taskflow():

    @task
    def task_a():
        print('TASK A')
        return 42

    @task
    def task_b(value):
        print('TASK B')
        print(value)

    task_b(task_a())

taskflow()