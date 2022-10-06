import datetime
import pendulum

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)


with DAG(
    dag_id='hudi_with_dbt_glue',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule_interval= '@once'
) as dag:
    k = KubernetesPodOperator(
    name="dbt_models",
    image="715267777840.dkr.ecr.ap-south-1.amazonaws.com/hudi_models:v1",
    service_account_name="dbt-glue",
    task_id="dbt_glue_demo",
    namespace="airflow"
)