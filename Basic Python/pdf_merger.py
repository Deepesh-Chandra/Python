from pypdf import PdfWriter
from tkinter import filedialog, messagebox
import tkinter as tk
import os;



#GUI for PDF merger app
window = tk.Tk()

window.title("PDF Merger App")
window.geometry("500x500")


def opendialoguebox():
    pdf_selected = filedialog.askopenfilenames(
        title= "Select PDF files",
        filetypes= [("PDF Files", ".pdf")]
    )
    if pdf_selected:
        selected_pdfs.delete(0, tk.END)
        for pdf in pdf_selected:
            selected_pdfs.insert(tk.END, pdf)

def merge_pdfs_function():

    #get PDFs from pdf_list
    pdfs=list(selected_pdfs.get(0, tk.END))

    if not pdfs:
        messagebox.showerror("Error", "Kindly select the PDF files.")
        return;

    # Initialize the writer
    merger = PdfWriter()

    try:
        # Append each PDF to the merger
        for pdf in pdfs:
            merger.append(pdf)

        output_filename = filedialog.asksaveasfilename(
            defaultextension = ".pdf",
            filetypes = [("PDF files", "*.pdf")],
            title = "Save your merged PDF as"
        )
        print(">>>>", output_filename)
        if output_filename:
            # Write out the combined PDF
            merger.write(output_filename)
            merger.close()

            #Showing success message
            messagebox.showinfo("Success", f"You PDFs have been merged as {os.path.basename(output_filename)}")

        


    except Exception as e:

        messagebox.showerror("Error", f"An error occured {str(e)}.")
        
        

label = tk.Label(window, text="Merge You PDFs Here", font=("Montserrat", 20),)

label.pack()

# Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Creating canvas
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

#creating content frame
content_frame = tk.Frame(canvas)
canvas.create_window(
    (0, 0),
    window=content_frame,
    anchor="nw"
)

# Tell scrollbar to control Canvas
scrollbar.config(command=canvas.yview)

#PDF Selection button
select_pdfs_button= tk.Button(
    content_frame,
    text="Select PDFs",
    command=opendialoguebox,
    padx=5,  # Horizontal padding inside the button
    pady=5,   # Vertical padding inside the button
)

select_pdfs_button.pack()

selected_pdfs= tk.Listbox(
    content_frame,
    selectmode=tk.MULTIPLE,
    width= 50,
    height= 10
)

selected_pdfs.pack()

#PDF Merge button
merge_pdfs_button = tk.Button(
    content_frame,
    text="Merge PDFs",
    command=merge_pdfs_function,
    padx=5,  # Horizontal padding inside the button
    pady=5,   # Vertical padding inside the button
)

merge_pdfs_button.pack()

#Telling canvas to scroll all the content inside the canvas with scroller
canvas.configure(scrollregion=canvas.bbox("all"))

#Scrollbar


window.mainloop()


