from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_images():
    url = request.json['url']
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Extract image URLs from network traffic
    image_urls = re.findall(r'https?://[^\s/$.?#].[^\s]*\.(?:jpg|png|gif|jpeg)', response.text)
    
    # List to store URLs of images larger than 5KB
    large_image_urls = []
    
    # Check each image
    for image_url in image_urls:
        image_response = requests.get(image_url)
        
        # Check if the image size is greater than 5KB
        if len(image_response.content) > 5000:
            large_image_urls.append(image_url)
    
    return jsonify(large_image_urls)

if __name__ == '__main__':
    app.run(debug=True)