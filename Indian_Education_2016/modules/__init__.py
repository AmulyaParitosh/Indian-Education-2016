import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import json
import plotly.express as px


state_df = pd.read_csv("data/2015_16_Statewise_Secondary.csv")

dist_df = pd.read_csv("data/data.csv")
g_dist_df = dist_df.groupby("STATNAME")

state_names = list(g_dist_df.groups.keys())
variables = {
    "Area": ["AREA_SQKM", "area_sqkm"],
    "Total Population": ["TOTPOPULAT", "tot_population"],
    "Urban Population": ["P_URB_POP", "urban_population"],
    "Growth Rate": ["GROWTHRATE", "grwoth_rate"],
    "Sex Ratio": ["SEXRATIO", "sexratio"],
    "Literacy Rate": ["OVERALL_LI", "literacy_rate"],
    "Literacy Rate Ratio": ["literacy_rate_ratio", "literacy_rate_ratio"],
    "No. of Schools": ["SCHTOT", "schools"],
}

with open("data/india_states.geojson", "r") as fp:
    state_wise_india = json.load(fp)

with open("data/district_geodata.json", "r") as fp:
    district_wise_india = json.loads(fp.read())

loc = pd.read_csv("data/lat_lng.csv")
loc.set_index("statname", inplace=True)

colors = {"background": "#111111", "text": "#7FDBFF", "bg_highlight": "#262626"}

all_vars = dist_df.iloc[:, 3:].columns.to_list()
