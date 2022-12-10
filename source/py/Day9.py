import numpy as np

move_vectors = {
    "U": np.array([1, 0]),
    "R": np.array([0, 1]),
    "D": np.array([-1, 0]),
    "L": np.array([0, -1]),
}

visited_positions = []

def parse_input(path):
    with open(path) as f:
        return [line.split(" ") for line in f.read().splitlines()]
    
def move_head(commands, knots):
    for com in commands:
        for i in range(int(com[1])):
            knots[0] += move_vectors[com[0]]
            move_tail(knots)
            if [knots[-1][0], knots[-1][1]] not in visited_positions:
                visited_positions.append([knots[-1][0], knots[-1][1]])

def move_tail(knots):
    t_mov_vector = knots[0] - knots[1]
    if np.sum(np.abs(t_mov_vector)) == 2:
        lol = (t_mov_vector / 2).astype(int)    # Move straight
        knots[1] += lol
    if np.sum(np.abs(t_mov_vector)) > 2:    # Move diagonal
        lol = (t_mov_vector / np.abs(t_mov_vector)).astype(int)
        knots[1] += lol

if __name__ == "__main__":
    num_of_knots = 2
    knots_pos = np.zeros((num_of_knots, 2)).astype(int)
    commands = parse_input("data/input9.txt")
    move_head(commands, knots_pos)
    print(len(visited_positions))