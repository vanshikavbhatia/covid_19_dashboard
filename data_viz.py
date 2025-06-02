import pandas as pd
import plotly.express as px

# Load dataset with the correct filename
df = pd.read_csv('data/covid_19_india.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate confirmed cases by date for all states combined
daily_cases = df.groupby('Date')['Confirmed'].sum().reset_index()

# Plot line chart of confirmed cases over time
fig = px.line(daily_cases, x='Date', y='Confirmed', title='Total COVID-19 Confirmed Cases in India Over Time')

fig.show()
