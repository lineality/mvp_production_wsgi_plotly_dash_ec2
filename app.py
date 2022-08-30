"""
Minimal Plotly Dash in Production Server

This is extremely minimal for a proof of concept
for running Plotly Dash Community Edition in a Production Server

The overall template for this was take from the plotly dash 
docs page for heroku (see link below), 
then adapted and simplified for general production deployment use.

references:
Less minimal app.py code here:
https://dash.plotly.com/deployment
+ 
correct invocation line here:
https://community.plotly.com/t/error-with-gunicorn-application-object-must-be-callable/31397 

Test invoke with: 
(but will end when your ec2 terminal session ends, resets, etc.)
    $ gunicorn app:server --bind=0.0.0.0:8050

For persistent production you will need: (end with kill process number) 
    (ENV)$ nohup gunicorn app:server --bind=0.0.0.0:8050 &
    or
    (ENV)$ screen gunicorn app:server --bind=0.0.0.0:8050 &

"""

# Import your Python Libraries (you may need boto3 for AWS)
from dash import Dash, dcc, html, Input, Output
import os

# Connects Dash -> Flask (for wsgi/gunicorn production server)
app = Dash(__name__)

# needed for gunicorn/wsgi to connect
server = app.server

# Your visualization code goes here etc.
app.layout = html.Div([
    html.H2('Hello World')
])

if __name__ == '__main__':
    """
    You may add code here, 
    e.g. to force a port and or turn off debug
    """
    # app.run_server(debug=True)
    app.run_server(host= '0.0.0.0', port=8050)
