with open('print_keys.txt', 'w') as file:
    line1 = "print("
    for k in range(2):
        for i in range(1, 14):
                line = f' + str(m[l1n{i}v{k+1}_1]) + " "'
                line1 = line1 + line       
    line1 = line1.rstrip()  # Remove trailing whitespace
    line1 = line1 + ")"
    file.write(line1)

