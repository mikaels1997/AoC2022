letters = "abcdefghijklmnopqrstuvwxyz"
adj_vectors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
adj_func = lambda n1, n2: (n1[0] + n2[0], n1[1] + n2[1])    # To check adjancent nodes
is_inside = lambda coord: coord[0] >= 0 and coord[0] <= grid_size[0] and coord[1] >= 0 and coord[1] <= grid_size[1]
grid_size = (0, 0)

def parse_input(path):
    global grid_size
    start, end = 0, 0
    nodes = {}
    with open(path) as f:
        for y, row in enumerate(f.read().splitlines()):
            for x, c in enumerate(row):
                grid_size = (max(grid_size[0], x), max(grid_size[1], y))
                start = (x, y) if c == 'S' else start
                end = (x, y) if c == 'E' else end
                nodes[(x, y)] = letters.find(c)
    return nodes, start, end

def bfs(nodes, start, end, constr, part2=False):          
    visited, queue = [start], [start]   # Visited nodes, node queue for BFS
    parents = {}    # Node and their parent (for backtracking path length)
    while len(queue) > 0:
        node = queue.pop(0)
        height = nodes[node]    # Current height
        if node == end or (part2 and height == letters.find('a')):
            return backtrack(node, start, parents)  # If goal reached
        adj = [adj_func(node, v) for v in adj_vectors if is_inside(adj_func(node, v))]
        for n in adj:   # For adjancent nodes
            if n not in visited and constr(height, nodes[n]):   # If not in visited and satisfies contraint
                visited.append(n)
                parents[n] = node
                queue.append(n)

def backtrack(goal, start, parents):
    path_length = 0
    node = goal
    while True:
        node = parents[node]
        path_length += 1
        if node == start:
            return path_length  # Backtracks the path length from parent nodes

if __name__ == "__main__":
    nodes, start, end = parse_input("data/input12.txt")

    # Part1: constrained BFS from start node to end node
    constraint = lambda h1, h2: h1 - h2 >= -1
    print("Part 1 shortest length:",bfs(nodes, start, end, constraint))

    # Part2: constrained BFS from end node to goal (height=0)
    constraint = lambda h1, h2: h1 - h2 <= 1
    print("Part 2 shortest length:",bfs(nodes, end, (-1, -1), constraint, True))