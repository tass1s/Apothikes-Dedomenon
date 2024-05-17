import pandas as pd
import folium

# Φόρτωση δεδομένων
df = pd.read_json('C:\\Users\\User\\Downloads\\output\\output.json', lines=True)  # Ρύθμισε τη διαδρομή προς το αρχείο JSON

# Διόρθωση εάν το JSON δεν φορτώνεται σωστά
# df = pd.read_json('path_to_your_json_file.json', lines=True) 
m = folium.Map(location=[52.370216, 4.895168], zoom_start=7)  # Κεντράρισμα χάρτη σε σημείο της Ολλανδίας

# Προσθήκη κάθε σημείου στον χάρτη
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['geo']['coordinates'][0], row['geo']['coordinates'][1]],
        radius=5,
        fill=True,
        color='blue',
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(m)

# Αποθήκευση του χάρτη σε HTML αρχείο
m.save('map.html')