import operator
import math

part1 = True
lcm = 1

class Monkey:
    def __init__(self, starting_items, oper, test, target_t, target_f):
        self.items = starting_items # Queue of items
        self.operation = oper       # The operation function
        self.count = 0              # Inspect count
        self.test = test            # Division test number
        self.target_t = target_t    # Target if test passed
        self.target_f = target_f    # Target if test not passed

    def inspect_items(self):
        throw_targets = []
        for i, item in enumerate(self.items):
            item = self.items[i]
            self.count += 1
            item = self.operation(item) # Increase worry
            item =  self.get_bored(item) if part1 else item # Get bored if part 1
            passed, item = self.do_test(item)   # Do test
            throw_targets.append((self.throw_item(passed), item))
        self.items = []
        return throw_targets

    def do_test(self, item):
        return item % self.test == 0, item % lcm    # Divide by lcm to save memory

    def get_bored(self, item):
        return int(item / 3)

    def throw_item(self, is_true):
        return self.target_t if is_true else self.target_f

    def receive_item(self, item):
        self.items.append(item)

def parse_input(path):
    helper = lambda x: int(x.split(" ")[-1].strip(":"))
    monkeys = []
    global lcm
    with open(path) as f:
        for info in f.read().split("\n\n"):
            i_list = info.split("\n")
            items = [x.strip(',') for x in i_list[1].split(" ")[4:]]
            op = form_operation(i_list[2].split("=")[1].strip(" "))
            test = helper(i_list[3])
            lcm = math.lcm(lcm, test)   # Least common multiplier to save memory
            target_t = helper(i_list[4])
            target_f = helper(i_list[5])
            monkeys.append(Monkey(items, op, test, target_t, target_f))
    return monkeys

def form_operation(str):
    ops = { "+": operator.add, "*": operator.mul }
    l = str.split(" ")
    helper = lambda x, y: int(x) if y == "old" else int(y)  # Parse "old"
    func = lambda x: ops[l[1]](helper(x, l[0]), helper(x, l[2]))    # Form test function
    return func

def monkey_business(monkeys):
    counts = [monkey.count for monkey in monkeys]
    counts.sort(reverse=True)
    return counts[0] * counts[1]

def simulate(monkeys, rounds):
    num = len(monkeys)
    for i in range(0, rounds*num):
        targets = monkeys[i % num].inspect_items()
        [monkeys[target[0]].receive_item(target[1]) for target in targets]
    return monkey_business(monkeys)

    
if __name__ == "__main__":
    monkeys = parse_input("data/input11.txt")
    print("Monkey business for part1:", simulate(monkeys, 20))
    part1 = False
    monkeys = parse_input("data/input11.txt")
    print("Monkey business for part2:", simulate(monkeys, 10000))
