import os
import pandas as pd
from PIL import Image

def validate_dataset(csv_path, image_dir):
    df = pd.read_csv(csv_path)
    valid_entries = []
    
    for idx, row in df.iterrows():
        img_path = os.path.join(image_dir, row['image_name'])
        
        if not os.path.exists(img_path):
            print(f"Missing image: {row['image_name']}")
            continue
            
        try:
            with Image.open(img_path) as img:
                if img.width != row['width'] or img.height != row['height']:
                    print(f"Dimension mismatch: {row['image_name']}")
                    continue
                    
                if (row['x1'] <= row['x0'] or row['y1'] <= row['y0']):
                    print(f"Invalid bbox: {row['image_name']}")
                    continue
                    
                valid_entries.append(row)
                
        except Exception as e:
            print(f"Corrupted image: {row['image_name']} - {str(e)}")
    
    valid_df = pd.DataFrame(valid_entries)
    valid_df.to_csv(csv_path, index=False)
    print(f"Validation complete. Remaining entries: {len(valid_df)}")
