def output_file(filename):
    try:
        with open(filename) as file:
            print(file.read())
    except FileNotFoundError:
        pass


output_file('dogs.txt')
output_file('cats.txt')
output_file('birds.txt')