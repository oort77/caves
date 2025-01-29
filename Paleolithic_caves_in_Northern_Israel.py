import marimo

__generated_with = "0.10.18-dev12"
app = marimo.App(
    width="medium",
    app_title="Paleolithic caves in Northern Israel",
)


@app.cell
def _():
    import marimo as mo
    import folium
    from folium import plugins
    return folium, mo, plugins


@app.cell
def _(mo):
    mo.md(r"""**Paleolithic caves in Northern Israel**""")
    return


@app.cell
def _():
    # Data
    caves = [
        {"name": "Nahal Me'arot", "lat": 32.670, "lon": 35.010, "period": "Lower Paleolithic (500,000 BP), Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)"},
        {"name": "Tabun Cave", "lat": 32.667, "lon": 35.017, "period": "Lower Paleolithic (500,000 BP), Middle Paleolithic (250,000-45,000 BP)"},
        {"name": "Skhul Cave", "lat": 32.669, "lon": 35.013, "period": "Middle Paleolithic (250,000-45,000 BP)"},
        {"name": "El-Wad Cave", "lat": 32.672, "lon": 35.015, "period": "Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)"},
        {"name": "Misliya Cave", "lat": 32.666, "lon": 35.017, "period": "Lower Paleolithic (250,000-160,000 BP)"},
        {"name": "Qafzeh Cave", "lat": 32.694, "lon": 35.362, "period": "Middle Paleolithic (100,000-90,000 BP)"},
        {"name": "Kebara Cave", "lat": 32.596, "lon": 34.959, "period": "Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)"},
        {"name": "Manot Cave", "lat": 32.987, "lon": 35.268, "period": "Upper Paleolithic (40,000 BP)"},
        {"name": "Amud Cave", "lat": 32.952, "lon": 35.511, "period": "Middle Paleolithic (250,000-45,000 BP)"},
        {"name": "Zuttiyeh Cave", "lat": 33.016, "lon": 35.573, "period": "Middle Paleolithic (150,000 BP)"},
        {"name": "Hayonim Cave", "lat": 33.023, "lon": 35.389, "period": "Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)"},
        {"name": "Hilazon Tachtit Cave", "lat": 32.919, "lon": 35.281, "period": "Natufian culture (15,000 - 11,500 BP)"},
        {"name": "Raqefet Cave", "lat": 32.700, "lon": 35.050, "period": "Natufian culture (15,000 - 11,500 BP)"},
        {"name": "Sefunim Cave", "lat": 32.728, "lon": 34.966, "period": "Upper Paleolithic (40,000 BP)"},
        {"name": "Meged Cave", "lat": 32.625, "lon": 35.066, "period": "Upper Paleolithic (30,000 BP)"},
        {"name": "Jamila Cave", "lat": 32.724, "lon": 35.062, "period": "Upper Paleolithic (25,000 BP)"},
        {"name": "Hefzibah Cave", "lat": 32.610, "lon": 35.094, "period": "Middle Paleolithic (250,000-45,000 BP)"},
        {"name": "Carmel Cave", "lat": 32.718, "lon": 34.967, "period": "Upper Paleolithic (30,000 BP)"},
        {"name": "Malham Cave", "lat": 32.715, "lon": 35.007, "period": "Middle Paleolithic (250,000-45,000 BP)"},
        {"name": "Es Skhul Cave", "lat": 32.670, "lon": 35.012, "period": "Middle Paleolithic (250,000-45,000 BP)"},
        {"name": "Geula Cave", "lat": 32.794, "lon": 34.989, "period": "Middle Paleolithic (250,000-45,000 BP)"}
    ]
    return (caves,)


@app.cell
def _(caves, folium):
    # Create a map centered on Northern Israel
    map_center_lat = sum(cave['lat'] for cave in caves) / len(caves)
    map_center_lon = sum(cave['lon'] for cave in caves) / len(caves)
    m = folium.Map(location=[map_center_lat, map_center_lon], zoom_start=10)
    return m, map_center_lat, map_center_lon


@app.cell
def _(caves, folium, m):
    # Add markers for each cave
    for cave in caves:
        popup_text = f"{cave['name']}<br>Period: {cave['period']}"
        folium.Marker(
            location=[cave['lat'], cave['lon']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=cave['name']
        ).add_to(m)
    return cave, popup_text


@app.cell
def _(caves, m):
    # Fit map to bounds with margin
    coords = [(cave['lat'], cave['lon']) for cave in caves]
    m.fit_bounds(coords, padding=(0.20,0.20))
    return (coords,)


@app.cell
def _(m):
    # Display the map in Colab
    m
    return


@app.cell
def _(m):
    # import folium
    from IPython.display import HTML

    # m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
    HTML(m._repr_html_())
    return (HTML,)


@app.cell
def _():
    # m.save('map.html')
    return


if __name__ == "__main__":
    app.run()
