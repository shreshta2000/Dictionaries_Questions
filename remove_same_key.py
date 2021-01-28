dic={
    'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
    }
my_dic={}
for i in dic:
    if i in dic:
        my_dic.update(dic)
print(my_dic)
