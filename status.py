


def main():
    number = int (input("PLease enter a number "))

    Status=num(number)

    print(Status)




def num(num):

    if num % 2 == 0:
        print("number is even")

        status = True
    else:
        print ("number is odd")
        status = False
        return status

main()

    
