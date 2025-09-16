# key - value
# 35 = izmir - 20 = denizli
""" # listelerle böyle yapılır
sehirler = ["izmir","denizli"]
plakalar = [35,20]
print(plakalar[sehirler.index("izmir")])
"""
# dictionary ile tek liste ile hepsini saklama
"""
plakalar = {"izmir":35,"denizli":20}
# print(plakalar["izmir"]) #35 değerini veriyor
plakalar ["istanbul"]=34
plakalar ["ankara"]=6
print(plakalar["ankara"]) # 6 değerini veriyor
"""
"""
user = {
    "sekokara":{
        "age":21,"school":"deu"
    } ,
    "bekokara":{
        "age":24,"school":"haceptepe"
    }
}
print(user["sekokara"]) # "age":21,"school":"deu"
print(user["sekokara"]["age"]) # 21 değeri çıkar
"""
"""
students = {
    "120": {
        "name":"seko",
        "surname":"kara",
        "phone":"111"
    },
    "121":{
        "name":"beko",
        "surname":"kara",
        "phone":"222"
    },
    "122":{
        "name":"hakan",
        "surname":"türk",
        "phone":"333"
    }
}
"""
#-------------------------------------------------------
studentNo=input("student no: ")
name = input("name: ")
surname=input("surname: ")
age = input("age: ")

students = {
    studentNo:{
        "name":name ,
        "surname":surname,
        "age":age
    }
}
print(students)
