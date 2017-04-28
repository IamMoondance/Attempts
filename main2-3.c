/*Шибанова Дарья ИУ7-22
Вычислить с точность eps приближённое значение функции s(x), точное значение функции f(x), абсолютную f(x)-s(x) и
относительную |(f(x)-s(x))/f(x)| ошибки приближенного значения.
Накопление суммы следует выполнять до тех пор, пока очередной член ряда по абсолютной 
величине будет больше заданной величины eps.
s(x) = 1 - 2*3*x/2 + 3*4*x*x/2 - 4*5*x*x*x/2 + 5*6*x*x*x*x/2 + ... , |x| < 1, f(x) = (1 + x) ^ (-3) */

#include <stdio.h>
#include <math.h>

double next_element(double element, double x, double number)
{
    return (-1.0 * element * number * (number + 1) * x / 2.0);
}

int main(void)
{
    setbuf(stdout,NULL);

    double eps;
    double x;
    double element = 1.0;
    double summ = 0.0;
    double i = 2.0;
    double func;

    printf("Input x: \n");
    scanf("%lf", &x);
    printf("Input eps: \n");
    scanf("%lf", &eps);

    if (fabs(x) >= 1.0)
    {
        printf("Incorrect x");
        return 0;
    }

    while (fabs(element) > eps)
    {
        summ += element;
        element = next_element(element, x, i);
        i++;
        printf("%lf\n", element);
    }

    func = 1/powf((x + 1.0), 3.0);
    printf("%lf %lf %lf %lf", summ, func, fabs(func - summ), fabs((func - summ) / func));

    return 0;
}