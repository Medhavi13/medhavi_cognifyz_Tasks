import pandas as pd
import folium
from folium.plugins import HeatMap

file_path = 'C:\\Users\\medhavi\\Downloads\\Dataset  (1).csv'
df = pd.read_csv(file_path)

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

for idx, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(restaurant_map)

restaurant_map.save('C:\\Users\\medhavi\\Downloads\\Dataset  (1).csv')

city_counts = df['City'].value_counts()
locality_counts = df['Locality'].value_counts()

city_stats = df.groupby('City').agg({
    'Aggregate rating': 'mean',
    'Average Cost for two': 'mean',
    'Price range': 'mean'
}).reset_index()

locality_stats = df.groupby('Locality').agg({
    'Aggregate rating': 'mean',
    'Average Cost for two': 'mean',
    'Price range': 'mean'
}).reset_index()

top_cities_by_rating = city_stats.sort_values(by='Aggregate rating', ascending=False).head(5)
top_localities_by_rating = locality_stats.sort_values(by='Aggregate rating', ascending=False).head(5)

city_stats.to_csv('C:\\Users\\medhavi\\Downloads\\Dataset  (1).csv', index=False)
locality_stats.to_csv('C:\\Users\\medhavi\\Downloads\\Dataset  (1).csv', index=False)
top_cities_by_rating.to_csv('C:\\Users\\medhavi\\Downloads\\Dataset  (1).csv', index=False)
top_localities_by_rating.to_csv('C:\\Users\\medhavi\\Downloads\\Dataset  (1).csv', index=False)

print("Top 5 Cities by Average Rating:")
print(top_cities_by_rating)

print("\nTop 5 Localities by Average Rating:")
print(top_localities_by_rating)
