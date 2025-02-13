import sys
import os
sys.path.append('src')  # Add this line

from preprocessing.validate import validate_dataset
from preprocessing.preprocess import preprocess_data
from preprocessing.convert_yolo import convert_to_yolo

def convert_to_yolo(processed_dir, output_dir):
    # Create directories if they don't exist
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)
    
    # Rest of your conversion code

if __name__ == "__main__":
    raw_dir = "data/raw"
    processed_dir = "data/processed"
    csv_path = "data/raw/face.csv"
    yolo_dir = "data/yolo"
    
    # 1. Validate dataset
    validate_dataset(csv_path, raw_dir)
    
    # 2. Remove duplicates and process
    preprocess_data(raw_dir, processed_dir, csv_path)
    
    # 3. Convert to YOLO format
    convert_to_yolo(processed_dir, yolo_dir)
    
    print("Pipeline executed successfully!")
