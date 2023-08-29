import json
import nltk
import re
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Read the JSON file
json_file_path = 'extracted_text.json'  # Update this with the path to your JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Process the data and tokenize words
processed_data = []
for entry in data:
    filename = entry['filename']
    text_lines = entry['text_lines']

    processed_lines = []
    for line in text_lines:
        if line is not None:
            line = line.lower()
            line = re.sub(r'[^a-zA-Z\s]', '', line)
            tokens = word_tokenize(line)
            processed_line = ' '.join(tokens)
            processed_lines.append(processed_line)

    if processed_lines:
        processed_data.append({
            'filename': filename,
            'processed_text_lines': processed_lines
        })

# Write processed data to a new JSON file
output_file = 'processed_data.json'
with open(output_file, 'w') as json_file:
    json.dump(processed_data, json_file, indent=4)

print(f"Processed data saved to {output_file}")
