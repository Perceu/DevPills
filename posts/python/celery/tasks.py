"""
Usando celery para executar tarefas assincronas
$ pip install celery
Para executar o rabbitMQ use o docker-compose abaixo
docker-compose.yml:

'''
services:
  rabbit:
    image: rabbitmq:3-management
    container_name: rabbitmq_management
    ports:
     - 5672:5672
     - 15672:15672
'''

para executar a tarefa abaixo execute 

celery -A tasks worker --loglevel=INFO

worker:
"""
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

@app.task
def hello():
    print("hello world")
    return 'hello world'