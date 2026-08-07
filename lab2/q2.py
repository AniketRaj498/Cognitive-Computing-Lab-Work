
original_L = [int(digit) * 10 for digit in "1024170146"]
scores = tuple(original_L[:8])
print("\n2. Original Scores Tuple:", scores)

# i. 
highest_score = max(scores)
highest_index = scores.index(highest_score)
lowest_score = min(scores)
lowest_count = scores.count(lowest_score)
print(f"2.i. Highest: {highest_score} at index {highest_index}. Lowest: {lowest_score} appears {lowest_count} times.")

# ii. 
reversed_list = list(scores)[::-1]
print("2.ii. Reversed as list:", reversed_list)
# Tuples are immutable and cannot be changed in place; they lack methods like .reverse() that modify the original object in memory.

# iii. 
user_score = int(input("2.iii. Enter a score to search: "))
if user_score in scores:
    print(f"Score found at index: {scores.index(user_score)}")
else:
    print("Score not present.")

# iv. 
try:
    scores[0] = 100
except TypeError as e:
    print(f"2.iv. Error caught: {e}")
# Tuples do not support item assignment because they are immutable, unlike lists which are mutable and allow their elements to be changed.

# v.
first_score, second_score, *remaining_scores = scores
print(f"2.v. First: {first_score}, Second: {second_score}, Remaining: {remaining_scores}")