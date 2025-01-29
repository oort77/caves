import folium
from branca.element import Element


# Function to parse periods from a cave's period string
def parse_periods(period_string):
    periods = []
    if "Lower Paleolithic" in period_string:
        periods.append("Lower Paleolithic")
    if "Middle Paleolithic" in period_string:
        periods.append("Middle Paleolithic")
    if "Upper Paleolithic" in period_string:
        periods.append("Upper Paleolithic")
    if "Natufian culture" in period_string:
        periods.append("Natufian culture")
    return periods


caves = [
    {
        "name": "Nahal Me'arot",
        "lat": 32.670,
        "lon": 35.010,
        "period": "Lower Paleolithic (500,000 BP), Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Nahal_Me%27arot_Nature_Reserve"
    },
    {
        "name": "Tabun Cave",
        "lat": 32.667,
        "lon": 35.017,
        "period": "Lower Paleolithic (500,000 BP), Middle Paleolithic (250,000-45,000 BP)",
         "wiki_url": "https://en.wikipedia.org/wiki/Tabun_Cave"
    },
    {
        "name": "Skhul Cave",
        "lat": 32.669,
        "lon": 35.013,
        "period": "Middle Paleolithic (250,000-45,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Skhul_and_Qafzeh_hominins"
    },
    {
        "name": "El-Wad Cave",
        "lat": 32.672,
        "lon": 35.015,
        "period": "Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)",
        "wiki_url":"https://en.wikipedia.org/wiki/Nahal_Me%27arot_Nature_Reserve#El_Wad_Cave"
    },
    {
        "name": "Misliya Cave",
        "lat": 32.666,
        "lon": 35.017,
        "period": "Lower Paleolithic (250,000-160,000 BP)",
         "wiki_url": "https://en.wikipedia.org/wiki/Misliya_cave"
    },
    {
        "name": "Qafzeh Cave",
        "lat": 32.694,
        "lon": 35.362,
        "period": "Middle Paleolithic (100,000-90,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Skhul_and_Qafzeh_hominins"
    },
   {
        "name": "Kebara Cave",
        "lat": 32.596,
        "lon": 34.959,
        "period": "Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Kebara_Cave"
    },
    {
        "name": "Manot Cave",
        "lat": 32.987,
        "lon": 35.268,
        "period": "Upper Paleolithic (40,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Manot_Cave"
    },
    {
        "name": "Amud Cave",
        "lat": 32.952,
        "lon": 35.511,
        "period": "Middle Paleolithic (250,000-45,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Amud_Cave"
    },
    {
        "name": "Zuttiyeh Cave",
        "lat": 33.016,
        "lon": 35.573,
        "period": "Middle Paleolithic (150,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Zuttiyeh_cave"
    },
   {
        "name": "Hayonim Cave",
        "lat": 33.023,
        "lon": 35.389,
        "period": "Middle Paleolithic (250,000-45,000 BP), Natufian culture (15,000 - 11,500 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Hayonim_Cave"
    },
    {
        "name": "Hilazon Tachtit Cave",
        "lat": 32.919,
        "lon": 35.281,
        "period": "Natufian culture (15,000 - 11,500 BP)",
         "wiki_url": "https://en.wikipedia.org/wiki/Hilazon_Tachtit"
    },
    {
        "name": "Raqefet Cave",
        "lat": 32.700,
        "lon": 35.050,
        "period": "Natufian culture (15,000 - 11,500 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Raqefet_Cave"
    },
    {
        "name": "Sefunim Cave",
        "lat": 32.728,
        "lon": 34.966,
        "period": "Upper Paleolithic (40,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Sefunim_Cave"
    },
    {
        "name": "Meged Cave",
        "lat": 32.625,
        "lon": 35.066,
        "period": "Upper Paleolithic (30,000 BP)",
         "wiki_url": "https://en.wikipedia.org/wiki/Meged_Cave"
     },
    {
        "name": "Jamila Cave",
        "lat": 32.724,
        "lon": 35.062,
        "period": "Upper Paleolithic (25,000 BP)",
         "wiki_url": "https://en.wikipedia.org/wiki/Jamila_Cave"
    },
    {
        "name": "Hefzibah Cave",
        "lat": 32.610,
        "lon": 35.094,
        "period": "Middle Paleolithic (250,000-45,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Hefzibah_Cave"
    },
   {
        "name": "Carmel Cave",
        "lat": 32.718,
        "lon": 34.967,
        "period": "Upper Paleolithic (30,000 BP)",
       "wiki_url": "https://en.wikipedia.org/wiki/Carmel_Cave"
    },
    {
        "name": "Malham Cave",
        "lat": 32.715,
        "lon": 35.007,
        "period": "Middle Paleolithic (250,000-45,000 BP)",
         "wiki_url": "https://en.wikipedia.org/wiki/Malham_Cave"
   },
    {
        "name": "Es Skhul Cave",
        "lat": 32.670,
        "lon": 35.012,
        "period": "Middle Paleolithic (250,000-45,000 BP)",
        "wiki_url": "https://en.wikipedia.org/wiki/Skhul_and_Qafzeh_hominins"
    },
        {
        "name": "Geula Cave",
        "lat": 32.794,
        "lon": 34.989,
        "period": "Middle Paleolithic (250,000-45,000 BP)",
         "wiki_url":"https://en.wikipedia.org/wiki/Nahal_Me%27arot_Nature_Reserve#Other_caves"
    }
]


def get_popup_text(cave):
    return f"""
    {cave['name']}<br>
    Period: {cave['period']}<br>
    <a href="{cave['wiki_url']}" target="_blank">Information</a>
    """

# Create a map centered on Northern Israel
map_center_lat = sum(cave['lat'] for cave in caves) / len(caves)
map_center_lon = sum(cave['lon'] for cave in caves) / len(caves)
m = folium.Map(location=[map_center_lat, map_center_lon], zoom_start=10)

# Create feature groups for each period
all_caves = folium.FeatureGroup(name="All Caves", show=True)
lower_paleolithic = folium.FeatureGroup(name="Lower Paleolithic", show=False)
middle_paleolithic = folium.FeatureGroup(name="Middle Paleolithic", show=False)
upper_paleolithic = folium.FeatureGroup(name="Upper Paleolithic", show=False)
natufian = folium.FeatureGroup(name="Natufian culture", show=False)

# Add markers for each cave
for cave in caves:
    popup_text = get_popup_text(cave)
    marker = folium.Marker(
        location=[cave['lat'], cave['lon']],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=cave['name']
    )
    
    # Add to all caves layer
    marker.add_to(all_caves)
    
    # Add to specific period layers
    cave_periods = parse_periods(cave['period'])
    for period in cave_periods:
        if period == "Lower Paleolithic":
            folium.Marker(
                location=[cave['lat'], cave['lon']],
                popup=folium.Popup(popup_text, max_width=300),
                tooltip=cave['name']
            ).add_to(lower_paleolithic)
        elif period == "Middle Paleolithic":
            folium.Marker(
                location=[cave['lat'], cave['lon']],
                popup=folium.Popup(popup_text, max_width=300),
                tooltip=cave['name']
            ).add_to(middle_paleolithic)
        elif period == "Upper Paleolithic":
            folium.Marker(
                location=[cave['lat'], cave['lon']],
                popup=folium.Popup(popup_text, max_width=300),
                tooltip=cave['name']
            ).add_to(upper_paleolithic)
        elif period == "Natufian culture":
            folium.Marker(
                location=[cave['lat'], cave['lon']],
                popup=folium.Popup(popup_text, max_width=300),
                tooltip=cave['name']
            ).add_to(natufian)

# Add layer groups to the map
all_caves.add_to(m)
lower_paleolithic.add_to(m)
middle_paleolithic.add_to(m)
upper_paleolithic.add_to(m)
natufian.add_to(m)

# Add layer control with overlays configuration
folium.LayerControl(
    position='bottomright',
    collapsed=False,
    overlays={
        "All Caves": all_caves,
        "Lower Paleolithic": lower_paleolithic,
        "Middle Paleolithic": middle_paleolithic,
        "Upper Paleolithic": upper_paleolithic,
        "Natufian culture": natufian
    }
).add_to(m)

title_html = '''
    <div style="
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500&display=swap');
        position: absolute;
        top: 50px;
        left: 100px;
        z-index: 1000;
        font-family: 'Cinzel';
        font-style: normal;
        font-weight: 500; /* Or 700 if you want bold */
        color: #2e6c97; /* #000080 */
        font-size: 40px;
        background-color: transparent;
        padding: 5px;
    ">
        Paleolithic caves in Northern Israel
    </div>
'''
m.get_root().html.add_child(Element(title_html))

# Fit map to bounds with margin
coords = [(cave['lat'], cave['lon']) for cave in caves]
m.fit_bounds(coords, padding=(0.20,0.20))

# Save the map
m.save('index.html')

# Display the map
m
