/*В одномерном массиве, считанном из файла, где первой строкой в файле указан размер массива, 
поменять местами первый минимальный элемент с последним отрицательным*/

#include <stdio.h>

#define OK 0
#define OP_ERR -1
#define INCOR_LEN -2
#define INCOR_INP -3
#define NO_OTR -4
#define MAX_LEN 20

int main(int argc, char **argv);
int read_arr(FILE *f, int *arr, int *size);
int print_arr(int *arr, int size);
int min_el(int *arr, int size);
int otr_el(int *arr, int size);
int change_els(int *arr, int size);
int write_arr(FILE *f, int *arr, int size);

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

int print_arr(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%i ", arr[i]);
    }

    return OK;
}

int write_arr(FILE *f, int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        fprintf(f, "%i ", arr[i]);
    }

    return OK;
}


int min_el(int *arr, int size)
{
    int minel = arr[0];
    int indmin = 0;

    for (int i = 1; i < size; i++)
    {
        if (arr[i] < minel)
        {
            minel = arr[i];
            indmin = i;
        }
    }

    return indmin;
}

int otr_el(int *arr, int size)
{
    //int otrel;
    int indotr;
    int count = 0;

    for (int i = 0; i < size; i++)
    {
        if (arr[i] < 0)
        {
            //otrel = arr[i];
            indotr = i;
            count++;
        }
    }
    if (count == 0)
    {
        return NO_OTR;
    }

    return indotr;
}

int change_elem_another(int *arr, int size)
{
    for (int i = size - 1; i >= 0; i--)
    {
        if (arr[i] < 0)
        {
            return i;
        }
    }
    return NO_OTR;
}

int change_els(int *arr, int size)
{
    int buf;
    int minel, otrel;

    minel = min_el(arr, size);
    otrel = otr_el(arr, size);

    if (otrel == NO_OTR)
    {
        printf("Can't change cause there is no otr elements");

        return OK;
    }
    else
    {
        buf = arr[minel];
        arr[minel] = arr[otrel];
        arr[otrel] = buf;
    }

    return OK;
}

int main(int argc, char **argv)
{
    setbuf(stdout, NULL);

    int arr[MAX_LEN];
    int size;
    FILE *f1, *f2;

    if (argc != 3)
    {
        printf("Incorrect number of arguments");

        return OP_ERR;
    }

    f1 = fopen(argv[1], "r");
    f2 = fopen(argv[2], "w");

    if ((f1 == NULL) || (f2 == NULL))
    {
        printf("Can't open files");

        return OP_ERR;
    }

    read_arr(f1, arr, &size);
    print_arr(arr, size);
    change_els(arr, size);
    write_arr(f2, arr, size);

    return OK;
}