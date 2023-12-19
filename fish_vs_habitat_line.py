import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'fish_inverts.csv'
data = pd.read_csv(file_path)

# Convert 'date' to a datetime type
data['date'] = pd.to_datetime(data['date'])

# Filter out rows where observations are fish
fish_data = data[data['fish_invert'] == 'fish']

# Group by 'date' and 'habitat', and count the number of fish observations
fish_habitat_counts = fish_data.groupby(['date', 'habitat']).size().reset_index(name='counts')

# Pivot the data to have dates as rows and habitats as columns
fish_habitat_pivot = fish_habitat_counts.pivot(index='date', columns='habitat', values='counts').fillna(0)

# Plotting
plt.figure(figsize=(15, 7))
sns.lineplot(data=fish_habitat_pivot)
plt.title('Fish Observations Across Different Habitats Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Observations')
plt.legend(title='Habitat')
plt.xticks(rotation=45)
plt.tight_layout()  # This adjusts the plot to ensure everything fits without overlapping
plt.show()
