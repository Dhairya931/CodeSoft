def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Error! Division by zero."
    else:
        return float(a)/float(b)
    
def main():
    print("\t\t\t Welcome to the Calculator!!")
    print("======================================================================================================")
    while True:
        print("Choose the operation you want to perform among the following:")
        print("Press 1 for Addition")
        print("Press 2 for Subtraction")
        print("Press 3 for Multiplication")
        print("Press 4 for Division ")
        print("Press 0 for Exit")
        print("======================================================================================================")
        ch=int(input("Enter your choice from the above menu: "))
        if ch==1:
            print ("Enter the numbers")
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number: "))
            x=add(num1,num2)
            print("Adition of given numbers is:",x)
            print("======================================================================================================")
        elif ch==2:
            print ("Enter the numbers")
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number: "))
            x=sub(num1,num2)
            print("Subtraction of given numbers is:",x)
            print("======================================================================================================")
        elif ch==3:
            print ("Enter the numbers")
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number: "))
            x=mul(num1,num2)
            print("Multiplication of given numbers is:",x)
            print("======================================================================================================")
        elif ch==4:
            print ("Enter the numbers")
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter second number: "))
            y=div(num1,num2)
            print("Divison of the numbers is:",y)
            print("======================================================================================================")
        elif ch==0:
            print("Thank You for using Calculator")
            print("======================================================================================================")
            return False
        else:
            print("Invalid Choice. Please Enter Again.")
            print("======================================================================================================")
            
if __name__=="__main__":
    main()