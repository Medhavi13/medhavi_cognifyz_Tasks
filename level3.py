import pandas as pd

# Load the dataset
file_path = "c:\\Users\\Administrator\\Downloads\\Railway_info.csv"
data = pd.read_csv(file_path)
# Convert 'days' column to categorical type if not already
data['days'] = data['days'].astype('category')

# Task 1: Identify the source station with the most variety in destination stations
source_variety = data.groupby('Source_Station_Name')['Destination_Station_Name'].nunique()
most_varied_source_station = source_variety.idxmax()
most_varied_source_count = source_variety.max()

print(f"Source station with the most variety in destination stations: {most_varied_source_station} with {most_varied_source_count} unique destinations")

# Task 2: Identify the destination station receiving trains from the most variety of source stations
destination_variety = data.groupby('Destination_Station_Name')['Source_Station_Name'].nunique()
most_varied_destination_station = destination_variety.idxmax()
most_varied_destination_count = destination_variety.max()

print(f"Destination station receiving trains from the most variety of source stations: {most_varied_destination_station} with {most_varied_destination_count} unique source stations")

# Task 3: Determine the most frequent train routes (from source to destination)
route_counts = data.groupby(['Source_Station_Name', 'Destination_Station_Name']).size().reset_index(name='count')
most_frequent_route = route_counts.loc[route_counts['count'].idxmax()]

print("\nMost frequent train route:")
print(f"From {most_frequent_route['Source_Station_Name']} to {most_frequent_route['Destination_Station_Name']} with {most_frequent_route['count']} trains")

# Additional: Top 5 most frequent train routes
top_5_routes = route_counts.sort_values(by='count', ascending=False).head(5)

print("\nTop 5 most frequent train routes:")
print(top_5_routes[['Source_Station_Name', 'Destination_Station_Name', 'count']])
