import random
import time
import os


#from mistralai import Mistral

MAJOR_ODU = [
    "Ogbe",
    "Oyeku",
    "Iwori",
    "Odi",
    "Irosun",
    "Owonrin",
    "Obara",
    "Okanran",
    "Ogunda",
    "Osa",
    "Ika",
    "Oturupon",
    "Otura",
    "Irete",
    "Ose",
    "Ofun",
]

def rand_bit():
    return random.randint(0, 1)

def get_stroke_from_num(num):
    if num == 0:
        return '|'
    elif num == 1:
        return '||'
    else:
        raise ValueError("invalid num")

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

def get_left_right_bits_from_grid(grid):
    l_bits, r_bits = '', ''
    for i in range(2):
        for j in range(len(grid)):
            if i == 0:
                l_bits += str(grid[j][i])
            if i == 1:
                r_bits += str(grid[j][i])
    return l_bits, r_bits

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
print("Major ODU pair:")
l_bits, r_bits = get_left_right_bits_from_grid(grid)
l_idx, r_idx = int(l_bits, 2), int(r_bits, 2)
print(l_bits, r_bits)
print(f"{MAJOR_ODU[l_idx]}-{MAJOR_ODU[r_idx]}")
print()
print(f"ID:{get_int_id_from_grid(grid)}")

with open('699831075-Ifa-A-Complete-Divination.txt') as file:
    print(file.readlines())
