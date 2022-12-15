import numpy as np

map_matrix = []
map_dict = {}
floor = 0

def parse_input(path):
    h = lambda c: np.array([*map(int, c.strip(' ').split(','))], dtype=int)
    with open(path) as f:
        return [[*map(h, c.split('->'))] for c in f.read().splitlines()]

def form_map(input):
    global floor
    for l in input: # For every line
        for i in range(0, len(l) - 1): # For every pair (overlappig)
            diff = l[i+1] - l[i]
            unit_diff = (diff / abs(np.sum(diff))).astype(int)
            for c in range(np.abs(np.sum(diff)) + 1):
                if not l[i][0] in map_dict:  map_dict[l[i][0]] = set()
                floor = max(l[i][1], floor)
                map_dict[l[i][0]].add(l[i][1])
                l[i] += unit_diff

def drop_sand(abyss, floor=None):
    count = 0
    done = False
    hit_floor = lambda h: (floor and h + 1 == floor)
    while not done:
        sand_pos = np.array([500, 0])
        while sand_pos[1] < abyss or (floor and sand_pos[1] < floor):
            if sand_pos[0] - 1 not in map_dict:  
                map_dict[sand_pos[0]-1] = set() # If left not in dict
            if sand_pos[0] + 1 not in map_dict:
                map_dict[sand_pos[0]+1] = set() # If right not in dict
            if hit_floor(sand_pos[1]) and sand_pos[1] not in map_dict[sand_pos[0]]:
                map_dict[sand_pos[0]].add(sand_pos[1])  # Sand to rest
                count += 1
                map_dict[sand_pos[0]].add(sand_pos[1] + 1)  # Add floor
            elif sand_pos[1] + 1 not in map_dict[sand_pos[0]]:
                sand_pos[1] += 1    # Falls straight down
            elif sand_pos[1] + 1 not in map_dict[sand_pos[0] - 1]:
                sand_pos += np.array([-1, 1])   # Falls to left
            elif sand_pos[1] + 1 not in map_dict[sand_pos[0] + 1]:
                sand_pos += np.array([1, 1])    # Falls to right
            elif floor and sand_pos[1] + 1 == floor:
                map_dict[sand_pos[0]].add(floor - 1)    # Add to rest
                sand_pos[1] += 1
            else: 
                map_dict[sand_pos[0]].add(sand_pos[1])
                count += 1
                break
        if (not floor and sand_pos[1] == abyss) or sand_pos[1] == 0: # or (floor and sand_pos[0] > 500):
            done = True
                
    return count

if __name__ == "__main__":
    parsed = parse_input("data/input14.txt")
    form_map(parsed)
    print("Sand to rest without floor:", drop_sand(floor))
    print("Sand to rest with floor:", drop_sand(floor, floor + 2))