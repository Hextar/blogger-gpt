def save_string_to_txt(input_string, filename, output_directory = "/outputs" ):
    """
    Save an input string to a .txt file in the specified directory.

    Args:
        input_string (str): The string to save to the .txt file.
        filename (str): The name of the .txt file (including the ".txt" extension).
        output_directory (str, optional): The directory where the .txt file will be saved.
    """
    # Create the full file path
    file_path = os.path.join(output_directory, filename)

    try:
        # Open the file in write mode and save the string
        with open(file_path, 'w') as file:
            file.write(input_string)
        print(f"File saved successfully at: {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")