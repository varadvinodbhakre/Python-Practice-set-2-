# 1. if-elif-else....
# Q.1 Write a program that asks the user for a number and prints whether it is positive, negative, or zero.

num = int(input("Enter any number : "))

if (num>0):
    print("This is a Positive... ")

elif(num<0):
    print("This number is Negative...")

else:
    print("This number is Zero...")


# Q.2 Create a program that checks if a person is eligible to vote (age >= 18).

age = int(input("Enter your age : "))

if(age>=18):
    print("You are eligible to vote...")

else:
    print("You are not eligible to vote...")

# Q.3 Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

num = int(input("Enter any number : "))

if(num%2==0):
    print(num,"is a even number...")

else:
    print(num,"is a odd number...")   

# 2. Match Case Statements
# Q.1 Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

Day = int(input("Enter any day : "))

match Day :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid ....")    

# Q.2 Write a program using match case that simulates a simple calculator.Ask the user for two numbers and an operation (+, -, *, /).Perform the operation using match case.

a =int(input("Enter first number : "))
b =int(input("Enter second number : "))
print("1 - Addition")
print("2 - Substraction")
print("3 - Multiply")
print("4 - Division")
choice = int(input("Enter your Choice : "))

match choice:
    case 1:
        print(a,"+",b,"=",a+b)
    case 2:
        print(a,"-",b,"=",a-b) 
    case 3:
        print(a,"x",b,"=",a*b) 
    case 4:
        print(a,"/",b,"=",a/b) 
        
#  3. For Loops...
# Q.1 Print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# Q.2 Calculate the sum of all numbers from 1 to 100 using a for loop.
Sum = 0
for i in range(1,101):
    print(i)
    Sum += i
print(Sum)

# Q.3 Print the multiplication table of a number (entered by user).
num = int(input("Enter any number : "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)


# Q.4 Print the following pattern using a for loop:
'''''
*
**
***
****
'''''

for i in range(1,5):
    print("*"*i)


# While loops....
# Q.1 Print numbers from 1 to 10 using a while loop.

i = 1
while i <=10:
    print(i)
    i +=1

# Q.2 Write a program that keeps asking the user to enter a password until they enter the correct one.

Password = ("yjks$324")
entered_pass = input("Enter a Password : ")

while (entered_pass!= Password):
    entered_pass=input("Wrong Password ! Try again enter a password : ")

print("Sucess you are loged in...")    

# Q.3 Use a while loop to reverse a given number (e.g., 123 → 321).

n = int(input("Enter any number : "))
i =1
print(int(str(n)[::-1]))


# 5. Break, Continue, and Pass Statements

# Q.1 Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
for i in range (1,10):
    print(i)
    if (i==7):
        break

# Q.2 Print numbers from 1 to 10, skipping the number 5 (use continue).

for i in range(1,10):
    if(i==5):
        continue
    print(i)

#  Q.3 Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).

for i in range(1,6):
    match i :
        case 1:
            print("1")
        case 2:
            print("2")
        case 3:
            pass
        case 4:
            print("4")
        case 5:
            print("5")

