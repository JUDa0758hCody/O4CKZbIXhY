# 代码生成时间: 2025-09-08 14:20:45
import os
import shutil
from gradio import gr
from datetime import datetime

"""
Data Backup and Restore Application

This application allows users to backup and restore data using the Gradio framework.
It provides a simple interface for users to select files or directories for backup and
restore operations.
"""

class DataBackupRestore:
    def __init__(self):
        # Create backup directory if it does not exist
        self.backup_dir = "backups"
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def backup(self, file_path):
        """
        Backs up the selected file or directory to the backup directory.
        
        Args:
            file_path (str): The path to the file or directory to backup.
        """
        try:
            # Create a timestamped backup directory
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = os.path.join(self.backup_dir, timestamp)
            if os.path.isdir(file_path):
                shutil.copytree(file_path, backup_path)
            else:
                shutil.copy2(file_path, backup_path)
            return f"Backup successful: {backup_path}"
        except Exception as e:
            return f"Backup failed: {str(e)}"

    def restore(self, backup_path):
        """
        Restores the selected backup to its original location.
        
        Args:
            backup_path (str): The path to the backup to restore.
        """
        try:
            # Extract the original file path from the backup path
            original_path = os.path.relpath(backup_path, self.backup_dir)
            if os.path.isdir(backup_path):
                shutil.rmtree(original_path)
                shutil.copytree(backup_path, original_path)
            else:
                os.remove(original_path)
                shutil.copy2(backup_path, original_path)
            return f"Restore successful: {original_path}"
        except Exception as e:
            return f"Restore failed: {str(e)}"

# Create an instance of the DataBackupRestore class
app = DataBackupRestore()

# Define the Gradio interface
demo = gr.Interface(
    fn=app.backup,
    inputs=gr.Textbox(label="File/Directory Path"),
    outputs="text",
    title="Data Backup and Restore"
)

# Add a restore button
restore_button = gr.Button("Restore").click(
    fn=app.restore,
    inputs=[gr.Textbox(label="Backup Path