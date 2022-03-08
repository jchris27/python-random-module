import random
import my_module

random_integer = random.randint(0, 5)

# print(random_integer)
# print(my_module.pi)

random_float = random.random()

random_decimal_number = random_integer + random_float

print(random_decimal_number)

# Randomisation 0 - 5 but not included 5.
random_decimal = random_float * 5
print(random_decimal)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")
