import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
dingosplit = pd.read_csv('/content/gdrive/My Drive/Rue Cafe Data Analytics/Transactions/Payments_2022v02.csv')

# Convert the 'payment_date' column to datetime objects
dingosplit['payment_date'] = pd.to_datetime(dingosplit['payment_date'])

# Filter data starting from March 2022
start_date = '2022-03-01'
filtered_data = dingosplit[dingosplit['payment_date'] >= start_date]

# Calculate the average transaction volume per week
weekly_avg = filtered_data.resample('W', on='payment_date')['amount'].mean()

# Plotting the average transaction volume per week
plt.figure(figsize=(10, 6))  # Set the figure size

# Customize the line plot
plt.plot(weekly_avg, marker='o', linestyle='-', color='blue', linewidth=2)

plt.title('Average Transaction Amount per Week', fontsize=16, fontweight='bold')  # Set the title with larger font size and bold
plt.xlabel('Week', fontsize=12)  # Set the x-axis label with a larger font size
plt.ylabel('Average Transaction Amount', fontsize=12)  # Set the y-axis label with a larger font size

plt.xticks(rotation=45, fontsize=10)  # Rotate x-axis labels and set a smaller font size
plt.yticks(fontsize=10)  # Set a smaller font size for y-axis tick labels

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)  # Add gridlines with customized style

plt.tight_layout()  # Adjust layout to prevent overlapping elements

plt.show()  # Display the plot
