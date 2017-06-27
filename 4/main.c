/*В массиве числа, которые являются числами Фибоначчи, заменить на их индексы*/

#include <stdio.h>

#define OK 0
#define INCOR_INP -1
#define INCOR_LEN -2
#define OP_ERR -3
#define MAX_LEN 20

int main(int argc, char **argv);
int read_arr(FILE *f, int *arr, int *size);
int print_arr(int *arr, int size);
int is_fib(int number);
int change_arr(int *arr, int size);
int write_arr(FILE *f, int *arr, int size);

int read_arr(FILE *f, int *arr, int *size)
{
    if ((fscanf(f, "%i", size) != 1) || (*size > MAX_LEN) || (*size < 1))
    {
        printf("Incorrect size\n");

        return INCOR_LEN;
    }
    for (int i = 0; i < *size; i++)
    {
        if (fscanf(f, "%i", &(arr[i])) != 1)
        {
            printf("Incorrect input\n");

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

int is_fib(int number)
{
    int a = 0;
    int b = 1;
    //int buf;

    while (b <= number)
    {
        /*buf = b;
        b += a;
        a = buf;*/

        b += a; //b - сумма
        a = b - a; //новый a = b = сумма - a

        if (b == number)
        {
            return 1;
        }
    }

    return 0;
}

int change_arr(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (is_fib(arr[i]) == 1)
        {
            arr[i] = i;
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
    change_arr(arr, size);
    print_arr(arr, size);
    write_arr(f2, arr, size);

    return OK;
}