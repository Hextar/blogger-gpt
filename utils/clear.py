import os
import atexit
import shutil

def clear_temp_files_on_exit():
    temp_directory = "temp"

    if os.path.exists(temp_directory):
        print("Deleting temp files...")
        for filename in os.listdir(temp_directory):
            file_path = os.path.join(temp_directory, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

atexit.register(clear_temp_files_on_exit)
