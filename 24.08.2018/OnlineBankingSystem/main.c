#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

const int Upper = 10000, Lower = 1000;

struct User
{
    int AccNo;
    char UserName[20], Password[100], Name[20];
};

void UserRegster(struct User *NewUser)
{
    printf("\n\nWELCOME TO SMIT BANK\n");

    printf("\nEnter Your Name : ");
    gets(NewUser->Name);
    printf("Select Username : ");
    gets(NewUser->UserName);
    printf("Enter The Password : ");
    gets(NewUser->Password);

    NewUser->AccNo =  (rand() % (Upper - (Lower + 1))) + Lower;
    printf("\n\nRegistration Has Been Complete!\nNew Account Number : %d", NewUser->AccNo);
}

void UserDisplay(struct User NewUser)
{
    printf("\n\nUser Information\n");
    printf("\nName : %s\nUserName : %s\nAccount Number : %d\n", NewUser.Name, NewUser.UserName, NewUser.AccNo);
}

void UserLogIn(int *UserList)
{
    int AccNo;
    char Password[100];

    printf("\n\nENTER LOG-IN DETAILS\n");

    printf("\nEnter Your Account Number : ");
    scanf("%d", &AccNo);
    printf("Enter The Password : ");
    gets(Password);

    for(int i=0; i<100; i++)
    {
        if(AccNo == UserList[i].AccNo)
        {
            if(Password == UserList[i].Password)
            {
                printf("\nLog-In Successful!");
                break;
            }

            else
            {
                printf("\nWrong Password");
                break;
            }
        }
    }
}

int main()
{
    struct User UserList[100];
    int *ptr;

    //ptr = &UserList;
    UserRegster(&UserList[1]);
    UserDisplay(UserList[1]);
    //UserLogIn(ptr);
    return 0;
}