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
                        html.H2("Details"),
                        dist_name := dcc.Dropdown(clearable=False),
                    ],
                ),
                html.Div(
                    className="item7",
                    children=[
                        html.Div(className="tbl tbl-1", children=["India"]),
                        html.Div(
                            className="tbl title", children=["Total Population (cr)"]
                        ),
                        html.Div(className="tbl", children=["132.45"]),
                        html.Div(
                            className="tbl title", children=["Total Area (million km²)"]
                        ),
                        html.Div(className="tbl", children=["3.287 "]),
                        html.Div(className="tbl title", children=["No. of States"]),
                        html.Div(className="tbl", children=["36"]),
                        html.Div(className="tbl title", children=["Literacy Rate"]),
                        html.Div(className="tbl", children=["78.30"]),
                        html.Div(className="tbl title", children=["Growth Rate"]),
                        html.Div(className="tbl", children=["19.99"]),
                        html.Div(className="tbl title", children=["Sex Ratio"]),
                        html.Div(className="tbl", children=["930"]),
                        html.Div(
                            className="tbl tbl-2",
                            id="table_state_name",
                            children=["Bihar"],
                        ),
                        html.Div(
                            className="tbl title", children=["Total Population (cr)"],
                        ),
                        html.Div(className="tbl", id="00"),
                        html.Div(
                            className="tbl title", children=["Total Area million km²"]
                        ),
                        html.Div(className="tbl", id="01"),
                        html.Div(className="tbl title", children=["No. of Districts"]),
                        html.Div(className="tbl", id="02"),
                        html.Div(className="tbl title", children=["Literacy Rate"]),
                        html.Div(className="tbl", id="03"),
                        html.Div(className="tbl title", children=["Growth Rate"]),
                        html.Div(className="tbl", id="04"),
                        html.Div(className="tbl title", children=["Sex Ratio"]),
                        html.Div(className="tbl", id="05"),
                        html.Div(
                            className=" tbl tbl-3 ",
                            id="table-dist-name",
                            children=["Paschim Champaran"],
                        ),
                        html.Div(
                            className="tbl title", children=["Total Population (cr)"],
                        ),
                        html.Div(className="tbl", id="06"),
                        html.Div(
                            className="tbl title", children=["Total Area (million km²)"]
                        ),
                        html.Div(className="tbl", id="07"),
                        html.Div(className="tbl title", children=["No. of Blocks"]),
                        html.Div(className="tbl", id="08"),
                        html.Div(className="tbl title", children=["No. of Villages"]),
                        html.Div(className="tbl", id="09"),
                        html.Div(className="tbl title", children=["No. of Clusters"]),
                        html.Div(className="tbl", id="10"),
                        html.Div(className="tbl title", children=["Literacy Rate"]),
                        html.Div(className="tbl", id="11"),
                        html.Div(className="tbl title", children=["Growth Rate"]),
                        html.Div(className="tbl", id="12"),
                        html.Div(className="tbl title", children=["Sex Ratio"]),
                        html.Div(className="tbl", id="13"),
                    ],
                ),
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
            className="item8",
            children=[
                html.Div(
                    className="item details",
                    children=[
                        html.H4("X-axis"),
                        detail_var_1 := dcc.Dropdown(
                            all_vars, all_vars[0], clearable=False
                        ),
                    ],
                ),
                html.Div(
                    className="item details",
                    children=[
                        html.H4("Y-axis"),
                        detail_var_2 := dcc.Dropdown(
                            all_vars, all_vars[1], clearable=False
                        ),
                    ],
                ),
                html.Div(
                    className="item details",
                    children=[
                        html.H4("Size"),
                        detail_var_3 := dcc.Dropdown(
                            all_vars, all_vars[2], clearable=False
                        ),
                    ],
                ),
                html.Div(
                    className="item details",
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
    Output("table_state_name", "children"),
    Output("00", "children"),
    Output("01", "children"),
    Output("02", "children"),
    Output("03", "children"),
    Output("04", "children"),
    Output("05", "children"),
    Input(state_name, "value"),
)
def get_dist_name(selected_state):
    data = g_dist_df.get_group(selected_state)["DISTNAME"].unique()
    pop = (
        state_df["tot_population"].loc[state_df["statname"] == selected_state].item()
        / 10000
    ).__ceil__()
    area = state_df["area_sqkm"].loc[state_df["statname"] == selected_state].item()
    num_dict = g_dist_df.get_group(selected_state)["DISTRICTS"].sum()
    lit_r = state_df["literacy_rate"].loc[state_df["statname"] == selected_state].item()
    gr_r = state_df["grwoth_rate"].loc[state_df["statname"] == selected_state].item()
    sx_r = state_df["sexratio"].loc[state_df["statname"] == selected_state].item()

    return data, data[0], selected_state, pop, area, num_dict, lit_r, gr_r, sx_r


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


@app.callback(
    Output("table-dist-name", "children"),
    Output("06", "children"),
    Output("07", "children"),
    Output("08", "children"),
    Output("09", "children"),
    Output("10", "children"),
    Output("11", "children"),
    Output("12", "children"),
    Output("13", "children"),
    Input(dist_name, "value"),
)
def output_dist_name(name):
    pop = (
        dist_df.loc[dist_df["DISTNAME"] == name]["TOTPOPULAT"].item() / 10000
    ).__ceil__()
    area = dist_df.loc[dist_df["DISTNAME"] == name]["AREA_SQKM"].item()
    blocks = dist_df.loc[dist_df["DISTNAME"] == name]["BLOCKS"].item()
    vill = dist_df.loc[dist_df["DISTNAME"] == name]["VILLAGES"].item()
    clus = dist_df.loc[dist_df["DISTNAME"] == name]["CLUSTERS"].item()
    lit_r = dist_df.loc[dist_df["DISTNAME"] == name]["OVERALL_LI"].item()
    gr_r = dist_df.loc[dist_df["DISTNAME"] == name]["GROWTHRATE"].item()
    sx_r = dist_df.loc[dist_df["DISTNAME"] == name]["SEXRATIO"].item()

    return name, pop, area, blocks, vill, clus, lit_r, gr_r, sx_r


app.run_server(debug=True)
