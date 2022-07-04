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
        height=700,
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
        height=700,
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
