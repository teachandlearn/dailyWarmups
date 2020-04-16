# Write a program that prints out, in reverse order, every multiple of 3 between 1 and 200
# https://stackoverflow.com/questions/117812/alternate-fizzbuzz-questions

# empty list to store the multiples of three
multiples_of_three = []

# add all of the multiples of three to the list
for i in range(1, 201):
    if i % 3 == 0:
        multiples_of_three.append(i)

# print each multiple of three in reverse order
counter = 1
while counter < len(multiples_of_three):
    print(multiples_of_three[counter * -1])
    counter += 1
