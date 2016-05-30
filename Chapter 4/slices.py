nums = [value for value in range(3,33,3)]

for num in nums:
    print(num)

print("\nThe first 3 threes are:")
for num in nums[:3]:
    print(num)

print("\nThe middle 4 threes are:")
for num in nums[3:-3]:
    print(num)

print("\nThe first 3 threes are:")
for num in nums[-3:]:
    print(num)
