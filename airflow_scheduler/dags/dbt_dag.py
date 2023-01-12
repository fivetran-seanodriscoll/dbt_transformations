from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from fivetran_provider_async.operators import FivetranOperatorAsync

from datetime import datetime, timedelta

with DAG(
    dag_id="dbt_dag",
    start_date=datetime(2023,1,10),
    schedule_interval=timedelta(minutes=5),
    catchup=False,
    tags= ["fivetran_demo"],
    default_args={
        "owner": "SEAN_ODRISCOLL",
        "retries": 2,
        "retry_delay": timedelta(minutes=1)
    }
) as dag:

    t1 = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd ../../warn_vertebra && dbt run"
    )

    t2 = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd ../../warn_vertebra && dbt test"
    )

    t1 >> t2
