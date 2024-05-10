# string = input("Enter a string: ")

# res = []

# for i in range(0,len(string)):
#     if(string[i].isupper()):
#         res.append(i)


# reversed_str = string[::-1].lower()



# new_string = ''
# for i in range(len(reversed_str)):
#     if i in res:
#         new_string += reversed_str[i].upper()
#     else:
#         new_string += reversed_str[i]

# print(new_string)


string = input("Enter a string: ")
string_split = string.split()
result = []

for word in string_split:
    res = []
    for i in range(len(word)):
        if word[i].isupper():
            res.append(i)
    
    reversed_word = word[::-1].lower()
    
    new_word = ''
    
    for i in range(len(reversed_word)):
        if i in res:
            new_word += reversed_word[i].upper()
        else:
            new_word += reversed_word[i]
    
    result.append(new_word)

new_string = ' '.join(result)

print(new_string)
