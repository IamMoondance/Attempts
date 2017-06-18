/*Вводится последовательность, максимально из n элементов. Вывести элементы, являющиеся полными квадратами,
 а также их количество*/

#include <stdio.h>
#include "list.h"

#define OK 0
#define INCOR_N -1

int count(int n);
int is_sqr(int number);

int main(void)
{
    setbuf(stdout, NULL);

    int n;

    printf("Input max size of the arange\n");
    if ((scanf("%i", &n) != 1) || (n <= 0))
    {
        printf("Inccorect length");

        return INCOR_N;
    }
    else
    {
        printf("The number of the useful elements is %i\n", count(n));
    
    }

    return OK;
}