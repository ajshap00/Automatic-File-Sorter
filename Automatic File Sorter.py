import os
import shutil

# Function to move a file to a specified destination folder
def move_file(file, destination_folder):
    destination_path = os.path.join(path, destination_folder, file)
    if os.path.exists(destination_path):
        print(f"File '{file}' already exists in '{destination_folder}'. Skipped.")
    else:
        shutil.move(os.path.join(path, file), destination_path)

# Function to organize files based on their extensions
def organize_files(files, extensions, destination_folder):
    for file in files:
        for ext in extensions:
            if ext in file:
                move_file(file, destination_folder)
                break

# Specify the path where the files are located
path = r"C:/Users/Alex Shapiro/Downloads/"

# Get a list of all files in the specified path
file_names = os.listdir(path)

# Dictionary to store folder names and their corresponding file extensions
folders = {
    'video files': ['.mp4', '.mov'],
    'image files': ['.png', '.jpg', '.jpeg', '.webp'],
    'text files': ['.txt', '.docx'],
    'exe files': ['.exe', '.msi'],
    'java files': ['.java'],
    'powerpoint files': ['.pptx'],
    'zip files': ['.zip'],
    'html & pdf files': ['.html', '.pdf']
}

# Iterate through folders and organize files
for folder, extensions in folders.items():
    destination_path = os.path.join(path, folder)
    # Create the folder if it does not exist already
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    # Organize files based on their extensions
    organize_files(file_names, extensions, folder)
