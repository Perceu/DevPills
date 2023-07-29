"""
pip install plotly
pip install dash

python sample.py
"""
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

app.layout = html.Div([
        html.H1('Hello World'),
        dcc.Graph(figure=fig)
    ],
    style={
        'margin':'auto', 
        'width': '50%'
    }
)

app.run_server(debug=True)