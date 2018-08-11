#include<stdio.h>
#include<ctype.h>

//Defining all structure

struct studentDetails
{
    char nam[20], sec, dep[10], pas[20];
    int sem, reg;
};

struct studentMarks
{
    char sub[20];
    int marks;
};

struct studentAttendance
{
    char sub[20];
    int att;
};

struct studentRemarks
{
    char nam[20], rem[100];
};

struct teacherDetails
{
    char nam[20], pas[20];
    int t_id;
};

// Defining All Functions

void studentRegister(struct studentDetails newStudent)
{
    printf("\n\nWELCOME TO STUDENT REGISTRATION\n\nEnter Your Name : ");
    scanf("%s", &newStudent.nam[20]);
    printf("Enter Section : ");
    scanf("%s", &newStudent.sec);
    printf("Enter Department : ");
    scanf("%s", &newStudent.dep[10]);
    printf("Enter Semester : ");
    scanf("%d", &newStudent.sem);
    printf("Enter Registration Number : ");
    scanf("%d", &newStudent.reg);
    printf("Enter Password : ");
    scanf("%s", &newStudent.pas[20]);

    printf("\nThank You. Your Registration Has Been Completed!");
}

int studentLogIn(struct studentDetails oldStudent)
{
    char tempPas[20];

    printf("Enter Password : ");
    scanf("%f", &tempPas);

    if(tempPas == oldStudent.pas)
    {
        printf("\nSuccessfully Logged-In!\n");
        return 1;
    }

    else
    {
        printf("\nWRONG PASSWORD!\n");
        return 0;
    }
}

void teacherRegister(struct teacherDetails newTeacher)
{
    printf("\n\nWELCOME TO TEACHER REGISTRATION\n\nEnter Your Name : ");
    scanf("%s", &newTeacher.nam);
    printf("Enter Teacher Id : ");
    scanf("%d", &newTeacher.t_id);
    printf("Enter Password : ");
    scanf("%s", &newTeacher.pas);

    printf("\nThank You. Your Registration Has Been Completed!");
}

int teacherLogIn(struct teacherDetails oldTeacher)
{
    char tempPas[20];

    printf("Enter Password : ");
    scanf("%s", &tempPas);

    if(tempPas == oldTeacher.pas)
    {
        printf("\nSuccessfully Logged-In\n");
        return 1;
    }

    else
    {
        printf("\nWRONG PASSWORD!\n");
        return 0;
    }
}

void studentPortal(struct studentDetails det, struct studentMarks mar, struct studentAttendance att, struct studentRemarks rem)
{
    int choice;

    printf("\n\nWELCOME %s TO THE STUDENT PORTAL\n\n", det.nam);

    while(1) {
        printf("1. Check Marks\n2. Check Attendance\n3. Check Remarks\n4. Log Out\nChoice : ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("\n\tSUBJECT\t\tMARKS\n");
            printf("%s, %d", mar.sub, mar.marks);
        }
        else if (choice == 2)
        {
            printf("\n\tSUBJECT\t\tATTENDANCE\n");
            printf("%s, %d", att.sub, att.att);
        }

        else if(choice == 3)
        {
            printf("\n\tSUBJECT\t\tREMARKS\n");
            printf("%s, %s", rem.nam, rem.rem);
        }

        else if(choice == 4)
        {
            printf("\nBye Bye!");
            break;
        }

        else
        {
            printf("\nInavlid Input!\nTry Agiain!");
        }
    }
}


int main()
{
    struct studentDetails stu[10];
    struct studentMarks mar[10];
    struct studentAttendance att[10];
    struct studentRemarks rem[10];
    struct teacherDetails tec[10];

    int teaFlag = 0, stuFlag = 0, choice, choice1, choice2;

    while(1)
    {
        printf("\n\nWELCOME TO SMIT PORTAL\n\n");

        printf("1. Student Portal\n2. Teacher Portal\n3. Exit\nChoice : ");
        scanf("%d", &choice);

        if(choice == 1)
        {
            while(1)
            {
                printf("\n\n1. Student Register\n2. Student Log-In\n3. Back\nChoice : ");
                scanf("%d", &choice1);

                if(choice1 == 1)
                {
                    studentRegister(stu[stuFlag]);
                    stuFlag++;
                }

                else if(choice1 == 2)
                {
                    int tempReg, tempFlag = 0, res;

                    printf("\nEnter Registration Number : ");
                    scanf("%d", &tempReg);

                    for(int i=0; i<stuFlag; i++)
                    {
                        if(stu[i].reg == tempReg)
                        {
                            tempFlag++;
                            res = studentLogIn(stu[i]);

                            if(res == 1)
                            {
                                studentPortal(stu[i], mar[i], att[i], rem[i]);
                            }
                        }
                    }

                    if(tempFlag == 0)
                    {
                        printf("\nUSER NOT FOUND!\n");
                    }
                }

                else if(choice1 == 3)
                {
                    break;
                }

                else
                {
                    printf("\nInvalid Input!\nTry Again!");
                }
            }

        }

        else if(choice == 2)
        {
            while(1)
            {
                printf("\n\n1. Teacher Register\n2. Teacher Log-In\n3. Back\nChoice : ");
                scanf("%d", &choice2);

                if(choice2 == 1)
                {
                    teacherRegister(tec[teaFlag]);
                    teaFlag++;
                }

                else if(choice2 == 2)
                {
                    int tempId, tempFlag = 0, res, tecChoice, stuReg, tempFlag2 = 0;

                    printf("\nEnter Teacher Id : ");
                    scanf("%d", &tempId);

                    for(int i=teaFlag; i<teaFlag; i++)
                    {
                        if(tec[i].t_id == tempId)
                        {
                            tempFlag++;
                            res = teacherLogIn(tec[i]);

                            if(res == 1)
                            {
                                while(1)
                                {
                                    printf("\n\nWELCOME %s TO TEACHER PORTAL\n\n", tec[i]);

                                    printf("\n1. Enter Marks\n2. Enter Attendance\n3. Enter Remarks\n4. Log-Out\n Choice : ");
                                    scanf("%d", &tecChoice);

                                    if(tecChoice == 1)
                                    {
                                        tempFlag2 = 0;

                                        printf("\nEnter Student Registration Number : ");
                                        scanf("%d", &stuReg);

                                        for(int i=0; i<stuFlag; i++)
                                        {
                                            if(stu[i].reg == stuReg)
                                            {
                                                tempFlag2++;

                                                printf("\nEnter Subject : ");
                                                scanf("%s", &mar[i].sub);
                                                printf("Enter Marks : ");
                                                scanf("%d", &mar[i].marks);

                                                printf("\nMarks Has Been Updated!");
                                            }
                                        }

                                        if(tempFlag2 == 0)
                                        {
                                            printf("\nUSER NOT FOUND!\n");
                                        }
                                    }

                                    else if(tecChoice == 2)
                                    {
                                        tempFlag2 = 0;

                                        printf("\nEnter Student Registration Number : ");
                                        scanf("%d", &stuReg);

                                        for(int i=0; i<stuFlag; i++)
                                        {
                                            if(stu[i].reg == stuReg)
                                            {
                                                tempFlag2++;

                                                printf("\nEnter Subject : ");
                                                scanf("%s", &att[i].sub);
                                                printf("Enter Marks : ");
                                                scanf("%d", &att[i].att);

                                                printf("\nAttendance Has Been Updated!");
                                            }
                                        }

                                        if(tempFlag2 == 0)
                                        {
                                            printf("\nUSER NOT FOUND!\n");
                                        }
                                    }

                                    else if(tecChoice == 3)
                                    {
                                        tempFlag2 = 0;

                                        printf("\nEnter Student Registration Number : ");
                                        scanf("%d", &stuReg);

                                        for(int i=0; i<stuFlag; i++)
                                        {
                                            if(stu[i].reg == stuReg)
                                            {
                                                tempFlag2++;

                                                printf("\nEnter Subject : ");
                                                scanf("%s", &rem[i].nam);
                                                printf("Enter Marks : ");
                                                scanf("%s", &rem[i].rem);

                                                printf("\nRemarks Has Been Updated!");
                                            }
                                        }

                                        if(tempFlag2 == 0)
                                        {
                                            printf("\nUSER NOT FOUND!\n");
                                        }
                                    }

                                    else if(tecChoice == 4)
                                    {
                                        break;
                                    }

                                    else
                                    {
                                        printf("\nInvalid Input! Try Again!");
                                    }
                                }
                            }
                        }

                        if(tempFlag == 0)
                        {
                            printf("\nUSER NOT FOUND!\n");
                        }
                    }
                }

                else if(choice2 == 3)
                {
                    break;
                }

                else
                {
                    printf("\nInvalid Input!\nTry Again!\n");
                }
            }

        }

        else if(choice == 3)
        {
            printf("\nTHANK YOU!\n");
            break;
        }

        else
        {
            printf("\nInvalid Input!\nTry Again!");
        }
    }
}
