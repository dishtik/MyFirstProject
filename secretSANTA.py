import random

def main():
    santas = ["Guna", "Lakshmi", "Mahendra", "Aditi", "Abhilash", "Samya", "Evan", "Tanya", "Eshwar","Vardhan", "Rishita","Swayamsiddh", "Megha", "Jenil","Prerna", "Varadh","Saloni", "Priyasha","Eby", "Niharika", "Suhaas","Karthik", "Rakshit"]
    recipient = ["Guna", "Lakshmi", "Mahendra", "Aditi", "Abhilash", "Samya", "Evan", "Tanya", "Eshwar","Vardhan", "Rishita","Swayamsiddh", "Megha", "Jenil","Prerna", "Varadh","Saloni", "Priyasha","Eby", "Niharika", "Suhaas","Karthik", "Rakshit"]
    santas.sort()
    
    def insert_name():
        name = input("Enter a name:")
        santas.append(name)
        recipient.append(name)
        santas.sort()
        print(len(santas))

    def pair():
        n = random.randint(0,(len(santas))-1)
        if (santas[0] == recipient[n]) :
            pair()
        else :
            print("\nSanta   : "+santas[0])
            print("Gift To : "+recipient[n])
            del santas[0]
            del recipient[n]
        
        
    print("\nWELCOME TO SECRET SANTA\n")
    while(len(santas) > 0) :
        print("\nChoose:\n1 - To add new member to game.\n2 - To generate pair of santa and their recipient.\n")
        choice = int(input())
    
        if choice==1 :
            insert_name()
        elif choice == 2:
            pair()
        else :
            print("\n----WRONG CHOICE---\n")

main()