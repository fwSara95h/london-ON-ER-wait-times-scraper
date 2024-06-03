import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'ER-wait-times.csv'
df = pd.read_csv(file_path)

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Plotting the data
plt.figure(figsize=(14, 7))
plt.plot(df['Time'], df['UH'], label='University Hospital', marker='o')
plt.plot(df['Time'], df['VH'], label='Victoria Hospital', marker='o')

plt.title('Emergency Room Wait Time in London Ontario')
plt.xlabel('Date and Time')
plt.ylabel('Wait Time (hours)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
