import pdfplumber
import os
import requests
from PIL import Image
from io import BytesIO

def download_and_save_image(url, path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base}_{counter}{ext}"
        counter += 1
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save(path)
            print(f"Saved {path}")
        else:
            print(f"Failed to download {url}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the PDF file name to the name of your PDF file
pdf_name = "Danna Aguilar_Install Photos - SOLRITE_20240612100635.pdf"
pdf_path = os.path.join(script_dir, pdf_name)

output_dir = os.path.join(script_dir, 'Images', pdf_name.split('_')[0])
os.makedirs(output_dir, exist_ok=True)

with pdfplumber.open(pdf_path) as pdf:
    image_data = []
    for page_number, page in enumerate(pdf.pages):
        print(f"Page {page_number + 1} text extracted")
        if page.annots:
            for annot in page.annots:
                if 'uri' in annot and annot['uri']:
                    url = annot['uri'].replace('\x00', '')  # Clean the URL
                    filename = f"Page{page_number + 1}_Image{len(image_data) + 1}.png"
                    filepath = os.path.join(output_dir, filename)
                    image_data.append((url, filepath))

for url, filepath in image_data:
    download_and_save_image(url, filepath)

print("Image extraction complete.")
