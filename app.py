import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the processed data
data = pd.read_csv("processed_data.csv")

# Convert the date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualizer"

# Define the app layout
app.layout = html.Div([
    # Header
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center', 'color': '#4CAF50'}),
    
    # Description
    html.P(
        "Use the radio buttons below to filter sales data by region. Analyze trends to determine whether sales were higher before or after the price increase on January 15, 2021.",
        style={'textAlign': 'center', 'color': '#555', 'fontSize': '18px'}
    ),
    
    # Radio buttons for region selection
    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'fontSize': '16px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'margin': '10px'}
        ),
    ], style={'textAlign': 'center', 'margin': '20px'}),
    
    # Line chart
    dcc.Graph(id='sales-chart'),

    # Footer
    html.Footer(
        "Soul Foods Sales Analysis © 2024",
        style={'textAlign': 'center', 'marginTop': '30px', 'color': '#888'}
    )
], style={'fontFamily': 'Arial, sans-serif', 'margin': '20px'})

# Callback to update the chart based on the selected region
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'] == selected_region]
    
    # Create the line chart
    fig = px.line(
        filtered_data,
        x='date',
        y='Sales',
        color='region',
        title=f"Pink Morsel Sales ({selected_region.capitalize()})",
        labels={'date': 'Date', 'Sales': 'Total Sales ($)', 'region': 'Region'},
    )
    fig.update_layout(
        title={'x': 0.5, 'xanchor': 'center'},
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#ffffff',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True),
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
