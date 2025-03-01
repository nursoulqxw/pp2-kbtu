def copy_file(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())

# Example usage
copy_file("source.txt", "destination.txt")
