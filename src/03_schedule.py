import random
from datetime import datetime, timedelta

from prefect import Flow, task
from prefect.schedules import IntervalSchedule
from prefect.triggers import all_failed, all_successful


@task(name="Task A", max_retries=3, retry_delay=timedelta(seconds=1))
def task_a():
    if random.random() > 0.3:
        raise ValueError("Non-deterministic error has occured.")


@task(name="Task B", trigger=all_successful)
def task_b():
    # do something interesting
    pass


@task(name="Task C", trigger=all_failed)
def task_c():
    # do something interesting
    pass


# ずっと起動し続けてフローを定期実行する
# intervalは前回の終了からじゃなくて開始からの時間(TaskAが起動してから)
schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    interval=timedelta(seconds=10),
)

with Flow("Trigger example", schedule=schedule) as flow:
    success = task_b(upstream_tasks=[task_a])
    fail = task_c(upstream_tasks=[task_a])

flow.set_reference_tasks([success])

flow.run()
