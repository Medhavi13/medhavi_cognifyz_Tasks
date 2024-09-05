import pandas as pd

# Load the dataset
file_path = "c:\\Users\\Administrator\\Downloads\\Railway_info.csv"
data = pd.read_csv(file_path)

# Task 1: Identify stations that are both source and destination with equal frequency
source_freq = data['Source_Station_Name'].value_counts()
destination_freq = data['Destination_Station_Name'].value_counts()

# Combine the source and destination frequencies into a DataFrame
freq_df = pd.DataFrame({'Source_Frequency': source_freq, 'Destination_Frequency': destination_freq}).fillna(0)

# Find stations where source and destination frequencies are equal
equal_freq_stations = freq_df[freq_df['Source_Frequency'] == freq_df['Destination_Frequency']]

print("Stations that are both source and destination with equal frequency:")
print(equal_freq_stations)

# Task 2: Analyze the distribution of train operations across the days of the week
train_by_day = data['days'].value_counts()

print("\nTrain operations distribution by day of the week:")
print(train_by_day)

# Finding the day with the highest traffic
highest_traffic_day = train_by_day.idxmax()
highest_traffic_count = train_by_day.max()

print(f"\nDay with the highest traffic: {highest_traffic_day} with {highest_traffic_count} train operations")

# Task 3: Identify potential anomalies (e.g., duplicated routes, unusual frequency)
# Checking for duplicated routes (same source and destination station pair)
duplicated_routes = data[data.duplicated(['Source_Station_Name', 'Destination_Station_Name'], keep=False)]

if not duplicated_routes.empty:
 print("\nDuplicated routes found:")
print(duplicated_routes[['Train_No', 'Source_Station_Name', 'Destination_Station_Name']].head(10))  # Display top 10

# Checking for any unusual frequency in train routes (e.g., routes with extremely high or low frequency)
route_counts = data.groupby(['Source_Station_Name', 'Destination_Station_Name']).size().reset_index(name='count')

# Finding routes with extremely high frequency (top 1%)
high_frequency_threshold = route_counts['count'].quantile(0.99)
high_frequency_routes = route_counts[route_counts['count'] > high_frequency_threshold]

print(f"\nRoutes with unusually high frequency (Top 1% of routes):")
print(high_frequency_routes)

# Finding routes with extremely low frequency (bottom 1%)
low_frequency_threshold = route_counts['count'].quantile(0.01)
low_frequency_routes = route_counts[route_counts['count'] < low_frequency_threshold]

print(f"\nRoutes with unusually low frequency (Bottom 1% of routes):")
print(low_frequency_routes)
