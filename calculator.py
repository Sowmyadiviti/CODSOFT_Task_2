def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Please select the operation.")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
choice=input("Please enter choice(1/2/3/4):")
num_1=int(input("Please enter the first number:"))
num_2=int(input("Please enter the second number:"))
if choice=='1':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=='2':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
elif choice=='3':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
else:
    print("This ia an invalid input")
