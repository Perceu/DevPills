#
# pip install diagrams
# depends on graphviz
# 
#
# python diagram.py

from posts.python.diagram import Diagram
from diagrams.onprem.network import Nginx
from diagrams.onprem.network import Gunicorn
from diagrams.programming.framework import Django
from diagrams.onprem.database import Postgresql

with Diagram("Django App", show=False):
    Nginx("Nginx") >> Gunicorn("Gunicorn") \
        >> Django("django") >> Postgresql("Postgres")