import tkinter as tk
from tkinter import filedialog
from docx import Document
from fpdf import FPDF

def convert_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.add_font('Arial', '', 'arial.tff', uni=True)
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)

    pdf.output(pdf_path)

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select Word File",
        filetypes=(("Word files", "*.docx"), ("All files", "*.*"))
    )
    if file_path:
        save_path = filedialog.asksaveasfilename(
            title="Save PDF As",
            defaultextension=".pdf",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        if save_path:
            convert_to_pdf(file_path, save_path)
            print(f"File converted and saved as {save_path}")

if __name__ == "__main__": 
    select_file()
