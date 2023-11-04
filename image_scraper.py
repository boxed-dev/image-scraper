import requests
import re
import os

def scrape_images(url, output_dir):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Extract image URLs from network traffic
    image_urls = re.findall(r'https?://[^\s/$.?#].[^\s]*\.(?:jpg|png|gif|jpeg)', response.text)
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download and save each image
    for image_url in image_urls:
        image_filename = image_url.split('/')[-1]
        image_path = os.path.join(output_dir, image_filename)
        image_response = requests.get(image_url)
        
        # Check if the image size is greater than 5KB
        if len(image_response.content) > 5000:
            with open(image_path, 'wb') as f:
                f.write(image_response.content)
                print(f"Downloaded: {image_filename}")

# Example usage
url = 'https://www.nike.com/'
output_dir = 'images'
scrape_images(url, output_dir)