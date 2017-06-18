/*Программа считывает массив из файла, имя которого передаётся при запуске программы,
выводит на экран, сортирует пузырьком, выводит на экран, записывает в новый файл, имя которого
так же передаётся при запуске*/

#include <stdio.h>

#define OK 0
#define INCOR_LEN -1
#define OP_ERR -2
#define INCOR_ARG -3
#define INCOR_INPUT -4
#define ARR_LEN 20

int main(int argc, char **argv);
int reading(FILE *f, int *arr, int *size);
int print_arr(int *arr, int size);
int sort(int *arr, int size);
int writing(FILE *f, int *arr, int size);

int reading(FILE *f, int *arr, int *size)
{
    *size = 0;
    int buf;

    while (fscanf(f, "%i", &buf) == 1)
    {
        if (*size == ARR_LEN)
        {
            printf("Too many numbers in file; pass\n");
            return OK;
        }
        arr[*size] = buf;
        (*size)++;
    }

    if (*size == 0)
    {
        return INCOR_LEN;
    }

    return OK;
}

int read_arr(FILE *f, int *arr, int *size)
{
    if ((fscanf(f, "%i", size) != 1) || (*size < 1) || (*size > ARR_LEN))
    {
        return INCOR_LEN;
    }
    for (int i = 0; i < *size; i++)
    {
        if (fscanf(f, "%i", &(arr[i])) != 1)
        {
            return INCOR_INPUT;
        }
    }
    return OK;
}

int print_arr(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%i ", arr[i]); // *(arr + i)
    }

    return OK;
}

int sort(int *arr, int size)
{
    int buf;

    for (int i = size-1; i >= 0; i--)
    {
        for (int j = i; j < size-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                buf = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = buf;
            }
        }
    }

    return OK;
}

int writing(FILE *f, int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {
        fprintf(f, "%i ", arr[i]);
    }

    return OK;
}

int main(int argc, char **argv)
{
    setbuf(stdout, NULL);

    int arr[ARR_LEN];
    int size;
    FILE *f1, *f2;

    if (argc != 3)
    {
        printf("Incorrect args count");
        return INCOR_ARG;
    }
    f1 = fopen(argv[1], "r");
    f2 = fopen(argv[2], "w");
    if ((f1 == NULL) || (f2 == NULL))
    {
        printf("Error when open files");
        return OP_ERR;
    }

    if (reading(f1, arr, &size) == INCOR_LEN)
    {
        printf("There are no numbers in the file");

        return INCOR_LEN;
    }
    else
    {
        print_arr(arr, size);
        sort(arr, size);
        writing(f2, arr, size);
        printf("Sorted array had been written in the second file\n");
        printf("The array after the sort:\n");
        print_arr(arr, size);
    }

    return OK;
}