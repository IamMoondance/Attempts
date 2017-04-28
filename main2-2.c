/*Шибанова Дарья ИУ7-22
Определить принадлежит ли точка отрезку.*/

#include <stdio.h>
#include <math.h>

float length(float x1, float y1, float x2, float y2)
{
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

int main(void)
{
    float x1, y1;
    float x2, y2;
    float x3, y3;

    setbuf(stdout, NULL);

    printf("Input coordinates of the beginning point of the piece:\n");
    scanf("%f%f", &x1, &y1);
    printf("Input coordinates of the ending point of the piece:\n");
    scanf("%f%f", &x2, &y2);
    printf("Input coordinates of the point:\n");
    scanf("%f%f", &x3, &y3);

    if ((x1 == x2) && (y1 == y2))
    {
        printf("The length of the piece is zero\n");
    }

    if (length(x1, y1, x3, y3) + length(x3, y3, x2, y2) == length(x1, y1, x2, y2))
    {
        printf("The point lays on the piece");
    }
    else
    {
        printf("It's an outer point");
    }

    return 0;
}