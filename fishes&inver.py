import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = 'fish_inverts.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Ensure that 'date' is a datetime column
data['date'] = pd.to_datetime(data['date'])

# Separate the data for fishes and invertebrates
fish_data = data[data['fish_invert'] == 'fish']
invert_data = data[data['fish_invert'] == 'invert']

# Group the data by date and habitat, and get counts for fishes and invertebrates
fish_counts = fish_data.groupby(['date', 'habitat']).size().reset_index(name='fish_counts')
invert_counts = invert_data.groupby(['date', 'habitat']).size().reset_index(name='invert_counts')

# Pivot the data for plotting
fish_pivot = fish_counts.pivot(index='date', columns='habitat', values='fish_counts').fillna(0)
invert_pivot = invert_counts.pivot(index='date', columns='habitat', values='invert_counts').fillna(0)

# Plotting the line graphs
plt.figure(figsize=(14, 7))

# Plot for fishes
for column in fish_pivot.columns:
    plt.plot(fish_pivot.index, fish_pivot[column], label=f'Fish - {column}')

# Plot for invertebrates
for column in invert_pivot.columns:
    plt.plot(invert_pivot.index, invert_pivot[column], label=f'Invert - {column}', linestyle='--')

plt.title('Observations of Fishes and Invertebrates in Different Habitats Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Observations')
plt.legend()
plt.show()
