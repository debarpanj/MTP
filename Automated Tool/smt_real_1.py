from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

in1,in2 = Reals('in1 in2')
l1n1v1_1,l1n1v1_2 = Reals('l1n1v1_1 l1n1v1_2')
l1n2v1_1,l1n2v1_2 = Reals('l1n2v1_1 l1n2v1_2')
l2n1v1_1 = Real('l2n1v1_1')
l2n2v1_1 = Real('l2n2v1_1')
l1n1v2_1,l1n1v2_2 = Reals('l1n1v2_1 l1n1v2_2')
l1n2v2_1,l1n2v2_2 = Reals('l1n2v2_1 l1n2v2_2')
l2n1v2_1 = Real('l2n1v2_1')
l2n2v2_1 = Real('l2n2v2_1')
ov1_1,ov1_2,ov1_3 = Reals('ov1_1 ov1_2 ov1_3')
ov2_1,ov2_2,ov2_3 = Reals('ov2_1 ov2_2 ov2_3')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',RealSort()),('2',RealSort()),('3',RealSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3)

def NN(in1,in2,l1n1_1,l1n1_2,l1n2_1,l1n2_2,l2n1_1,l2n2_1):
	l2out_1,l2out_2 = Reals('l2out_1 l2out_2')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * l1n1_2) + (in2 * l1n2_2) 
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	
	l3out_1 = Real('l3out_1')
	l3out_1 = (l2out_1 * l2n1_1) + (l2out_2 * l2n2_1) 
	l3out_1 = If(l3out_1 < 0, 0, l3out_1)
	
	out = tuple.tuple(l2out_1,l2out_2,l3out_1)
	
	return out

s = Tactic('smt').solver()


s.add(NN(in1,in2,l1n1v1_1,l1n1v1_2,l1n2v1_1,l1n2v1_2,l2n1v1_1,l2n2v1_1) == out1)
s.add(NN(in1,in2,l1n1v2_1,l1n1v2_2,l1n2v2_1,l1n2v2_2,l2n1v2_1,l2n2v2_1) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]

	out_tup = tuple.tuple(out[0],out[1],out[2])

	s.add(NN(inp1,inp2,l1n1v1_1,l1n1v1_2,l1n2v1_1,l1n2v1_2,l2n1v1_1,l2n2v1_1) == out_tup)
	s.add(NN(inp1,inp2,l1n1v2_1,l1n1v2_2,l1n2v2_1,l1n2v2_2,l2n1v2_1,l2n2v2_1) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Finished in " + str(time.time() - start_time))
