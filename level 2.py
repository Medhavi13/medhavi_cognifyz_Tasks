import pandas as pd

# Load the dataset
file_path = "c:\\Users\\Administrator\\Downloads\\Railway_info.csv"
data = pd.read_csv(file_path)

# Convert 'days' column to categorical type if not already
data['days'] = data['days'].astype('category')

# Task 1: Frequency distribution of trains by source and destination stations
source_station_counts = data['Source_Station_Name'].value_counts()
destination_station_counts = data['Destination_Station_Name'].value_counts()

# Display the top 10 source and destination stations by train frequency
print("\nTop 10 Source Stations by Train Frequency:")
print(source_station_counts.head(10))

print("\nTop 10 Destination Stations by Train Frequency:")
print(destination_station_counts.head(10))

# Task 2: Distribution of train operations by days of the week
day_counts = data['days'].value_counts()

print("\nFrequency of Train Operations by Days of the Week:")
print(day_counts)

# Task 3: Analysis of the trains that operate only on a specific day
unique_day_trains = data.groupby('Train_No').filter(lambda x: len(x['days'].unique()) == 1)

print(f"\nNumber of trains that operate only on a specific day: {len(unique_day_trains['Train_No'].unique())}")
print("\nExamples of trains that operate on a specific day:")
print(unique_day_trains[['Train_No', 'Train_Name', 'Source_Station_Name', 'Destination_Station_Name', 'days']].head(10))
