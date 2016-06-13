word = 'this'
number = 2
words = list(word)
#numbers = list(number)

print(words)
#print(numbers)

fib = [0, 1]

for value in range(2, 10):
    fib.append(fib[value - 2] + fib[value - 1])

print(fib)

def make_list(x):
    items = []
    for item in range(1,x):
        items.append(item)
    return list


def square_list(items):
    for item in items:
        item = item**2
    return list

numbers = make_list(5)
#print(square_list(numbers))
