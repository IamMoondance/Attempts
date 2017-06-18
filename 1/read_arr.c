#include <stdio.h>
#include "list.h" 

#define OK 0
#define INCOR_INP -1
#define INCOR_LEN -2
#define OP_ERR -3
#define INCOR_NUMB -4
#define MAX_LEN 20

int read_arr(FILE *f, int *arr, int *size)
{
    if ((fscanf(f, "%i", size) != 1) || (*size > MAX_LEN) || (*size < 1))
    {
        return INCOR_LEN;
    }
    for (int i = 0; i < *size; i++)
    {
        if (fscanf(f, "%i", &(arr[i])) != 1)
        {
            return INCOR_INP;
        }
    }
    return OK;
}