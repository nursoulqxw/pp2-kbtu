import os

def delete_file(filepath):
    if os.path.exists(filepath) and os.access(filepath, os.W_OK):
        os.remove(filepath)
        print(f"{filepath} has been deleted.")
    else:
        print("File either does not exist or cannot be deleted.")

# Example usage
delete_file("example.txt")
