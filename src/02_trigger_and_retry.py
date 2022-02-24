import random
from datetime import timedelta

from prefect import Flow, task
from prefect.triggers import all_failed, all_successful


# Aが失敗したらA: Retrying, B,C: Pendingのステータス
# その後指定時間まってリトライが走る
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


with Flow("Trigger example") as flow:
    success = task_b(upstream_tasks=[task_a])
    fail = task_c(upstream_tasks=[task_a])

# taskAが成功したときCは呼び出されずTriggerFailedとなる
# このときフロー全体の状態としてはfailedになる(TriggerFailedはFailedを継承しているから)
# そのため参照タスクを設定し、Bが呼ばれているなら全体として成功とみなす必要がある
flow.set_reference_tasks([success])

flow.run()
