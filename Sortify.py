import os
import shutil
import tkinter as tk
from tkinter import filedialog, PhotoImage

def set_background(image_path):
    bg_image = PhotoImage(file=image_path)
    background_label = tk.Label(window, image=bg_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = bg_image

def organize_files(source_dir, file_types):
    # Define a dictionary mapping file extensions to folder names
    file_types.update({
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.xls': 'Documents',
        '.xlsx': 'Documents',
        '.ppt': 'Documents',
        '.csv': 'Documents',
        '.zip': 'Archives',
        '.exe': 'Archives',
        '.rar': 'Archives',
        '.tar': 'Archives',
        '.gz': 'Archives',
        # Add more extensions here
    })

    # ... (rest of the file organizer code, same as before)

def browse_button():
    source_directory = filedialog.askdirectory(initialdir=default_directory)
    if source_directory:
        organize_files(source_directory, file_types)
        status_label.config(text="File organization completed.")

# Create a GUI window
window = tk.Tk()
window.title("File Organizer")

# Set the background image
set_background("your_background.png")  # Replace with the actual image file name

# Define configuration directly in the script
default_directory = os.getcwd()
file_types = {
    '.txt': 'TextFiles',
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.gif': 'Images',
    '.png': 'Images',
    '.mp3': 'Music',
    '.wav': 'Music',
    '.flac': 'Music',
    '.aac': 'Music',
    '.ogg': 'Music',
    '.wma': 'Music',
    '.m4a': 'Music',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.mov': 'Videos',
    '.wmv': 'Videos',
    '.flv': 'Videos',
    '.webm': 'Videos',
    '.mpeg': 'Videos',
    '.3gp': 'Videos',
    '.m4v': 'Videos',
    '.divx': 'Videos',
    # Add more extensions here
}

# Create a button to browse for a directory
browse_button = tk.Button(window, text="Browse", command=browse_button)
browse_button.pack(pady=20)

# Create a label to display the status
status_label = tk.Label(window, text="", fg="green")
status_label.pack()

# Run the GUI main loop
window.mainloop()
