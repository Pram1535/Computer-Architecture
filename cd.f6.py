counter=1
a=int(input("ENTER NUMBER-1-"))
counter=counter+1
b=int(input("ENTER NUMBER-2-"))
counter=counter+1
print("1-ADDITION 2-SUBTRACTION 3-MULTIPLICATION 4-DIVISION")
print("Enter Your Choice")
choice=int(input("enter 1 or 2 or 3 or 4="))
if choice==1:
    print("Performing addition...") 
    res=a+b
    counter=counter+1 
elif choice==2:
    print("Performing Subtraction...")
    res=a-b
    counter=counter+1 
elif choice==3:
    print("Performing Multiplication")
    res=a*b
    counter=counter+1
elif choice==4:
    if b==0:
        print("Denominator can't be Zero")
    print("Performing Division")
    res=a/b
    counter=counter+1
else:
    print("Enter Correct Input")
    print(res)
    counter=counter+1
print("CYCLE VALUE IS:",counter)
ins=int(input("Enter the No.of instructions:"))
performance_measure =ins/counter
print("performance measure is: ", performance_measure)
