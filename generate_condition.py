with open('generate_condition.txt', 'w') as file:
    line1="Or("
    for i in range(1, 6):
        for j in range(1, 6):
            for k in range(2):
              if(k==0):
                   line = f"l1n{i}v{k+1}_{j}!="
              else :
                   line = f"l1n{i}v{k+1}_{j},"
              line1=line1+line       
    line1=line1+")"          
    file.write(line1)

