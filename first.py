import random


print(" Lets Start ! Roll Dice-->(y/n): ",end='')
con=input()

while con.upper()=='Y':
    a=random.randint(1,6)
   
    if a==1:
        print(" _____")
        print("|     |")
        print("|  0  |")
        print("|_____|")
        print('')
        print('GOOD !')
    elif a==2:
        print(" _____")
        print("|     |")
        print("| 0 0 |")
        print("|_____|")
        print('')
        print(' Nice move!')
    elif a==3:
        print(" _____")
        print("|  0  |")
        print("|     |")
        print("|_0_0_|")
        print('')
        print(' Great!')    
    elif a==4:
        print(" _____")
        print("| 0 0 |")
        print("|     |")
        print("|_0_0_|") 
        print('')
        print(' Awsome..')
    elif a==5:
        print(" _____")
        print("| 0 0 |")
        print("|  0  |")
        print("|_0_0_|") 
        print('')
        print(' Excellent!')  
    elif a==6:
        print(" _____")
        print("| 0 0 |")
        print("| 0 0 |")
        print("|_0_0_|") 
        print('')
        print(' Outstanding!!')
    print('')
    print("NUMBER: ",a)
    
    print("Roll Dice again? (y/n): ",end='')
    con=input()