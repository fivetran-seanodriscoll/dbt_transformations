from datetime import datetime, timedelta

from airflow import DAG
from fivetran_provider.operators.fivetran import FivetranOperator

from fivetran_provider_async.operators import FivetranOperatorAsync
from fivetran_provider_async.sensors import FivetranSensorAsync

default_args = {
    "owner": "Airflow",
    "start_date": datetime(2023, 1, 10),
    "fivetran_conn_id": "fivetran_default",
}

dag = DAG(
    dag_id="demo_fivetran_sync",
    default_args=default_args,
    schedule_interval=timedelta(minutes=60),
    catchup=False,
)

with dag:
    fivetran_async_op = FivetranOperatorAsync(
        task_id="fivetran_async_op",
        connector_id="flap_meaningful",
    )

    fivetran_sync_op = FivetranOperator(
        task_id="fivetran_sync_op",
        connector_id="flap_meaningful",
    )

    fivetran_async_sensor = FivetranSensorAsync(
        task_id="fivetran_async_sensor",
        connector_id="flap_meaningful",
        poke_interval=5,
        xcom="{{ task_instance.xcom_pull('fivetran_sync_op', key='return_value') }}",
    )

    fivetran_async_op >> fivetran_sync_op >> fivetran_async_sensor
