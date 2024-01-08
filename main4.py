# Welcome
def welcome():
    print('\t\t*** Welcome to State Bank Of India Atm. ***')

def exit():
    print('Thankyou for using SBI')
    print('Remove Card')

# Move previous option
def previous():
    print('Type 1 for moving previos Option')
    num=enterValue()
    while True:
        if num==1:
            options()
            break
        else:
            num=enterValue()
            

# Remove money to bank account
balance=2000
def withdrawlLogic():
    global balance
    balance=balance - withdrawlAmount
            
def withdrawl():
    print('Enter amount you want to Withdrawl\n')
    global withdrawlAmount
    withdrawlAmount=enterValue()
    while True:
        if withdrawlAmount<=balance and withdrawlAmount>0:
            print(withdrawlAmount,'has been Remove')
            print('Move to previos option to check balance')
            withdrawlLogic()
            previous()
            break
        else:
            print("Please check the balance and enter the correct amount")
            previous()
            withdrawlAmount=enterValue()




def depositlLogic():
    global balance
    balance=balance + depositAmount
            


# Add money to bank account
def deposit():
    print('Enter amount you want to deposit\n')
    global depositAmount
    depositAmount=enterValue()
    while True:
        if depositAmount>0:
            print(depositAmount,'has been Added')
            print('Move to previos option to check balance')
            depositlLogic()
            previous()
            break
        else:
            print('Please enter Correct Amount')
            depositAmount=enterValue()
            




# Check Balance
# startingCurruntBalance=2000
# newBalance=2000
def checkBalance():
    global balance
    # global newBalance
    print('Current Balance :\t',balance)
    previous()

# Person Account Detail
def acoountDetail():
    print('-'*50)
    print('Acc name :\tNikhil Dasgupta')
    print('-'*50)
    print('Acc no. :\tXXXXX2345')
    print('-'*50)
    print('\n')

# Authentication Officer
def auth():
    value=1234
    count=3
    print('Enter PIN: \n')
    pinnum=enterValue()
    flag=True
    while flag:
        if value==pinnum:
            acoountDetail()
            options()
            flag=False
        else:
            count-=1
            if count==0:
                print('You have exceeded your limit *** CARD HAS BEEN BLOCKED ***')
                flag=False
            else:
                print('You have',count,'chance.\n')
                print('Enter correct PIN please.')
                pinnum=enterValue()






# Options
def options():
    print('''
        1. DEPOSIT\t\t2. WITHDRAWL\n
        3. CHANGE PIN\t\t4. CHECK BALANCE\n
        5. EXIT''')
    print('\nPress the Option to move further:')
    global num
    num=enterValue()
    flag=True
    while flag:
        if num==1:
            print('Deposit')
            deposit()
            flag=False
        elif num==2:
            print('Withdrawl')
            withdrawl()
            flag=False
        elif num==3:
            print('Change Pin')
            flag=False
        elif num==4:
            print('\nCheck Balance\n')
            checkBalance()
            print('\n')
            previous()
            print('\n')
            flag=False
        elif num==5:
            exit()
            flag=False
        else:
            print('Please choose the right Option')
            num=enterValue()
        

# SBI Main Interface
def sbiMain():
    welcome()
    auth()


# User will Input
def enterValue():
    num=int(input('Enter: '))
    return num


sbiMain()