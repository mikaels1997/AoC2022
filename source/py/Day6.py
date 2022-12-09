def parse_input(path):
    data_stream = []
    with open(path) as f:
        for line in f.read().splitlines():
            data_stream += [*line]
    return data_stream

def signal_start(stream, signal_length):
    char_buffer = []
    for i, char in enumerate(stream):
        char_buffer.append(char)
        if len(char_buffer) < signal_length:
            continue
        if len(char_buffer) <= len(set(char_buffer)) and len(char_buffer) == signal_length:
            return i + 1
        char_buffer.pop(0)

if __name__ == "__main__":
    stream = parse_input("data/input6.txt")
    print("Start index for packet:", signal_start(stream, 4))
    print("Start index for message:", signal_start(stream, 14))