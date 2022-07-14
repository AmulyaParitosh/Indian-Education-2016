import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data/2015_16_Statewise_Secondary.csv")
df.fillna(0)
df['urban_pop'] = df[['tot_population',
                      'urban_population']].apply(lambda x: x[1] * x[0] / 100,
                                                 axis=1)
df['rural_pop'] = df[['tot_population',
                      'urban_pop']].apply(lambda x: x[0] - x[1], axis=1)
app = Dash(__name__)

colors = {'background': '#111111', 'text': '#7FDBFF'}

fig1 = go.Bar(name="tot",
              x=df.sort_values('tot_population')['statname'],
              y=df.sort_values('tot_population')['rural_pop'])

fig2 = go.Bar(name="urban",
              x=df.sort_values('tot_population')['statname'],
              y=df.sort_values('tot_population')['urban_pop'])

pop_fig = go.Figure(data=[fig1, fig2])
pop_fig.update_layout(barmode='stack',
                      plot_bgcolor=colors['background'],
                      paper_bgcolor=colors['background'],
                      font_color=colors['text'])

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
                          html.H1(children='Indian Eduacation - 2015-16'),
                          html.Div(children='''
        Analysis of Eduacation of India in the year of 2015 - 2016
    '''),
                          dcc.Graph(id='polulation-graph', figure=pop_fig),
                          dcc.Graph(id='litracy-graph'),
                          html.Label('Minimum Felame Literacy Rate'),
                          dcc.Slider(
                              id="litracy-graph-slider",
                              min=0,
                              max=100,
                              marks={i: str(i)
                                     for i in range(100)},
                              value=0,
                          )
                      ])


@app.callback(Output('litracy-graph', 'figure'),
              Input('litracy-graph-slider', 'value'))
def lit_fig_callback(min_lit_rate):
    data = df.loc[df["female_literacy_rate"] > min_lit_rate].sort_values(
        "literacy_rate")

    fig = px.scatter(data,
                     x="male_literacy_rate",
                     y="female_literacy_rate",
                     size='tot_population',
                     color="literacy_rate",
                     hover_name="statname",
                     log_x=True,
                     size_max=90,
                     title="Literacy Rate and Population",
                     labels={
                         "female_literacy_rate": "Felame Literacy Rate",
                         "male_literacy_rate": "Male Literacy Rate",
                         "literacy_rate": "Literacy Rate",
                         "tot_population": "Total Population"
                     })

    fig.update_layout(plot_bgcolor=colors['background'],
                      paper_bgcolor=colors['background'],
                      font_color=colors['text'])

    return fig


app.run_server(debug=True)