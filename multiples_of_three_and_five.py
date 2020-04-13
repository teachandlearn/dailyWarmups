# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Warm up prompt: https://projecteuler.net/problem=1


# variables
sum_of_multiples = 0
multiples_of_three_num = 0
multiples_of_five_num = 0
multiples_of_both_num = 0


# iterating through every number up to 1000
for i in range(0, 1000):
    if i % 3 == 0 and i % 5 == 0:
        sum_of_multiples += i
        multiples_of_both_num += 1
    elif i % 3 == 0:
        sum_of_multiples += i
        multiples_of_three_num += 1
    elif i % 5 == 0:
        sum_of_multiples += i
        multiples_of_five_num += 1
    else:
        sum_of_multiples += 0


# output
print("The sum of the multiples of three and five: " + str(sum_of_multiples))
print("The number of multiples of both three and five: " + str(multiples_of_both_num))
print("The number of multiples of only three: " + str(multiples_of_three_num))
print("The number of multiples of only five: " + str(multiples_of_five_num))
