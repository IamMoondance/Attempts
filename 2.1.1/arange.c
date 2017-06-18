#include <stdio.h>
#include "list.h"

int arange(void) //возвращает число элементов и меняет количество чётных по указателю
{
    int count = 0;
    int even = 0;
    int number;

    while (scanf("%i", &number) == 1)
    {
        count++;
        if (count > 10)
        {
            printf("Too much elements!\n");
            break;
        }

        if (is_even(number) == 1)
            even += 1;
        //even += is_even(number);
    }

    if (count == 0)
    {
        return -1;
    }

    return even;
}