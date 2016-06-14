fav_nums = {'dan': [3, 7, 13], 'jim': [7, 2], 'bob': [10], 'corie': [2, 1], 'shien': [5, 7, 10, 11]}

for person in fav_nums:
    print(person.title() + ":")
    for number in fav_nums[person]:
        print("\t" + str(number))
    print()