import cv2
import pandas as pd
import albumentations as A
from .deduplicate import find_duplicates

def preprocess_data(raw_dir, processed_dir, csv_path):
    # Remove duplicates
    dupes = find_duplicates(raw_dir, csv_path)
    print(f"Removed {len(dupes)} duplicates")

    # Load annotations
    df = pd.read_csv(csv_path)
    
    # Create augmentation pipeline
    transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.Rotate(limit=20, p=0.3),
        A.RandomBrightnessContrast(p=0.2),
        A.CLAHE(p=0.3)
    ], bbox_params=A.BboxParams(format='pascal_voc'))

    # Process images
    for idx, row in df.iterrows():
        img_path = os.path.join(raw_dir, row['image_name'])
        img = cv2.imread(img_path)
        
        # Apply augmentations
        transformed = transform(
            image=img,
            bboxes=[[row['x0'], row['y0'], row['x1'], row['y1']]]
        )
        
        # Save processed image
        output_path = os.path.join(processed_dir, row['image_name'])
        cv2.imwrite(output_path, transformed['image'])
        
        # Update CSV with new coordinates
        if transformed['bboxes']:
            df.at[idx, 'x0'], df.at[idx, 'y0'], df.at[idx, 'x1'], df.at[idx, 'y1'] = transformed['bboxes'][0]

    # Save updated CSV
    df.to_csv(os.path.join(processed_dir, 'processed_annotations.csv'), index=False)
