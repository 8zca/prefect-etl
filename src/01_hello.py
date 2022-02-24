import prefect
from prefect import Flow, Parameter, task


@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")


@task
def hello_mytask(org_id: Parameter):
    logger = prefect.context.get("logger")
    if org_id == "1":
        logger.info("first org")
    else:
        logger.info("other org")


with Flow("hello-flow") as flow:
    hello_task()

    org_id = Parameter("org_id")
    hello_mytask(org_id)

flow.run(org_id="1")
