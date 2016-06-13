numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 1:
        end = "st"
    elif num == 2:
        end = "nd"
    elif num == 3:
        end = "rd"
    else:
        end = "th"
    print(str(num) + end)