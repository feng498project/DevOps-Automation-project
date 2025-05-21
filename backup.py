import os
import shutil
from datetime import datetime

def backup_folder(source_folder, backup_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"backup_{timestamp}"
    destination = os.path.join(backup_folder, backup_name)

    try:
        shutil.copytree(source_folder, destination)
        print(f"Backup created at: {destination}")
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    source = input("Enter the folder to back up: ").strip()
    destination = input("Enter the destination backup folder: ").strip()
    backup_folder(source, destination)
