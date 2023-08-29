import os
import cv2
import pytesseract
import json

# Set the path to your Tesseract executable (change this to your installation path)
pytesseract.pytesseract.tesseract_cmd = r'G:/Tesseract-OCR/tesseract.exe'

# Path to the folder containing images
image_folder = 'G:/Github/ocr/achievements/resource'

# List to store extracted text data
extracted_text_data = []

for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Split text by newline and add non-empty lines to the extracted_text_data list
        split_lines = text.split('\n')
        non_empty_lines = [line.strip() for line in split_lines if line.strip()]
        
        if non_empty_lines:
            extracted_text_data.append({
                'filename': filename,
                'text_lines': non_empty_lines,
                'filename_int': int(filename.split('.')[0])  # Add the integer value of the filename
            })

# Sort extracted_text_data by filename_int
extracted_text_data.sort(key=lambda x: x['filename_int'])

# Write extracted text data to a JSON file
output_file = 'extracted_text.json'
with open(output_file, 'w') as json_file:
    json.dump(extracted_text_data, json_file, indent=4)

print(f"Extracted and corrected text data saved to {output_file}")
