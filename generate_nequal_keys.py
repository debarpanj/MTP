with open('generate_keys_notequal.txt', 'w') as file:
  k=2
  line1 = "Or("
  for i in range(1, 8):
     for j in range(1, 8):
        line = "l1n{}v{}_{}!=m[l1n{}v{}_{}],".format(i, k, j,i,k,j)
        line1 = line1 + line  
  line1=line1+")"            
  file.write(line1)

