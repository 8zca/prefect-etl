from prefect import Flow, task


@task
def add_ten(x):
    return x + 10


with Flow("simple map") as flow:
    mapped_result = add_ten.map([1, 2, 3])

state = flow.run()

# [11,12,13]
print(state.result[mapped_result].result)
