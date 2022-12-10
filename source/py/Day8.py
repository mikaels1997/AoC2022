import numpy as np

def parse_input(path):
    with open(path) as f:
        lines = f.read().split("\n")
        return [list((int(char) for char in line)) for line in lines][:-1]

def find_visible_trees(trees):
    trees = np.array(parse_input("data/input8.txt"))
    visible = np.zeros_like(trees)
    max_matrix = np.zeros((np.max(trees.shape), 4), dtype=int).T - 1    # Top, right, down, left
    for i in range(np.max(trees.shape)):
        temp = [trees[i,:], trees[:,-i-1], trees[-i-1,:], trees[:,i]]
        visible[i,:] = (temp[0] > max_matrix[0]) | visible[i,:]
        visible[:,-i-1] = (temp[1] > max_matrix[1]) | visible[:,-i-1]
        visible[-i-1,:] = (temp[2] > max_matrix[2]) | visible[-i-1,:]
        visible[:,i] = (temp[3] > max_matrix[3]) | visible[:,i]

        max_matrix[0] = np.maximum(temp[0], max_matrix[0])
        max_matrix[1] = np.maximum(temp[1], max_matrix[1])
        max_matrix[2] = np.maximum(temp[2], max_matrix[2])
        max_matrix[3] = np.maximum(temp[3], max_matrix[3])
    return np.sum(visible)

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
    print("Number of visible trees:", find_visible_trees(trees))
    print("Maximum score for tree:", find_maximum_score(trees))