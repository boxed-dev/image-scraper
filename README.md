
# Web Image Scraper

A Python application and a Flask API to scrape images from a given URL and download them to a specified directory.

🚀 Kickstart your image scraping project with this easy-to-use tool.

## Table of Contents

- Features
- Getting Started
- Flask API
  - Scrape Images Route
- Standalone Script
- Example Usage

## Features

✅ Scrape images from a URL.

✅ Download images to a specified directory.

✅ Flask API to provide image scraping as a service.

## Getting Started

To get started with this image scraper, follow these steps:

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/web-image-scraper.git
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the Flask API or the standalone script.

## Flask API

### Scrape Images Route

The Flask API provides a `POST` route for scraping images from a URL and returning the URLs of images larger than 5KB. 

**Endpoint:** `/scrape`

**Method:** POST

**Request JSON Payload:**
```json
{
  "url": "https://example.com"
}
```

**Response JSON:**
```json
{
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.png"
  ]
}
```

📝 Example usage:
```python
import requests

url = 'http://localhost:5000/scrape'
data = {'url': 'https://example.com'}

response = requests.post(url, json=data)
print(response.json())
```

## Standalone Script

The standalone script `scrape_images.py` allows you to scrape images from a URL and download them to a specified directory on your local system.

📝 Example usage:

```sh
python scrape_images.py
```
