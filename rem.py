li = [1, (), 2, [], 3]
res = [x for x in li if x != ()]
print(res)  # Output: [1, 2, 3]
