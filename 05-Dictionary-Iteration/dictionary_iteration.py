ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

reversed_dict = {}

for key, value in ascii_dict.items():
    reversed_dict[value] = key

print(reversed_dict)