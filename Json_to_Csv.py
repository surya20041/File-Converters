import json
import csv

# Open the JSON file for reading
with open("C:/Users/surya/OneDrive/Documents/Programs/File converters/full_df.json", 'r') as json_file:

    # Load the JSON data
    data = json.load(json_file)

    # Open the CSV file for writing
    with open("C:/Users/surya/OneDrive/Documents/Programs/She values/Naukri.csv", 'w', newline='',encoding='latin-1') as csv_file:

        # Create a CSV writer
        writer = csv.writer(csv_file) 

        # Write the header row
        writer.writerow(data[0].keys())

        # Write the data rows
        for row in data:
            writer.writerow(row.values())
