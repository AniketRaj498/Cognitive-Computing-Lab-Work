my_dict = {
    "name": "Aniket Raj",
    "roll_no": "1024170146",
    "branch": "<fill branch here>", 
    "age": 20, 
    "city": "<fill city here>" 
}

# i. 
my_dict["location"] = my_dict.pop("city")
print("\n5.i. After renaming city to location:", my_dict)

# ii. 
my_dict["cgpa"] = 9.0 
print("5.ii. After adding cgpa:", my_dict)

# iii. 
my_dict["age"] += 1
print("5.iii. After updating age:", my_dict)

# iv. 
dict_copy1 = my_dict.copy()
dict_copy2 = my_dict.copy()

popped_branch = dict_copy1.pop("branch")
del dict_copy2["branch"]

# v. 
print("5.v. Iterating over dictionary:")
for key, value in my_dict.items():
    print(f"{key} -> {value}")

# vi. 
if "email" in my_dict:
    print(my_dict["email"])
else:
    print("5.vi. Fallback message: The key 'email' does not exist in this dictionary.")

# vii. 
friend_dict = {
    "name": "John Doe",
    "roll_no": "1024170999",
    "branch": "Computer Science",
    "age": 21,
    "location": "New York"
}
merged_dict = {**my_dict, **friend_dict}
print("5.vii. Merged Dictionary:", merged_dict)

# viii. 
str_dict = {k: v for k, v in my_dict.items() if type(v) == str}
print("5.viii. Keys with string values:", str_dict)