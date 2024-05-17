import folium
from folium.plugins import HeatMap
import pandas as pd

# Φόρτωση των δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)

# Εξαγωγή των γεωγραφικών συντεταγμένων
df['lat'] = df['coordinates'].apply(lambda x: x['coordinates'][1] if x is not None else None)
df['lon'] = df['coordinates'].apply(lambda x: x['coordinates'][0] if x is not None else None)
df = df.dropna(subset=['lat', 'lon'])

# Δημιουργία χάρτη θερμότητας
map = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=6)
HeatMap(data=df[['lat', 'lon']], radius=15).add_to(map)

# Εμφάνιση του χάρτη
map.save('heatmap.html')
map
