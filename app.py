import plotly.graph_objects as go
from dash import Dash, html, dcc

import csv

# Initialize dash app
app = Dash(__name__)

# Map information from csv file to our figure.
usernames = []
followers_old = []
followers_now = []

# Map old csv to object

with open('data/2016.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        usernames.append(row[0])
        followers_old.append(row[1])

with open('data/2022.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        followers_now.append(row[1])


fig = go.Figure()
fig.add_trace(go.Bar(x=usernames, y=followers_old, name='2016',
              marker_color='lightsalmon'))
fig.add_trace(go.Bar(x=usernames, y=followers_now, name='2022',
              marker_color='indianred'))

fig.update_layout(
    autotypenumbers='convert types',
    barmode='group',
    xaxis={'categoryorder': 'total ascending'},
    title='Top 25 instagram accounts growth from 2016 to 2022',
    xaxis_title='Usernames',
    yaxis_title='Followers (in millions)',
    legend_title='Year',
    xaxis_tickangle=-50,
)

app.layout = html.Div(children=[
    dcc.Graph(
        id='my-graph',
        figure=fig,
        style={'width': '170vh', 'height': '100vh'}
    )
])
server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
