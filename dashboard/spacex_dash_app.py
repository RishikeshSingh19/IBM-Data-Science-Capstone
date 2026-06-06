import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# App
app = dash.Dash(__name__)

# Dropdown options
site_options = [{'label': 'All Sites', 'value': 'ALL'}]

for site in spacex_df['Launch Site'].unique():
    site_options.append({
        'label': site,
        'value': site
    })

# Layout
app.layout = html.Div([

    html.H1(
        'SpaceX Launch Records Dashboard',
        style={
            'textAlign': 'center',
            'color': '#503D36'
        }
    ),

    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder='Select a Launch Site',
        searchable=True
    ),

    html.Br(),

    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.P("Payload range (Kg):"),

    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        value=[min_payload, max_payload],
        marks={
            int(min_payload): str(int(min_payload)),
            int(max_payload): str(int(max_payload))
        }
    ),

    html.Br(),

    dcc.Graph(id='success-payload-scatter-chart')

])

# Pie Chart Callback
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):

    if selected_site == 'ALL':

        success_df = (
            spacex_df[spacex_df['class'] == 1]
            .groupby('Launch Site')
            .size()
            .reset_index(name='Success Count')
        )

        fig = px.pie(
            success_df,
            values='Success Count',
            names='Launch Site',
            title='Total Successful Launches by Site'
        )

    else:

        site_df = spacex_df[
            spacex_df['Launch Site'] == selected_site
        ].copy()

        site_df['Outcome'] = site_df['class'].map({
            1: 'Success',
            0: 'Failure'
        })

        fig = px.pie(
            site_df,
            names='Outcome',
            title=f'Success vs Failure for {selected_site}'
        )

    return fig


# Scatter Plot Callback
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [
        Input('site-dropdown', 'value'),
        Input('payload-slider', 'value')
    ]
)
def update_scatter(selected_site, payload_range):

    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if selected_site == 'ALL':

        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Payload vs Launch Outcome (All Sites)'
        )

    else:

        filtered_df = filtered_df[
            filtered_df['Launch Site'] == selected_site
        ]

        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Payload vs Launch Outcome for {selected_site}'
        )

    return fig


if __name__ == '__main__':
    app.run(debug=True)