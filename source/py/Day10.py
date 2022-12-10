def parse_input(path):
    with open(path) as f:
        return [int(line.strip("nopadx ")) if line.strip("nopadx -").isdigit()
             else 0 for line in f.read().splitlines()]  # Parse input to array of numbers

def execute(stream, h, w):
    cycle = 0           # Current cycle
    signal = 1          # Current signal
    history = []        # History of signals
    c_buffer = [0]      # Queue buffer 
    crt = [[0]*w for i in range(h)]   # CRT screen

    while c_buffer:
        if cycle < len(stream):
            command = stream[cycle]
            c_buffer.extend([0] if command == 0 else [0, command])
        cycle += 1
        signal += c_buffer.pop(0)
        if abs((cycle - 1) % w - signal) < 2 and cycle <= h * w:  # If overlaps with sprite
            crt[(cycle-1)//w][(cycle-1) % w] = 1    # Light pixel
        history.append(signal)
        
    print_ctr(crt)
    return history

def print_ctr(crt):
    for row in crt:
        crt_row = ''.join(list(map(lambda x: "#" if x else ".", row)))
        print(crt_row)

def sum_of_signal(memory, points):
    total_sum = 0
    for point in points:
        total_sum += point * memory[point - 1]
    return total_sum

if __name__ == "__main__":
    time_points = [20, 60, 100, 140, 180, 220]
    stream = parse_input("data/input10.txt")
    history = execute(stream, 6, 40)
    print("Sum of signals:", sum_of_signal(history, time_points))