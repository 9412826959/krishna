# name=("krishna Bansal")
# print(len(name))
# age=int(input("enter the age: "))
# if age>=15:
#     print("enter")
# else:
#     print("not enter")
# score=int(input("enter your score: "))
# if score>=85:
#     print("good")
# elif score<=85:
#     print("nice")
# else: 
#     print("hard work")
# raining=False
# cold=True
# if raining:
#     print("bring an umbrella")
#     if cold:
#         print("wear a jacket")
# number=10
# if number>0:
#     print("the number is positive")
# else:
#     print("the number is negatve")
# number=0
# if number>0:
#     print("the number is positive")
# elif number<0:
#     print("the number is negatve")
# else:
#     print("the number is zero")
# ram={1, 2, 3, 4, 5}
# print(ram.add(7))
# print(ram)
# ram.remove(2)
# print(ram)
# ram.discard(4)
# print(ram)
# b={23, 332, 22, 53, 4, 2}
# c=b.union(ram)
# print(c)
# b={23, 332, 22, 53, 4, 2}
# c=b.intersection(ram)
# print(c)
# b={23, 332, 22, 53, 4, 2,"nitin", "raj"}
# c=b.difference(ram)
# print(c)
# b={23, 332, 22, 53, 4, 2}
# c=b.symmetric_difference(ram)
# print(c)
# class Dog:
#     def __init__(self, name):
#         self.name=name

# dog1=Dog("buddy")
# print(dog1.name)
# class car:
#     def __init__(self, make, model):
#         self.make=make
#         self.model=model

# car1=car("toyota", "camry")
# car2=car("honda", "civic")
# print(car1.make, car1.model)
# print(car2.make, car2.model)
# class friend:
#     def __init__(self, name, good):
#         self.best=name
#         self.good=good

# friend=friend("raj", "best")
# class backaccount:
#     def __init__(self, account_number, balanced):
#         self.account_number=account_number
#         self.balanced=balanced
    
#     def get_balanced(self):
#         return self.__balanced

# account=backaccount("123456", 1000)
# print(account.account_number)
# print(account.balanced)
# class animal:
#     def __init__(self, name):
#         self.name=name
    
#     def speak(self):
#         pass

# class dog(animal):
#     def speak(self):
#         return "woof!"
# class cat(animal):
#     def speak(self):
#         return "meow!"
# dog =dog("buddy")
# cat=cat("whiskers")
# print(dog.name, dog.speak())
# print(cat.name, cat.speak())
# employees=['corey', 'jim', 'steven']
# developer=['corey', 'raj', 'jim']
# result=set(employees).intersection(developer)
# print(result) 
# student={
#     "name": "rkishna bansal",
#     "age": "25",
#     "grade": "A"
# }
# print(student.get("age"))
# student["age"]=23
# student["student"]="first_year"
# print(student)
# for key, value in student.items():
#     print(f"{key}: {value}")
#     print("{key}: {value}")
# squares={num: num**3 for num in range(1, 6)}
# print(squares)
# student={
#     "name": "rkishna bansal",
#      "age": "25",
#      "grade": "A"
#  }
# del student["name"]
# student["course"]="B-tech"
# print(student.get("age"))
# print(student)
# dictionary={
#     0:10,
#     1:20
# }
# print(dictionary)
# dictionary[4]=9
# print(dictionary)
# a={
#     1:2, 
#     3:4
# }
# b={
#     5:6, 
#     7:8
# }
# c={
#     9:10,
#     10:11
# }
# a.update(b)
# a.update(c)
# print(a)
# a.union
# d={'x':10, 'y': 20, "z":30}
# for key, value in d.items():
#     print(f"{key}: {value}")
# my_dict={'data1': 100, 'data2': -54, "data3": 247}
# for key in sorted(my_dict):
#     print("%s:%s"%(key, my_dict[key]))
# a={
# 1:10, 2:20, 3:30, 4:40, 5:50, 6:60
# }
# for x, y in a.items():
#     print(f"{x}: {y}")
# n=int(input("enter a value"))
# if n in a:
#     print("it is a avaliable")
# else:
#     print("not avaliable")
# keys=['name', 'class', 'section', 'roll.no', 'course']
# values=['krishna', 314, 'EB', 18, 'B-tech']
# result=dict(zip(keys, values))
# print(result)
# .....
# import prettytable
# information={'name': 'krishna', 'class': 314, 'section': 'EB', 'roll.no': 18, 'course': 'B-tech'}
# table=prettytable(['keys', 'values'])
# for keys, values in information.items():
#     table.add_rows([keys, values])
# table.align='1'
# print(table)
####
# data={
#     'A':10,
#     'B':20, 
#     'C':5,
#     'D':15
# }
# max_key=max(data, key=data.get)
# min_key=min(data, key=data.get)
# max_value=data[max_key]
# min_value=data[min_key]
# print(f"maximum: keys={max_key}, value={max_value}")
# print(f"minimum: keys={min_key}, value={min_value} ")
# class ObjectToDictionary:
#     def __init__(self, field1, field2, field3):
#         self.field1='value1'
#         self.field2='value2'
#         self.field3='value3'
#     def to_dict(self):
#         attribute=vars(self)
#         obj_dict = {key: value for key, value in attribute.items()}
# obj=ObjectToDictionary()
# result_dict=obj.to_dict()
# print(result_dict)
        




# def my_function():
#     x=10
#     print(x)

# my_function()
# def my_friends():
#     x="as"
#     d="fgjh"
#     print(x, d)
# my_friends()
# x=19
# def modify_global():
#     global x
#     x=20
# modify_global()


# import random
# def _guess_number():
#     return random.randrange(1, 100)
# target_number=_guess_number()
# attempt=0
# while True:
#     user_guess=int(input("guess the number: "))
#     attempt += 1
#     if user_guess==target_number:
#         print("congratulation! you guess a correct number\n", attempt, "attempt")
#         break
#     elif user_guess<target_number:
#         print("try a higher number")
#     else:
#         print("try a lower number")

    