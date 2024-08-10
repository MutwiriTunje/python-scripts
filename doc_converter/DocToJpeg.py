import tkinter as tk
from tkinter import filedialog
from spire.doc import Document, ImageType
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

# Select the file
file_path = select_file()

# Check if the file is in use
if is_file_in_use(file_path):
    print(f"The file {file_path} is currently in use. Please close any applications using the file and try again.")
else:
    # Create a Document object
    document = Document()

    # Load the selected Word document
    document.LoadFromFile(file_path)

    # Convert the document to a list of image streams
    image_streams = document.SaveImageToStreams(ImageType.Bitmap)

    # Save each image stream to a PNG file with a specified name
    for i, image in enumerate(image_streams, start=1):
        save_path = filedialog.asksaveasfilename(
            title=f"Save Page {i} as",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            initialfile=f"page_{i}.png"
        )
        if save_path:
            with open(save_path, 'wb') as image_file:
                image_file.write(image.ToArray())

    # Close the document
    document.Close()

    print


