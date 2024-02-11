with open('parameters_range.txt', 'w') as file:
    for i in range(1, 8):
        for j in range(1, 8):
            line = f"l1n{i}_{j} 0 11\n"
            file.write(line)

