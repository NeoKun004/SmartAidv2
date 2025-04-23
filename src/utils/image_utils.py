# File path: src/utils/image_utils.py
import os
import base64
from PIL import Image
import requests

def load_local_image(image_path):
    """Load a local image"""
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        return None

def get_image_base64(image_path):
    """Convert an image to base64 for embedding in HTML"""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    else:
        return ""

def get_base64_of_bin_file(bin_file):
    """Convert a binary file to base64"""
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

def get_img_with_href(url):
    """Get base64 encoding of an image from URL"""
    try:
        response = requests.get(url)
        img_data = response.content
        return base64.b64encode(img_data).decode()
    except:
        return ""

# Try to load the images from common paths
try:
    dyscalc_b64 = get_image_base64("/home/ubuntu/side/SmartAid/data/dyscalc.png")
except:
    dyscalc_b64 = ""

try:
    dtha_b64 = get_image_base64("/home/ubuntu/side/SmartAid/data/dtha.png")
except:
    dtha_b64 = ""

# If images couldn't be loaded, provide fallback paths
if not dyscalc_b64:
    try:
        dyscalc_b64 = get_image_base64("data/dyscalc.png")
    except:
        dyscalc_b64 = ""

if not dtha_b64:
    try:
        dtha_b64 = get_image_base64("data/dtha.png")
    except:
        dtha_b64 = ""

# Add dyslexie image with the same pattern
try:
    dyslexie_b64 = get_image_base64("/home/ubuntu/side/SmartAid/data/dyslexie.png")
except:
    dyslexie_b64 = ""

if not dyslexie_b64:
    try:
        dyslexie_b64 = get_image_base64("data/dyslexie.png")
    except:
        dyslexie_b64 = ""

# If still no image, provide a placeholder base64
if not dyslexie_b64:
    dyslexie_b64 = """
    iVBORw0KGgoAAAANSUhEUgAAASwAAAD6CAYAAAAbbXrzAAAABGdBTUEAALGPC/SxoQAAAWFJREFUeJzt1DEBACAMwDDAv+dxIoEeiYK+2d0zAQL+dwMAHoYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZCzn0QJm8zHRjwAAAABJRU5ErkJggg==
    """

# Add dysgraphie image with the same pattern
try:
    dysgraphie_b64 = get_image_base64("/home/ubuntu/side/SmartAid/data/dysgraphie.png")
except:
    dysgraphie_b64 = ""

if not dysgraphie_b64:
    try:
        dysgraphie_b64 = get_image_base64("data/dysgraphie.png")
    except:
        dysgraphie_b64 = ""

# If still no image, provide a placeholder base64
if not dysgraphie_b64:
    dysgraphie_b64 = """
    iVBORw0KGgoAAAANSUhEUgAAASwAAAD6CAYAAAAbbXrzAAAABGdBTUEAALGPC/SxoQAAAWFJREFUeJzt1DEBACAMwDDAv+dxIoEeiYK+2d0zAQL+dwMAHoYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZBgWkGFYQIZhARmGBWQYFpBhWECGYQEZhgVkGBaQYVhAhmEBGYYFZCzn0QJm8zHRjwAAAABJRU5ErkJggg==
    """

def set_background_image(image_path):
    """
    Set a background image for the Streamlit app.
    
    Args:
        image_path (str): Path to the image file
    """
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
        
        encoded_img = base64.b64encode(img_bytes).decode()
        
        page_bg_img = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        print(f"Background image file not found: {image_path}")