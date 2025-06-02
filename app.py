import dash
from dash import html, dcc, Output, Input
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('covid_19_india.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Layout with title, dropdown, and graph
app.layout = html.Div([
    html.H1("COVID-19 India Dashboard", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in df['State/UnionTerritory'].unique()],
        placeholder="Select a State",
        style={'width': '50%', 'margin': 'auto'}
    ),
    
    dcc.Graph(id='covid-graph')
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('covid-graph', 'figure'),
    Input('state-dropdown', 'value')
)
def update_graph(selected_state):
    if selected_state:
        filtered_df = df[df['State/UnionTerritory'] == selected_state]
    else:
        filtered_df = df
    
    fig = px.line(
        filtered_df,
        x='Date',
        y='Confirmed',
        title=f'Confirmed COVID-19 Cases in {selected_state if selected_state else "India"}',
        labels={'Confirmed': 'Confirmed Cases', 'Date': 'Date'}
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
