import argparse

import input
import output
from client import Client
from solution import solve

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="""name of file can be 'a' or 'b' or 'c' or 'd' or 'e'""")
    return parser.parse_args()

def main():

    args = parse_arguments()
    if args.file not in ('a','b','c','d','e'):
        raise ValueError("argument file (-f) must be equal to 'a' or 'b' or 'c' or 'd' or 'e'")

    # read the file
    content = input.read_file(input.path_files[args.file])
    # separate the first line
    first_line, content = input.separate_first_line(content)
    nb_custumers = int(first_line)

    lines = content.split("\n")

    clients = []

    for i in range(nb_custumers):
        nb_ingredients_likde, liked_ingredients = input.line_content(lines[2*i])
        nb_ingredients_disliked, disliked_ingredients = input.line_content(lines[2*i + 1])

        clients.append(Client(liked_ingredients, disliked_ingredients))

    pizza_ingredients = solve(clients)

    output.write_file(args.file, pizza_ingredients)

if __name__ == '__main__':
    main()
