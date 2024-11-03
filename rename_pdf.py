import os
import sys
import re

def sanitize_name(name):
    """Replace special characters in the name with safe characters and handle empty names."""
    sanitized_name = re.sub(r'[<>:"/\\|?*\']', '_', name).strip()
    if not sanitized_name:
        raise ValueError("The new name cannot be empty or consist only of invalid characters.")
    return sanitized_name

def rename_file(file_path, new_name):
    try:
        # Check if the file path exists and is a file
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist or is not a file.")
        
        # Sanitize the new name to avoid special characters
        new_name = sanitize_name(new_name)

        # Extract the directory from the file path
        directory = os.path.dirname(file_path)

        # Get the original file extension
        extension = os.path.splitext(file_path)[1]

        # Ensure the new file path is not the same as the old one
        new_file_path = os.path.join(directory, new_name + extension)
        if file_path == new_file_path:
            raise ValueError("The new file name is the same as the original name.")

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"File renamed to: {new_file_path}")
    
    except FileNotFoundError as e:
        print(f"File Error: {e}")
    except PermissionError:
        print("Permission Error: You do not have permission to modify this file.")
    except OSError as e:
        print(f"OS Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3
