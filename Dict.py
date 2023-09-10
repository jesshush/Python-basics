#dictionary

student = {
    'name': 'John Doe',
    'age': 25,
    'roll_number': 'ABC123',
    'marks': [90, 85, 95]
}
print("Student Name:", student['name'])


#constructor dict()
my_dict = dict(name='John', age=30, city='New York')
print(my_dict['name'])

#modifying
my_dict['name'] = 'luke'
print(my_dict)

#adding
my_dict['year'] = 2023
print(my_dict)

#deleting
del my_dict['year']
print(my_dict)

#dictionary comprehension
fruits = ['Mango','Apple','Banana','Orange']
fruit_length = {fruit : len(fruit) for fruit in fruits}
print(fruit_length)


#range function
numbers = [1,2,3,4]
squared_numbers = {x: x*x for x in numbers}
print(squared_numbers)
even_numbers = {x: x*x for x in numbers if x%2 == 0}
print(even_numbers)