import json
import os


def store_number(num, filename):
    with open(filename, 'w') as file:
        json.dump(num, file)


def retrieve_number(filename):
    with open(filename) as file:
        num = json.load(file)
    return num


def delete_file(filename):
    os.remove(filename)


def find_number():
    filename = 'number.json'
    try:
        num = retrieve_number(filename)
    except FileNotFoundError:
        num = input("What's your favorite number? ")
        store_number(num, filename)
    else:
        ask = input("Is " + num + " your favorite number? (y/n) ")
        if ask == 'n':
            delete_file(filename)
            find_number()
        else:
            print("Your favorite number is..." + num)


find_number()
