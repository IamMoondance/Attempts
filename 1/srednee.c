#include <stdio.h>
#include "list.h" 

#define OK 0
#define INCOR_INP -1
#define INCOR_LEN -2
#define OP_ERR -3
#define INCOR_NUMB -4
#define MAX_LEN 20

int srednee(int *arr, int size, float *sredn)
{
    int summa = 0;
    int count = 0;

    for (int i = 0; i < size; i++)
    {
        if ((arr[i] != find_min(arr, size)) && (arr[i] != find_max(arr, size)))
        {
            summa += arr[i];
            count++;
        }
    }
    if (count > 0)
    {
        *sredn = summa/count;

        return OK;
    }
    else
    {
        printf("Inccorect number of right elements without max and min\n");

        return INCOR_NUMB;
    }

    return OK;
}