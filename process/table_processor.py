import json
import re
import os
from nltk.tokenize import word_tokenize

class TableProcessor:
    def __init__(self, input_file='table_data.json'):
        self.input_file = os.path.join('json_data', input_file)
        self.data = []

    def process_table_data(self):
        with open(self.input_file, 'r', encoding='utf-8') as json_file:
            table_data = json.load(json_file)

        processed_table_data = []
        for row in table_data:
            processed_row = {}
            for key, value in row.items():
                if key == "Achievement":
                    processed_value = re.sub(r'[^a-zA-Z\s]', '', value)
                    tokens = word_tokenize(processed_value)
                    processed_value = ' '.join(tokens).lower()
                    processed_row['processed_value'] = processed_value
                processed_row[key] = value
                
            processed_table_data.append(processed_row)

        self.data = processed_table_data

    def find_matching_data(self, text_data):
        uncompleted_acheivement_data = []
        completed_achievement_data = []
        for entry1 in self.data:
            achievement = entry1.get('processed_value')
            if achievement:
                match_condition = next((entry2 for entry2 in text_data if achievement.lower() in ' '.join(entry2.get('processed_text_lines')).lower()), None)
                if not match_condition:
                    uncompleted_acheivement_data.append(entry1)
                else:
                    completed_achievement_data.append(entry1)
                    
        return uncompleted_acheivement_data, completed_achievement_data

    def save_data_to_json(self, data, output_file):
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)