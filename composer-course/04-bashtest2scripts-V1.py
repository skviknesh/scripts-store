""" DOCUMENT HERE

ACTIVITIES DONE IN THIS SCRIPT:
1. Creating a python script called "04-test.py" and uploaded it in "Data" folder in GCS bucket.
2. Data folder is in the same bucket location where "dag" folder is.
3. Created a task with Bash operator to run a python script in "data" folder.
4. Path to get the python script in "data" folder is called "mapped directory" - Example: "/home/airflow/gcs/data/"
    The documentation to it is available at, https://cloud.google.com/composer/docs/composer-2/cloud-storage

REFERENCE DOCUMENTATIONS ON AIRFLOW WEBSITE:
1. Documentation for all operators-submodules:
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/index.html#submodules

2. Documentation for Templates: (Jinja templates)
https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html

3. Documentation for Bash operator:
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/bash/index.html#module-airflow.operators.bash

4. Documentation for Tasks: Concepts->Tasks (& relationships):
https://airflow.apache.org/docs/apache-airflow/stable/concepts/tasks.html
"""

import datetime
from airflow import models
from airflow.operators import bash_operator

# CREATING YESTERDAY'S DATE
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())


default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    #'start_date': datetime.datetime(2022, 6, 15),
    'start_date': yesterday
}

with models.DAG(
        'composer_call_bashoperator_python',
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:

    # CREATING A TASK WITH BASH OPERATOR - TO RUN PYTHON SCRIPT IN DATA FOLDER.
    run_python = bash_operator.BashOperator(
        task_id='run_python3',
        # This example runs a Python script from the data folder to prevent
        # Airflow from attempting to parse the script as a DAG.
        bash_command='python2 /home/airflow/gcs/data/04-test.py')