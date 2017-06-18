#include <stdio.h>
#include "list.h" 

#define OK 0
#define INCOR_INP -1
#define INCOR_LEN -2
#define OP_ERR -3
#define INCOR_NUMB -4
#define MAX_LEN 20

int print_arr(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%i ", arr[i]);
    }

    return OK;
}