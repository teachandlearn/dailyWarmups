# write an app to return the factors of a given number
# https://stackoverflow.com/questions/117812/alternate-fizzbuzz-questions

# variable for storing number value and empty list for factors
num = 1020
factors = []

# iterate every whole number up to one half of the given number
for i in range(1, round(num/2 + 1)):
    if num % i == 0:
        factors.append(i)

# output
print(factors)
