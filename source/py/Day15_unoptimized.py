def parse_input(path):
    helper = lambda l: int(l.strip(" y,cloestbnisax:"))
    with open(path) as f:
        return [[*map(helper, l[12:].split("="))] for l in f.read().splitlines()]

def manhattan_distance(p1, p2):
    return sum([abs(p2[0]-p1[0]), abs(p2[1]-p1[1])])

def map_sensors(data):
    sensors = {}
    beacons = set()
    for d in data:
        beacons.add(tuple(d[2:4]))
        sensors[tuple(d[0:2])] = manhattan_distance(d[0:2], d[2:4])
    return sensors, beacons

def check_row(y, sensors, beacons):
    occupied = set()
    all_beacons = [b[0] for b in beacons if b[1] == y]   # 2
    row_beacons = set()
    for sensor in sensors:
        col = sensor[0]
        y_over = sensors[sensor] - abs(sensor[1] - y)
        occ_num = 2 * y_over + 1 if y_over >= 0 else 0
        occ_ind  = [i for i in range(col-y_over, col+y_over+1) if occ_num > 0]
        [row_beacons.add(i) for i in occ_ind if i in all_beacons]
        occupied.update(occ_ind)
    return len(occupied) - len(row_beacons)

def find_gap(sensors):
    print("Starting search for part 2...")
    for i in range(0, 4000000): # 0 <= y <= 4 million
        region = []
        for sensor in sensors:
            region = occupy_row_tiles(i, sensor[0], sensor[1], sensors[sensor], region)
        if i % 100000 == 0:
            print("y = ", i)
        if len(region) > 1: # Found a row with not fully connected region
            x_gap = region[0][1] + 1
            print("GAP FOUND!----- y={0}, x={1}".format(i, x_gap))
            print("Part 2 solution:", 4000000*x_gap + i)
            
def occupy_row_tiles(y, sensor_x, sensor_y, sensor_range, regions):
    left_limit = sensor_x - sensor_range + abs(y - sensor_y)
    right_limit = sensor_x + sensor_range - abs(y - sensor_y)
    if right_limit < left_limit:
        return regions

    if regions == []: return [[left_limit, right_limit]]
    return unite_regions(left_limit, right_limit, regions)

def unite_regions(left_limit, right_limit, regions): # Unites 1d regions based on added region
    union_reg = [left_limit, right_limit]
    start_ind = 0
    end_ind = len(regions) - 1
    for i, r in enumerate(regions):
        if left_limit > r[0] and left_limit <= r[1]:
            union_reg[0] = r[0] # If new left limit within existing region
            start_ind = i
        if right_limit < r[1] and right_limit >= r[0]:
            union_reg[1] = r[1] # If new right limit within existing region
            end_ind = i
            break
        if left_limit > r[1]:   # New region formed to the right
            start_ind = i + 1
        if right_limit < r[0]:  # New region formed to the left
            end_ind = i - 1
            break
    regions.insert(start_ind, union_reg)
    if end_ind >= start_ind:
        del regions[start_ind+1:end_ind+2]  # Remove regions within regions
    return regions

if __name__ == "__main__":
    data = parse_input("data/input15.txt")
    sensors, beacons = map_sensors(data)
    print("Part 1 solution:", check_row(2000000, sensors, beacons))
    find_gap(sensors)
