# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import json


# Load data
with open("trimester/trimester_5_kws_topaz-data732--france--fr.sputniknews.africa--20190101--20211231.json", 'r') as fichier:
    data = json.load(fichier)


# Initialize the app - incorporate assets
external_stylesheets = ['./assets/css/style.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)


# App layout
app.layout = html.Div([

    # MAIN TITLE
    html.Div(children='Event in France and world by Quarter (2018-2021)',
             className='main_title'),

    # DROPDOWN CONTAINER
    html.Div(className='container_all_dropdown', children=[

        # CONTAINER TITLE DROPDOWN YEAR
        html.Div(className='container_title_dropdown', children=[
            # TITLE YEAR
            html.P('YEAR :', className='input_title'),

            # DROPDOWN YEAR
            html.Div([
                dcc.Dropdown(['2018', '2019', '2020', '2021'], '2021', id='year_dropdown'),
                html.Div(id='dd_year_output_container')
            ]),
        ]),

        # CONTAINER TITLE DROPDOWN QUARTER
        html.Div(className='container_title_dropdown', children=[
            # TITLE YEAR
            html.P('QUARTER :', className='input_title'),

            # DROPDOWN TRIMESTER
            html.Div([
                dcc.Dropdown(['1', '2', '3', '4'], '2', id='trimester_dropdown'),
                html.Div(id='dd_trimester_output_container')
            ]),
        ]),
    ]),

    # CONTAINER TITLE YEAR TRIMESTER
    html.Div(className='container_title_year_trimester', children=[
        html.H1(className='title_not_bold', children=f'Visualization for: '),

        html.Div(className='sub_container_year_trimester', children=[
            html.H1(className='year_title', id='year_output'),
            html.H1('- QUARTER ', className='separator_title'),
            html.H1(className='trimester_title', id='trimester_output'),
        ]),

    ]),


    # CONTAINER ALL GRAPH
    html.Div(className='container_all_graph', children=[

        # CONTAINER LINK AND P EVENT
        html.Div(className='container_txt_link_event', children=[
            # TXT EVENT
            html.P('Key Event: ', className='txt_event'),

            # LINK EVENT
            html.A(className='link_event', id='link_event'),
        ]),



        # CONTAINER BAR PIE CHART
        html.Div(className='container_bar_pie_chart', children=[
            html.Div(className='', children=[
                dcc.Graph(figure={}, id='kws_hist')
            ]),

            html.Div(className='', children=[
                dcc.Graph(figure={}, id='locs_pieChart')
            ])
        ])
    ])
])


# Add controls to build the interaction
@callback(
    Output(component_id='kws_hist', component_property='figure'),
    Output(component_id='locs_pieChart', component_property='figure'),
    Output(component_id='year_output', component_property='children'),
    Output(component_id='trimester_output', component_property='children'),
    Output(component_id='link_event', component_property='children'),
    Output(component_id='link_event', component_property='href'),
    Input(component_id='year_dropdown', component_property='value'),
    Input(component_id='trimester_dropdown', component_property='value')
)
def update_graph(year_chosen, trimester_chosen):
    # Dict to DataFrame
    kws_df = pd.DataFrame(data[year_chosen][str(int(trimester_chosen)-1)]['kws'].items(), columns=['kw', 'freq'])
    locs_df = pd.DataFrame(data[year_chosen][str(int(trimester_chosen)-1)]['locs'].items(), columns=['loc', 'freq'])

    print(locs_df.to_string())

    # Get Year and Trimester Selected to display it
    year_output = year_chosen
    trimester_output = trimester_chosen

    # LINK TO EVENT
    name_event_output = data[year_chosen][str(int(trimester_chosen)-1)]['event']['title']
    url_event_output = data[year_chosen][str(int(trimester_chosen)-1)]['event']['url']

    # Make Graph
    kws_hist = px.histogram(kws_df, x='kw', y='freq', histfunc='avg')
    locs_pieChart = px.pie(locs_df, values='freq', names='loc', title='Lieux les plus cités')

    return kws_hist, locs_pieChart, year_output, trimester_output, name_event_output, url_event_output


# Run the app
if __name__ == '__main__':
    app.run(debug=True)