
# coding: utf-8

# In[17]:


studentDetails = {}
studentMarks = {}
studentAttendance = {}
studentRemarks = {}

teacherDetails = {}


# In[18]:


def studentRegister():
    print("\n\n\nWELCOME TO STUDENT REGISTRATION\n\n")
    
    nam = input("Enter Your Name : ")
    sec = input("Enter Your Section : ")
    dep = input("Enter Your Department : ")
    reg = int(input("Enter Your Registration Number : "))
    pas = input("Enter Your Password : ")
    
    temp = []
    temp.append(nam)
    temp.append(sec)
    temp.append(dep)
    temp.append(reg)
    temp.append(pas)
 
    studentDetails[reg] = temp
    studentMarks[reg] = []
    studentAttendance[reg] = []
    studentRemarks[reg] = []
    
    print("\nSTUDENT REGISTRATION SUCCESSFUL\n")


# In[19]:


def studentLogIn():
    print("\n\n\nWELCOME TO STUDENT PORTAL\n\n")
    
    reg = int(input("Enter The Registration Number : "))
    pas = input("Enter The Password : ")
    
    if reg in studentDetails.keys():
        if(studentDetails[reg][4] == pas):
            print("\nLog-In Successful\n")
            studentPortal(reg)
        else:
            print("\nWrong Password\n")
    else:
        while(True):
            choice = ("\nStudent Not Registered!\nDo You Want To Register ?\n1. Yes\n2. No\nChoice : ")
        
            if(choice == 1):
                studentRegister()
            elif(choice == 2):
                break
            else:
                print("Invalid Input!\nTry Again!")
                


# In[20]:


def teacherRegister():
    print("\n\n\nWELCOME TO TEACHER REGISTRATION\n\n")
    
    nam = input("Enter Your Name : ")
    t_no = int(input("Enter Your Teacher Number : "))
    pas = input("Enter Your Password : ")
    
    temp = []
    temp.append(nam)
    temp.append(t_no)
    temp.append(pas)
    
    teacherDetails[t_no] = temp
    print("\n\nTEACHER REGISTRATION SUCCESSFUL\n")


# In[21]:


def teacherLogIn():
    print("\n\n\nWELCOME TO TEACHER PORTAL\n\n")
    
    t_no = int(input("Enter Teacher Number : "))
    pas = input("Enter Password : ")
    
    if t_no in teacherDetails.keys():
        if(teacherDetails[t_no][2] == pas):
            print("\nLog-In Successful!\n")
            teacherPortal(t_no)
            
        else:
            print("\nWrong Password!")
    else:
        while(True):
            choice = int(input("\nTeacher Not Registered!\nDo You Want To Register ?\n1. Yes\n2. No\nChoice : "))
        
            if(choice == 1):
                teacherRegister()
            elif(choice == 2):
                break
            else:
                print("\n\nInvalid Input!\nTry Again!")


# In[22]:


def teacherPortal(t_no):
    print("\n\n\nWELCOME {} TO THE TEACHER PORTAL" .format(teacherDetails[t_no][0].upper()))
    
    while(True):
        choice = int(input("\n\n1. Enter Student Marks\n2. Enter Student Attendance\n3. Enter Student Remarks\n4. Exit\nChoice : "))

        if(choice == 1):
            reg = int(input("\n\nEnter The Student Registartion Number : "))

            if reg in studentDetails.keys():
                sub = input("Enter The Subject : ")
                mar = int(input("Enter The Marks : "))

                studentMarks[reg].append(sub)
                studentMarks[reg].append(mar)

                print("\n\nMarks Has Been Updated!")

            else:
                print("Student Not Found!")

        elif(choice == 2):
            reg = int(input("Enter The Student Registartion Number : "))

            if reg in studentDetails.keys():
                sub = input("Enter The Subject : ")
                att = int(input("Enter The Attendance : "))

                studentAttendance[reg].append(sub)
                studentAttendance[reg].append(att)

                print("\n\nAttendance Has Been Updated!")

            else:
                print("Student Not Found!")


        elif(choice == 3):
            reg = int(input("Enter The Student Registartion Number : "))

            if reg in studentDetails.keys():
                rem = input("Enter The Remarks : ")
                
                studentRemarks[reg].append(teacherDetails[t_no][0])
                studentRemarks[reg].append(rem)

                print("\n\nRemarks Has Been Updated!")

            else:
                print("\nStudent Not Found!")

                
        elif(choice == 4):
            print("\nBye Bye!")
            break
            
        else:
            print("\nInvalid Input!\nTry Again!")


# In[23]:


def studentPortal(reg):
        print("\n\n\nWELCOME {} TO THE STUDENT PORTAL" .format(studentDetails[reg][0]))
        
        while(True):
            choice = int(input("\n\n1. Check Marks\n2. Check Attendance\n3. Check Remarks\n4. Exit\nChoice : "))
            
            if(choice == 1):
                print("\n\nSUBJECT\t\tMARKS\n")
                for i in range(0, int((len(studentMarks[reg])/2))):
                    print(studentMarks[reg][2*i],"\t\t",studentMarks[reg][2*i + 1])

            elif(choice == 2):
                print("\n\nSUBJECT\t\tATTENDANCE\n")
                for i in range(0, int((len(studentAttendance[reg])/2))):
                    print(studentAttendance[reg][2*i],"\t\t",studentAttendance[reg][2*i + 1])

            elif(choice == 3):
                print("\n\nTEACHER\t\tREMARKS\n")
                for i in range(0, int((len(studentRemarks[reg])/2))):
                    print(studentRemarks[reg][2*i],"\t\t",studentRemarks[reg][2*i + 1])
            
            elif(choice == 4):
                print("\n\nBye Bye!")
                break
                
            else:
                print("\n\nInvalid Input")


# In[ ]:


while(True):
    choice = int(input("\n\n\nWELCOME TO SMIT\n1. Student Portal\n2. Teacher Portal\n3. Exit\nChoice : "))
    
    if(choice == 1):
        
        while(True):
            choice_student = int(input("\n1. Student Registration\n2. Student Log-In\n3. Back\nChoice : "))

            if(choice_student == 1):
                studentRegister()
            elif(choice_student == 2):
                studentLogIn()
            elif(choice_student == 3):
                break
            else:
                print("\nInvalid Input!\nTry Again!")
        
    elif(choice == 2):
        
        while(True):
            choice_teacher = int(input("\n1. Teacher Registration\n2. Teacher Log-In\n3. Back\nChoice : "))

            if(choice_teacher == 1):
                teacherRegister()
            elif(choice_teacher == 2):
                teacherLogIn()
            elif(choice_teacher == 3):
                break
            else:
                print("\nInvalid Input!\nTry Again!")
                
    elif(choice == 3):
        print("\nBye Bye!")
        break
        exit()
        
    else:
        print("\nInvalid Input!\nTry  Again!")

