import pandas as pd

# Load the dataset
file_path = 'c:\\Users\\Administrator\\Downloads\\Railway_info.csv'
data = pd.read_csv(file_path)

# Task 1.1: Load and Inspect Data
# Display the first 10 rows
print("First 10 rows of the dataset:")
print(data.head(10))

# Understand the basic structure of the data
print("\nBasic structure of the data:")
print(data.info())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Task 1.2: Basic Statistics
# Calculate the number of trains
num_trains = len(data)
print(f"\nNumber of trains: {num_trains}")

# Count of unique source stations and destination stations
num_unique_source_stations = data['Source_Station_Name'].nunique()
num_unique_destination_stations = data['Destination_Station_Name'].nunique()
print(f"Number of unique source stations: {num_unique_source_stations}")
print(f"Number of unique destination stations: {num_unique_destination_stations}")

# Find the most common source and destination stations
most_common_source_station = data['Source_Station_Name'].mode()[0]
most_common_destination_station = data['Destination_Station_Name'].mode()[0]
print(f"Most common source station: {most_common_source_station}")
print(f"Most common destination station: {most_common_destination_station}")

# Task 1.3: Data Cleaning
# Handle missing values by imputing with the most frequent value
data.fillna(data.mode().iloc[0], inplace=True)
print("\nMissing values after imputation:")
print(data.isnull().sum())

# Standardize the format of station names
data['Source_Station_Name'] = data['Source_Station_Name'].str.upper()
data['Destination_Station_Name'] = data['Destination_Station_Name'].str.upper()

print("\nStandardized station names (first 10 rows):")
print(data[['Source_Station_Name', 'Destination_Station_Name']].head(10))
