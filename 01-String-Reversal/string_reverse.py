string = input("Enter a string: ")
split_string = string.split()
reversed_string=""
for word in split_string:
    reversed_string += word[::-1]+" "
print(reversed_string)