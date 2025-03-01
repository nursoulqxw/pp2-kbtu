import os

def check_access(path):
    print(f"Testing access for: {path}")
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# Example usage
check_access("example.txt")
