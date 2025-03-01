def write_list_to_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

# Example usage
my_list = ["Apple", "Banana", "Cherry"]
write_list_to_file("fruits.txt", my_list)
