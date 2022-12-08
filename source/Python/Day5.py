import re

def parse_input(path):
    procedure = False
    crate_stacks = {}
    instructions = []
    with open(path) as f:
        for line in f.read().splitlines():
            if line == "":
                procedure = True
                continue
            if not procedure:
                crates = [line[i:i+4] for i in range(0, len(line), 4)]  # Split by every four characters
                for c, crate in enumerate(crates):
                    if c not in crate_stacks:
                        crate_stacks[c] = []
                    label = crate.strip().strip("[]")   # Crate label (letter)
                    if label.isdigit() or label == "":
                        continue
                    crate_stacks[c].append(label)
            else:
                instructions.append(tuple(re.findall(r'\b\d+\b', line)))    # Parse every digit
    crate_stacks = reverse_stacks(crate_stacks)
    return crate_stacks, instructions

def reverse_stacks(stacks):
    for stack in stacks.values():
        stack.reverse()
    return stacks

def follow_procedure(stacks, procedure, enhanced=False):
    for pr in procedure:
        stack_to_move = []
        for i in range(int(pr[0])):  # The number of crates to move
            crate = stacks[int(pr[1])-1].pop()    # Pop from source
            if enhanced:
                stack_to_move.append(crate)       # Make new stack if enhanced crate mover
                continue
            stacks[int(pr[2])-1].append(crate)    # Append to target
        if enhanced:
            stack_to_move.reverse()
            stacks[int(pr[2])-1] += stack_to_move       # Concatenate to target
    return stacks

def top_crates(stacks):
    top_crates = ""
    for stack in stacks:
        top_crates += stacks[stack][-1]
    return top_crates

if __name__ == "__main__":

    # CrateMover9000
    stacks, procedure = parse_input("data/input5.txt")
    updated_stack = follow_procedure(stacks, procedure)
    print("Top crates with CrateMover9000:", top_crates(updated_stack))

    # CrateMover9001
    stacks, procedure = parse_input("data/input5.txt")
    updated_stack = follow_procedure(stacks, procedure, enhanced=True)
    print("Top crates with CrateMover9001:", top_crates(updated_stack))