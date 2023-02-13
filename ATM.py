###ATM 
import os
os.system('cls')
balance=0

def option():

    print("\nEnter your option :")
    print("1.Balance check")
    print("2.Money Withdraw")
    print("3.Add money ")
    print("4. EXIT")

i=0
while 1:    
    os.system('cls')
    print("\n\t ATM\n")

    option()
    
    menu_option=input("press : ")
    if menu_option=="1":
        #Balance check
        os.system('cls')
        print("Your current balance is ",balance)
        
        press_continue1=input("\n\tEnter any key to continue \n")
        
    elif menu_option=="2":
        #Money withdraw
        os.system('cls')

        print(" Money Withdraw ")
        withdraw =int(input("\nHow much money do you want to withdraw :"))
        # print("line check")

        if balance == 0:
            print("\nYou don't have any money in your account!")            

        elif withdraw<500:
            print("\nSorry, minimun limit is 500tk")

        else:
            print(f"You have withdraw {withdraw} tk\n& you current banlace is {balance - withdraw}")           
            balance=balance-withdraw 
 
        press_continue2=input("\n\tEnter any key to continue \n")    
    
    elif menu_option=="3":
        # Add money
        os.system('cls')
        add_money= int(input("How much money do you want to add : "))
        if add_money<500:
            print("\nMinimum you have to add 500tk\n")

        elif add_money>50000:
            print("\nYou can not add more than 50,000tk in ATM\n")    

        else:
            balance+=add_money
            print(f"\nYour balance is updated\n {add_money} tk is added to your account")

        press_continue3=input("\n\tEnter any key to continue \n")

    elif menu_option=="4":
        # exit
        break               
                            

print("\nThank you\n")