import dash
import dash_core_components as dcc
import dash_html_components as html

def generate_table(dataframe, max_rows=3):
    return html.Div(children= [
        html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns],style={'text-align':'left'})
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ],style={'text-align':'left'}) for i in range(min(len(dataframe), max_rows))
        ])
    ],style={'width':'1080px'})
    ],style={
            'display':'flex',
            'justify-content':'center',
        })