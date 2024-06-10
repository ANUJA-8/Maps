import plotly.express as px
import pandas as pd
import requests

# Define the data including Odisha and the older part of Jammu and Kashmir
data = {
    'State': ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
              'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
              'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands',
              'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Jammu and Kashmir', 'Ladakh',
              'Lakshadweep', 'Puducherry'],
    'Count': [2046, 35, 1834, 8496, 2059, 103, 10608, 685, 2217, 2049, 6143, 3712, 4554, 21959,
              273, 315, 50, 274, 4238, 3500, 7935, 193, 6247, 3728, 269, 7572, 672, 5694, 156,
              316, 275, 2090, 712, 648, 59, 321]
}

df = pd.DataFrame(data)

# URL for GeoJSON file with older Jammu and Kashmir boundaries
geojson_url = "https://raw.githubusercontent.com/datameet/indian_states/master/IndianStates.geojson"

# Fetch GeoJSON file
response = requests.get(geojson_url)
geojson = response.json()

# Create the choropleth map
fig = px.choropleth(
    df,
    geojson=geojson,
    featureidkey='properties.st_nm',
    locations='State',
    color='Count',
    color_continuous_scale='Blues',
    title='Choropleth Map of India with State Borders and Counts',
    hover_name='State',
    labels={'Count': 'Count'},
)

# Add count as text on the map
df['text'] = df['Count'].astype(str)
fig.update_traces(text=df['text'], textposition='middle center')

fig.update_geos(fitbounds="locations", visible=False)

# Show the map
fig.show()

# Save the map as an HTML file
fig.write_html("india_choro_map_with_counts.html")
