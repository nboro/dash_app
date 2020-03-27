import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from view import layout

cars = pd.read_csv('cars_processed.csv')
cars_years = pd.read_csv('years_manufacturers.csv')

#replace with bootstrap
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,meta_tags=[{'name': 'viewport', 'content': 'width=device-width',
    'title':'Nemania Borovits | HW3 Data Visualization | MPG Dataset',
    'keywords':'Nemania Borovits, python dash, data visualization',
    'description':'Nemania Borovits made this simple python dash app as part of hw3 for data visualization course'}],
    external_stylesheets=external_stylesheets
)
# app.css.append_css({'external_url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'})
app.title = 'Nemania Borovits | HW3 Data Visualization | MPG Dataset'
app.layout = layout

#first visualizations callbacks
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])    
def update_figure(selected_year):
    filtered_df = cars[cars['model year'] == selected_year]
    traces = []
    for i in filtered_df.country.unique():
        df_by_country = filtered_df[filtered_df['country'] == i]
        traces.append(dict(
            x=df_by_country['weight'],
            y=df_by_country['mpg'],
            text=df_by_country['manufacturer']+ ' '+ df_by_country['model'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'Linear', 'title': 'Vehicle Weight',
                   'range':[1500, 5500]},
            yaxis={'title': 'MPG fuel consumption', 'range': [5, 50]},
            margin={'l': 60, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }
#first visualizations callbacks end

#second visualizations callbacks
@app.callback(
    Output('graph-with-slider2', 'figure'),
    [Input('year-slider2', 'value')])    
def update_figure2(selected_year):
    filtered_df2 = cars_years[cars_years['model year'] == selected_year]
    traces = []
    for i in filtered_df2.country.unique():
        df_by_country2 = filtered_df2[filtered_df2['country'] == i]
        traces.append(dict(
            x=df_by_country2['manufacturer'],
            y=df_by_country2['mean_mpg'],
            # text=df_by_country2['manufacturer']+ ' ',
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'Linear', 'title': 'Manufacturers'},
            yaxis={'title': 'Mean MPG', 'range': [5, 45]},
            margin={'l': 60, 'b': 80, 't': 10, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode = 'closest',
            transition = {'duration': 500},
        )
    }

#click/hover
@app.callback(
    Output('hover-data', 'figure'),
    [Input('graph-with-slider2', 'hoverData')])
def display_hover_data(hoverData):
    if hoverData:
        cc = hoverData['points'][0]
        target = cc['x']
        filtered_cars_year = cars_years[cars_years['manufacturer'] == target]
        traces23 = []
        traces23.append(dict(
            x=filtered_cars_year['model year'],
            y=filtered_cars_year['mean_mpg'],
            # text=df_by_country2['manufacturer']+ ' ',
            mode='lines+markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name='To mouni tis mana sou',
        ))

    return {
        'data': traces23,
        'layout': dict(
            xaxis={'type': 'Linear', 'title': 'Years'},
            yaxis={'title': 'Mean MPG Manufacturer', 'range': [5, 45]},
            margin={'l': 60, 'b': 80, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            clickmode = 'event+select',
            transition = {'duration': 500},
        )
    }
#second visualizations callbacks end


if __name__ == '__main__':
    app.run_server(debug=True)