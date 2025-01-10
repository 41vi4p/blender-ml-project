# This file provides utility functions used throughout the pipeline, such as image transformations and logging.

import logging
from PIL import Image
import torchvision.transforms as transforms

def setup_logging(log_file='app.log'):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def load_image(image_path):
    """Load an image from the specified path."""
    try:
        image = Image.open(image_path).convert('RGB')
        return image
    except Exception as e:
        logging.error(f"Error loading image {image_path}: {e}")
        return None

def transform_image(image):
    """Apply transformations to the image."""
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    return transform(image)