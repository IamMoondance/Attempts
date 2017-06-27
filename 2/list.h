#pragma once

#ifndef __LIST_H__
#define __LIST_H__

int read_arr(FILE *f, int *arr, int *size);
int print_arr(int *arr, int size);
int min_el(int *arr, int size);
int otr_el(int *arr, int size);
int change_els(int *arr, int size);
int write_arr(FILE *f, int *arr, int size);

#endif