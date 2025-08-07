# 代码生成时间: 2025-08-08 00:43:48
import os
import shutil
# TODO: 优化性能
import tarfile
from gradio import Interface, File

"""
A Gradio application that provides data backup and restore functionality.
This program allows users to backup their files by creating a tar archive and
restore their files by extracting the contents of the tar archive.
"""

class DataBackupRestore:
    def __init__(self, backup_dir, restore_dir):
        """
        Initializes the DataBackupRestore object with backup and restore directories.
# 增强安全性
        :param backup_dir: The directory where the backup will be stored.
        :param restore_dir: The directory where the files will be restored from.
# NOTE: 重要实现细节
        """
        self.backup_dir = backup_dir
        self.restore_dir = restore_dir

    def backup(self, source_files):
        """
# 优化算法效率
        Backs up the specified files by creating a tar archive.
        :param source_files: A list of file paths to be backed up.
        :return: The path to the created backup archive.
        """
        try:
            # Create a tar archive
            with tarfile.open(os.path.join(self.backup_dir, 'backup.tar'), 'w') as tar:
                for file in source_files:
# NOTE: 重要实现细节
                    tar.add(file, arcname=os.path.basename(file))
            return os.path.join(self.backup_dir, 'backup.tar')
# 添加错误处理
        except Exception as e:
            raise Exception(f"Backup failed: {str(e)}")

    def restore(self, backup_path):
        """
# 改进用户体验
        Restores the files from the specified backup archive.
        :param backup_path: The path to the backup archive to restore from.
        """
        try:
            # Extract the contents of the tar archive
            with tarfile.open(backup_path, 'r') as tar:
                tar.extractall(self.restore_dir)
        except Exception as e:
            raise Exception(f"Restore failed: {str(e)}")

    def clear_backup(self, backup_path):
# FIXME: 处理边界情况
        """
        Removes the backup archive to free up space.
        :param backup_path: The path to the backup archive to be deleted.
        """
        try:
            os.remove(backup_path)
        except Exception as e:
            raise Exception(f"Failed to delete backup: {str(e)}")

# Define the directories for backup and restore
backup_dir = 'backup'
# NOTE: 重要实现细节
restore_dir = 'restore'

# Create directories if they don't exist
os.makedirs(backup_dir, exist_ok=True)
os.makedirs(restore_dir, exist_ok=True)
# TODO: 优化性能

# Initialize the DataBackupRestore object
data_backup_restore = DataBackupRestore(backup_dir, restore_dir)

# Define the Gradio interface
iface = Interface(
    fn=data_backup_restore.backup,
    inputs=File(label='Select files to backup'),
    outputs='file',
    title='Data Backup',
    description='Backup your files by creating a tar archive.'
)
# NOTE: 重要实现细节

# Define the Gradio interface for restore
restore_iface = Interface(
    fn=data_backup_restore.restore,
    inputs='file',
    outputs='text',
    title='Data Restore',
    description='Restore your files from a backup archive.'
)

# Define the Gradio interface for clearing backup
clear_backup_iface = Interface(
    fn=data_backup_restore.clear_backup,
    inputs='file',
    outputs='text',
    title='Clear Backup',
    description='Remove the backup archive to free up space.'
)

# Launch the Gradio application
# 改进用户体验
iface.launch()
restore_iface.launch()
clear_backup_iface.launch()