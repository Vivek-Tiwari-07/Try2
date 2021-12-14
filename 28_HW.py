'''a = "refrigerator" 
count = 0 
for i in a:
   count = count+1 
print (count)  
#Q2
print ('e' in 'Umbrella')'''

#Q3
'''list =[1,2,3,4,5,6,7,8,9,10]    
for i in list:  
    c = i*i
    print('list_of_Square',c)'''
#Q4
string= input("Please Enter the String : ")#a,e,i,o,u
vowels = 0
for i in string:
    if(i == 'a')or(i == 'e') or (i == 'i') or (i == 'o') or (i == 'u'):
        vowels = vowels + 1
print("Total Number of Vowels in this String = ", vowels)

#Q5
n=4
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print()
#Q6
print("Enter 1 for addition\n")
print("Enter 2 for subtaction\n")
print("Enter 3 for division\n")
print("Enter 4 for multiplication\n")
print("Enter 5 for mod of two number\n")
print("Enter 6 for floor division\n")
print("Enter 7 to exit : ")

#while choice>0:
while True :
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=int(input("Enter 1st Number:"))
        b=int(input("Enter 2nd Number:"))
        tot1=a+b
        print("tot is",tot1)
    elif choice==2:
        a=int(input("Enter 1st Number:"))
        b=int(input("Enter 2nd Number:"))
        s1=a-b
        print("s1 is",s1)
    elif choice==3:
        a=int(input("Enter The First number "))
        b=int(input("Enter the second number"))
        c=a/b
        print("The Multiplication of the two number is ",c)
    elif choice==4:
        a=int(input("Enter The First number "))
        b=int(input("Enter the second number"))
        c=a*b
        print("The multiplication of two Number is ",c)
    elif choice==5:
        a=int(input("Enter The First number "))
        b=int(input("Enter the second number"))
        c=a%b
        print("The Mod of two number",c)
    elif choice==6:
        a=int(input("Enter The First number "))
        b=int(input("Enter the second number"))
        c=a//b
        print("The Mod of two number",c)
    else:
        print("Wrong Choice")
     
choice+=1 




























