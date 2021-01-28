key = input("entre your key")
dict={'name':'Raju', 'marks':56}
for i in dict:
    if key in dict:
        print("key exist in dict",key)
        break
    else:
        print("not exists in dict",key)
        break