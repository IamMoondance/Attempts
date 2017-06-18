#include <stdio.h>
#include "list.h"

int count(int n)
{
    int count = 0;
    int number;

    for (int i = 0; i < n; i++)
    {
        if (scanf("%i", &number) == 1)
        {
            if (is_sqr(number) == 1)
            {
                printf("%i\n", number);
                count++;
            }
        }
        else
        {
            break; 
        }
    }

    return count;
}