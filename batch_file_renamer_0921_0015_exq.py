# 代码生成时间: 2025-09-21 00:15:39
import os
import re
from pathlib import Path
import gradio as gr

"""
A batch file renamer tool using GrADIO framework.
This tool allows users to select multiple files and specify a new pattern for renaming.
"""

class BatchFileRenamer:
    def __init__(self, directory):
        """Initialize the class with the directory containing files to rename."""
        self.directory = directory
        self.files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    def rename_files(self, prefix):
        """Rename the files in the directory with a given prefix."""
        try:
            for i, file in enumerate(self.files):
                # Construct new filename with prefix and original file extension
                new_filename = f"{prefix}_{i + 1}{os.path.splitext(file)[1]}"
                # Rename the file
                os.rename(os.path.join(self.directory, file), os.path.join(self.directory, new_filename))
            return f"Successfully renamed {len(self.files)} files."
        except Exception as e:
            return f"An error occurred: {e}"

# Set the directory containing the files
directory_path = "./"  # Change to your desired directory
renamer = BatchFileRenamer(directory_path)

# GrADIO interface
def rename_file(input_files, new_prefix):
    """Function to handle file renaming."""
    # Update the directory path and files list based on user input
    renamer.directory = "./"  # Directory path should be updated here if different
    renamer.files = [f for f in os.listdir(renamer.directory) if os.path.isfile(os.path.join(renamer.directory, f)) and f in input_files]
    # Rename the selected files
    return renamer.rename_files(new_prefix)

iface = gr.Interface(
    fn=rename_file,
    inputs=[gr.File(file_count="multiple"), gr.Textbox(label="New Prefix")],
    outputs="text",
    title="Batch File Renamer",
    description="Select multiple files to rename them with a new prefix.",
)

# Run the GrADIO interface
iface.launch()