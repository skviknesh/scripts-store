""" DOCUMENT HERE

ACTIVITIES DONE IN THIS SCRIPT:
1. Created a bash operator to print date.
2. Created another bash operator to wait (sleep) for 5 secs/mins.
3. Created a bash operator to use template (Jinja template).
    3.1 This template - prints date (ds), adds that date & uses the "params" parameter to read the command passed

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

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 6, 15)
}

dag = DAG('tutorial', default_args=default_args, schedule_interval=timedelta(days=1))

# TASK 1:
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

# TASK 2:
t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

# CREATING A JINJA TEMPLATE FOR TASK 3:
templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""
# TEMPLATE: ds - prints date, macros.ds_add() - adds date, params - reads the "my_param" passed in task 3.

# TASK 3:
t3 = BashOperator(
    task_id='templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

# TASK RELATIONSHIPS:
t2.set_upstream(t1) # Similar to t1 >> t2 (task 2 performed after task 1)
t3.set_upstream(t1) # Similar to t1 >> t3 (task 3 performed after task 1)