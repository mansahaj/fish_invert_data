import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
file_path = 'fish_inverts.csv'  # Make sure to update this to your actual file path
data = pd.read_csv(file_path)

# Convert 'date' to a datetime type
data['date'] = pd.to_datetime(data['date'])

# Filter out rows where observations are invertebrates
invert_data = data[data['fish_invert'] == 'invert']

# Group by 'date' and 'habitat', and count the number of invertebrate observations
invert_habitat_counts = invert_data.groupby(['date', 'habitat']).size().reset_index(name='counts')

# Pivot the data to have dates as rows and habitats as columns
invert_habitat_pivot = invert_habitat_counts.pivot(index='date', columns='habitat', values='counts').fillna(0)

# Plotting
plt.figure(figsize=(15, 7))
sns.lineplot(data=invert_habitat_pivot)
plt.title('Invertebrate Observations Across Different Habitats Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Observations')
plt.legend(title='Habitat')
plt.xticks(rotation=45)
plt.tight_layout()  # This adjusts the plot to ensure everything fits without overlapping
plt.show()
