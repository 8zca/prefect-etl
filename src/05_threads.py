from time import sleep

from prefect import Flow, task
from prefect.executors import LocalDaskExecutor


@task
def add_ten(x):
    sleep(1)
    return x + 10


with Flow("simple map") as flow:
    # 配列の順番は保持されるが、計算される順序はバラバラ
    mapped_result = add_ten.map([1, 2, 3])

state = flow.run(executor=LocalDaskExecutor(scheduler="threads", num_workers=3))

# [11,12,13]
print(state.result[mapped_result].result)
