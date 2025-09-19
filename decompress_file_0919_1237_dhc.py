# 代码生成时间: 2025-09-19 12:37:41
import os
import zipfile
import tarfile
from gradio import Interface, components

"""
A Gradio interface for a file decompression tool.
This program can decompress zip and tar files."""

class Decompressor:
    def __init__(self, output_dir=""):
        self.output_dir = output_dir

    def decompress(self, input_file):
        """Decompresses a given file."""
        file_path = input_file.name
        file_extension = file_path.split('.')[-1]

        try:
            if file_extension == "zip":
                self._decompress_zip(file_path)
            elif file_extension == "tar":
                self._decompress_tar(file_path)
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            return str(e)

    def _decompress_zip(self, path):
        """Decompresses a zip file."""
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(self.output_dir)
            return f"Decompressed {path} successfully."

    def _decompress_tar(self, path):
        """Decompresses a tar file."""
        with tarfile.open(path, 'r') as tar_ref:
            tar_ref.extractall(self.output_dir)
            return f"Decompressed {path} successfully."

# Initialize the decompressor with an output directory
decompressor = Decompressor(output_dir="decompressed_files/")

# Create a Gradio interface
iface = Interface(
    fn=decompressor.decompress,
    inputs=components.File(label="Upload file"),
    outputs="text",
    title="File Decompression Tool",
    description="Upload zip or tar file to decompress."
)

# Run the interface
iface.launch()