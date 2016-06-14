glossary = {
    'variable': 'holds onto data to use later',
    'for': 'loops through the given loop or range',
    'if': 'does something if given conditional it true',
    'list': 'holds onto many pieces of data',
    'dictionary': 'holds onto key-value pairs'
    }

for word, define in glossary.items():
    print(word.title() + ":\n\t" + str(define))