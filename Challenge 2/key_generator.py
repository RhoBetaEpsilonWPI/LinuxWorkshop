#!/usr/bin/python3
# This file will be given with instructions to change the permissions on it to make it readable. 
# It createss a file called "key.txt" that ccontains the password to the next challenge.
# The password characters are preceded by the / character and students are encouraged to 
# use grep and | to find the characters for the password. 

import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

f = open("key.txt", "w")
for i in range (1,50):
    if i == 12:
        line = get_random_string(32) + "/i" + get_random_string(16) + '\n'
    elif i == 16:
        line = get_random_string(22) + "/R" + get_random_string(26) + '\n'
    elif i == 21:
        line = get_random_string(8) + "/c" + get_random_string(40) + '\n'
    elif i == 10:
        line = get_random_string(42) + "/C" + get_random_string(6) + '\n'
    elif i == 31:
        line = get_random_string(21) + "/u" + get_random_string(27) + '\n'
    elif i == 39:
        line = get_random_string(17) + "/1" + get_random_string(31) + '\n'
    elif i == 47:
        line = get_random_string(15) + "/t" + get_random_string(33) + '\n'
    else:
        line = get_random_string(50) + '\n'
    f.write(line)
f.close()

print("You have successfully written a file named \"key.txt\". This file contains")
print("a password masked by hundreds of randon characters. The password is composed")
print("of letters that follow the \'/\' character. You can easily find these using")
print("commands that you just learned: cat, grep, and |. Good luck!")
