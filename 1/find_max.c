#include <stdio.h>
#include "list.h" 

#define OK 0
#define INCOR_INP -1
#define INCOR_LEN -2
#define OP_ERR -3
#define INCOR_NUMB -4
#define MAX_LEN 20

int find_max(int *arr, int size)
{
    int max_el;

    max_el = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > max_el)
        {
            max_el = arr[i];
        }
    }

    return max_el;
}