elves_list = []

with open("input_day1.txt", 'r') as file:
    elf_load = []
    for row in file:
        if row == "\n":
            elves_list.append(elf_load)
            elf_load = []
        else:
            elf_load.append(int(row.rstrip('\n')))

sum_loads_sorted = sorted([sum(loads) for loads in elves_list], reverse=True)

print("Sum of top three calories carried:", sum(sum_loads_sorted[:3]))
