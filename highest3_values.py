my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
first_max = 0
second_max = 0
third_max = 0
max_dict ={}
for i in my_dict:
    if (first_max < my_dict[i]):
        first_max = my_dict[i]
    for j in my_dict:
        if first_max > my_dict[j] and second_max < my_dict[j]: 
            second_max = my_dict[j]
    for k in my_dict:
        if first_max > my_dict[k] and second_max > my_dict[k] and third_max < my_dict[k]:
            third_max = my_dict[k]
max_dict["first max"] = first_max
max_dict["second max"] = second_max
max_dict["third max"] = third_max
print(max_dict)


