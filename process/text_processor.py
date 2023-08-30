import os
import cv2
import pytesseract
import json
import nltk
import re
from nltk.tokenize import word_tokenize
nltk.download('punkt')

class TextProcessor:
    def __init__(self, image_folder='achievements/resource'):
        self.image_folder = image_folder
        self.data = []

    def process_text_data(self):
        pytesseract.pytesseract.tesseract_cmd = r'G:/Tesseract-OCR/tesseract.exe'
        
        extracted_text_data = []
        for filename in os.listdir(self.image_folder):
            if filename.endswith('.png'):
                image_path = os.path.join(self.image_folder, filename)
                image = cv2.imread(image_path)

                text = pytesseract.image_to_string(image)

                split_lines = text.split('\n')
                non_empty_lines = [line.strip() for line in split_lines if line.strip()]
                
                if non_empty_lines:
                    extracted_text_data.append({
                        'filename': filename,
                        'text_lines': non_empty_lines,
                        'order': int(filename.split('.')[0])
                    })

        extracted_text_data.sort(key=lambda x: x['order'])

        processed_data = []
        for entry in extracted_text_data:
            processed_lines = self.process_text_lines(entry['text_lines'])
            if processed_lines:
                processed_data.append({
                    'filename': entry['filename'],
                    'processed_text_lines': processed_lines
                })

        self.data = processed_data

    def process_text_lines(self, text_lines):
        processed_lines = []
        for line in text_lines:
            if line is not None:
                line = line.lower()
                line = re.sub(r'[^a-zA-Z\s]', '', line)
                tokens = word_tokenize(line)
                processed_line = ' '.join(tokens)
                processed_lines.append(processed_line)
        return processed_lines

    def save_processed_data(self, output_file='processed_data.json'):
        with open(output_file, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
