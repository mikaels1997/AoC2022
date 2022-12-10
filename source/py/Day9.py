import numpy as np

move_vectors = {
    "U": np.array([1, 0]),
    "R": np.array([0, 1]),
    "D": np.array([-1, 0]),
    "L": np.array([0, -1]),
}

def parse_input(path):
    with open(path) as f:
        return [line.split(" ") for line in f.read().splitlines()]
    
def read_commands(commands, num_of_knots):
    visited_positions = set()
    knots = np.zeros((num_of_knots, 2)).astype(int)         # Knot positions
    indexes = [[x, x+1] for x in range(knots.shape[0]-1)]   # The sequential index vectors
    for com in commands:                                    # For every command
        for i in range(int(com[1])):                        # For the number of moves
            knots[0] += move_vectors[com[0]]                # Move head
            [move_knots([knots[i[0]], knots[i[1]]]) for i in indexes] # Move knots sequentially
            visited_positions.add((knots[-1][0], knots[-1][1])) # Add visited
    return len(visited_positions)

def move_knots(knots):
    mov_vector = knots[0] - knots[1]
    if np.sum(np.abs(mov_vector)) == 2:
        mov_vector = (mov_vector / 2).astype(int)    # Move straight
        knots[1] += mov_vector
    if np.sum(np.abs(mov_vector)) > 2:    # Move diagonal
        mov_vector = (mov_vector / np.abs(mov_vector)).astype(int)
        knots[1] += mov_vector

if __name__ == "__main__":
    commands = parse_input("data/input9.txt")
    print("Visited positions with 2 knots:", read_commands(commands, 2))
    print("Visited positions with 10 knots:", read_commands(commands, 10))
