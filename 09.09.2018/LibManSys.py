# Library Management System
import time

MemDetails = {}
BookData = {1: ["Java", 2, 1], 2 : ["DAA", 2, 1], 3 : ["COA", 2, 1], 4 : ["Maths", 2, 1]}

def BookIssue():
    reg = int(input("Enter The  Registration Number : "))
    MemDetails[reg] = []
    
    print("\nISBN\t\tBook Name\t\tNumber Of Books\n")
    for i in BookData.keys():
        print("{}\t\t{}\t\t\t{}" .format(i, BookData[i][0], BookData[i][1]))
            
    choice = int(input("Enter The ISBN To Issue : "))
    
    if BookData[choice][2] == 1:
        temp = []
        temp.append(choice)
        temp.append(time.time())
        temp.append("No")
        MemDetails[reg].append(temp)
        print("\nBook Has Been Issued\n")
        
        BookData[choice][1] -= 1        
        if BookData[choice][1] == 0:
            BookData[choice][2] = 0
        else:
            pass
        
    else:
        print("Sorry, Book Not Available")
        
        
def ReturnBook():
    reg = int(input("Enter The Registartion Number : "))
    
    print("\nISBN\t\tNAME\t\t\tRETURN STATUS\t\tTIME\n")
    
    for i in range(0, len(MemDetails[reg])):
        print("{}\t\t{}\t\t{}\t\t{}" .format(MemDetails[reg][i][0], BookData[MemDetails[reg][i][0]][0], MemDetails[reg][i][2], (time.time() - MemDetails[reg][i][1])))
        
    choice = int(input("Enter The ISBN To Return : "))
    
    for i in range(0, len(MemDetails[reg])):
        if choice == MemDetails[reg][i][0]:
            MemDetails[reg][i][2] = "Yes"
            print("\nBook Has Been Returned")            
            if time.time() - MemDetails[reg][i][1] > 60:
                print("FINE : {}", format((60 - time.time() - MemDetails[reg][i][1]) * 2))
            else:
                print("FINE : 0")
        else:
            print("\nWrong ISBN Number\n")
            
            
def MemDet():
    reg = int(input("Enter The Registartion Number : "))
    
    print("\nISBN\t\tNAME\t\t\tRETURN STATUS\t\tTIME\n")
    
    for i in range(0, len(MemDetails[reg])):
        print("{}\t\t{}\t\t{}\t\t{}" .format(MemDetails[reg][i][0], BookData[MemDetails[reg][i][0]][0], MemDetails[reg][i][2], (time.time() - MemDetails[reg][i][1])))

while(True):
    print("\nWELCOME TO LIBRARY MANAGEMENT SYSTEM\n")
    
    print("1. Book Issue\n2. Return Book\n3. Member Details\n4. Exit\n\nChoice : ")
    choice = int(input("Choice : "))
    
    if choice == 1:
        BookIssue()
    elif choice == 2:
        ReturnBook()
    elif choice == 3:
        MemDet()   
    elif choice == 4:
        break
    else:
        print("Invalid Input")