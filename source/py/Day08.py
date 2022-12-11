import numpy as np

def parse_input(path):
    with open(path) as f:
        lines = f.read().split("\n")
        return [list((int(char) for char in line)) for line in lines][:-1]

def count_visible(trees):
    visible = np.ones((trees.shape[0], trees.shape[1], 4))  # Axis 2: boolean for 4 directions
    for r, row in enumerate(trees):
        for c, tree in enumerate(row):
            visible[0:r, c, 0][trees[0:r, c] <= tree] = 0   # Obscure up
            visible[r,c+1:, 1][trees[r,c+1:] <= tree] = 0   # Obscure right
            visible[r+1:,c, 2][trees[r+1:,c] <= tree] = 0   # Obscure down
            visible[r, 0:c, 3][trees[r, 0:c] <= tree] = 0   # Obscure left
    return np.sum(np.sum(visible, axis= 2) > 0)

def find_maximum_score(trees):
    scores = np.ones_like(trees)
    for r, row in enumerate(trees):
        for c, tree in enumerate(row):
            t_trees = find_blocking(trees[0:r,c][::-1], tree)
            r_trees = find_blocking(trees[r,c+1:], tree)
            d_trees = find_blocking(trees[r+1:,c], tree)
            l_trees = find_blocking(trees[r,0:c][::-1], tree)
            scores[r,c] = t_trees * r_trees * d_trees * l_trees
    return np.max(scores)

def find_blocking(vector, value):
    if len(vector) == 0:
        return 0
    seen = 0
    for v_val in vector:
        seen += 1
        if v_val >= value:
            return seen
    return seen


if __name__ == "__main__":
    trees = np.array(parse_input("data/input8.txt"))
    print("Number of visible trees:", count_visible(trees))
    print("Maximum score for tree:", find_maximum_score(trees))