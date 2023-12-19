import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
file_path = 'path_to_your_file/fish_inverts.csv'
data = pd.read_csv(file_path)

# Converting 'date' to datetime for analysis
data['date'] = pd.to_datetime(data['date'])

# Grouping data by fish_invert and date, then counting the occurrences
fish_invert_time_data = data.groupby([data['date'].dt.to_period('M'), 'fish_invert']).size().reset_index(name='count')

# Pivoting the data for easier plotting
fish_invert_time_data_pivot = fish_invert_time_data.pivot(index='date', columns='fish_invert', values='count').fillna(0)

# Plotting
plt.figure(figsize=(15, 10))
sns.heatmap(fish_invert_time_data_pivot, cmap='viridis', lw=0.5)
plt.title('Occurrences of Fish and Invertebrates Over Time')
plt.xlabel('Fish/Invertebrate')
plt.ylabel('Time (Monthly)')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()

# Note: The heatmap will display fish and invertebrate categories on the x-axis and time on the y-axis.
