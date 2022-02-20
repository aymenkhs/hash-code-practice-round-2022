import os

outputs_files = ['a', 'b', 'c', 'd', 'e']

def write_file(outputs_file, ingredients):
    file_path = os.path.join("output", outputs_file)
    string = ""
    string += str(len(ingredients))
    for ingredient in ingredients:
        string += " "
        string += ingredient

    with open(file_path, "w") as file:
        content = file.write(string)
