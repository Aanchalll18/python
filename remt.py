a = [1, 2, (), [], '', (3, 4), (), 0, (5,)]
res = [x for x in a if x != ()]
print(res)
