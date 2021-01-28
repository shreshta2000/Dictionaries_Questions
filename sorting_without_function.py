# my_dict = {'bijender':10,'deepak':20,'sakshi':100,'param':30,'anjali':80,'roshini':40,}
# for i in my_dict:
#     for j in my_dict :        
#         if my_dict[i] < my_dict[j]:
#             a = my_dict[i]
#             b = my_dict[j]
#             my_dict[i] = b
#             my_dict[j] = a

# print(my_dict) 

# import json
# f = open("student.json","r")
# b = json.load(f)
# print(b)
# with open("student.json", "r") as read_content: 
# 	print(json.load(read_content))

# import json

# with open('student.json') as f:
#   data = json.loads(f)

# # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)
num = int(input("number  "))
i = 2
s = 0
while i <= num/2:
    if num%i == 0:
        s = 1
        if s == 1:
          break
    i = i +1
if s == 0:
    print("prime number")
    
else:
    print("not prime number")










