"""
Usando celery para executar tarefas assincronas

para executar atividades dentro do mesmo projeto 
mas assincronamente use tarefa delay

local publish:
"""
from tasks import hello

hello.delay()