# write a script that finds the greatest common factor of two numbers

# variable for storing number value and empty list for factors
num_one = 1020
factors_num_one = []

num_two = 18
factors_num_two = []

# common factor list
common_factors = []

# find the factors of both numbers
for i in range(1, num_one + 1):
    if num_one % i == 0:
        factors_num_one.append(i)

for i in range(1, num_two + 1):
    if num_two % i == 0:
        factors_num_two.append(i)

# determine the greatest common factor
for factor in factors_num_one:
    for factor_two in factors_num_two:
        if factor == factor_two:
            common_factors.append(factor)

greatest_common_factor = common_factors[-1]

print(greatest_common_factor)
print(common_factors)
