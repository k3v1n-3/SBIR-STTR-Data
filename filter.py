import pandas as pd
import os

# Check if file exists
if not os.path.exists("award_data.csv"):
    print("The file award_data.csv does not exist.")
else:
    filtered_data = pd.DataFrame()
    chunk_iter = pd.read_csv("award_data.csv", usecols=["Award Year", "Award Amount"], thousands=',', chunksize=10000)

    for chunk in chunk_iter:
        if chunk.isna().any().any():
            print("Data contains missing values. Handling missing values...")
            chunk.dropna(inplace=True)
        
        # Here, we assume the data types should now be correct due to the thousands=',' parameter
        if chunk['Award Year'].min() < 1900 or chunk['Award Amount'].min() < 0:
            print("Data contains out-of-range values.")
            continue

        filtered_data = pd.concat([filtered_data, chunk], ignore_index=True)

    if filtered_data.empty:
        print("No data to write.")
    else:
        filtered_data.to_csv("awardData.csv", index=False, header=['Award Year', 'Award Amount'])
