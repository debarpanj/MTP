with open('generate_condition.txt', 'w') as file:
    line1="Or("
    for i in range(1, 14):
            for k in range(2):
              if(k==0):
                   line = f"l1n{i}v{k+1}_1!="
              else :
                   line = f"l1n{i}v{k+1}_1,"
              line1=line1+line       
    line1=line1+")"          
    file.write(line1)

