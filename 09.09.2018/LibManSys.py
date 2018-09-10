# Library Management System
import time

MemDetails = {}
BookData = {1: ["Java", 2, 1], 2 : ["DAA", 2, 1], 3 : ["COA", 2, 1], 4 : ["Maths", 2, 1]}

def BookIssue():
    reg = int(input("Enter The  Registration Number : "))
    
    if reg not in MemDetails.keys():
        MemDetails[reg] = []
    else:
        pass
    
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
    ret = 0
    
    if reg in MemDetails.keys():
        print("\nISBN\t\tNAME\t\tRETURN STATUS\t\tTIME\n")

        for i in range(0, len(MemDetails[reg])):
            print("{}\t\t{}\t\t{}\t\t\t{}" .format(MemDetails[reg][i][0], BookData[MemDetails[reg][i][0]][0], MemDetails[reg][i][2], time.time() - MemDetails[reg][i][1]))

        choice = int(input("Enter The ISBN To Return : "))

        for i in range(0, len(MemDetails[reg])):
            if choice == MemDetails[reg][i][0] and MemDetails[reg][i][2] == "No":
                MemDetails[reg][i][2] = "Yes"
                BookData[choice][1] += 1
                
                if BookData[choice][1] == 0:
                    BookData[choice][2] = 0
                else:
                    BookData[choice][2] = 1
                    
                print("\nBook Has Been Returned")            
                if time.time() - MemDetails[reg][i][1] > 60:
                    print("FINE : Rs. {}" .format((time.time() - MemDetails[reg][i][1] - 60) * 2))
                else:
                    print("FINE : 0")

                ret = 1

            elif choice == MemDetails[reg][i][0] and MemDetails[reg][i][2] == "Yes":
                print("\nBook Has Already Been Returned\n")
                ret = 1
                
            else:
                pass
        
        if ret != 1:
            print("\nWrong ISBN Number\n")
    
    else:
        print("\nMember Not Found\n")
            
            
def MemDet():
    reg = int(input("Enter The Registartion Number : "))
    
    if reg in MemDetails.keys():
        print("\nISBN\t\tNAME\t\tRETURN STATUS\t\tTIME\n")
    
        for i in range(0, len(MemDetails[reg])):
            print("{}\t\t{}\t\t{}\t\t\t{}" .format(MemDetails[reg][i][0], BookData[MemDetails[reg][i][0]][0], MemDetails[reg][i][2], (time.time() - MemDetails[reg][i][1])))
    else:
        print("\nMember Not Found\n")

while(True):
    print("\nWELCOME TO LIBRARY MANAGEMENT SYSTEM\n")
    
    print("1. Book Issue\n2. Return Book\n3. Member Details\n4. Exit\n\n")
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