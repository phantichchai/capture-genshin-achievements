# process/processor.py

import argparse
import time
from .video_processor import VideoProcessor
from .text_processor import TextProcessor
from .table_processor import TableProcessor
from .web_scraper import WebScraper

def run(video_path):
    start_time = time.time()

    # Initialize the VideoProcessor
    video_processor = VideoProcessor(video_path)
    video_processor.capture_frames()
    video_duration = time.time() - start_time
    print(f"Video processing time: {video_duration:.2f} seconds")

    start_time = time.time()
    # Initialize the TextProcessor and process text data
    text_processor = TextProcessor()
    text_processor.process_text_data()
    text_processing_duration = time.time() - start_time
    print(f"Text processing time: {text_processing_duration:.2f} seconds")

    start_time = time.time()
    # Initialize the WebScraper and scrape table data
    table_scraper = WebScraper(url='https://genshin-impact.fandom.com/wiki/Wonders_of_the_World', output_file='table_data.json')
    table_scraper.scrape_table_data()
    web_scraping_duration = time.time() - start_time
    print(f"Web scraping time: {web_scraping_duration:.2f} seconds")

    start_time = time.time()
    # Initialize the TableProcessor and process table data
    table_processor = TableProcessor()
    table_processor.process_table_data()
    table_processing_duration = time.time() - start_time
    print(f"Table processing time: {table_processing_duration:.2f} seconds")

    start_time = time.time()
    # Filter and match data between text and table
    filtered_data = table_processor.filter_matching_data(text_processor.data)

    # Save the filtered data to a JSON file
    filtered_output_file = 'filtered_data.json'
    table_processor.save_data_to_json(filtered_data, filtered_output_file)
    filtering_and_saving_duration = time.time() - start_time
    print(f"Filtering and saving time: {filtering_and_saving_duration:.2f} seconds")

    total_duration = video_duration + text_processing_duration + web_scraping_duration + table_processing_duration + filtering_and_saving_duration
    print(f"Total execution time: {total_duration:.2f} seconds")

    print(f"Filtered data saved to {filtered_output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Genshin Impact achievements data.")
    parser.add_argument("video_path", help="Path to the video file")
    args = parser.parse_args()

    run(args.video_path)
