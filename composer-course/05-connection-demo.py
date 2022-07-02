"""
There are 3 connections:
1. task_default_connection - has no connection,
2. task_explicit_connection - google_cloud_default
3. task_custom_connection - my_gcp_connection (This is the one which has to be created)

In Airflow, under Admin -> Connections, enter
    Connection id (name it), connection type (Google cloud), enter a project id ("searce-practice-data-analytics")
Json keyfile path: "/home/airflow/gcs/data/searce-practice-data-analytics-0a878e5359ac.json"
"""

import datetime
from airflow import models
from airflow.contrib.operators import bigquery_operator

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())

default_dag_args = {
    'start_date': yesterday
}

# Define a DAG (directed acyclic graph) of tasks.
# Any task you create within the context manager is automatically added to the
# DAG object.
with models.DAG(
        'composer_sample_connections',
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:


    task_default = bigquery_operator.BigQueryOperator(
        task_id='task_default_connection',
        bql='SELECT 1', use_legacy_sql=False)


    task_explicit = bigquery_operator.BigQueryOperator(
        task_id='task_explicit_connection',
        bql='SELECT 1', use_legacy_sql=False,
        # Composer creates a 'google_cloud_default' connection by default.
        bigquery_conn_id='google_cloud_default')


    task_custom = bigquery_operator.BigQueryOperator(
        task_id='task_custom_connection',
        bql='SELECT 1', use_legacy_sql=False,
        # Set a connection ID to use a connection that you have created.
        bigquery_conn_id='my_gcp_connection')
    # [END composer_connections_custom]