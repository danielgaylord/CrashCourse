glossary = {
    'variable': 'holds onto data to use later',
    'for': 'loops through the given loop or range',
    'if': 'does something if given conditional it true',
    'list': 'holds onto many pieces of data',
    'dictionary': 'holds onto key-value pairs'
    }

for key in glossary:
    print(key.title() + ":\n\t" + str(glossary[key]))