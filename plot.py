import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data/cleaned_dataset.csv")

fig = go.Figure(go.Scatter(x=df['USERNAMES'], y=df['FOLLOWERS'],
                           name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time (2014)',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True)

fig.show()
