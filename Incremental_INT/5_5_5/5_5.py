from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5 = Ints('in1 in2 in3 in4 in5')
l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5 = Ints('l1n1v1_1 l1n1v1_2 l1n1v1_3 l1n1v1_4 l1n1v1_5')
l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5 = Ints('l1n2v1_1 l1n2v1_2 l1n2v1_3 l1n2v1_4 l1n2v1_5')
l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5 = Ints('l1n3v1_1 l1n3v1_2 l1n3v1_3 l1n3v1_4 l1n3v1_5')
l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5 = Ints('l1n4v1_1 l1n4v1_2 l1n4v1_3 l1n4v1_4 l1n4v1_5')
l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5 = Ints('l1n5v1_1 l1n5v1_2 l1n5v1_3 l1n5v1_4 l1n5v1_5')
l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5 = Ints('l1n1v2_1 l1n1v2_2 l1n1v2_3 l1n1v2_4 l1n1v2_5')
l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5 = Ints('l1n2v2_1 l1n2v2_2 l1n2v2_3 l1n2v2_4 l1n2v2_5')
l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5 = Ints('l1n3v2_1 l1n3v2_2 l1n3v2_3 l1n3v2_4 l1n3v2_5')
l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5 = Ints('l1n4v2_1 l1n4v2_2 l1n4v2_3 l1n4v2_4 l1n4v2_5')
l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5 = Ints('l1n5v2_1 l1n5v2_2 l1n5v2_3 l1n5v2_4 l1n5v2_5')
ov1_1,ov1_2,ov1_3,ov1_4,ov1_5 = Ints('ov1_1 ov1_2 ov1_3 ov1_4 ov1_5')
ov2_1,ov2_2,ov2_3,ov2_4,ov2_5 = Ints('ov2_1 ov2_2 ov2_3 ov2_4 ov2_5')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()),('2',IntSort()),('3',IntSort()),('4',IntSort()),('5',IntSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3,ov1_4,ov1_5)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3,ov2_4,ov2_5)

def NN(in1,in2,in3,in4,in5,l1n1_1,l1n1_2,l1n1_3,l1n1_4,l1n1_5,l1n2_1,l1n2_2,l1n2_3,l1n2_4,l1n2_5,l1n3_1,l1n3_2,l1n3_3,l1n3_4,l1n3_5,l1n4_1,l1n4_2,l1n4_3,l1n4_4,l1n4_5,l1n5_1,l1n5_2,l1n5_3,l1n5_4,l1n5_5):
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
	
	out = tuple.tuple(l2out_1,l2out_2,l2out_3,l2out_4,l2out_5)
	
	return out

s = Tactic('smt').solver()

s.add(l1n1v1_1 >= 0, l1n1v1_1 < 11)
s.add(l1n1v2_1 >= 0, l1n1v2_1 < 11)
s.add(l1n1v1_2 >= 0, l1n1v1_2 < 11)
s.add(l1n1v2_2 >= 0, l1n1v2_2 < 11)
s.add(l1n1v1_3 >= 0, l1n1v1_3 < 11)
s.add(l1n1v2_3 >= 0, l1n1v2_3 < 11)
s.add(l1n1v1_4 >= 0, l1n1v1_4 < 11)
s.add(l1n1v2_4 >= 0, l1n1v2_4 < 11)
s.add(l1n1v1_5 >= 0, l1n1v1_5 < 11)
s.add(l1n1v2_5 >= 0, l1n1v2_5 < 11)
s.add(l1n2v1_1 >= 0, l1n2v1_1 < 11)
s.add(l1n2v2_1 >= 0, l1n2v2_1 < 11)
s.add(l1n2v1_2 >= 0, l1n2v1_2 < 11)
s.add(l1n2v2_2 >= 0, l1n2v2_2 < 11)
s.add(l1n2v1_3 >= 0, l1n2v1_3 < 11)
s.add(l1n2v2_3 >= 0, l1n2v2_3 < 11)
s.add(l1n2v1_4 >= 0, l1n2v1_4 < 11)
s.add(l1n2v2_4 >= 0, l1n2v2_4 < 11)
s.add(l1n2v1_5 >= 0, l1n2v1_5 < 11)
s.add(l1n2v2_5 >= 0, l1n2v2_5 < 11)
s.add(l1n3v1_1 >= 0, l1n3v1_1 < 11)
s.add(l1n3v2_1 >= 0, l1n3v2_1 < 11)
s.add(l1n3v1_2 >= 0, l1n3v1_2 < 11)
s.add(l1n3v2_2 >= 0, l1n3v2_2 < 11)
s.add(l1n3v1_3 >= 0, l1n3v1_3 < 11)
s.add(l1n3v2_3 >= 0, l1n3v2_3 < 11)
s.add(l1n3v1_4 >= 0, l1n3v1_4 < 11)
s.add(l1n3v2_4 >= 0, l1n3v2_4 < 11)
s.add(l1n3v1_5 >= 0, l1n3v1_5 < 11)
s.add(l1n3v2_5 >= 0, l1n3v2_5 < 11)
s.add(l1n4v1_1 >= 0, l1n4v1_1 < 11)
s.add(l1n4v2_1 >= 0, l1n4v2_1 < 11)
s.add(l1n4v1_2 >= 0, l1n4v1_2 < 11)
s.add(l1n4v2_2 >= 0, l1n4v2_2 < 11)
s.add(l1n4v1_3 >= 0, l1n4v1_3 < 11)
s.add(l1n4v2_3 >= 0, l1n4v2_3 < 11)
s.add(l1n4v1_4 >= 0, l1n4v1_4 < 11)
s.add(l1n4v2_4 >= 0, l1n4v2_4 < 11)
s.add(l1n4v1_5 >= 0, l1n4v1_5 < 11)
s.add(l1n4v2_5 >= 0, l1n4v2_5 < 11)
s.add(l1n5v1_1 >= 0, l1n5v1_1 < 11)
s.add(l1n5v2_1 >= 0, l1n5v2_1 < 11)
s.add(l1n5v1_2 >= 0, l1n5v1_2 < 11)
s.add(l1n5v2_2 >= 0, l1n5v2_2 < 11)
s.add(l1n5v1_3 >= 0, l1n5v1_3 < 11)
s.add(l1n5v2_3 >= 0, l1n5v2_3 < 11)
s.add(l1n5v1_4 >= 0, l1n5v1_4 < 11)
s.add(l1n5v2_4 >= 0, l1n5v2_4 < 11)
s.add(l1n5v1_5 >= 0, l1n5v1_5 < 11)
s.add(l1n5v2_5 >= 0, l1n5v2_5 < 11)

s.add(NN(in1,in2,in3,in4,in5,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5,l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5,l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5) == out1)
s.add(NN(in1,in2,in3,in4,in5,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5,l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5,l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5) == out2)

while s.check(out1 != out2,Or(l1n1v1_1!=l1n1v2_1,l1n1v1_2!=l1n1v2_2,l1n1v1_3!=l1n1v2_3,l1n1v1_4!=l1n1v2_4,l1n1v1_5!=l1n1v2_5,l1n2v1_1!=l1n2v2_1,l1n2v1_2!=l1n2v2_2,l1n2v1_3!=l1n2v2_3,l1n2v1_4!=l1n2v2_4,l1n2v1_5!=l1n2v2_5,l1n3v1_1!=l1n3v2_1,l1n3v1_2!=l1n3v2_2,l1n3v1_3!=l1n3v2_3,l1n3v1_4!=l1n3v2_4,l1n3v1_5!=l1n3v2_5,l1n4v1_1!=l1n4v2_1,l1n4v1_2!=l1n4v2_2,l1n4v1_3!=l1n4v2_3,l1n4v1_4!=l1n4v2_4,l1n4v1_5!=l1n4v2_5,l1n5v1_1!=l1n5v2_1,l1n5v1_2!=l1n5v2_2,l1n5v1_3!=l1n5v2_3,l1n5v1_4!=l1n5v2_4,l1n5v1_5!=l1n5v2_5)) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3]) + " " + str(m[in4]) + " " + str(m[in5])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]
	inp4 = m[in4]
	inp5 = m[in5]

	out_tup = tuple.tuple(out[0],out[1],out[2],out[3],out[4])

	s.add(NN(inp1,inp2,inp3,inp4,inp5,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5,l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5,l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5) == out_tup)
	s.add(NN(inp1,inp2,inp3,inp4,inp5,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5,l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5,l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5) == out_tup)

while s.check(l1n1v1_1==l1n1v2_1,l1n1v1_2==l1n1v2_2,l1n1v1_3==l1n1v2_3,l1n1v1_4==l1n1v2_4,l1n1v1_5==l1n1v2_5,l1n2v1_1==l1n2v2_1,l1n2v1_2==l1n2v2_2,l1n2v1_3==l1n2v2_3,l1n2v1_4==l1n2v2_4,l1n2v1_5==l1n2v2_5,l1n3v1_1==l1n3v2_1,l1n3v1_2==l1n3v2_2,l1n3v1_3==l1n3v2_3,l1n3v1_4==l1n3v2_4,l1n3v1_5==l1n3v2_5,l1n4v1_1==l1n4v2_1,l1n4v1_2==l1n4v2_2,l1n4v1_3==l1n4v2_3,l1n4v1_4==l1n4v2_4,l1n4v1_5==l1n4v2_5,l1n5v1_1==l1n5v2_1,l1n5v1_2==l1n5v2_2,l1n5v1_3==l1n5v2_3,l1n5v1_4==l1n5v2_4,l1n5v1_5==l1n5v2_5) !=unsat:
	try:
		m=s.model()
	except:
		break
	print(str(m[l1n1v1_1]) + " " + str(m[l1n1v1_2]) + " " + str(m[l1n1v1_3]) + " " + str(m[l1n1v1_4]) + " " + str(m[l1n1v1_5]) + " " + str(m[l1n2v1_1]) + " " + str(m[l1n2v1_2]) + " " + str(m[l1n2v1_3]) + " " + str(m[l1n2v1_4]) + " " + str(m[l1n2v1_5]) + " " + str(m[l1n3v1_1]) + " " + str(m[l1n3v1_2]) + " " + str(m[l1n3v1_3]) + " " + str(m[l1n3v1_4]) + " " + str(m[l1n3v1_5]) + " " + str(m[l1n4v1_1]) + " " + str(m[l1n4v1_2]) + " " + str(m[l1n4v1_3]) + " " + str(m[l1n4v1_4]) + " " + str(m[l1n4v1_5]) + " " + str(m[l1n5v1_1]) + " " + str(m[l1n5v1_2]) + " " + str(m[l1n5v1_3]) + " " + str(m[l1n5v1_4]) + " " + str(m[l1n5v1_5]) + " " + str(m[l1n1v2_1]) + " " + str(m[l1n1v2_2]) + " " + str(m[l1n1v2_3]) + " " + str(m[l1n1v2_4]) + " " + str(m[l1n1v2_5]) + " " + str(m[l1n2v2_1]) + " " + str(m[l1n2v2_2]) + " " + str(m[l1n2v2_3]) + " " + str(m[l1n2v2_4]) + " " + str(m[l1n2v2_5]) + " " + str(m[l1n3v2_1]) + " " + str(m[l1n3v2_2]) + " " + str(m[l1n3v2_3]) + " " + str(m[l1n3v2_4]) + " " + str(m[l1n3v2_5]) + " " + str(m[l1n4v2_1]) + " " + str(m[l1n4v2_2]) + " " + str(m[l1n4v2_3]) + " " + str(m[l1n4v2_4]) + " " + str(m[l1n4v2_5]) + " " + str(m[l1n5v2_1]) + " " + str(m[l1n5v2_2]) + " " + str(m[l1n5v2_3]) + " " + str(m[l1n5v2_4]) + " " + str(m[l1n5v2_5]))
	s.add(Or(l1n1v1_1!=m[l1n1v1_1],l1n1v1_2!=m[l1n1v1_2],l1n1v1_3!=m[l1n1v1_3],l1n1v1_4!=m[l1n1v1_4],l1n1v1_5!=m[l1n1v1_5],l1n2v1_1!=m[l1n2v1_1],l1n2v1_2!=m[l1n2v1_2],l1n2v1_3!=m[l1n2v1_3],l1n2v1_4!=m[l1n2v1_4],l1n2v1_5!=m[l1n2v1_5],l1n3v1_1!=m[l1n3v1_1],l1n3v1_2!=m[l1n3v1_2],l1n3v1_3!=m[l1n3v1_3],l1n3v1_4!=m[l1n3v1_4],l1n3v1_5!=m[l1n3v1_5],l1n4v1_1!=m[l1n4v1_1],l1n4v1_2!=m[l1n4v1_2],l1n4v1_3!=m[l1n4v1_3],l1n4v1_4!=m[l1n4v1_4],l1n4v1_5!=m[l1n4v1_5],l1n5v1_1!=m[l1n5v1_1],l1n5v1_2!=m[l1n5v1_2],l1n5v1_3!=m[l1n5v1_3],l1n5v1_4!=m[l1n5v1_4],l1n5v1_5!=m[l1n5v1_5]))
	s.add(Or(l1n1v2_1!=m[l1n1v2_1],l1n1v2_2!=m[l1n1v2_2],l1n1v2_3!=m[l1n1v2_3],l1n1v2_4!=m[l1n1v2_4],l1n1v2_5!=m[l1n1v2_5],l1n2v2_1!=m[l1n2v2_1],l1n2v2_2!=m[l1n2v2_2],l1n2v2_3!=m[l1n2v2_3],l1n2v2_4!=m[l1n2v2_4],l1n2v2_5!=m[l1n2v2_5],l1n3v2_1!=m[l1n3v2_1],l1n3v2_2!=m[l1n3v2_2],l1n3v2_3!=m[l1n3v2_3],l1n3v2_4!=m[l1n3v2_4],l1n3v2_5!=m[l1n3v2_5],l1n4v2_1!=m[l1n4v2_1],l1n4v2_2!=m[l1n4v2_2],l1n4v2_3!=m[l1n4v2_3],l1n4v2_4!=m[l1n4v2_4],l1n4v2_5!=m[l1n4v2_5],l1n5v2_1!=m[l1n5v2_1],l1n5v2_2!=m[l1n5v2_2],l1n5v2_3!=m[l1n5v2_3],l1n5v2_4!=m[l1n5v2_4],l1n5v2_5!=m[l1n5v2_5]))

print("Finished in " + str(time.time() - start_time))
