points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

game_logic = {  # Opponent input: (losing player move, draw player move, winning player move)
    "A": ("Z", "X", "Y"),
    "B": ("X", "Y", "Z"),
    "C": ("Y", "Z", "X")
}

def normal_strategy(strategy):
    total_score = 0
    for inputs in strategy:
        result_points = 0
        if game_logic[inputs[0]][2] == inputs[1]:   # Winning move
            result_points = 6
        if game_logic[inputs[0]][1] == inputs[1]:   # Drawing move
            result_points = 3
        total_score += points[inputs[1]] + result_points
    return total_score

def secret_strategy(strategy):
    total_score = 0
    for inputs in strategy:
        player_input = game_logic[inputs[0]][0]     # Losing move
        if inputs[1] == "Y":
            total_score += 3
            player_input = game_logic[inputs[0]][1] # Drawing move
        elif inputs[1] == "Z":
            total_score += 6
            player_input = game_logic[inputs[0]][2] # Winning move
        total_score += points[player_input]
    return total_score

def parse_input(path):
    game_list = []
    with open(path) as f:
        for line in f.readlines():
            inputs = line.split(" ")
            game_list.append((inputs[0], inputs[1].strip()))
    return game_list


if __name__ == "__main__":
    strategy = parse_input("data/input02.txt")
    print("Normal strategy total points:", normal_strategy(strategy))
    print("Secret strategy total points:", secret_strategy(strategy))