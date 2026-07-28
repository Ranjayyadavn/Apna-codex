print("select an program to perfrom")

print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divition")


opration= input("Enter your choice; 1/2/3/4:").strip()

if opration=="1":
    num1= input("Enter the first number :")
    num2= input("Enter the second number :")
    Sum= int(num1) + int(num2)
    print("sum of two number is:",str(Sum))
    
                    
elif opration=="2":
    num1= input("Enter the first number :")
    num2= input("Enter the second number :")
    Sub= int(num1) + int(num2)
    print("subtract of two number is:",str(Sub))
    
elif opration=="3":
    num1= input("Enter the first number :")
    num2= input("Enter the second number :")
    Mul= int(num1) + int(num2)
    print("multiply of two number is:",str(Mul))
    
elif opration=="4":
            num1= input("Enter the first number :")
            num2= input("Enter the second number :")
                                
            if opration==0:
                             print("can not be zero")
            else:
                        
                    Div= int(num1) + int(num2)
                    print("divition of two number is:",str(Div))
                
else:
    print("Enter the valid number!!")
        
        #   CREATE BY MR. RANJAY YADAV 