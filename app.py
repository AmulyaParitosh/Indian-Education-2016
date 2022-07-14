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
            children=[
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
                html.Div(className="item5", children=[map := dcc.Graph()],),
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    className="item",
                    children=[
                        html.H2("State"),
                        state_name := dcc.Dropdown(
                            state_names, state_names[4], clearable=False,
                        ),
                    ],
                ),
                html.Div(className="item6", children=[details_graph := dcc.Graph()]),
            ]
        ),
        html.Div(
            children=[
                html.Div(
                    className="item",
                    children=[
                        html.H2("District"),
                        dist_name := dcc.Dropdown(clearable=False),
                    ],
                ),
                html.Div(className="item7", children=[]),
            ]
        ),
        html.Div(
            className="item8",
            children=[
                html.Div(
                    className="item",
                    children=[
                        html.H4("x-axis"),
                        detail_var_1 := dcc.Dropdown(
                            all_vars, all_vars[0], clearable=False
                        ),
                    ],
                ),
                html.Div(
                    className="item",
                    children=[
                        html.H4("y-axis"),
                        detail_var_2 := dcc.Dropdown(
                            all_vars, all_vars[1], clearable=False
                        ),
                    ],
                ),
                html.Div(
                    className="item",
                    children=[
                        html.H4("Size"),
                        detail_var_3 := dcc.Dropdown(
                            all_vars, all_vars[2], clearable=False
                        ),
                    ],
                ),
                html.Div(
                    className="item",
                    children=[
                        html.H4("Color"),
                        detail_var_4 := dcc.Dropdown(
                            all_vars, all_vars[3], clearable=False
                        ),
                    ],
                ),
            ],
        ),
        html.Div(className="item9", children=[scat_graph := dcc.Graph()]),
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


@app.callback(
    Output(scat_graph, "figure"),
    Input(state_name, "value"),
    Input(detail_var_1, "value"),
    Input(detail_var_2, "value"),
    Input(detail_var_3, "value"),
    Input(detail_var_4, "value"),
)
def display_map(state, var1, var2, var3, var4):
    return lit_fig_callback(state, var1, var2, var3, var4)


app.run_server(debug=True, port=8051)
