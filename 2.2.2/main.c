/*Сумма элементов массива, произведение элементов массива, среднее значение элементов*/
/*Допущение: сумма всех, произведение стоящих на чётных местах по тому, как видит программист*/

#include <stdio.h>

#define OK 0
#define SIZE -1

#define MAX_SIZE 10

int read_array(int *array)
{
    int size;

    printf("Input the size of an array, up to %d:\n", MAX_SIZE);
    if (scanf("%i", &size) != 1)
    {
        printf("Incorrect size");

        return SIZE; 
    }
    else
    {
        if (size >= 0)
        {
            for (int i = 0; i < size; i++)
            {
                scanf("%d", &array[i]);
            }
        }
        else
        {
            printf("Incorrect size");

            return SIZE;
        }
    }

    return size;
}

int sum(int *array, int size)
{
    int summa = 0;

    for (int i = 0; i < size; i++)
    {
        summa += array[i];
    }

    return summa;
}

float srednee(int *array, int size)
{
    float sredn;

    sredn = sum(array, size)/size;

    return sredn;
}

int proizv(int *array, int size)
{
    int proizved = 1;
    int count = 0;

    if (size != 0)
    {
        for (int i = 0; i < size; i += 2)
        {
            proizved *= array[i];
            count++;
        }
    }

    return proizved;
}

int main(void)
{
    setbuf(stdout, NULL);

    int size;
    int summa;
    float sredn;
    int proizved;

    int array[MAX_SIZE];

    size = read_array(array);
    summa = sum(array, size);
    printf("\nSumma = %d", summa);
    sredn = srednee(array, size);
    printf("\nSrednee = %f", sredn);
    proizved = proizv(array, size);
    if (size != 0)
    {
        printf("\nProizv = %d", proizved);
    }
    else
    {
        printf("\nThe length of the array is zero");
    }

    return OK;
}