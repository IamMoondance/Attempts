/*Отсортировать нечётные элементы в массиве*/

#include <stdio.h>

#define OK 0
#define OP_ERR -1
#define INCOR_LEN -2
#define INCOR_INP -3
#define MAX_LEN 20

int main(int argc, char **argv);
int read_arr(FILE *f, int *arr, int *size);
int print_arr(int *arr, int size);
int write_arr(FILE *f, int *arr, int size);
int sort_odd(int *arr, int size);
int is_odd(int *arr, int size, int *arr_ind, int *ind_size);

int read_arr(FILE *f, int *arr, int *size)
{
    if ((fscanf(f, "%i", size) != 1) || (*size > MAX_LEN) || (*size < 1))
    {
        printf("Incorrect length of the array\n");

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

int is_odd(int *arr, int size, int *arr_ind, int *ind_size)
{
    *ind_size = 0;

    for (int i = 0; i < size; i++)
    {
        if (arr[i] % 2 == 1)
        {
            arr_ind[*ind_size] = i;
            (*ind_size)++;
        }
    }
    return OK;
}

int sort_odd(int *arr, int size)
{
    int arr_ind[MAX_LEN];
    int ind_size = 0;
    int buf;

    is_odd(arr, size, arr_ind, &ind_size);

    //sorting; arr[arr_ind[j]]

    for (int i = 0; i < ind_size; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (arr[arr_ind[j]] < arr[arr_ind[j-1]])
            {
                buf = arr[arr_ind[j]];
                arr[arr_ind[j]] = arr[arr_ind[j-1]];
                arr[arr_ind[j-1]] = buf;
            }
        }
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
        printf("Incorrect number of arguments\n");

        return INCOR_INP;
    }

    f1 = fopen(argv[1], "r");
    f2 = fopen(argv[2], "w");

    if ((f1 == NULL) || (f2 == NULL))
    {
        printf("Can't open files\n");

        return OP_ERR;
    }

    read_arr(f1, arr, &size);
    print_arr(arr, size);
    printf("\n");
    sort_odd(arr, size);
    print_arr(arr, size);

    return OK;
}