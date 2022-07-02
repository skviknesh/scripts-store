""" DOCUMENT HERE

ACTIVITIES DONE IN THIS SCRIPT:
1. Created a python function & called it using Python operator to print "Hello world"
2. Created a Bash operator to print "Bye"

REFERENCE DOCUMENTATIONS ON AIRFLOW WEBSITE:
1. Documentation for all operators-submodules:
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/index.html#submodules

2. Documentation for python_operators: Refer for - "callable" on page.
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#module-airflow.operators.python

3. Documentation for Bash operator:
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/bash/index.html#module-airflow.operators.bash

4. Documentation for Tasks: Concepts->Tasks (& relationships):
https://airflow.apache.org/docs/apache-airflow/stable/concepts/tasks.html
"""

from __future__ import print_function
import datetime
from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator


# CREATING DEFAULT ARGUMENTS FOR DAG
default_dag_args = {
    'start_date': datetime.datetime(2022, 6, 15)
}

# DEFINING A DAG
with models.DAG(
        'composer_sample_simple_greeting_two',
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:

    # CREATING A PYTHON FUNCTION WHICH IS CALLED BY PYTHON OPERATOR:
    def greeting():
        import logging
        logging.info('Hello World!')

    # CREATING A TASK - USING PYTHON OPERATOR:
    hello_python = python_operator.PythonOperator(
        task_id='hello',
        python_callable=greeting)

    # CREATING ANOTHER TASK - USING BASH OPERATOR:
    goodbye_bash = bash_operator.BashOperator(
        task_id='bye',
        bash_command='echo Goodbye.')


    # CREATING TASK RELATIONSHIPS:
    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hello_python >> goodbye_bash