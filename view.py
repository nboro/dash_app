import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from generate_table import generate_table

cars = pd.read_csv('cars_processed.csv')
cars_years = pd.read_csv('years_manufacturers.csv')

layout = html.Div(children=[

    html.H4(children='Nemania Borovits, 2032374: HW3 Implementation Interactive visualization - 01/04/2020', style={
        'text-align':'center'
    }),

    html.Div(children=[
        html.H4(children='Auto+MPG Data Set')        
    ]
    ,style = {
        'text-align':'center',
        'text-decoration':'underline'}),
        
    html.Div(children=[
        generate_table(cars)       
    ],style = {
        'text-align':'center'}),

    html.Div(children=[
        html.Hr(style={'border-top': '7px dotted black',
        'width':'65%'})
    ]),

    #visualizations

    #first visualization
    html.Div(children=[
            html.H4(children='MPG and vehicle weight filtered by year and country')        
        ],style = {'text-align':'center','text-decoration':'underline'}),

    html.Div(children=[

        html.Div(children=[
            dcc.Graph(id='graph-with-slider')
        ],style={'width':'1080px'}),        
        
        html.Div(children=[
            dcc.Slider(
                id='year-slider',
                min=cars['model year'].min(),
                max=cars['model year'].max(),
                value=cars['model year'].min(),
                marks={str(year): str(year) for year in cars['model year'].unique()},
                step=None,
                vertical = True
            )
        ]),

        html.Div(children=[
            html.P(children='Car model year',style={'width':'75%','margin-left':'5px','text-align':'center'})])

        ],style = {'display':'flex','align-items':'center','justify-content':'center'}),

        html.Div(children=[
            html.Hr(style={'border-top': '7px dotted black',
        'width':'65%'})
        ]),

        #first visualization end
        #second visualization 

        html.Div(children=[
            html.H4(children='Mean MPG per year and per manufacturer')        
        ]
        ,style = {
            'text-align':'center',
            'text-decoration':'underline'}),

        html.Div(children=[

            html.Div(children=[
                dcc.Graph(id='graph-with-slider2')
            ],style={'width':'60%'}),        
        

            # html.Pre(id='hover-data'),
            html.Div([
                dcc.Graph(id='hover-data'),
            ], style={'width': '40%'}),

        ],style = {'display':'flex','align-items':'center','justify-content':'center'}),

        html.Div(children=[

            html.Div(children=[
                html.P(children='Car model year',style={'width':'75%','margin-left':'5px','text-align':'center'})]),

            html.Div(children=[
                dcc.Slider(
                    id='year-slider2',
                    min=cars_years['model year'].min(),
                    max=cars_years['model year'].max(),
                    value=cars_years['model year'].min(),
                    marks={str(year): str(year) for year in cars_years['model year'].unique()},
                    step=None,
                    vertical = False
                )
            ],style = {'width':'700px'}),

        ],style = {'display':'flex','align-items':'center','justify-content':'center','float':'left','margin-bottom':'90px'}),        

        #second visualization end
])