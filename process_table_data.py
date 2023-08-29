import json
import re
from nltk.tokenize import word_tokenize

# Read the extracted table data JSON file
input_file = 'table_data.json'
with open(input_file, 'r') as json_file:
    table_data = json.load(json_file)

# Post-process the data by removing special characters, converting to lowercase, and joining tokens
processed_table_data = []
for row in table_data:
    processed_row = {}
    for key, value in row.items():
        if key != "Version":
            processed_value = re.sub(r'[^a-zA-Z\s]', '', value)
            tokens = word_tokenize(processed_value)
            processed_value = ' '.join(tokens).lower()  # Join tokens and convert to lowercase
            processed_row[key] = processed_value
        else:
            processed_row[key] = value
    processed_table_data.append(processed_row)

# Save the processed table data to a new JSON file
output_file = 'processed_table_data.json'
with open(output_file, 'w') as json_file:
    json.dump(processed_table_data, json_file, indent=4)

print(f"Processed table data saved to {output_file}")
