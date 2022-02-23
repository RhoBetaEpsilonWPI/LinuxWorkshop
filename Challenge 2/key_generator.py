#!/usr/bin/python3

import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# Seed the file to get the correct key
random.seed(1234)
f = open("key.txt", "w")
for i in range (1,50):
    if i == 12:
        line = get_random_string(32) + "/" + get_random_string(16) + '\n'
    elif i == 16:
        line = get_random_string(22) + "/" + get_random_string(26) + '\n'
    elif i == 21:
        line = get_random_string(8) + "/" + get_random_string(40) + '\n'
    elif i == 10:
        line = get_random_string(42) + "/" + get_random_string(6) + '\n'
    elif i == 31:
        line = get_random_string(21) + "/" + get_random_string(27) + '\n'
    elif i == 39:
        line = get_random_string(17) + "/" + get_random_string(31) + '\n'
    elif i == 47:
        line = get_random_string(15) + "/" + get_random_string(33) + '\n'
    else:
        line = get_random_string(50) + '\n'
    f.write(line)
f.close()

print("You have successfully written a file named \"key.txt\". This file contains")
print("a password masked by hundreds of randon characters. The password is composed")
print("of letters that follow the \'/\' character. You can easily find these using")
print("commands that you just learned: cat, grep, and |. Good luck!")
