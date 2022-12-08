def parse_input(file_name):
    elf_dict = {"1": 0}
    elf_count = 1
    with open(file_name) as f:
        for line in f.readlines():
            if line == "\n":
                elf_count += 1
                elf_dict[str(elf_count)] = 0
                continue
            elf_dict[str(elf_count)] += int(line)
    return elf_dict

def find_most_calories(elf_dict):
    most_cal_number = max(elf_dict.values())
    return most_cal_number

def top_calory_sum(elf_dict, top_amount):
    cal_list = elf_dict.values()
    sorted_list = sorted(cal_list, reverse=True)
    return sum(sorted_list[0:top_amount])

if __name__ == "__main__":
    elf_dict = parse_input("Day 1 Calorie Counting/input.txt")
    most_calories = find_most_calories(elf_dict)
    print("Most calories:", most_calories)
    top_three_cal = top_calory_sum(elf_dict, 3)
    print("Sum of top 3 calories:", top_three_cal)