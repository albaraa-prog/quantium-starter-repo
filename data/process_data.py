import pandas as pd
import os

# Define the data directory and output file
data_dir = "data"
output_file = "processed_data.csv"

# List the input files
input_files = [
    os.path.join(data_dir, "daily_sales_data_0.csv"),
    os.path.join(data_dir, "daily_sales_data_1.csv"),
    os.path.join(data_dir, "daily_sales_data_2.csv"),
]

# Initialize an empty DataFrame for processed data
processed_data = pd.DataFrame()

# Process each file
for file in input_files:
    # Load the CSV file
    df = pd.read_csv(file)
    
    # Remove the "$" sign from the price column and convert it to a float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Filter rows for "Pink Morsels"
    df = df[df['product'] == 'pink morsel']
    
    # Create the "Sales" column
    df['Sales'] = df['price'] * df['quantity']
    
    # Select the required columns
    df = df[['Sales', 'date', 'region']]
    
    # Append to the main DataFrame
    processed_data = pd.concat([processed_data, df], ignore_index=True)

# Save the processed data to a CSV file
processed_data.to_csv(output_file, index=False)
print(f"Processed data saved to {output_file}")
