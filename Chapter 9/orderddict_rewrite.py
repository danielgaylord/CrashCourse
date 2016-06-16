from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'holds onto data to use later'
glossary['for'] = 'loops through the given loop or range'
glossary['if'] = 'does something if given conditional it true'
glossary['list'] = 'holds onto many pieces of data'
glossary['dictionary'] = 'holds onto key-value pairs'

for word, define in glossary.items():
    print(word.title() + ":\n\t" + str(define))