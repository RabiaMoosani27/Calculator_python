                    #Calculator#

def cal_add():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter Second number:"))
    add=num1+num2
    return add

def cal_sub():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter Second number:"))
    sub=num1-num2
    return sub

def cal_multiply():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter Second number:"))
    multiply=num1*num2
    return multiply

def cal_divide():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter Second number:"))
    if(num2==0):
        print("Division not possible (zero error)")
        return 
    divide=num1/num2
    return divide

def cal_reminder():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter Second number:"))
    reminder=num1%num2
    return reminder


while True:

    print("\n\t\tCalculator\t\t\t\t\t")
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Reminder")
    print("6-Exit")

    choice = int(input("Enter your choice(1-6): "))

    if(choice == 1):
        print("Addition is:", cal_add())
        input("Press Enter to continue...")

    elif(choice == 2):
        print("Subtraction is:", cal_sub())
        input("Press Enter to continue...")

    elif(choice == 3):
        print("Multiplication is:", cal_multiply())
        input("Press Enter to continue...")

    elif(choice == 4):
        print("Division is:", cal_divide())
        input("Press Enter to continue...")

    elif(choice == 5):
        print("Reminder is:", cal_reminder())
        input("Press Enter to continue...")

    elif choice == 6:
        print("Exiting calculator... Bye 👋")
        break

    else:
        print("Invalid choice! Try again.")

