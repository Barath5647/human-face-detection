import os
import hashlib
import pandas as pd
from PIL import Image

def find_duplicates(raw_dir, csv_path):
    # Load CSV data
    df = pd.read_csv(csv_path)
    
    # Track hashes and duplicates
    hashes = {}
    duplicates = []
    
    # Process each image
    for img_name in os.listdir(raw_dir):
        img_path = os.path.join(raw_dir, img_name)
        
        # Calculate perceptual hash
        with Image.open(img_path) as img:
            hash = hashlib.md5(img.tobytes()).hexdigest()
            
        if hash in hashes:
            duplicates.append(img_name)
            # Keep the first occurrence
            if img_name not in df['image_name'].values:
                os.remove(img_path)
        else:
            hashes[hash] = img_name
    
    # Filter CSV entries
    df = df[df['image_name'].isin(os.listdir(raw_dir))]
    df.to_csv(csv_path, index=False)
    
    return duplicates
