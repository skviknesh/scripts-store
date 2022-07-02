""" DOCUMENT HERE

ACTIVITIES DONE IN THIS SCRIPT:
1. Three tasks are created 1-dummy, 2-gets variable using bash & 3-gets variable using python.
2. Variables are set in Airflow UI -> Admin -> variables. (Set as a dictionary - key, value)
3. Why variables have to be set?
    If a variable has to be used across multiple DAG's, then setting variables under Admin helps.

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

from __future__ import print_function
from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators import python_operator

# CREATING DEFAULT ARGUMENTS FOR DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 6, 15),
    'end_date': datetime(2022, 6, 15)
}

# CREATING DAG
dag = DAG('multi_variable_options', 
    schedule_interval="@once", 
    default_args=default_args)


# CREATING A DUMMY TASK USING DUMMY OPERATOR
start = DummyOperator(
    task_id="start",
    dag=dag
)

# CREATING A FUNCTION TO USE IN PYTHON OPERATOR
# Variable.get() gets the variable value
def cals():
        import logging
        var = Variable.get("var2")
        nv = 5 + int(var)
        logging.info(nv)


# CREATING TASK 1:
t1 = BashOperator(
    task_id="get_variable_value",
    bash_command='echo {{ var.value.var3 }} ',
    dag=dag,
)

# CREATING TASK 2:
# You can directly use a variable from a jinja template
# {{ var.value.<variable_name> }} - receives variable value
t2 = python_operator.PythonOperator(
      task_id='comput',
      python_callable=cals,
      dag=dag,
)

# TASK RELATIONSHIP
start >> t1 >> t2