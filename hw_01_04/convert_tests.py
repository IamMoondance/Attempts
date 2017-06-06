#!/usr/bin/env python3

base = open("test.txt", "r")

tests = base.readlines()

base.close()

is_in = False
is_out = False
test_number = 0
for line in tests:
    if line == 'Input:\n':
        is_out = False
        is_in = True
        if test_number > 0:
            test_out.close()
        test_in = open("in_"+str(test_number)+'.txt', "w")
    elif line == 'Output:\n':
        is_out = True
        is_in = False
        test_in.close()
        test_out = open("out_"+str(test_number)+'.txt', "w")
        test_number += 1
    elif is_in:
        test_in.write(line)
    elif is_out:
        test_out.write(line)

exit(test_number - 1)
