CC := gcc
COM := -std=c99 -Wall -Werror
LIB := read_arr.o srednee.o print_arr.o find_max.o find_min.o writing.o

mode?=release

ifeq ($(mode),debug)
	COM += -g3
endif

all: main.exe

%.exe: $(LIB) %.o
	$(CC) $(COM) -o $@ $^

%.o: %.c list.h
	$(CC) $(COM) -c $< -o $@ 

clean:
	rm -f main.exe *.[ios]