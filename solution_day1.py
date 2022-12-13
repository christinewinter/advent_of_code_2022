elves_list = []

with open("input_day1.txt", 'r') as file:
    elf_load = []
    for row in file:
        if row == "\n":
            elves_list.append(elf_load)
            elf_load = []
        else:
            elf_load.append(int(row.rstrip('\n')))

sum_loads = [sum(loads) for loads in elves_list]

print("Most calories carried:", max(sum_loads))
