
digits = [1, 0, 2, 4, 1, 7, 0, 1]


set_A = {d * 7 for d in digits}
set_B = {d * 9 for d in digits}
print("\n4. Set A:", set_A)
print("4. Set B:", set_B)

# vi. 
print("4.vi. Union:", set_A.union(set_B))

# vii. 
print("4.vii. Intersection:", set_A.intersection(set_B))

# viii. 
print("4.viii. A - B:", set_A.difference(set_B))
print("4.viii. B - A:", set_B.difference(set_A))

# ix. 
print("4.ix. Symmetric Difference:", set_A.symmetric_difference(set_B))

# x. 
print("4.x. Is A a subset of B?", set_A.issubset(set_B))
print("4.x. Is B a superset of A?", set_B.issuperset(set_A))

# xi. 
user_val = int(input("4.xi. Enter a value X to discard from Set A: "))
set_A.discard(user_val)
