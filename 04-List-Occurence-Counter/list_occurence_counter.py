sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

new_list = [ele for ele in sample_list if sample_list.count(ele) > 1]
print(list(set(new_list)))