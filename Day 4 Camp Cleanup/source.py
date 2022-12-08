def parse_input(path):
    pairs = []
    with open(path) as f:
        for line in f.readlines():
            first = line.split(",")[0].split("-")
            second = line.split(",")[1].split("-")
            pair = [int(first[0]), int(first[1]), int(second[0]), int(second[1].strip())]
            pairs.append(pair)
    return pairs

def fully_contained(pairs):
    pair_number = 0
    for pair in pairs:
        if pair[0] <= pair[2] and pair[1] >= pair[3]:   # Second pair within first
            pair_number += 1
        elif pair[0] >= pair[2] and pair[1] <= pair[3]: # First pair within second
            pair_number += 1
    return pair_number

def partially_contained(pairs):
    pair_number = 0
    for pair in pairs:
        if pair[0] <= pair[2] and pair[2] <= pair[1]:
            pair_number += 1
        elif pair[2] <= pair[0] and pair[0] <= pair[3]:
            pair_number += 1
    return pair_number


if __name__ == "__main__":
    pairs = parse_input("Day 4 Camp Cleanup/input.txt")
    print("Fully contained pairs:", fully_contained(pairs))
    print("Partially contained pairs:", partially_contained(pairs))