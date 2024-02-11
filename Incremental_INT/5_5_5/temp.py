from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5 = Ints('in1 in2 in3 in4 in5')
# l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5 = Ints('l1n1v1_1 l1n1v1_2 l1n1v1_3 l1n1v1_4 l1n1v1_5')
# l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5 = Ints('l1n2v1_1 l1n2v1_2 l1n2v1_3 l1n2v1_4 l1n2v1_5')
# l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5 = Ints('l1n3v1_1 l1n3v1_2 l1n3v1_3 l1n3v1_4 l1n3v1_5')
# l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5 = Ints('l1n4v1_1 l1n4v1_2 l1n4v1_3 l1n4v1_4 l1n4v1_5')
# l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5 = Ints('l1n5v1_1 l1n5v1_2 l1n5v1_3 l1n5v1_4 l1n5v1_5')
l2n1v1_1,l2n1v1_2,l2n1v1_3,l2n1v1_4,l2n1v1_5 = Ints('l2n1v1_1 l2n1v1_2 l2n1v1_3 l2n1v1_4 l2n1v1_5')
l2n2v1_1,l2n2v1_2,l2n2v1_3,l2n2v1_4,l2n2v1_5 = Ints('l2n2v1_1 l2n2v1_2 l2n2v1_3 l2n2v1_4 l2n2v1_5')
l2n3v1_1,l2n3v1_2,l2n3v1_3,l2n3v1_4,l2n3v1_5 = Ints('l2n3v1_1 l2n3v1_2 l2n3v1_3 l2n3v1_4 l2n3v1_5')
l2n4v1_1,l2n4v1_2,l2n4v1_3,l2n4v1_4,l2n4v1_5 = Ints('l2n4v1_1 l2n4v1_2 l2n4v1_3 l2n4v1_4 l2n4v1_5')
l2n5v1_1,l2n5v1_2,l2n5v1_3,l2n5v1_4,l2n5v1_5 = Ints('l2n5v1_1 l2n5v1_2 l2n5v1_3 l2n5v1_4 l2n5v1_5')
# l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5 = Ints('l1n1v2_1 l1n1v2_2 l1n1v2_3 l1n1v2_4 l1n1v2_5')
# l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5 = Ints('l1n2v2_1 l1n2v2_2 l1n2v2_3 l1n2v2_4 l1n2v2_5')
# l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5 = Ints('l1n3v2_1 l1n3v2_2 l1n3v2_3 l1n3v2_4 l1n3v2_5')
# l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5 = Ints('l1n4v2_1 l1n4v2_2 l1n4v2_3 l1n4v2_4 l1n4v2_5')
# l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5 = Ints('l1n5v2_1 l1n5v2_2 l1n5v2_3 l1n5v2_4 l1n5v2_5')
l2n1v2_1,l2n1v2_2,l2n1v2_3,l2n1v2_4,l2n1v2_5 = Ints('l2n1v2_1 l2n1v2_2 l2n1v2_3 l2n1v2_4 l2n1v2_5')
l2n2v2_1,l2n2v2_2,l2n2v2_3,l2n2v2_4,l2n2v2_5 = Ints('l2n2v2_1 l2n2v2_2 l2n2v2_3 l2n2v2_4 l2n2v2_5')
l2n3v2_1,l2n3v2_2,l2n3v2_3,l2n3v2_4,l2n3v2_5 = Ints('l2n3v2_1 l2n3v2_2 l2n3v2_3 l2n3v2_4 l2n3v2_5')
l2n4v2_1,l2n4v2_2,l2n4v2_3,l2n4v2_4,l2n4v2_5 = Ints('l2n4v2_1 l2n4v2_2 l2n4v2_3 l2n4v2_4 l2n4v2_5')
l2n5v2_1,l2n5v2_2,l2n5v2_3,l2n5v2_4,l2n5v2_5 = Ints('l2n5v2_1 l2n5v2_2 l2n5v2_3 l2n5v2_4 l2n5v2_5')
ov1_1,ov1_2,ov1_3,ov1_4,ov1_5,ov1_6,ov1_7,ov1_8,ov1_9,ov1_10 = Ints('ov1_1 ov1_2 ov1_3 ov1_4 ov1_5 ov1_6 ov1_7 ov1_8 ov1_9 ov1_10')
ov2_1,ov2_2,ov2_3,ov2_4,ov2_5,ov2_6,ov2_7,ov2_8,ov2_9,ov2_10 = Ints('ov2_1 ov2_2 ov2_3 ov2_4 ov2_5 ov2_6 ov2_7 ov2_8 ov2_9 ov2_10')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()),('2',IntSort()),('3',IntSort()),('4',IntSort()),('5',IntSort()),('6',IntSort()),('7',IntSort()),('8',IntSort()),('9',IntSort()),('10',IntSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3,ov1_4,ov1_5,ov1_6,ov1_7,ov1_8,ov1_9,ov1_10)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3,ov2_4,ov2_5,ov2_6,ov2_7,ov2_8,ov2_9,ov2_10)

def NN(in1,in2,in3,in4,in5,l1n1_1,l1n1_2,l1n1_3,l1n1_4,l1n1_5,l1n2_1,l1n2_2,l1n2_3,l1n2_4,l1n2_5,l1n3_1,l1n3_2,l1n3_3,l1n3_4,l1n3_5,l1n4_1,l1n4_2,l1n4_3,l1n4_4,l1n4_5,l1n5_1,l1n5_2,l1n5_3,l1n5_4,l1n5_5,l2n1_1,l2n1_2,l2n1_3,l2n1_4,l2n1_5,l2n2_1,l2n2_2,l2n2_3,l2n2_4,l2n2_5,l2n3_1,l2n3_2,l2n3_3,l2n3_4,l2n3_5,l2n4_1,l2n4_2,l2n4_3,l2n4_4,l2n4_5,l2n5_1,l2n5_2,l2n5_3,l2n5_4,l2n5_5):
	l2out_1,l2out_2,l2out_3,l2out_4,l2out_5 = Ints('l2out_1 l2out_2 l2out_3 l2out_4 l2out_5')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) + (in3 * l1n3_1) + (in4 * l1n4_1) + (in5 * l1n5_1) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * l1n1_2) + (in2 * l1n2_2) + (in3 * l1n3_2) + (in4 * l1n4_2) + (in5 * l1n5_2) 
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	l2out_3 = (in1 * l1n1_3) + (in2 * l1n2_3) + (in3 * l1n3_3) + (in4 * l1n4_3) + (in5 * l1n5_3) 
	l2out_3 = If(l2out_3 < 0, 0, l2out_3)
	l2out_4 = (in1 * l1n1_4) + (in2 * l1n2_4) + (in3 * l1n3_4) + (in4 * l1n4_4) + (in5 * l1n5_4) 
	l2out_4 = If(l2out_4 < 0, 0, l2out_4)
	l2out_5 = (in1 * l1n1_5) + (in2 * l1n2_5) + (in3 * l1n3_5) + (in4 * l1n4_5) + (in5 * l1n5_5) 
	l2out_5 = If(l2out_5 < 0, 0, l2out_5)
	
	l3out_1,l3out_2,l3out_3,l3out_4,l3out_5 = Ints('l3out_1 l3out_2 l3out_3 l3out_4 l3out_5')
	l3out_1 = (l2out_1 * l2n1_1) + (l2out_2 * l2n2_1) + (l2out_3 * l2n3_1) + (l2out_4 * l2n4_1) + (l2out_5 * l2n5_1) 
	l3out_1 = If(l3out_1 < 0, 0, l3out_1)
	l3out_2 = (l2out_1 * l2n1_2) + (l2out_2 * l2n2_2) + (l2out_3 * l2n3_2) + (l2out_4 * l2n4_2) + (l2out_5 * l2n5_2) 
	l3out_2 = If(l3out_2 < 0, 0, l3out_2)
	l3out_3 = (l2out_1 * l2n1_3) + (l2out_2 * l2n2_3) + (l2out_3 * l2n3_3) + (l2out_4 * l2n4_3) + (l2out_5 * l2n5_3) 
	l3out_3 = If(l3out_3 < 0, 0, l3out_3)
	l3out_4 = (l2out_1 * l2n1_4) + (l2out_2 * l2n2_4) + (l2out_3 * l2n3_4) + (l2out_4 * l2n4_4) + (l2out_5 * l2n5_4) 
	l3out_4 = If(l3out_4 < 0, 0, l3out_4)
	l3out_5 = (l2out_1 * l2n1_5) + (l2out_2 * l2n2_5) + (l2out_3 * l2n3_5) + (l2out_4 * l2n4_5) + (l2out_5 * l2n5_5) 
	l3out_5 = If(l3out_5 < 0, 0, l3out_5)
	
	out = tuple.tuple(l2out_1,l2out_2,l2out_3,l2out_4,l2out_5,l3out_1,l3out_2,l3out_3,l3out_4,l3out_5)
	
	return out

s = Tactic('smt').solver()

s.add(l2n1v1_1 >= 0, l2n1v1_1 < 11)
s.add(l2n1v2_1 >= 0, l2n1v2_1 < 11)
s.add(l2n1v1_2 >= 0, l2n1v1_2 < 11)
s.add(l2n1v2_2 >= 0, l2n1v2_2 < 11)
s.add(l2n1v1_3 >= 0, l2n1v1_3 < 11)
s.add(l2n1v2_3 >= 0, l2n1v2_3 < 11)
s.add(l2n1v1_4 >= 0, l2n1v1_4 < 11)
s.add(l2n1v2_4 >= 0, l2n1v2_4 < 11)
s.add(l2n1v1_5 >= 0, l2n1v1_5 < 11)
s.add(l2n1v2_5 >= 0, l2n1v2_5 < 11)
s.add(l2n2v1_1 >= 0, l2n2v1_1 < 11)
s.add(l2n2v2_1 >= 0, l2n2v2_1 < 11)
s.add(l2n2v1_2 >= 0, l2n2v1_2 < 11)
s.add(l2n2v2_2 >= 0, l2n2v2_2 < 11)
s.add(l2n2v1_3 >= 0, l2n2v1_3 < 11)
s.add(l2n2v2_3 >= 0, l2n2v2_3 < 11)
s.add(l2n2v1_4 >= 0, l2n2v1_4 < 11)
s.add(l2n2v2_4 >= 0, l2n2v2_4 < 11)
s.add(l2n2v1_5 >= 0, l2n2v1_5 < 11)
s.add(l2n2v2_5 >= 0, l2n2v2_5 < 11)
s.add(l2n3v1_1 >= 0, l2n3v1_1 < 11)
s.add(l2n3v2_1 >= 0, l2n3v2_1 < 11)
s.add(l2n3v1_2 >= 0, l2n3v1_2 < 11)
s.add(l2n3v2_2 >= 0, l2n3v2_2 < 11)
s.add(l2n3v1_3 >= 0, l2n3v1_3 < 11)
s.add(l2n3v2_3 >= 0, l2n3v2_3 < 11)
s.add(l2n3v1_4 >= 0, l2n3v1_4 < 11)
s.add(l2n3v2_4 >= 0, l2n3v2_4 < 11)
s.add(l2n3v1_5 >= 0, l2n3v1_5 < 11)
s.add(l2n3v2_5 >= 0, l2n3v2_5 < 11)
s.add(l2n4v1_1 >= 0, l2n4v1_1 < 11)
s.add(l2n4v2_1 >= 0, l2n4v2_1 < 11)
s.add(l2n4v1_2 >= 0, l2n4v1_2 < 11)
s.add(l2n4v2_2 >= 0, l2n4v2_2 < 11)
s.add(l2n4v1_3 >= 0, l2n4v1_3 < 11)
s.add(l2n4v2_3 >= 0, l2n4v2_3 < 11)
s.add(l2n4v1_4 >= 0, l2n4v1_4 < 11)
s.add(l2n4v2_4 >= 0, l2n4v2_4 < 11)
s.add(l2n4v1_5 >= 0, l2n4v1_5 < 11)
s.add(l2n4v2_5 >= 0, l2n4v2_5 < 11)
s.add(l2n5v1_1 >= 0, l2n5v1_1 < 11)
s.add(l2n5v2_1 >= 0, l2n5v2_1 < 11)
s.add(l2n5v1_2 >= 0, l2n5v1_2 < 11)
s.add(l2n5v2_2 >= 0, l2n5v2_2 < 11)
s.add(l2n5v1_3 >= 0, l2n5v1_3 < 11)
s.add(l2n5v2_3 >= 0, l2n5v2_3 < 11)
s.add(l2n5v1_4 >= 0, l2n5v1_4 < 11)
s.add(l2n5v2_4 >= 0, l2n5v2_4 < 11)
s.add(l2n5v1_5 >= 0, l2n5v1_5 < 11)
s.add(l2n5v2_5 >= 0, l2n5v2_5 < 11)

s.add(NN(in1,in2,in3,in4,in5,0,1,0,5,4,6,2,7,6,7,9,2,4,6,4,4,3,2,3,6,5,2,10,0,3,l2n1v1_1,l2n1v1_2,l2n1v1_3,l2n1v1_4,l2n1v1_5,l2n2v1_1,l2n2v1_2,l2n2v1_3,l2n2v1_4,l2n2v1_5,l2n3v1_1,l2n3v1_2,l2n3v1_3,l2n3v1_4,l2n3v1_5,l2n4v1_1,l2n4v1_2,l2n4v1_3,l2n4v1_4,l2n4v1_5,l2n5v1_1,l2n5v1_2,l2n5v1_3,l2n5v1_4,l2n5v1_5) == out1)
s.add(NN(in1,in2,in3,in4,in5,0,1,0,5,4,6,2,7,6,7,9,2,4,6,4,4,3,2,3,6,5,2,10,0,3,l2n1v2_1,l2n1v2_2,l2n1v2_3,l2n1v2_4,l2n1v2_5,l2n2v2_1,l2n2v2_2,l2n2v2_3,l2n2v2_4,l2n2v2_5,l2n3v2_1,l2n3v2_2,l2n3v2_3,l2n3v2_4,l2n3v2_5,l2n4v2_1,l2n4v2_2,l2n4v2_3,l2n4v2_4,l2n4v2_5,l2n5v2_1,l2n5v2_2,l2n5v2_3,l2n5v2_4,l2n5v2_5) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3]) + " " + str(m[in4]) + " " + str(m[in5])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]
	inp4 = m[in4]
	inp5 = m[in5]

	out_tup = tuple.tuple(out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7],out[8],out[9])

	s.add(NN(inp1,inp2,inp3,inp4,inp5,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5,l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5,l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5,l2n1v1_1,l2n1v1_2,l2n1v1_3,l2n1v1_4,l2n1v1_5,l2n2v1_1,l2n2v1_2,l2n2v1_3,l2n2v1_4,l2n2v1_5,l2n3v1_1,l2n3v1_2,l2n3v1_3,l2n3v1_4,l2n3v1_5,l2n4v1_1,l2n4v1_2,l2n4v1_3,l2n4v1_4,l2n4v1_5,l2n5v1_1,l2n5v1_2,l2n5v1_3,l2n5v1_4,l2n5v1_5) == out_tup)
	s.add(NN(inp1,inp2,inp3,inp4,inp5,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5,l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5,l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5,l2n1v2_1,l2n1v2_2,l2n1v2_3,l2n1v2_4,l2n1v2_5,l2n2v2_1,l2n2v2_2,l2n2v2_3,l2n2v2_4,l2n2v2_5,l2n3v2_1,l2n3v2_2,l2n3v2_3,l2n3v2_4,l2n3v2_5,l2n4v2_1,l2n4v2_2,l2n4v2_3,l2n4v2_4,l2n4v2_5,l2n5v2_1,l2n5v2_2,l2n5v2_3,l2n5v2_4,l2n5v2_5) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))
