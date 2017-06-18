/*Найти среднее арифметическое массива, исключив минимум и максимум*/

#include <stdio.h>
#include "list.h"

#define OK 0
#define INCOR_INP -1
#define INCOR_LEN -2
#define OP_ERR -3
#define INCOR_NUMB -4
#define MAX_LEN 20

int main(int argc, char **argv);
int read_arr(FILE *f, int *arr, int *size);
int srednee(int *arr, int size, float *sredn);
int print_arr(int *arr, int size);
int writing(FILE *f, float sredn);
int find_max(int *arr, int size);
int find_min(int *arr, int size);

int main(int argc, char **argv)
{
    setbuf(stdout, NULL);

    int arr[MAX_LEN];
    int size;
    float sredn;
    FILE *f1, *f2;

    if (argc != 3)
    {
        printf("Incorrect args count");
        return INCOR_INP;
    }

    f1 = fopen(argv[1], "r");
    f2 = fopen(argv[2], "w");

    if ((f1 == NULL) || (f2 == NULL))
    {
        printf("There is an error with opening files\n");
        return OP_ERR;
    }

    if (read_arr(f1, arr, &size) == INCOR_LEN)
    {
        printf("There are no numbers in the file\n");

        return INCOR_LEN;
    }
    else
    {
        printf("An array:\n");
        print_arr(arr, size);
        if (srednee(arr, size, &sredn) == 0)
        {
            writing(f2, sredn);
            printf("\nSrednee had been written in the second file\n");
            printf("Srednee = %f", sredn);
            
            return INCOR_NUMB;
        }
    }

    return OK;
}