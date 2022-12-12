import numpy as np

current_path = []
dir_sizes = {}
dir_contents = {}

def parse_input(path):
    with open(path) as f:
        return f.read().splitlines()

def analyze_inputs(inputs, path):
    for input in inputs:
        target = check_target(path, input)
        input_list = input.split(" ")
        if input_list[0] == "$":
            path = update_path(path, target) # Update current path
            if target and target not in dir_sizes:  # Begin tracking the dir
                dir_sizes[target] = 0
                dir_contents[target] = []
        else:
            if input_list[0].isdigit():  # Increase dir sizes
                temp_path = ""
                if target not in dir_contents["/"]:
                    dir_sizes["/"] += int(input_list[0])
                for dir in path[1:]:    # Increase size of every dir in current path
                    temp_path += "/" + dir
                    if target not in dir_contents[temp_path]:
                        dir_sizes[temp_path] += int(input_list[0])
                        dir_contents[temp_path].append(target)

def check_target(path, input):
    input_list = input.strip("$ ").split(" ")
    if len(input_list) < 2:
        return None
    if input_list[1] == ".." or input_list[1] == "/":
        return input_list[1]
    if len(input_list) >= 2:
        new_path = path[:]
        new_path.append(input_list[1])
        new_path = ('/').join(new_path)[1:]
        return new_path
    
def update_path(path, target=None):
    if not target:
        return path
    if target == "/":
        path = ["/"]
    elif target == "..":
        path.pop()
    elif len(target) >= 1:
        target_file = target.split('/')[-1]
        path.append(target_file)
    return path

def sum_of_sizes(dirs, constraint=None):
    total = 0
    for size in dirs.values():
        if not constraint or size <= constraint:
            total += size
    return total

def check_smallest(dir_sizes):
    remove_size = dir_sizes["/"] - (70_000_000 - 30_000_000)
    diffs = np.array(list(dir_sizes.values())) - remove_size
    over_zero = diffs[diffs > 0]
    smallest_size = np.min(over_zero) + remove_size
    return smallest_size

if __name__ == "__main__":
    inputs = parse_input("data/input07.txt")
    analyze_inputs(inputs, current_path)
    print("Sum of sizes of dirs:", sum_of_sizes(dir_sizes, 100000))
    print("Smallest dir to remove:", check_smallest(dir_sizes))