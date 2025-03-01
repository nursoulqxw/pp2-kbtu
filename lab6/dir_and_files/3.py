import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

# Example usage
check_path("example.txt")
