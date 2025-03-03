from airflow.decorators import dag
from airflow.operators.dummy_operator import DummyOperator #Substituindo por um operador padrão do Airflow.
from datetime import datetime


@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["smooth"],
)
def smooth(): #adicionando os : na definição da função
    video = DummyOperator(
        task_id="youtube_video"
    )


smooth()
