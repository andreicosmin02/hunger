from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup

# Set up the web driver (ensure the driver path is correct)
driver_path = './chromedriver.exe'  # Update this with your actual driver path
browser = webdriver.Chrome()

# Open the website
url = 'https://emojikitchen.dev/'
browser.get(url)

# Press on the emoji you want
# then press enter in the console to continue
input()

# Scroll down to load all images (you might need to adjust the number of scrolls)
for _ in range(5):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'html.parser')

# Find all elements with class 'MuiImageListItem-img'
image_elements = soup.find_all('img', class_='MuiImageListItem-img')

# Create a directory to save the images
output_dir = 'farfurie_images'
os.makedirs(output_dir, exist_ok=True)

# Download the images
for idx, image_element in enumerate(image_elements):
    image_url = image_element['src']
    if image_url[-3:] != "png":
        continue

    response = requests.get(image_url)
    if response.status_code == 200:
        image_filename = os.path.join(output_dir, f'image_{idx}.png')
        with open(image_filename, 'wb') as f:
            f.write(response.content)
        print(f'Downloaded: {image_filename}')
    else:
        print(f'Failed to download image {idx}.')

# Close the browser
browser.quit()

