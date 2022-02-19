import os

path_files = {
    "a": os.path.join("input", "a_an_example.in.txt"),
    "b": os.path.join("input", "b_basic.in.txt"),
    "c": os.path.join("input", "c_coarse.in.txt"),
    "d": os.path.join("input", "d_difficult.in.txt"),
    "e": os.path.join("input", "e_elaborate.in.txt"),
}

def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def separate_first_line(content):
    # find the index of the first '\n'
    index = content.find('\n')
    first_line = content[:index]
    content = content[index+1:]
    return first_line, content

def line_content(line):
    values = line.split(' ')
    nb_ingredients = int(values[0])
    ingrediants = values[1:]
    return nb_ingredients, ingrediants
