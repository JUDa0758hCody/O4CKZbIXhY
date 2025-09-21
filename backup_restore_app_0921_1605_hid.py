# 代码生成时间: 2025-09-21 16:05:41
import gradio as gr
import shutil
import os
from datetime import datetime

"""
A Gradio application for backing up and restoring data.
Includes error handling, comments, and follows Python best practices.
"""

class DataBackupRestore:
    def __init__(self, backup_dir="./backups"):
        self.backup_dir = backup_dir
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        self.backup_count = 0

    def backup_data(self, file_path):
        """
        Backup the specified file or directory.
        :param file_path: Path to the file or directory to backup.
        :return: A success or error message.
        """
        try:
            backup_time = datetime.now().strftime("%Y%m%d%H%M%S")
            backup_name = f"backup_{backup_time}.zip"
            backup_path = os.path.join(self.backup_dir, backup_name)
            shutil.make_archive(backup_path, 'zip', file_path)
            self.backup_count += 1
            return f"Backup created successfully: {backup_name}"
        except Exception as e:
            return f"Error occurred during backup: {str(e)}"

    def restore_data(self, backup_file_path):
        """
        Restore data from a specified backup file.
        :param backup_file_path: Path to the backup file to restore from.
        :return: A success or error message.
        """
        try:
            shutil.unpack_archive(backup_file_path, self.backup_dir)
            return f"Data restored successfully from: {backup_file_path}"
        except Exception as e:
            return f"Error occurred during restore: {str(e)}"

    def list_backups(self):
        """
        List all available backup files.
        :return: A list of backup files.
        """
        backup_files = [f for f in os.listdir(self.backup_dir) if f.endswith(".zip")]
        return backup_files

# Create a Gradio interface for the application
iface = gr.Interface(
    fn=lambda: "Welcome to the Data Backup and Restore application!",
    inputs="text",
    outputs="text",
    title="Data Backup and Restore Application"
)

# Add components for backup and restore functionality
iface.add_component(
    fn=DataBackupRestore.backup_data, 
    inputs=["file", "text"], 
    outputs="text", 
    title="Backup Data"
)
iface.add_component(
    fn=DataBackupRestore.restore_data, 
    inputs=["file", "text"], 
    outputs="text", 
    title="Restore Data"
)
iface.add_component(
    fn=DataBackupRestore.list_backups, 
    inputs=[], 
    outputs="list", 
    title="List Backups"
)

# Launch the application
iface.launch(share=True)