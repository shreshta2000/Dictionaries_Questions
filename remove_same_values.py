list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
my_dic = {}
i=0
while i<len(list1):
    if  i in list1.values[i]:
        my_dic.update(list1[i])
    i=i+1
print(my_dic)
