from pypdf import PdfWriter
from tkinter import filedialog, messagebox
import tkinter as tk

# Initialize the writer
merger = PdfWriter()

#GUI for PDF merger app
window = tk.Tk()

window.title("PDF Merger App")
window.geometry("500x500")

# I need to put the selected paths here
file_selected = []
def opendialoguebox():
    file_selected = filedialog.askopenfilenames(
        title= "Select PDF files",
        filetypes= [("PDF Files", ".pdf")]

    )
    return file_selected

def merge_pdfs_function():
    # Append each PDF to the merger
    for pdf in file_selected:
        merger.append(pdf)

    # Write out the combined PDF
    merger.write("merged_output.pdf")
    merger.close()


label = tk.Label(window, text="Merge You PDFs Here", font=("Montserrat", 20),)

label.pack()

select_pdfs_button= tk.Button(
    window,
    text="Select PDFs",
    command=opendialoguebox,
    padx=5,  # Horizontal padding inside the button
    pady=5,   # Vertical padding inside the button
)

merge_pdfs_button = tk.Button(
    window,
    text="Merge PDFs",
    command=merge_pdfs_function,
    padx=5,  # Horizontal padding inside the button
    pady=5,   # Vertical padding inside the button
)

select_pdfs_button.pack()
merge_pdfs_button.pack()

window.mainloop()


