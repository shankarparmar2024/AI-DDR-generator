"""
extract_data.py

This script extracts:
1. Text content from the PDF
2. Images from the PDF

We use PyMuPDF (fitz) because it can easily extract both text and images.
"""

import fitz  # PyMuPDF
import os


def extract_text_and_images(pdf_path, output_folder):
    """
    Extracts all text and images from a PDF file.

    Args:
        pdf_path (str): path to the PDF file
        output_folder (str): folder where images will be saved

    Returns:
        full_text (str): all extracted text
        image_paths (list): list of saved image file paths
    """

    # Open the PDF document
    doc = fitz.open(pdf_path)

    full_text = ""
    image_paths = []

    # Loop through each page in the PDF
    for page_index in range(len(doc)):

        page = doc.load_page(page_index)

        # Extract text from the page
        text = page.get_text()
        full_text += text + "\n"

        # Extract images from the page
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            # Get image reference
            xref = img[0]

            # Extract the image bytes
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Create a filename for the image
            image_filename = os.path.join(
                output_folder,
                f"page{page_index+1}_image{img_index+1}.png"
            )

            # Save image to disk
            with open(image_filename, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_filename)

    return full_text, image_paths