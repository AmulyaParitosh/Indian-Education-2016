import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data/data.csv")
df.fillna(0)
gdf = df.groupby("STATNAME")

sdf = pd.read_csv("data/2015_16_Statewise_Secondary.csv")
sdf.fillna(0)
sdf["urban_pop"] = sdf[["tot_population", "urban_population"]].apply(
    lambda x: x[1] * x[0] / 100, axis=1
)
sdf["rural_pop"] = sdf[["tot_population", "urban_pop"]].apply(
    lambda x: x[0] - x[1], axis=1
)

app = Dash(__name__)

colors = {"background": "#111111", "text": "#7FDBFF"}

fig1 = go.Bar(
    name="tot",
    x=sdf.sort_values("tot_population")["statname"],
    y=sdf.sort_values("tot_population")["rural_pop"],
)

fig2 = go.Bar(
    name="urban",
    x=sdf.sort_values("tot_population")["statname"],
    y=sdf.sort_values("tot_population")["urban_pop"],
)

pop_fig = go.Figure(data=[fig1, fig2])
pop_fig.update_layout(
    barmode="stack",
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)

app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="item item1",
            children=[
                html.H1(children="Indian Eduacation - 2015-16",),
                html.Div(
                    children="Analysis of Eduacation of India in the year of 2015 - 2016"
                ),
            ],
        ),
        html.Div(
            className="item", children=[polulation_graph := dcc.Graph(figure=pop_fig)],
        ),
        html.Div(
            className="item",
            children=[
                litracy_graph := dcc.Graph(),
                html.Label("Minimum Felame Literacy Rate"),
                litracy_graph_slider := dcc.Slider(
                    min=0, max=100, marks={i: str(i) for i in range(100)}, value=0,
                ),
            ],
        ),
        html.Div(className="item item4"),
        html.Div(
            className="item",
            children=[
                html.Label("State"),
                state_name := dcc.Dropdown(sorted(gdf.groups.keys()), "Bihar"),
                html.Label("District"),
                district_name := dcc.Dropdown(),
            ],
        ),
        html.Div(
            className="item", children=[district_growth_rate_graph := dcc.Graph()],
        ),
    ],
    style={"backgroundColor": colors["background"], "color": colors["text"]},
)


@app.callback(Output(litracy_graph, "figure"), Input(litracy_graph_slider, "value"))
def lit_fig_callback(min_lit_rate):
    data = sdf.loc[sdf["female_literacy_rate"] > min_lit_rate].sort_values(
        "literacy_rate"
    )

    fig = px.scatter(
        data,
        x="male_literacy_rate",
        y="female_literacy_rate",
        size="tot_population",
        color="literacy_rate",
        hover_name="statname",
        log_x=True,
        size_max=90,
        title="Literacy Rate and Population",
        labels={
            "female_literacy_rate": "Felame Literacy Rate",
            "male_literacy_rate": "Male Literacy Rate",
            "literacy_rate": "Literacy Rate",
            "tot_population": "Total Population",
        },
    )

    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


@app.callback(Output(district_growth_rate_graph, "figure"), Input(state_name, "value"))
def dist_gr_callback(state_name):
    data = gdf.get_group(state_name).sort_values("GROWTHRATE")

    fig = px.bar(
        data,
        x="DISTNAME",
        y="GROWTHRATE",
        hover_name="DISTNAME",
        color="OVERALL_LI",
        title="Groth Rate of Districts",
        labels={
            "DISTNAME": "District Name",
            "GROWTHRATE": "Growth Rate",
            "OVERALL_LI": "Literacy Rate",
        },
    )

    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig


@app.callback(
    Output(district_name, "options"),
    Output(district_name, "value"),
    Input(state_name, "value"),
)
def get_dist_name(selected_state):
    data = gdf.get_group(selected_state)["DISTNAME"].unique()
    return data, data[0]


app.run_server(debug=True)
