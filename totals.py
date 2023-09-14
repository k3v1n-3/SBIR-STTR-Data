import pandas as pd

# Read the filtered data from the CSV file
filtered_data = pd.read_csv('awardData.csv')

# Group by 'Award Year' and sum the 'Award Amount'
grouped_data = filtered_data.groupby('Award Year')['Award Amount'].sum().reset_index()

# Display the totals for each year
print("Total Award Amounts by Year:")
print(grouped_data)

# Optionally, save the totals to a new CSV file
grouped_data.to_csv('award_totals_by_year.csv', index=False)
