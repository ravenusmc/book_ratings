from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

from app import app

layout = html.Div([

    html.Div([

        html.Div([
            html.P('Hello World', className='center test'),
        ], className='test')
        
    ]),

    html.Div(id='app-1-display-value', className='test'),
    dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
