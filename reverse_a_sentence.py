# Reverse a sentence (i like pie -> pie like i)
# https://stackoverflow.com/questions/117812/alternate-fizzbuzz-questions

# variables and the list for holding the words
sentence = "yellow is the color of gold"
word = ""
word_list = []
reversed_sentence = ""

# populate word_list
for char in sentence:
    if char != " ":
        word += char
    else:
        word_list.append(word)
        word = ""

word_list.append(word)

# take each word in word list, in reverse, and add it to reversed_sentence 
for i in range(1, len(word_list) + 1):
    reversed_sentence += word_list[i*-1]
    reversed_sentence += " "

print(reversed_sentence)
