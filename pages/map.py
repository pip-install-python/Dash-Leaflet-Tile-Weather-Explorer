import dash
from dash import html, callback_context
import dash_mantine_components as dmc
import dash_leaflet as dl
from dash_iconify import DashIconify
import os
import json
from pathlib import Path

# ****************************************************
# Setup Config
# ****************************************************

# Get Root Directory
root_dir = os.getcwd()
# Current Directory
current_dir = Path(__file__).parent

with open(f'{current_dir}\config.json', 'r') as config_file:
    config = json.load(config_file)
    # Accessing configuration values
    jawg_matrix_access_token = config["jawg-matrix-access-token"]
    thunderforest_api_key = config["thunderforest-api-key"]
    openweathermap_appid = config["openweathermap-appid"]

# Register the page
page = dash.register_page(__name__, path="/")

# ****************************************************
# Setup the theme layer selector
# ****************************************************
# Initialize an empty list to store the image elements
image_elements = []
raw_image_element = []
x = 0
# Loop through all the files in the assets folder
for filename in os.listdir(f"{root_dir}/assets/layers"):
    # Check if the file is an image file
    if filename.endswith(".png"):
        img_element = dmc.Button(
            dmc.Tooltip(
                label=f"{filename}",
                position="top",
                offset=3,
                children=[
                    html.Img(
                        src=dash.get_asset_url(f"layers/{filename}"),
                        style={"width": "150px", "height": "150px"},
                    )
                ],
            ),
            variant="subtle",
            style={"height": "100%", "margin": "5px"},
            id=f"layer_button_{x}",
        )
        # Add the image element to the list
        image_elements.append(img_element)
        raw_image_element.append(f"layers/{filename}")
        x += 1

layer_select = html.Div(
    image_elements,
    style={
        "position": "absolute",
        "bottom": "-180px",
        "left": "60%",
        "transform": "translateX(-50%)",
        "z-index": "4",
        "width": "100%",
    },
)

# ****************************************************
# Setup initial map layers
# ****************************************************
map_list = []
# Base Layer Map
map_list.append(
    dl.TileLayer(
        url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        id="satellite_layer",
    )
)
# Top Layer Map
# map_list.append(dl.TileLayer(id='tilelayer', url="https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}", opacity=0.5))
# Clouds Layer
map_list.append(dl.TileLayer(id="clouds_layer"))
# Find User Location
map_list.append(dl.LocateControl(locateOptions={"enableHighAccuracy": True}))
# Full Screen Control
map_list.append(dl.FullScreenControl())
# Easy Buttons
map_list.append(
    dl.EasyButton(icon="fa fa-globe", title="Theme", id="layer_button"),
)
map_list.append(
    dl.EasyButton(
        icon="fa fa-tint",
        title="Rain Radar",
        id="rain_radar_btn",
    )
)
map_list.append(
    dl.EasyButton(
        icon="fa fa-cloud-download",
        title="Clouds",
        id="cloud_btn",
    )
)
map_list.append(dl.LayerGroup(id="rain_layers"))

# ****************************************************
# Setup the layout
# ****************************************************
layout = html.Div(
    [
        html.Div(
            [
                # Add the layer select div to the layout but hide it to fix "no components with that id exist in the layout" error
                html.Div(layer_select, style={"z-index": "-5", "visibility": "hidden"}),
                html.Div(id="layer_select"),
                html.Div(
                    dl.Map(
                        map_list,
                        style={"width": "80vw", "height": "90vh", "z-index": "0"},
                        center=[27.77, -96.65],
                        zoom=8,
                        id="map1",
                    )
                ),
                html.Div(id="layer_group"),
                # Rain Radar Buttons
                html.Div(
                    dmc.Group(
                        [
                            dmc.Button(
                                "None",
                                id="rain_none",
                                variant="gradient",
                                gradient={"from": "white", "to": "gray", "deg": 60},
                                leftIcon=DashIconify(
                                    icon="radix-icons:shadow-none", width=24, height=24
                                ),
                                color="blue",
                            ),
                            dmc.Button(
                                "1h",
                                id="rain_1h",
                                leftIcon=DashIconify(
                                    icon="fluent:database-plug-connected-20-filled"
                                ),
                            ),
                            dmc.Button(
                                "24h",
                                id="rain_24h",
                                variant="subtle",
                                rightIcon=DashIconify(icon="logos:twitter"),
                                color="blue",
                            ),
                            dmc.Button(
                                "48h",
                                id="rain_48h",
                                variant="outline",
                                leftIcon=DashIconify(icon="fluent:settings-32-regular"),
                            ),
                            dmc.Button(
                                "72h",
                                id="rain_72h",
                                variant="outline",
                                leftIcon=DashIconify(icon="fluent:settings-32-regular"),
                            ),
                        ],
                        style={"visibility": "hidden"},
                    ),
                    id="rain_button_group",
                ),
            ],
            style={"position": "relative", "width": "1000px", "height": "500px"},
        ),
    ]
)

# ****************************************************
# Setup the callbacks
# ****************************************************
@dash.callback(
    dash.Output("rain_button_group", "children"),
    dash.Input("rain_radar_btn", "n_clicks"),
)
def toggle_radar_button_layer(n_clicks):
    if n_clicks == None:
        return dash.no_update
    elif n_clicks % 2:
        return dmc.Group(
            [
                dmc.Button(
                    "None",
                    id="rain_none",
                    variant="gradient",
                    gradient={"from": "white", "to": "gray", "deg": 60},
                    leftIcon=DashIconify(
                        icon="radix-icons:shadow-none", width=24, height=24
                    ),
                    color="blue",
                ),
                dmc.Button(
                    "1h",
                    id="rain_1h",
                    variant="gradient",
                    gradient={"from": "teal", "to": "blue", "deg": 60},
                    leftIcon=DashIconify(
                        icon="meteocons:thermometer-raindrop-fill", width=32, height=32
                    ),
                    color="blue",
                ),
                dmc.Button(
                    "24h",
                    id="rain_24h",
                    variant="gradient",
                    gradient={"from": "teal", "to": "blue", "deg": 60},
                    leftIcon=DashIconify(
                        icon="meteocons:thermometer-raindrop-fill", width=32, height=32
                    ),
                    color="blue",
                ),
                dmc.Button(
                    "48h",
                    id="rain_48h",
                    variant="gradient",
                    gradient={"from": "teal", "to": "blue", "deg": 60},
                    leftIcon=DashIconify(
                        icon="meteocons:thermometer-raindrop-fill", width=32, height=32
                    ),
                ),
                # dmc.Button("72h", id='rain_72h', variant="gradient",  gradient={"from": "teal", "to": "blue", "deg": 60}, leftIcon=DashIconify(icon="meteocons:thermometer-raindrop-fill",width=32, height=32)),
            ],
            style={
                "position": "absolute",
                "bottom": "310px",
                "left": "50%",
                "transform": "translateX(-50%)",
                "z-index": "4",
                "width": "90%",
            },  # Adjust 'bottom' as needed
        )
    else:
        return []


@dash.callback(
    dash.Output("rain_layers", "children"),
    dash.Input("rain_none", "n_clicks"),
    dash.Input("rain_1h", "n_clicks"),
    dash.Input("rain_24h", "n_clicks"),
    dash.Input("rain_48h", "n_clicks"),
    # dash.Input("rain_72h", "n_clicks")
)
def rain_layer(*args):
    ctx = callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None
    if button_id == None:
        return []
    if button_id == "rain_none":
        return []
    elif button_id == "rain_1h":
        return [
            dl.WMSTileLayer(
                url="https://mesonet.agron.iastate.edu/cgi-bin/wms/us/mrms_nn.cgi",
                layers="mrms_p1h",
                format="image/png",
                transparent=True,
                id="radar_layer_1h",
            )
        ]
    elif button_id == "rain_24h":
        return [
            dl.WMSTileLayer(
                url="https://mesonet.agron.iastate.edu/cgi-bin/wms/us/mrms_nn.cgi",
                layers="mrms_p24h",
                format="image/png",
                transparent=True,
                id="radar_layer_24h",
            )
        ]
    elif button_id == "rain_48h":
        return [
            dl.WMSTileLayer(
                url="https://mesonet.agron.iastate.edu/cgi-bin/wms/us/mrms_nn.cgi",
                layers="mrms_p48h",
                format="image/png",
                transparent=True,
                id="radar_layer_48h",
            )
        ]
    # elif button_id == 'rain_72h':
    #     print('72 hit')
    #     return [dl.WMSTileLayer(url="https://mesonet.agron.iastate.edu/cgi-bin/wms/us/mrms.cgi",
    #                                     layers="mrms_p74h", format="image/png", transparent=True, id='radar_layer_72h')]
    else:
        return []


@dash.callback(dash.Output("clouds_layer", "url"), dash.Input("cloud_btn", "n_clicks"))
def cloud_layer(n_clicks):
    if n_clicks == None:
        return ""
    elif n_clicks % 2:
        return "http://{s}.tile.openweathermap.org/map/clouds/{z}/{x}/{y}.png?appid=" + f"{openweathermap_appid}"
    else:
        return ""


# satellite_laye
@dash.callback(
    dash.Output("satellite_layer", "url"),
    [dash.Input(f"layer_button_{i}", "n_clicks") for i in range(20)],
)
def theme_layer(*args):
    ctx = callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0] if ctx.triggered else None
    if not button_id:
        return dash.no_update
    if button_id == "layer_button_0":
        return "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    elif button_id == "layer_button_1":
        return "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
    elif button_id == "layer_button_2":
        return "https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png"
    elif button_id == "layer_button_3":
        return "https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}"
    elif button_id == "layer_button_4":
        return "https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}"
    elif button_id == "layer_button_5":
        return "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}"
    elif button_id == "layer_button_6":
        return "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}"
    elif button_id == "layer_button_7":
        return "https://tile.jawg.io/jawg-matrix/{z}/{x}/{y}{r}.png?access-token=" + f'{jawg_matrix_access_token}'
    elif button_id == "layer_button_8":
        return "https://tile.jawg.io/jawg-lagoon/{z}/{x}/{y}{r}.png?access-token=" + f'{jawg_matrix_access_token}'
    elif button_id == "layer_button_9":
        return "http://sgx.geodatenzentrum.de/wmts_topplus_open/tile/1.0.0/web_grau/default/WEBMERCATOR/{z}/{y}/{x}.png"
    elif button_id == "layer_button_10":
        return "https://map1.vis.earthdata.nasa.gov/wmts-webmerc/VIIRS_CityLights_2012/default/GoogleMapsCompatible_Level8/{z}/{y}/{x}.jpg"
    elif button_id == "layer_button_11":
        return "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png"
    elif button_id == "layer_button_12":
        return (
            "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png"
        )
    elif button_id == "layer_button_13":
        return "https://tiles.stadiamaps.com/tiles/stamen_terrain/{z}/{x}/{y}{r}.png"
    elif button_id == "layer_button_14":
        return "https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}{r}.png"
    elif button_id == "layer_button_15":
        return "https://tiles.stadiamaps.com/tiles/stamen_watercolor/{z}/{x}/{y}.jpg"
    elif button_id == "layer_button_16":
        return "https://{s}.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey=" + f'{thunderforest_api_key}'
    elif button_id == "layer_button_17":
        return "https://{s}.tile.thunderforest.com/transport-dark/{z}/{x}/{y}.png?apikey=" + f'{thunderforest_api_key}'
    elif button_id == "layer_button_18":
        return "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}"
    elif button_id == "layer_button_19":
        return "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}"


@dash.callback(
    dash.Output("layer_select", "children"),
    dash.Input("layer_button", "n_clicks"),
)
def display_click_data(n_clicks):
    if n_clicks is None:
        return dash.no_update
    elif n_clicks % 2:
        return layer_select
    return []
