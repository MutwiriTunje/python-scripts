import tkinter as tk
from tkinter import filedialog
from spire.doc import Document, FileFormat
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
    document.load_from_file(file_path)

    # Save the document as a PDF
    output_path = file_path.replace(".docx", ".pdf")
    document.save_to_file(output_path, FileFormat.PDF)

    print(f"PDF saved to: {output_path}")
