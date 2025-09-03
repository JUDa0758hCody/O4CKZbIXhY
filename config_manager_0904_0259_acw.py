# 代码生成时间: 2025-09-04 02:59:11
import json
from gradio import Interface
from pathlib import Path

"""
ConfigManager is a utility class for managing configuration files.
It uses Gradio for a simple user interface to load, save, and display configurations.
"""
class ConfigManager:
    def __init__(self, config_file):
        self.config_file = Path(config_file)
        self.config = {}
        self.load_config()

    def load_config(self):
        """Load the configuration from a JSON file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error loading configuration: {e}")
        else:
            print(f"Configuration file not found: {self.config_file}")

    def save_config(self):
        """Save the current configuration to a JSON file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"Error saving configuration: {e}")

    def update_config(self, key, value):
        "