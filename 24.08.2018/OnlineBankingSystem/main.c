#include <stdio.h>
#include <math.h>
#include <stdlib.h>Mihir
#include <string.h>

struct User
{
    int AccNo;
    char UserName[20], Password[100], PasswordCheck[100], Name[20];
};

struct UserRegster(struct User NewUser)
{
    char UserName[20];

    printf("\n\nWELCOME TO SMIT BANK\n");

    printf("\nEnter Your Name : ");
    gets(NewUser.UserName);

    return NewUser;
    //strcpy(NewUser->UserName, UserName);
    //scanf("%s", &NewUser.Name);
    //printf("Set Your Username : ");
    //scanf("%s", &NewUser.UserName);

};

int main() {
    struct User UserList[100];

    UserRegster(&UserList[1]);
    printf("Name : %s", UserList[1].Name);
    puts(UserList[1].Name);
    printf(UserList[1].Name);
    gets(UserList[1].Name);
    printf(UserList[1].Name);
    return 0;
}