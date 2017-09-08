# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

# expected output
# new_list = ['hello','world']

new_list = []

for word in word_list:
    for letter in word:
        if letter == char:
            new_list.append(word)
            break
print new_list
