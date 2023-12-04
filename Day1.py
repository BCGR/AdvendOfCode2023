import re

with open("input.txt", "r") as f:
    lines = f.readlines()



# #  Fix 'real' numbers
for i in range(len(lines)):

    line = lines[i].lower()

    
    nine = line.replace("nine","n9e")
    eight = nine.replace("eight","e8t")
    seven = eight.replace("seven","s7n")
    six = seven.replace("six","s6x")
    five = six.replace("five","f5e")
    four = five.replace("four","f4r")
    three = four.replace("three","t3e")
    two = three.replace("two","t2o")
    one = two.replace("one","o1e")
    
    lines[i] = one


adder = 0

# Add all numbers
for i in range(len(lines)):
    match = re.search("(\d{1})", lines[i])
    first_digit = match.group(1)
    match = re.search("(\d{1})\D*$", lines[i])
    second_digit = match.group(1)
    number = first_digit+second_digit
    adder = adder + int(number)

print(adder)

import re
