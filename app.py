import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the processed data
data = pd.read_csv("processed_data.csv")

# Convert the date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Create the Dash app
app = dash.Dash(__name__)

# Create a line chart
fig = px.line(
    data,
    x='date',
    y='Sales',
    color='region',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'Sales': 'Total Sales ($)', 'region': 'Region'},
)

# Define the app layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),
    html.P(
        "This visualizer shows sales data for Pink Morsels, allowing us to determine whether sales were higher before or after the price increase on January 15, 2021.",
        style={'textAlign': 'center'}
    ),
    dcc.Graph(figure=fig),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
