"""
Pagina simples com starlette

Dependencias:

>> pip3 install starlette[full]
>> pip3 install uvicorn

Executando:

>> uvicorn server:app 

server.py:
"""
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

def homepage(request):
    return PlainTextResponse('Hello, world!')

def startup():
    print('Ready to go')


routes = [
    Route('/', homepage),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])