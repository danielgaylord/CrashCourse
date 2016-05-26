things = []

things.append('pencil')
things.append('desks')
things.append('books')
things.append('chairs')

things[0] = 'pens'
things.sort()
things.sort(reverse=True)
things.reverse()
things.remove('books')
things.pop(2)
things.insert(1, 'computers')

print(sorted(things))
print(str(len(things)))
