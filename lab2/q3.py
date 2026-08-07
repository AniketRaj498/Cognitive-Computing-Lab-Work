import random


random.seed(1024170146)

# i. 
rand_nums = [random.randint(100, 900) for _ in range(100)]

# ii. 
odd_count = sum(1 for n in rand_nums if n % 2 != 0)
print(f"\n3.ii. Odd numbers count: {odd_count}")

# iii.
even_count = sum(1 for n in rand_nums if n % 2 == 0)
print(f"3.iii. Even numbers count: {even_count}")

# iv. 
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [n for n in rand_nums if is_prime(n)]
print(f"3.iv. Prime numbers found ({len(primes)}): {primes}")

# v. 
most_frequent = max(set(rand_nums), key=rand_nums.count)
print(f"3.v. Most frequent number: {most_frequent} (occurs {rand_nums.count(most_frequent)} times)")