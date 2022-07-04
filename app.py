from Indian_Education_2016 import *


app = Dash(__name__)


app.layout = html.Div(
    className="container",
    children=[
        html.Div(
            className="item1",
            children=[
                html.H1(children="Indian Eduacation - 2015-16",),
                html.Div(
                    children="Analysis of Eduacation of India in the year of 2015 - 2016"
                ),
            ],
        ),
        html.Div(
            className="item",
            children=[
                html.H2("Variable"),
                var_name := dcc.Dropdown(
                    list(variables.keys()),
                    list(variables.keys())[0],
                    clearable=False,
                    className="dropitem",
                ),
            ],
        ),
        html.Div(
            className="item",
            children=[
                html.H2("State"),
                state_name := dcc.Dropdown(
                    state_names, state_names[4], clearable=False,
                ),
            ],
        ),
        html.Div(
            className="item",
            children=[html.H2("District"), dist_name := dcc.Dropdown(clearable=False),],
        ),
        html.Div(className="item5", children=[map := dcc.Graph()],),
        html.Div(className="item6", children=[details_graph := dcc.Graph()]),
        html.Div(className="item7", children=[]),
    ],
)


@app.callback(
    Output(dist_name, "options"),
    Output(dist_name, "value"),
    Input(state_name, "value"),
)
def get_dist_name(selected_state):
    data = g_dist_df.get_group(selected_state)["DISTNAME"].unique()
    return data, data[0]


@app.callback(
    Output(map, "figure"), Input(var_name, "value"),
)
def display_map(var):
    return get_states_map(state_df, var)


@app.callback(
    Output(details_graph, "figure"),
    Input(state_name, "value"),
    Input(var_name, "value"),
)
def display_map(state_name, var_name):
    return get_dists_map(g_dist_df, state_name, var_name)


app.run_server(debug=True, port=8051)
