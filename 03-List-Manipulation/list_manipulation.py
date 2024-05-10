number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in number_list[::-1]:
    if i>50:
        number_list.remove(i)
print(number_list)