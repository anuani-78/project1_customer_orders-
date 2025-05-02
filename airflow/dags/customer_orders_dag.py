from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG('customer_orders_pipeline',
         default_args=default_args,
         schedule_interval='@once',
         catchup=False) as dag:

    clean_data = BashOperator(
        task_id='clean_data',
        bash_command='python /opt/airflow/dags/python/clean_data.py'
    )

    load_customers = BashOperator(
        task_id='load_customers',
        bash_command='python /opt/airflow/dags/python/load_customers.py'
    )

    load_orders = BashOperator(
        task_id='load_orders',
        bash_command='python /opt/airflow/dags/python/load_orders.py'
    )

    clean_data >> load_customers >> load_orders
