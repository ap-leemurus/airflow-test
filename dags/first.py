from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    dag_id="first_dag",
    start_date=datetime.now()
)

operation1 = PythonOperator(
    task_id="hello",
    python_callable=lambda: print("Hello"),
    dag=dag,
)

operation2 = PythonOperator(
    task_id="world",
    python_callable=lambda: print("World"),
    dag=dag,
)

operation1 >> operation2
