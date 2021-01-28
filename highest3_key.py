my_dict = {
    'a':390, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':900, 
    'f':200
    }
first_max = 0
second_max = 0
third_max = 0
max_list =[]
for i in my_dict:
    if first_max < my_dict[i]:
        first_max = my_dict[i]
        first_max_key = i
    for j in my_dict:
        if first_max > my_dict[j] and second_max < my_dict[j]:
            second_max = my_dict[j]
            second_max_key = j
        for k in my_dict:
            if first_max > my_dict[k] and second_max > my_dict[k] and third_max < my_dict[k]:
                third_max = my_dict[k]
                third_max_key = k
max_list.append(first_max_key)
max_list.append(second_max_key)
max_list.append(third_max_key)
print(max_list)
