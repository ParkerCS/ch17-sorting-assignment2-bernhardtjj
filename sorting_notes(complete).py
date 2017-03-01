list = ["abe", "bev", "cam", "dan", "eve", "flo"]

# Swapping

temp = list[0]
list[0] = list[1]
list[1] = temp
print(list)

list[4], list[5] = list[5], list[4]
print(list)

# Selection Sort
import random

my_list = []
for i in range(1000):
    my_list.append(random.randrange(100))
print(my_list)

for pos in range(len(my_list)):
    min_pos = pos
    for scan_pos in range(min_pos, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    temp = my_list[pos]
    my_list[pos] = my_list[min_pos]
    my_list[min_pos] = temp

print(my_list)

import random

random.shuffle(my_list)
print(my_list)

# Insertion Sort
# iterate through list starting at 1 through the end of list
for pos in range(1, len(random_list)):
    # set the key_pos to the i or pos
    key_pos = pos
    # set your scan_pos one left of the key_pos
    scan_pos = key_pos - 1
    # store the temp value at the key_pos
    key_val = random_list[key_pos]
    # make a while loop that keeps going until you reach the 0 pos
    # or you reach a point where the val at scan_pos > key_val
    # at the end of each loop, move one scan_pos left to keep searching
    while scan_pos >= 0 and random_list[scan_pos] > key_val:
        random_list[scan_pos + 1] = random_list[scan_pos]
        scan_pos -= 1
    # once you have exited the while loop, place temp val one to the right
    # of the last scanned position
    random_list[scan_pos + 1] = key_val

print(random_list)
