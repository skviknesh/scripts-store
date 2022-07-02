"""
https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/bigquery/index.html#airflow.providers.google.cloud.operators.bigquery.BigQueryCreateEmptyDatasetOperator
Home
airflow.providers.google
airflow.providers.google.cloud
airflow.providers.google.cloud.operators
airflow.providers.google.cloud.operators.bigquery
"""

import airflow
import datetime
from airflow import DAG
from airflow import models
from airflow.operators import bash_operator
from airflow.contrib.operators import bigquery_operator
from airflow.contrib.operators import bigquery_to_gcs
from airflow.utils import trigger_rule
# airflow.providers.google.cloud.operators.bigquery.BigQueryCreateEmptyDatasetOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

default_dag_args = {
     'start_date': airflow.utils.dates.days_ago(1),
     'email_on_failure': False,
     'email_on_retry': False,
     'retries': 1,
     'retry_delay' : datetime.timedelta(minutes=5)
}

output_file = 'gs://us-central1-gayathri-test-22fda0cf-bucket/data/vikneshemployee.csv'
#Replace <Your bucket> with your path details
with DAG(
       dag_id='demo_bq_dag',
       schedule_interval = datetime.timedelta(days = 1),
       default_args = default_dag_args) as dag:


    create_new_dataset = BigQueryCreateEmptyDatasetOperator(
        dataset_id = 'viknesh',
        project_id = 'searce-practice-data-analytics',
        # dataset_reference = {"friendlyName": "New Dataset"},
        gcp_conn_id = '_my_gcp_conn_',
        task_id = 'newDatasetCreator')

    # bq_airflow_commits_query = bigquery_operator.BigQueryOperator(
    #      task_id = 'bq_airflow_commits_query',
    #      bql = """    SELECT Address
    #      FROM [searce-practice-data-analytics:viknesh.employee]
    #       """)
    #
    #
    # export_commits_to_gcs = bigquery_to_gcs.BigQueryToCloudStorageOperator(
    #      task_id = 'export_airflow_commits_to_gcs',
    #      source_project_dataset_table = 'searce-practice-data-analytics:viknesh.employee',
    #      destination_cloud_storage_uris = [output_file],
    #      export_format = 'CSV')

    # bq_airflow_commits_query >> export_commits_to_gcs

    create_new_dataset















