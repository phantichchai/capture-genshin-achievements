import json

# Read the first JSON file
with open('processed_table_data.json', 'r') as json_file:
    schema1_data = json.load(json_file)

# Read the second JSON file
with open('processed_data.json', 'r') as json_file:
    schema2_data = json.load(json_file)

# Create a new list to store the filtered data
filtered_data = []

# Iterate through the data in the first schema
for entry1 in schema1_data:
    achievement = entry1.get('Achievement')
    if achievement:
        matched_entry = next((entry2 for entry2 in schema2_data if achievement.lower() in ' '.join(entry2.get('processed_text_lines')).lower()), None)
        if not matched_entry:
            filtered_data.append(entry1)

# Save the filtered data to a new JSON file
output_file = 'filtered_data.json'
with open(output_file, 'w') as json_file:
    json.dump(filtered_data, json_file, indent=4)

print(f"Filtered data saved to {output_file}")