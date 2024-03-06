import customtkinter
import tkinter
import os
import shutil
import json

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set the default path
        self.path = "C:\\Users\\Alex Shapiro\\Downloads"

        # GUI Frame
        self.title("Automatic File Sorter")
        self.geometry(f"{970}x{550}")

        # Configure grid weights
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.resizable(False, True)

        # Logo Frame
        self.logo_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.logo_frame.grid(row=0, column=0, sticky="nsew")
        self.logo_frame.grid_rowconfigure(0, weight=1)
        self.logo_frame.grid_columnconfigure(0, weight=1)

        # Application logo
        self.logo_label = customtkinter.CTkLabel(self.logo_frame, text="Automatic File Sorter", font=("Arial Black", 25), text_color="#116fa5")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(5, 0), sticky="n")

        #Folders Frame
        self.folders_title_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.folders_title_frame.grid(row=0, column=1, sticky="nsew")
        self.folders_title_frame.grid_rowconfigure(0, weight=1)
        self.folders_title_frame.grid_columnconfigure(0, weight=1)

        # Instructions Frame
        self.instructions_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.instructions_frame.grid(row=1, column=0, sticky="nsew")
        self.instructions_frame.grid_rowconfigure(0, weight=0)
        self.instructions_frame.grid_rowconfigure(1, weight=1)

        # Application instructions
        instructions_text = """
        Welcome to the Automatic File Sorter!

        To use this application, follow these steps:
        1. Enter the file explorer path in the 'File Explorer Path' field.
        2. Click the 'Store Path' button to set the path.
        3. Make sure your "config.json" file is in the same Directory as this executable.
        4. Check the file categories you want to organize.
        5. Click 'Organize Files' to move files to corresponding folders.
        (Folders will be made for you in the selected path.)
        6. You can go in config and add/remove folders and file extensions.
        """
        instructions_label = customtkinter.CTkLabel(self.instructions_frame, text=instructions_text, anchor="w", justify="left", font=("Arial Bold", 13))
        instructions_label.grid(row=1, column=0, padx=(0,15), pady=(5, 10), sticky="nsew")

        # Checkboxes Frame
        self.checkbox_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.checkbox_frame.grid(row=1, column=1, rowspan=3, sticky="nsew")
        self.checkbox_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

        # Title for the checkboxes frame
        checkbox_title_label = customtkinter.CTkLabel(self.folders_title_frame, text="Folders:", font=("Arial Black", 25), text_color="#116fa5")
        checkbox_title_label.grid(row=0, column=0, padx=(10, 20), pady=(5, 5), sticky="nsew")

        # Load folder names and file extensions from the configuration file
        with open("config.json", "r") as config_file:
            self.config_data = json.load(config_file)

        # Create checkboxes with specified names and file extensions
        self.checkboxes = []
        for i, (name, exts) in enumerate(self.config_data["folders"].items()):
            checkbox_text = f"{name} ({', '.join(exts)})"
            checkbox = customtkinter.CTkCheckBox(master=self.checkbox_frame, text=checkbox_text, corner_radius=36, font=("Arial Bold", 14))
            checkbox.grid(row=i + 1, column=0, pady=(5, 5), padx=(10, 20), sticky="w")
            self.checkboxes.append(checkbox)

        # Buttons Frame
        self.buttons_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.buttons_frame.grid(row=2, column=0, sticky="nsew")
        self.buttons_frame.grid_columnconfigure((0, 1), weight=1)

        # File Explorer Path
        self.input_line_label = customtkinter.CTkLabel(self.buttons_frame, text="File Explorer Path:", anchor="w", font=("Arial Bold", 14))
        self.input_line_label.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")

        self.input_line_entry = customtkinter.CTkEntry(self.buttons_frame, placeholder_text="C:\\Users\\John-Doe\\Downloads", text_color="orange", font=("Arial Bold", 12))
        self.input_line_entry.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew", columnspan=2)

        # Store Path button
        self.store_path_button = customtkinter.CTkButton(self.buttons_frame, text="Store Path", command=self.store_path, font=("Arial Bold", 14))
        self.store_path_button.grid(row=2, column=0, padx=15, pady=(0, 15), sticky="ew", columnspan=2)

        # Organize button
        self.organize_button = customtkinter.CTkButton(self.buttons_frame, text="Organize Files", command=self.organize_files_button, font=("Arial Bold", 14))
        self.organize_button.grid(row=3, column=0, padx=15, pady=(0, 15), sticky="ew", columnspan=2)

        # Appearance mode and UI scaling
        self.appearance_mode_label = customtkinter.CTkLabel(self.buttons_frame, text="Appearance Mode:", anchor="w", font=("Arial Bold", 14))
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(0, 5), sticky="w")
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.buttons_frame, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=20, pady=(0, 5), sticky="ew")

        self.scaling_label = customtkinter.CTkLabel(self.buttons_frame, text="UI Scaling:", anchor="w", font=("Arial Bold", 14))
        self.scaling_label.grid(row=6, column=0, padx=20, pady=(5, 0), sticky="w")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.buttons_frame, values=["100%", "75%", "50%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=7, column=0, padx=20, pady=(5, 10), sticky="ew")

    # Functions
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def move_file(self, file, destination_folder):
        destination_path = os.path.join(self.path, destination_folder, file)
        if os.path.exists(destination_path):
            print(f"File '{file}' already exists in '{destination_folder}'. Skipped.")
        elif file == "Automatic File Sorter.py" or file == "config.json":
            pass
        else:
            shutil.move(os.path.join(self.path, file), destination_path)
            print(f"Moved '{file}' to '{destination_folder}'.")

    def organize_files(self, files, extensions, destination_folder):
        destination_path = os.path.join(self.path, destination_folder)

        # Create the folder if it does not exist
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        for file in files:
            for ext in extensions:
                if ext in file:
                    self.move_file(file, destination_folder)
                    break

    def store_path(self):
        # Get the input value
        input_path = self.input_line_entry.get()

        # Update the class variable 'self.path'
        self.path = input_path

        print(f"Stored path: {self.path}")
        self.input_line_entry.delete(0, tkinter.END)

    def organize_files_button(self):
        # Get a list of all files in the specified path
        file_names = os.listdir(self.path)

        # Load folder names and file extensions from the configuration file
        config_path = os.path.join(script_dir, "config.json")
        with open("config.json", "r") as config_file:
            self.config_data = json.load(config_file)

        # Iterate through folders and organize files based on the selected checkboxes
        for checkbox, (folder, exts) in zip(self.checkboxes, self.config_data["folders"].items()):
            if checkbox.get() == 1:
                self.organize_files(file_names, exts, folder)

        print("Done")

if __name__ == "__main__":
    app = App()
    app.mainloop()
