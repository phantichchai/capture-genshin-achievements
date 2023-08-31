# process/processor.py

import argparse
import time
import os
from .video_processor import VideoProcessor
from .text_processor import TextProcessor
from .table_processor import TableProcessor
from .web_scraper import WebScraper

def run_video_processor(video_path) -> (VideoProcessor, str):
    json_data_folder = "json_data"
    if not os.path.exists(json_data_folder):
        os.makedirs(json_data_folder)

    start_time = time.time()
    video_processor = VideoProcessor(video_path)
    video_processor.process_video()
    video_duration = time.time() - start_time
    return video_processor, f"Video processing time: {video_duration:.2f} seconds"

def run_text_processor(temp_folder_path) -> (TextProcessor, str):
    start_time = time.time()
    text_processor = TextProcessor(temp_folder_path)
    text_processor.process_text_data()
    text_processing_duration = time.time() - start_time
    return text_processor, f"Text processing time: {text_processing_duration:.2f} seconds"

def run_web_scraper() -> str:
    start_time = time.time()
    table_scraper = WebScraper(url='https://genshin-impact.fandom.com/wiki/Wonders_of_the_World', output_file='table_data.json')
    table_scraper.scrape_table_data()
    web_scraping_duration = time.time() - start_time
    return f"Web scraping time: {web_scraping_duration:.2f} seconds"

def run_table_processor() -> (TableProcessor, str):
    start_time = time.time()
    table_processor = TableProcessor()
    table_processor.process_table_data()
    table_processing_duration = time.time() - start_time
    return table_processor, f"Table processing time: {table_processing_duration:.2f} seconds"

def find_and_save_matching_data(table_processor, text_data) -> str:
    start_time = time.time()
    (uncompleted_achievement_data, completed_achievement_data) = table_processor.find_matching_data(text_data)
    uncompleted_output_file = os.path.join('json_data', 'uncompleted_achievement_data.json')
    table_processor.save_data_to_json(uncompleted_achievement_data, uncompleted_output_file)
    completed_output_file = os.path.join('json_data', 'completed_achievement_data.json')
    table_processor.save_data_to_json(completed_achievement_data, completed_output_file)
    finding_and_saving_duration = time.time() - start_time
    print(f"Uncompleted data saved to {uncompleted_output_file}")
    print(f"Completed data saved to {completed_output_file}")
    return f"Finding and saving time: {finding_and_saving_duration:.2f} seconds"

def run(video_path):
    (video_processor, _) = run_video_processor(video_path)
    text_processor = run_text_processor(video_processor.temp_folder_path)
    run_web_scraper()
    table_processor = run_table_processor()
    text_data = text_processor.data
    find_and_save_matching_data(table_processor, text_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Genshin Impact achievements data.")
    parser.add_argument("video_path", help="Path to the video file")
    args = parser.parse_args()

    run(args.video_path)
