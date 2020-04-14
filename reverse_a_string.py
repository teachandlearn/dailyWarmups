# Reverse a string
# https://stackoverflow.com/questions/117812/alternate-fizzbuzz-questions

# create strings and the empty lsit
forward_string = "fear is the mind killer"
forward_string_list = []
backward_string = ""

# append each letter as a separate item in the forward string list
for letter in forward_string:
    forward_string_list.append(letter)

# add each character to the backward string
for i in range(1, len(forward_string_list) + 1):
    backward_string += forward_string_list[i * -1]
    print(i * -1)

# output
print(forward_string_list)
print(backward_string)
