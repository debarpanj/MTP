with open('generate_keys_equal.txt', 'w') as file:
    line1 = ""
    for i in range(1, 14):
            for k in range(2):
                if k == 0:
                    line = "l1n{}v{}_1==".format(i, k+1)
                else:
                    line = "l1n{}v{}_1,".format(i, k+1)
                line1 = line1 + line              
    file.write(line1)

