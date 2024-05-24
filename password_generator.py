import random
import string

def pwd(len):
    ch = string.ascii_letters + string.punctuation 
    password = ''.join(random.choices(ch, k=len))
    return password

print("\t\t\t Welcome to Password Generator")
print("====================================================================================================")

def main():
    while True:
        print("Enter 0 to exit")
        l = int(input("Enter the length of the password: "))
        if l>0:
            pswd= pwd(l)
            print("Generated Password:", pswd)
        else:
            print("Thank You for using the password generator!!")
            return False

if __name__=='__main__':
    main()