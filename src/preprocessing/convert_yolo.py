import pandas as pd
import os

def convert_to_yolo(processed_dir, output_dir):
    df = pd.read_csv(os.path.join(processed_dir, 'processed_annotations.csv'))
    
    # Create YOLO directory structure
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'labels'), exist_ok=True)
    
    for img_name in df['image_name'].unique():
        # Get all boxes for this image
        img_df = df[df['image_name'] == img_name]
        
        # Create label file
        label_path = os.path.join(output_dir, 'labels', img_name.replace('.jpg', '.txt'))
        
        with open(label_path, 'w') as f:
            for _, row in img_df.iterrows():
                # Convert to YOLO format
                width = row['width']
                height = row['height']
                
                x_center = (row['x0'] + row['x1']) / (2 * width)
                y_center = (row['y0'] + row['y1']) / (2 * height)
                box_width = (row['x1'] - row['x0']) / width
                box_height = (row['y1'] - row['y0']) / height
                
                f.write(f"0 {x_center} {y_center} {box_width} {box_height}\n")
        
        # Move image
        os.rename(
            os.path.join(processed_dir, img_name),
            os.path.join(output_dir, 'images', img_name)
        )
