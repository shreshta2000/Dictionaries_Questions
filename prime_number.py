def even(list1):
    i = 0
    prime = []
    not_prime = []
    while i < len(list1):
        num = list1[i]
        j = 2
        count = 0
        while j <= num:
            if num%j == 0:
                count = count+1
                if count >=2:
                    break
            j=j+1
        if count == 1 or count == 0:
            prime.append(list1[i])
        else:
            not_prime.append(list1[i])
        my_dic = {}
        my_dic["prime"] = prime
        my_dic["not prime"] = not_prime
       
        i=i+1
    return my_dic
print(even([1,2,3,31,13,51,8,991,444]))