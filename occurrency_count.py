word = "MISSISSIPPI" 
my_dic = {}
i = 0
count_m = 0
count_i = 0
count_s = 0
count_p = 0
while i <len(word):
    if "M" in word[i]:
        count_m = count_m + 1
        my_dic["M"] = count_m
    if "I" in word[i]:
        count_i = count_i + 1
        my_dic["I"] = count_i
    if "S" in word[i]:
        count_s = count_s+1
        my_dic["S"] = count_s
    if "P" in word[i]:
        count_p = count_p + 1
        my_dic["P"] = count_p
    i=i+1
print(my_dic)

