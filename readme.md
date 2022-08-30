# instructions 
Run Production Plotly Dash via wsgi gnunicorn


#### file structure: flat
$ ls 
(your project folder) ->
    app.py 
    requirement.txt 
    env(folder)


## app.py file code 
```
"""
Minimal Plotly Dash in Production Server

references:
https://dash.plotly.com/deployment
+ 
correct invocation line here:
https://community.plotly.com/t/error-with-gunicorn-application-object-must-be-callable/31397 

"""

from dash import Dash, dcc, html, Input, Output
import os

# css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = Dash(__name__, external_stylesheets=external_stylesheets)

# needed for gunicorn/wsgi to connect
server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['Earth_1', 'Earth_2', 'Mars'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
                
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
```


#### Terminal Code to create / Run: Part 1
```
$ mkdir viz; cd viz

$ python3 -m venv env; source env/bin/activate

(ENV)$ python3 -m pip install --upgrade pip

(ENV)$ pip install -r requirements.txt

$ touch app.py
```

Cut and paste code into app.py file.

#### Terminal Code to create / Run: Part 2

Run with
```
$ gunicorn app:server --bind=127.0.0.1:8050
```
For persistent production you may need to 
```
(ENV)$ nohup gunicorn app:server --bind=127.0.0.1:8050 &
    or
(ENV)$ screen gunicorn app:server --bind=127.0.0.1:8050 &
```

## references:

#### Roughly following "heroku" deploy here:
https://dash.plotly.com/deployment

+ 

#### correct invocation line here:
https://community.plotly.com/t/error-with-gunicorn-application-object-must-be-callable/31397 

