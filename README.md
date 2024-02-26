# Dash-Frontend
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC-pBvv8mzLpj0k-RIbc2Nog?style=social)
![Discord](https://img.shields.io/discord/396334922522165248)
![GitHub followers](https://img.shields.io/github/followers/pip-install-python?style=social)
![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/PipInstallPython?style=social)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![GitHub Sponsors](https://img.shields.io/github/sponsors/pip-install-python)

[![Project Software](https://skills.thijs.gg/icons?i=linux,flask,py,react,js,html,css,)](https://community.plotly.com/t/django-dash-token-authentication/82088)

![Initial_Map](assets/github/initial_load_with_clouds.png)

`Dash-Leaflet-Tile-Weather-Explorer` is a leaflet template aimed at showcasing 20 initial style tiles, current clouds and USA precipitation 1h, 24h, 48h.

This post is directed for other cartographer’s that might be lurking in the mist, personally I’ve always found the art of map making very interesting. Over time how it has evolved from scribbles on a piece of paper to interactive GUI’s.

The art of exploration and understanding of the world around us has never been easier with the advances we have seen in technology and information. My goal is to articulate, throughout history cartographer’s have always been important and useful careers. From solving problems with disease, war, logistics and many other. Coveted is the person that can give an understanding of the world and now is the best time to explore and create the tools and maps of the future. Inspiration and a challenge to build and innovate exceeding the initial seed planted with this project.
![Night](assets/github/night.png)

## Features
- **20 Map Styles:** More styles could be added or the ones provided could be replaced.
- **Rain Radar:** 1h, 24h, 48h rain radar
- **Cloud Radar:** toggle the current clouds 
- **User Location Detector:** Click the find me button to pinpoint users location.
- **Full Screen Mode:** inspect with the full width and height of your screens real-estate 

![tile_selector](assets/github/tile_selector.png)

API Keys are required for the clouds and some map tiles:
- **jawg-matrix-access-token:** https://www.jawg.io/
- **thunderforest-api-key:** https://www.thunderforest.com/
- **openweathermap-appid:** https://openweathermap.org/

![precipitation](assets/github/precipitation.png)

## Getting Started

To get started with `Dash-Leaflet-Tile-Weather-Explorer`, clone this repository to your local machine:

```bash
git clone https://github.com/pip-install-python/Dash-Leaflet-Tile-Weather-Explorer.git
cd weather_map
```
Ensure you have the following installed:

- Python (3.6 or later)
- pip
- Virtual environment (recommended)
- Create a config.json file in pages with the API Keys `jawg-matrix-access-token`, `thunderforest-api-key`, and `openweathermap-appid`

### Installation
1. Create and activate a virtual environment:

Windows:
```
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:
```

macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

2. Install the required packages:

```
pip install -r requirements.txt
```

### Config
Create a config.json file in pages with the API Keys 

### Running Examples
Navigate to the app.py file and execute the application:


```
python app.py
```

### Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Showcase your work and help others learn by contributing to: https://community.plotly.com/

### License
Open Source

### Contact
Pip Install Python

Project Link: https://github.com/pip-install-python/Dash-Leaflet-Tile-Weather-Explorer


