d1 = {
    'name': "Anu",
    'age': 25,
    'phone':7829692957,
    'subject':"python"
}

print(d1)  #{'name': 'Anu', 'age': 25, 'phone': 7829692957, 'subject': 'python'}
print(type(d1))  #<class 'dict'>

#Accessing 
print(d1['name'])  #Anu
print(d1['subject']) #python

for i in d1.keys():  #name-age-phone-subject-
    print(i, end = "-")

print()

for i in d1.values():  #Anu-25-7829692957-python-
    print(i, end="-")
print()

for i in d1.items():  #('name', 'Anu')-('age', 25)-('phone', 7829692957)-('subject', 'python')-
    print(i, end="-")
print()

'''
1.It is odered collection
2.It can contain duplicate values but not duplicate keys
3.it contain both heterogenous and homogenous values
4.It store data in key value pair'''

