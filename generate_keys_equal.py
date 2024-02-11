with open('generate_keys_equal.txt', 'w') as file:
    line1 = ""
    for i in range(1, 8):
        for j in range(1, 8):
            for k in range(2):
                if k == 0:
                    line = "l1n{}v{}_{}==".format(i, k+1, j)
                else:
                    line = "l1n{}v{}_{},".format(i, k+1, j)
                line1 = line1 + line              
    file.write(line1)

