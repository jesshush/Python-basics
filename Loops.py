#loop using for

my_list = [1,2,3,4,5,6]
for i in my_list:
    print(i)
    i+=1

#loop using while

names = ['Rosalin','Manisha','Jeslyn','Bhavesh']
i=0
while i < len(names):
    print(names[i])
    i+=1


#loop using range, enumerate()

fruits = ['Mango','Apple','Banana','Orange']

for i in range(len(fruits)):
    print(f"index {i}: {fruits[i]}")

#OR
my_list = ['John', 'Alice', 'Bob']

for index, name in enumerate(my_list):
    print(f"Index {index}: {name}")