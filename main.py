import os
import shutil
import tkinter as tk
from tkinter import filedialog, PhotoImage

def set_background(image_path):
    bg_image = PhotoImage(file=image_path)
    background_label = tk.Label(window, image=bg_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = bg_image

def set_logo(image_path):
    logo = PhotoImage(file=image_path)
    logo = logo.zoom(1)  # Set zoom factor to 1 (no resizing)
    logo_label = tk.Label(window, image=logo)
    logo_label.place(relx=0.5, rely=0.4, anchor="center")  # Center the logo with some spacing
    logo_label.image = logo

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
        '.exe': 'Executables',
        '.rar': 'Archives',
        '.tar': 'Archives',
        '.gz': 'Archives',
        '.pdf': 'PDFs',
        '.jpg': 'Images',
        '.jpeg': 'Images',
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
    })

    # Create a backup directory
    backup_dir = os.path.join(source_dir, 'Backup')
    os.makedirs(backup_dir, exist_ok=True)

    # Move the original files to the backup directory
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            src = os.path.join(root, filename)
            dest = os.path.join(backup_dir, filename)
            shutil.move(src, dest)

    # Create folders for organization
    for ext, folder in file_types.items():
        os.makedirs(os.path.join(source_dir, folder), exist_ok=True)

    # Move files to their corresponding folders
    for root, dirs, files in os.walk(backup_dir):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            folder = file_types.get(ext.lower())
            if folder:
                src = os.path.join(root, filename)
                dest = os.path.join(source_dir, folder, filename)
                shutil.move(src, dest)
            else:
                print(f"Skipping '{filename}' (no folder specified).")

def undo_organization(source_dir):
    backup_dir = os.path.join(source_dir, 'Backup')
    if not os.path.exists(backup_dir):
        print("No backup directory found.")
        return

    for root, dirs, files in os.walk(backup_dir):
        for filename in files:
            src = os.path.join(root, filename)
            dest = os.path.join(source_dir, filename)
            shutil.move(src, dest)

    shutil.rmtree(backup_dir)
    print("Undo complete.")

def browse_button():
    source_directory = filedialog.askdirectory(initialdir=default_directory)
    if source_directory:
        organize_files(source_directory, file_types)
        status_label.config(text="File organization completed.")

def undo_button():
    source_directory = filedialog.askdirectory(initialdir=default_directory)
    if source_directory:
        undo_organization(source_directory)
        status_label.config(text="Undo completed. Files restored to their original locations.")

# Create a GUI window
window = tk.Tk()
window.title("Sortify")

# Set the background image
set_background("your_background.png")

# Set the Sortify logo with spacing
set_logo("logo.png")  # Replace with your logo file name

# Define configuration directly in the script
default_directory = os.getcwd()
file_types = {
    '.txt': 'TextFiles',
    '.pdf': 'PDFs',
    # ... (rest of your file types)
}

# Create a label to display the status
status_label = tk.Label(window, text="", fg="green")
status_label.pack()

# Create spacing between the logo and the "Browse" button
spacing_label = tk.Label(window, text="", height=1)
spacing_label.pack()

# Create "Browse" and "Undo" buttons with increased size and centered
browse_button = tk.Button(window, text="Browse", command=browse_button, height=2, width=20, font=("Helvetica", 12))
browse_button.place(relx=0.5, rely=0.6, anchor="center")

undo_button = tk.Button(window, text="Undo", command=undo_button, height=2, width=20, font=("Helvetica", 12))
undo_button.place(relx=0.5, rely=0.7, anchor="center")

# Run the GUI main loop
window.mainloop()
