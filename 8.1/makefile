CC := gcc
COM := -std=c99 -Wall -Werror

mode?=release

ifeq ($(mode),debug)
	COM += -g3
endif

all: main.exe

%.exe: %.o
	$(CC) $(COM) -o $@ $<

%.o: %.c
	$(CC) $(COM) -c -o $@ $<

clean:
	rm -f main.exe *.[ios]