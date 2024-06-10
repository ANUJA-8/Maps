import plotly.express as px
import pandas as pd
import requests

# Define the data
data = {
    'State': ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
              'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
              'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands',
              'Chandigarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Jammu and Kashmir', 'Ladakh',
              'Lakshadweep', 'Puducherry'],
    'Count': [2046, 35, 1834, 8496, 2059, 103, 10608, 685, 2217, 2049, 6143, 3712, 4554, 21959,
              273, 315, 50, 274, 4238, 3500, 7935, 193, 6247, 3728, 269, 7572, 672, 5694, 156,
              316, 59, 216, 2090, 648, 159, 59, 321]
}

df = pd.DataFrame(data)

# URL for GeoJSON file
geojson_url = "file:///E:/Maps/State.geojson"

# Fetch GeoJSON file
response = requests.get(geojson_url)
geojson = response.json()

# Create the choropleth map
fig = px.choropleth(
    df,
    geojson=geojson,
    featureidkey='properties.NAME_1',
    locations='State',
    color='Count',
    color_continuous_scale='Blues',
    title='Choropleth Map of India with State Borders',
    hover_name='State',
    labels={'Count': 'Count'}
)

fig.update_geos(fitbounds="locations", visible=False)

# Show the map
fig.show()

# Save the map as an HTML file
fig.write_html("india_choropleth_map.html")
