/*
Шибанова Дарья, ИУ7-22
Составить программу, печатающую разложение на простые множители заданного
натурального числа n > 0. Если n равно 1, печатать ничего не надо.
*/

#include <stdio.h>

int next_mult(int number)
{
    for (int i = 2; i <= number; i++)
            {
                if (number % i == 0)
                {
                    number = number / i;
                    printf("%d ", i);
                    return number;
                }
            }
    return 1;
}

int main(void)
{
    setbuf(stdout, NULL);
    int number;

    printf("Input a number:\n");
    scanf("%d", &number);

    if (number < 1)
    {
        printf("Incorrect input data");
    }
    else
    {
        printf("Multipliers of the number:\n");
        while (number > 1)
        {
            number = next_mult(number);
        }
    }

    return 0;
}