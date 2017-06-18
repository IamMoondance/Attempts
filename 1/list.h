#pragma once

#ifndef LIST_FUNC
#define LIST_FUNC

int read_arr(FILE *f, int *arr, int *size);
int srednee(int *arr, int size, float *sredn);
int print_arr(int *arr, int size);
int writing(FILE *f, float sredn);
int find_max(int *arr, int size);
int find_min(int *arr, int size);

#endif