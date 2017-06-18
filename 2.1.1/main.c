/*Количество чётных элементов последовательности*/
/*Версия по максимальному числу элементов*/


#include <stdio.h>
#include "list.h"

#define OK 0

/*Допущение: ограничение по числу элементов (пока что 10)*/
/*Допущение: челочисленные элементы*/

int main(void)
{
    setbuf(stdout, NULL);

    int count = 0;

    printf("Input up to %d numbers:\n", NUMB_EL);

    count = arange();

    if (count == -1)
    {
        printf("Don't have correct numbers");
        return -1;
    }

    printf("\nThe number of even elements is %d", count);

    return OK;
}