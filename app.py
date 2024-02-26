import dash
from dash import (
    html,
)
from flask import Flask
import json

server = Flask(__name__)

app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    ],
    external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.1.0/chroma.min.js",
        "https://api.mapbox.com/mapbox-gl-js/v3.0.0-beta.1/mapbox-gl.js",
        "https://unpkg.com/leaflet@1.4.0/dist/leaflet.js",
    ],
    assets_url_path="assets",
    use_pages=True,
    server=server,
)

app.layout = html.Div(
    [
        dash.page_container,
    ],
)

if __name__ == "__main__":
    app.run_server(port=43212, debug=True)
