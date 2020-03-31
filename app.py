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
server = app.server
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
            text=df_by_country['car name'],
            # customdata = df_by_country['year'],
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


@app.callback(
    Output('graph-with-selection', 'figure'),
    [Input('graph-with-slider', 'selectedData'),
    Input('year-slider', 'value')])
def update_selection_figure(selectedData,selected_year):
    
    selection_traces = []
    point_list = selectedData['points']
    for point in point_list:

        filt_df = cars[(cars['car name'] == point['text']) & (cars['model year'] == selected_year) 
        & (cars['weight'] == point['x']) & (cars['mpg'] == point['y'])]
        acc = str(filt_df.iloc[0]['acceleration'])
        selection_traces.append(dict(
            x=filt_df['car name'],
            y=filt_df['acceleration'],
            text='The acceleration for '+ filt_df['car name']+ ' is ' + acc,
            type='bar',
            opacity=0.7,
            width = 0.2,
            # marker={
            #     'size': 5,
            #     'line': {'width': 0.5, 'color': 'white'}
            # },
            name= filt_df.iloc[0]['car name'],
        ))

    return {
        'data': selection_traces,
        'layout': dict(
            title = 'Acceleration for the selected cars',
            xaxis={'type': 'Linear', 'title': 'Car Name','rotate':'90'},
            yaxis={'title': 'Acceleration', 'range': [5, 30]},
            margin={'l': 60, 'b': 100, 't': 50, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
            barmode='group',
            bargap=0.15, # gap between bars of adjacent location coordinates.
            bargroupgap=0.1 # gap between bars of the same location coordinate.
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
            yaxis={'title': 'Average MPG', 'range': [5, 45]},
            margin={'l': 60, 'b': 80, 't': 10, 'r': 10},
            legend={'x': 1, 'y': 1},
            hovermode = 'closest',
            transition = {'duration': 500},
        )
    }


#click/hover
@app.callback(
    Output('hover-data', 'figure'),
    [Input('graph-with-slider2', 'clickData')])
def display_hover_data(clickData):
    if clickData:
        cc = clickData['points'][0]
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
        ))
        title = 'The average MPG for every year for manufacturer: '+'<b><i>{}</i></b>'.format(target)

    return {
        'data': traces23,
        'layout': dict(
            xaxis={'type': 'Linear', 'title': 'Years'},
            yaxis={'title': 'Average MPG Manufacturer', 'range': [5, 45]},
            margin={'l': 60, 'b': 80, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            clickmode = 'event+select',
            transition = {'duration': 500},
            annotations = [{'x': 0.1, 'y': 0.98, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text':title}]
        )
    }
#second visualizations callbacks end


if __name__ == '__main__':
    app.run_server(debug=False, port=80)