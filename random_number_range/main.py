import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_num = random.randint(lower_bound, upper_bound)

print(f"Random number between {lower_bound} and {upper_bound} is {random_num}")