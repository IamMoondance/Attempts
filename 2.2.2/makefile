COM := gcc -std=c99 -Wall -Werror

mode?=release

ifeq ($(mode),debug)
	COM += -g3
endif

all: main.exe

main.exe: main.c
	$(COM) -o $@ $<