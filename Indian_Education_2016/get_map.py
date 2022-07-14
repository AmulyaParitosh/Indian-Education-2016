from Indian_Education_2016.modules import *


def get_states_map(df, var):
    trace = go.Choroplethmapbox(
        geojson=state_wise_india,
        featureidkey="properties.NAME_1",
        locations=df["statname"],
        z=df[variables[var][1]],
        zmin=max(
            df[variables[var][1]].min(),
            df[variables[var][1]].sort_values().to_list()[1],
        ),
        zmax=df[variables[var][1]].max(),
        colorscale="Viridis",
        colorbar=dict(len=0.8, lenmode="fraction", tickfont={"color": colors["text"]}),
    )

    lyt = go.Layout(
        height=680,
        mapbox_style="white-bg",
        mapbox=dict(style="satellite",),
        mapbox_zoom=3.4,
        mapbox_center={"lat": 25.171044, "lon": 81.69784},
    )

    fig = go.FigureWidget(data=[trace], layout=lyt)
    fig.update_layout(paper_bgcolor=colors["bg_highlight"],)

    return fig


def get_dists_map(df, state, var):
    state_dist = [
        dist["properties"]["NAME_2"] for dist in district_wise_india[state]["features"]
    ]

    data = df.get_group(state)

    trace = go.Choroplethmapbox(
        geojson=district_wise_india[state],
        featureidkey="properties.NAME_2",
        locations=state_dist,
        z=data[variables[var][0]],
        zmin=max(
            data[variables[var][0]].min(),
            data[variables[var][0]].sort_values().to_list()[1],
        ),
        zmax=data[variables[var][0]].max(),
        colorscale="viridis",
        colorbar=dict(len=0.8, lenmode="fraction", tickfont={"color": colors["text"]}),
    )

    lyt = go.Layout(
        geo=dict(bgcolor="rgba(0,0,0,0)", lakecolor="#4E5D6C"),
        height=680,
        mapbox_style="white-bg",
        mapbox_zoom=5.5,
        mapbox_center={
            "lat": loc.loc[state, ["lat"]][0],
            "lon": loc.loc[state, ["long"]][0],
        },
    )

    fig = go.FigureWidget(data=[trace], layout=lyt)
    fig.update_layout(paper_bgcolor=colors["bg_highlight"],)

    return fig


def lit_fig_callback(state, var1, var2, var3, var4):
    data = g_dist_df.get_group(state)

    fig = px.scatter(
        data,
        x=str(var1),
        y=str(var2),
        size=str(var3),
        color=str(var4),
        hover_name="DISTNAME",
        log_x=True,
        size_max=90,
        labels={
            "female_literacy_rate": "Felame Literacy Rate",
            "male_literacy_rate": "Male Literacy Rate",
            "literacy_rate": "Literacy Rate",
            "tot_population": "Total Population",
        },
    )

    fig.update_layout(
        plot_bgcolor=colors["bg_highlight"],
        paper_bgcolor=colors["bg_highlight"],
        font_color=colors["text"],
        height=665,
    )

    return fig
