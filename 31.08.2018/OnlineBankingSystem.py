
# coding: utf-8

# In[ ]:


import random


# In[ ]:


UserDetails = {}
UserTransRecord = {}
AdminDetails = {'admin' : 'admin123'}


# In[ ]:


def UserReg():
    print("\nWELCOME TO USER REGISTRATION\n")
    
    nam = input("Enter Name : ")
    pas = input("Enter Password : ")
    accNo = random.randint(1000, 10000)
    
    while(True):
        if accNo not in UserDetails.keys():
            break
        else:
            accNo = random.randint(1000, 10000)
    
    bal = 10000
    temp = [nam, pas, accNo, bal]
    UserDetails[accNo] = temp
    UserTransRecord[accNo] = []
    
    print("\nYour New Account Number : {}" .format(accNo))
    print("\nREGISTRATION HAS BEEN COMPLETED!")


# In[ ]:


def UserLogIn():
    accNo = int(input("Enter Account Name : "))
    pas = input("Enter Password : ")
    
    if accNo in UserDetails.keys():
        if UserDetails[accNo][1] == pas:
            print("\nLog-In Successful!\n")
            UserPortal(accNo)
        else:
            print("\nWrong Password!")
    else:
        print("\nUser Not Found!")


# In[ ]:


def UserPortal(accNo):
    print("\n\nWELCOME {} TO CHOTU Sa BANK\n" .format(UserDetails[accNo][0]))
    
    while(True):
        choice = int(input("1. Check Balance\n2. Fund Transfer\n3. Transaction History\n4. Back\n\nChoice : "))
        
        if choice == 1:
            print("\nBalance : {}\n" .format(UserDetails[accNo][3]))
        
        elif choice == 2:
            FundTransfer(accNo)
            
        elif choice == 3:
            TransHist(accNo)
            
        elif choice == 4:
            break
            
        else:
            print("\nInvalid Input!\nTry Again!")


# In[ ]:


def FundTransfer(accNo):
    print("\n\nWELCOME {} TO FUND TRANSFER UNIT\n" .format(UserDetails[accNo][0]))
    print("Current Account Balance : {}" .format(UserDetails[accNo][3]))
    
    accNoTemp = int(input("Enter Account Number Of Reciever : "))
    amt = int(input("Enter Amount To Transfer : "))
    
    if amt > UserDetails[accNo][3]:
        print("\nSorry, Insufficient Balance!")
    else:
        UserDetails[accNo][3] -= amt
        UserDetails[accNoTemp][3] += amt
        
        record = (accNo, accNoTemp, amt)
        UserTransRecord[accNo].append(record)
        UserTransRecord[accNoTemp].append(record)
        
        print("\nSuccessfully Transfered {} To {}(Acc No. {})\n" .format(amt, UserDetails[accNoTemp][0], accNoTemp))
        print("Current Account Balance : {}" .format(UserDetails[accNo][3]))


# In[ ]:


def TransHist(accNo):
    print("\nTRANSACTION HISTORY OF {}\n\n" .format(UserDetails[accNo][0]))
    
    for i in range(0, len(UserTransRecord[accNo])):
        print("From : {}\tTo : {}\tAmount : {}" .format(UserTransRecord[accNo][i][0], UserTransRecord[accNo][i][1], UserTransRecord[accNo][i][2]))


# In[ ]:


while(True):
    print("\nWELCOME TO CHOTU Sa BANK\n")
    choice = int(input("1. User Registration\n2. User Log-In\n3. Exit\n\nChoice : "))
    
    if choice == 1:
        UserReg()
    elif choice == 2:
        UserLogIn()
    elif choice == 3:
        break
    else:
        print("\nInvalid Input! Try again!")

