import random

heads=1
tails=2
tosses=5

def main():

    for toss in range(tosses):

        num=random.randint(heads,tails)

        if num ==heads:
            print("Heads!")
        else:
            print("Tails!")

main()            
