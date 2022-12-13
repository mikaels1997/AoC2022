import ast
import functools

def parse_input(path):
    with open(path) as f:
        return [l.split('\n') for l in f.read().split('\n\n')]

def analyze_pairs(pairs):
    ps = []
    for p in pairs:
        ps.append(analyze_pair(ast.literal_eval(p[0]), ast.literal_eval(p[1])))
    return sum([i + 1 for i, x in enumerate(ps) if x])  #Return the sum of indices of correct packets

def sort_pairs(pairs):
    pairs = [[ast.literal_eval(p[0]), ast.literal_eval(p[1])] for p in pairs]
    pairs.append([[2], [6]])
    flattened = [item for sublist in pairs for item in sublist] # Detach the pairs
    criteria = lambda p1, p2: 1 if analyze_pair(p1, p2) else -1 # Sort criteria function
    sorted_pairs = sorted(flattened, key=functools.cmp_to_key(criteria), reverse=True)
    return (sorted_pairs.index([2])+1) * (sorted_pairs.index([6])+1)

def analyze_pair(p1, p2):
    for i in range(min(len(p1), len(p2))):  # For the number of elements in smaller list
        if str(p1[i]).isdigit() and str(p2[i]).isdigit():
            if p1[i] == p2[i]:  # If both are digits, compare them
                continue
            return int(p1[i] < p2[i])
        else:   # Convert to list if not already and call this function recursively
            p1_list = [p1[i]] if str(p1[i]).isdigit() else p1[i]
            p2_list = [p2[i]] if str(p2[i]).isdigit() else p2[i]
            if analyze_pair(p1_list, p2_list) != None:
                return analyze_pair(p1_list, p2_list)
    if len(p1) == len(p2):
        return None
    return int(len(p1) < len(p2))    # If after list iteration the lengths differs

if __name__ == "__main__":
    lines = parse_input("data/input13.txt")
    print("Sum of indices:", analyze_pairs(lines))
    print("Decoder key:", sort_pairs(lines))