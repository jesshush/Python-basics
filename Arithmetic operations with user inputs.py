#Basic Arithmetic operations with

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print(" options - 1:add ", " 2:subtract "," 3:multiply "," 4:divide ")
option = int(input("Enter your option: "))

if option == 1:
    result= a + b
    print("The answer of nos is:", result)
elif option == 2 :
    result= a - b
    print("The answer of nos is:", result)
elif option == 3:
    result = a*b
    print("The answer of nos is:", result)
elif b > a:
    result = b /a
    print("The answer of nos is:", result)
else:
        result = a / b
        print("The answer of nos is:", result)

