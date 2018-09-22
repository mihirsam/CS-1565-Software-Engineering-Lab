#include <stdio.h>
#include<stdbool.h>
#include <memory.h>
#include<string.h>

struct Student
{
    int reg, books[100], count;
};

struct Book
{
    char Name[100], Author[100], Status[10];
    int Count, Isbn;
};


int main()
{
    struct Book book[3];
    struct Student stu[10];
    int choice, issueCount = 0, reg, flag = 0, isbn;

    //defining books
    strcpy(book[0].Name, "JAVA");
    strcpy(book[1].Name, "PPL");
    strcpy(book[2].Name, "MATHS");

    strcpy(book[0].Author, "Mr. Getting");
    strcpy(book[1].Author, "Ms. Minakshi Roy");
    strcpy(book[2].Author, "Mrs. Acchi Mam");

    strcpy(book[0].Status, "YES");
    strcpy(book[1].Status, "YES");
    strcpy(book[2].Status, "YES");

    book[0].Count =  2;
    book[1].Count =  2;
    book[2].Count =  2;

    book[0].Isbn =  0;
    book[1].Isbn =  1;
    book[2].Isbn =  2;

    while(true)
    {
        printf("\n\nWELCOME TO THE LIBRARY\n1. ISSUE BOOK\n2. RETURN BOOK\n3. AVAILABLE BOOK\n4. STUDENT INFO\n5. EXIT\n\nCHOICE : ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            printf("\nEnter Registration Number : ");
            scanf("%d", &reg);

            for(int i=0; i<10; i++)
            {
                if(reg == stu[i].reg)
                {
                    printf("\n\nISBN\t\tNAME\t\tAUTHOR\t\tCOUNT\t\tAVAILABLE\n\n");
                    for(int j=0; j<3; j++)
                    {
                        printf("%d\t\t%s\t\t%s\t\t%d\t\t%s\n", book[j].Isbn, book[j].Name, book[j].Author, book[j].Count, book[j].Status);
                    }

                    printf("\nEnter The ISBN Number To Issue : ");
                    scanf("%d", &isbn);

                    if(book[isbn].Count > 0)
                    {
                        book[isbn].Count -= 1;
                        stu[i].books[stu[i].count] = isbn;

                        if(book[isbn].Count == 0)
                        {
                            strcpy(book[isbn].Status, "NO");
                        }

                        printf("\n\nBook Has Been Issued!\n");
                    }

                    else
                    {
                        printf("\n\nBook Not Available\n");
                    }
                    flag = 1;
                    break;
                }
            }

            if(flag == 0)
            {
                stu[issueCount].reg = reg;
                printf("\n\nISBN\t\tNAME\t\tAUTHOR\t\tCOUNT\t\tAVAILABLE\n\n");
                for(int j=0; j<3; j++)
                {
                    printf("%d\t\t%s\t\t%s\t\t%d\t\t%s\n", book[j].Isbn, book[j].Name, book[j].Author, book[j].Count, book[j].Status);
                }

                printf("\nEnter The ISBN Number To Issue : ");
                scanf("%d", &isbn);

                if(book[isbn].Count > 0)
                {
                    book[isbn].Count -= 1;
                    stu[issueCount].books[stu[issueCount].count] = isbn;

                    if(book[isbn].Count == 0)
                    {
                        strcpy(book[isbn].Status, "NO");
                    }

                    printf("\n\nBook Has Been Issued!\n");
                }

                else
                {
                    printf("\n\nBook Not Available\n");
                }

                issueCount += 1;
            }
        }

        else if(choice == 5)
        {
            break;
        }
    }
    return 0;
}