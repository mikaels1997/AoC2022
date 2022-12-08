def parse_input(path):
    rucksack_list = []
    with open(path) as f:
        for line in f.readlines():
            rucksack_list.append(line.strip())
    return rucksack_list

def form_priority_dict():
    priority_dict = {}
    for i, char in enumerate(list(map(chr,range(ord('a'),ord('z')+1)))):
        priority_dict[char] = i + 1
        priority_dict[char.capitalize()] = i + 27
    return priority_dict

def common_item_analysis(list, priority_dict):
    total_priority = 0
    for rucksack in list:
        comp_amount = int(len(rucksack) / 2)
        comp1 = rucksack[0:comp_amount]
        comp2 = rucksack[comp_amount:2*comp_amount]
        total_priority += common_priority([comp1, comp2], priority_dict)
    return total_priority

def elf_group_analysis(list, priority_dict):
    total_priority = 0
    group_number = int(len(list) / 3)
    for i in range(0, group_number):
        group = list[3*i:3*i+3]
        total_priority += common_priority(group, priority_dict)
    return total_priority

def common_priority(comp_list, priority_dict):
    total_priority = 0
    common = set.intersection(*map(set,comp_list))
    for char in common:
        total_priority += priority_dict[char]
    return total_priority

if __name__ == "__main__":
    rucksacks = parse_input("Day 3 Rucksack Reorganization/input.txt")
    priority_dict = form_priority_dict()
    print("Total priority for common items:", common_item_analysis(rucksacks, priority_dict))
    print("Priority with elf groups:", elf_group_analysis(rucksacks, priority_dict))
    