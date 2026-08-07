# 1. 
roll_no = "1024170146"
L = [int(digit) * 10 for digit in roll_no]

# i. 
print("1.i. Initial List L:", L)

# ii. 
L.append(80) 
L.insert(3, 50) 
print("1.ii. L after append and insert:", L)

# iii. 
L.remove(80) 
L.pop() 
print("1.iii. L after remove and pop:", L)

# iv. 
L.sort()
print("1.iv. L sorted ascending:", L)
L.sort(reverse=True)
print("1.iv. L sorted descending:", L)

# v. 
print("1.v. First three elements:", L[:3], "| Last three elements:", L[-3:])

# vi. 
avg_L = sum(L) / len(L)
L_filtered = [x for x in L if x > avg_L]
print("1.vi. Elements greater than average:", L_filtered)