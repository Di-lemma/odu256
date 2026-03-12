import random
import time
import os

def rand_bit():
    return random.randint(0, 1)

def get_stroke_from_num(num):
    if num == 0:
        return '|'
    elif num == 1:
        return '||'
    else:
        raise Exception("invalid num")

def render_odu_grid(grid):
    ifa = ''
    for item in grid:
        ifa += f"{get_stroke_from_num(item[0])}  {get_stroke_from_num(item[1])}"
        ifa += '\n'
    return ifa

def get_bin_config_from_grid(grid):
    bits = ''
    for i in range(2):
        for j in range(len(grid)):
            bits += str(grid[j][i])
            bits += ' '
        bits += '\n'
    return bits

def get_bin_str_from_grid(grid):
    bits = ''
    for i in range(2):
        for j in range(len(grid)):
            bits += str(grid[j][i])
    return bits

def get_int_id_from_grid(grid):
    bits = get_bin_str_from_grid(grid)

    # conversion
    value = int(bits, 2)
    return value

grid = [[rand_bit(), rand_bit()] for i in range(4)]

odu = render_odu_grid(grid)
print(odu)
print("Binary config:")
print(get_bin_config_from_grid(grid))
print("Binary string:")
print(get_bin_str_from_grid(grid))
print()
print(f"ID:{get_int_id_from_grid(grid)}")

"""
|  ||
|  |
||  |
|  |

Binary config:
0 0 1 0 
1 0 0 0 

Binary string:
00101000

ID:40
"""
