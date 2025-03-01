import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"This is {letter}.txt")

# Example usage
generate_files()
