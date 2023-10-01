import os
import re

def save_string_to_txt(input_string, filename, output_directory="outputs"):
    """
    Save an input string to a .txt file in the specified directory.
    This function also ensures that the output directory and the file exist.

    Args:
        input_string (str): The string to save to the .txt file.
        filename (str): The name of the .txt file (without the ".txt" extension).
        output_directory (str, optional): The directory where the .txt file will be saved.
    """
    # Replace spaces with underscores and remove special characters
    sanitized_filename = re.sub(
        r'[^a-zA-Z0-9_]',
        '',
        filename.replace(" ", "_")
    ) + ".txt"

    # Check if the output directory exists, if not create it
    if not os.path.exists(output_directory):
        try:
            os.makedirs(output_directory)
        except Exception as e:
            print(f"❌ An error occurred while creating the directory: {e}")
            return

    # Create the full file path
    file_path = os.path.join(output_directory, sanitized_filename)

    try:
        # Open the file in write mode and save the string
        with open(file_path, 'w') as file:
            file.write(input_string)
        print(f"🖨  File saved at: \"{file_path}\"\n")
    except Exception as e:
        print(f"❌ An error occurred while saving the file: {e}")
