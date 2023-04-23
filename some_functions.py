from random import choice

def list_to_file(list_items: list):
    """Takes a list as an input and add the list items to a file."""
    nameFile = input("Pick a name for your file: ")
    with open(nameFile, "w") as file:
        for x in list_items:
            file.write(f"{x}\n")

def random_line_from_file(file):
    """From the file return a random line."""
    with open(file, "r") as file_open:
        content = file_open.readlines()
        return choice(content)

