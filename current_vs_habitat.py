import pandas as pd
import matplotlib.pyplot as plt


file_path = 'fish_inverts.csv' 
data = pd.read_csv(file_path)

# Filter out rows where observations are invertebrates
invert_data = data[data['fish_invert'] == 'invert']

# Group by 'habitat' and 'swell_current', and count the number of invertebrate observations
habitat_current_counts = invert_data.groupby(['habitat', 'swell_current']).size().reset_index(name='counts')

# Pivot the data to have habitats as rows and current conditions as columns for easy plotting
habitat_current_pivot = habitat_current_counts.pivot(index='habitat', columns='swell_current', values='counts').fillna(0)

# Plotting a bar graph
habitat_current_pivot.plot(kind='bar', figsize=(10, 7))
plt.title('Invertebrate Observations by Current Conditions in Different Habitats')
plt.xlabel('Habitat')
plt.ylabel('Number of Observations')
plt.legend(title='Current Conditions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
