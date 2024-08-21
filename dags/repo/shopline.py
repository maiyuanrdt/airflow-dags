from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="shopline_data_sync", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="shopline_data_sync", bash_command="echo shopline_data_sync")

    @task()
    def airflow():
        print("shopline_data_sync")

    # Set dependencies between tasks
    hello >> airflow()