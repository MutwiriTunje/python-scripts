import tkinter as tk
from tkinter import filedialog
import pypandoc
from docx import Document as DocxDocument
from PIL import Image, ImageDraw
import os

# Function to select file
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a Word Document", filetypes=[("Word files", "*.docx")])
    return file_path

# Function to check if file is in use
def is_file_in_use(file_path):
    try:
        os.rename(file_path, file_path)
        return False
    except OSError:
        return True

# Function to convert DOCX to PDF
def convert_docx_to_pdf(file_path, output_path):
    pypandoc.convert_file(file_path, 'pdf', outputfile=output_path)

# Function to convert DOCX to images
def convert_docx_to_images(file_path, output_dir):
    doc = DocxDocument(file_path)
    for i, paragraph in enumerate(doc.paragraphs):
        image_path = os.path.join(output_dir, f"page_{i+1}.png")
        img = Image.new('RGB', (800, 100), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((10,10), paragraph.text, fill=(0,0,0))
        img.save(image_path)

# Select the file
file_path = select_file()

# Check if the file is in use
if is_file_in_use(file_path):
    print(f"The file {file_path} is currently in use. Please close any applications using the file and try again.")
else:
    # Convert DOCX to PDF
    pdf_output_path = filedialog.asksaveasfilename(
        title="Save PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile="output.pdf"
    )
    if pdf_output_path:
        convert_docx_to_pdf(file_path, pdf_output_path)
        print(f"PDF saved to: {pdf_output_path}")

    # Convert DOCX to images
    image_output_dir = filedialog.askdirectory(title="Select Directory to Save Images")
    if image_output_dir:
        convert_docx_to_images(file_path, image_output_dir)
        print(f"Images saved to: {image_output_dir}")
