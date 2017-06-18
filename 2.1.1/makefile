COM := gcc -std=c99 -Wall -Werror
mode?=release

ifeq ($(mode),debug)
	COM += -g3
endif

# Собрать и запустить программу
all: main.exe

main.exe: is_even.o arange.o main.o
	$(COM) -o $@ $^

%.o: %.c list.h
	$(COM) -c -o $@ $<

clean:
	rm -f main.exe *.[ios]