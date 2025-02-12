#!/bin/bash

# Navigate to project directory
cd ~/human-face-detection

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install core requirements
echo "Installing Python packages..."
pip install --upgrade pip
pip install numpy opencv-python-headless streamlit ultralytics fiftyone albumentations plotly python-dotenv

# Setup fiftyone database
fiftyone db create

echo -e "\n\033[1;32mSetup complete! Run \033[1;34msource venv/bin/activate\033[0m to activate virtual environment."
