"""
Usando celery para tarefas assincronas

para publicar remotamente tarefas numa fila use o send_task

remote publish:
"""

from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')
app.send_task('tasks.hello')