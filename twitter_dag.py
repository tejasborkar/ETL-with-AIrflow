from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from tweepy_api import run_twitter_etl

default_arges = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,10,16),
    'email': ['airflowexample@gmail.com'],
    'email_on_failure': False,
    'email_on_restart': False,
    'retries': 1,
    'retire_dealy': timedelta(minutes=1)
}


dag = DAG(
    'twitter_dag',
    default_arges=default_arges,
    description='my first etl code'
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag
)


run_etl