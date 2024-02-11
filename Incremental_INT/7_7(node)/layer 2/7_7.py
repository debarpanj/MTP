from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5,in6,in7 = Ints('in1 in2 in3 in4 in5 in6 in7')
l2n1v1_1,l2n2v1_1,l2n3v1_1,l2n4v1_1,l2n5v1_1,l2n6v1_1,l2n7v1_1 = Ints('l2n1v1_1 l2n2v1_1 l2n3v1_1 l2n4v1_1 l2n5v1_1 l2n6v1_1 l7n1v1_1')
l2n1v2_1,l2n2v2_1,l2n3v2_1,l2n4v2_1,l2n5v2_1,l2n6v2_1,l2n7v2_1 = Ints('l2n1v2_1 l2n2v2_1 l2n3v2_1 l2n4v2_1 l2n5v2_1 l2n6v2_1 l7n1v_1')
ov1_1 = Int('ov1_1')
ov2_1= Int('ov2_1')


def NN(in1,in2,in3,in4,in5,in6,in7,l2n1_1,l2n2_1,l2n3_1,l2n4_1,l2n5_1,l2n6_1,l2n7_1):

		l2out_1,l2out_2,l2out_3,l2out_4,l2out_5,l2out_6,l2out_7 = Ints('l2out_1 l2out_2 l2out_3 l2out_4 l2out_5 l2out_6 l2out_7')
		l2out_1 = (in1 * 6) + (in2 * 10) + (in3 * 6) + (in4 * 2) + (in5 * 1) + (in6 * 4) + (in7 * 0) 
		l2out_1 = If(l2out_1 < 0, 0, l2out_1)
		l2out_2 = (in1 * 0) + (in2 * 3) + (in3 * 8) + (in4 * 1) + (in5 * 1) + (in6 * 9) + (in7 * 6) 
		l2out_2 = If(l2out_2 < 0, 0, l2out_2)
		l2out_3 = (in1 * 1) + (in2 * 10) + (in3 * 7) + (in4 * 7) + (in5 * 7) + (in6 * 4) + (in7 * 2) 
		l2out_3 = If(l2out_3 < 0, 0, l2out_3)
		l2out_4 = (in1 * 1) + (in2 * 3) + (in3 * 5) + (in4 * 7) + (in5 * 9) + (in6 * 2) + (in7 * 4) 
		l2out_4 = If(l2out_4 < 0, 0, l2out_4)
		l2out_5 = (in1 * 2) + (in2 * 4) + (in3 * 6) + (in4 * 8) + (in5 * 10) + (in6 * 1) + (in7 * 3) 
		l2out_5 = If(l2out_5 < 0, 0, l2out_5)
		l2out_6 = (in1 * 0) + (in2 * 1) + (in3 * 2) + (in4 * 3) + (in5 * 4) + (in6 * 5) + (in7 * 6) 
		l2out_6 = If(l2out_6 < 0, 0, l2out_6)
		l2out_7 = (in1 * 1) + (in2 * 2) + (in3 * 3) + (in4 * 5) + (in5 * 5) + (in6 * 5) + (in7 * 1) 
		l2out_7 = If(l2out_7 < 0, 0, l2out_7)
		l3out_1 = Int('l3out_1')
		l3out_1 = (l2out_1 * l2n1_1) + (l2out_2 * l2n2_1) + (l2out_3 * l2n3_1) + (l2out_4 * l2n4_1) + (l2out_5 * l2n5_1) + (l2out_6 * l2n6_1) + (l2out_7 * l2n7_1) 
		l3out_1 = If(l3out_1 < 0, 0, l3out_1)
		
		return l3out_1

s = Tactic('smt').solver()

# s.add(l2n1v1_1 >= 0, l2n1v1_1 < 11)
# s.add(l2n1v2_1 >= 0, l2n1v2_1 < 11)
# s.add(l2n2v1_1 >= 0, l2n2v1_1 < 11)
# s.add(l2n2v2_1 >= 0, l2n2v2_1 < 11)
# s.add(l2n3v1_1 >= 0, l2n3v1_1 < 11)
# s.add(l2n3v2_1 >= 0, l2n3v2_1 < 11)
# s.add(l2n4v1_1 >= 0, l2n4v1_1 < 11)
# s.add(l2n4v2_1 >= 0, l2n4v2_1 < 11)
# s.add(l2n5v1_1 >= 0, l2n5v1_1 < 11)
# s.add(l2n5v2_1 >= 0, l2n5v2_1 < 11)
# s.add(l2n6v1_1 >= 0, l2n6v1_1 < 11)
# s.add(l2n6v2_1 >= 0, l2n6v2_1 < 11)
# s.add(l2n7v1_1 >= 0, l2n7v1_1 < 11)
# s.add(l2n7v2_1 >= 0, l2n7v2_1 < 11)

s.add(NN(in1,in2,in3,in4,in5,in6,in7,l2n1v1_1,l2n2v1_1,l2n3v1_1,l2n4v1_1,l2n5v1_1,l2n6v1_1,l2n7v1_1) == ov1_1)
s.add(NN(in1,in2,in3,in4,in5,in6,in7,l2n1v2_1,l2n2v2_1,l2n3v2_1,l2n4v2_1,l2n5v2_1,l2n6v2_1,l2n7v2_1) == ov2_1)

while s.check(ov1_1 != ov2_1,Or(l2n1v1_1!=l2n1v2_1,l2n2v1_1!=l2n2v2_1,l2n3v1_1!=l2n3v2_1,l2n4v1_1!=l2n4v2_1,l2n5v1_1!=l2n5v2_1,l2n6v1_1!=l2n6v2_1,l2n7v1_1!=l2n7v2_1)) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3]) + " " + str(m[in4]) + " " + str(m[in5]) + " " + str(m[in6]) + " " + str(m[in7])
	print(ia)
	out = Cexec(ia)

	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]
	inp4 = m[in4]
	inp5 = m[in5]
	inp6 = m[in6]
	inp7 = m[in7]


	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l2n1v1_1,l2n2v1_1,l2n3v1_1,l2n4v1_1,l2n5v1_1,l2n6v1_1,l2n7v1_1) == out[0])
	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l2n1v2_1,l2n2v2_1,l2n3v2_1,l2n4v2_1,l2n5v2_1,l2n6v2_1,l2n7v2_1) == out[0])

print("hi")
while s.check(l2n1v1_1==l2n1v2_1,l2n2v1_1==l2n2v2_1,l2n3v1_1==l2n3v2_1,l2n4v1_1==l2n4v2_1,l2n5v1_1==l2n5v2_1,l2n6v1_1==l2n6v2_1,l2n7v1_1==l2n7v2_1) !=unsat:
	try:
	 m=s.model()
	except:
		break
	print(str(m[l2n1v1_1]) + " " + str(m[l2n2v1_1]) + " " + str(m[l2n3v1_1]) + " " + str(m[l2n4v1_1]) + " " + str(m[l2n5v1_1]) + " " + str(m[l2n6v1_1]) + " " + str(m[l2n7v1_1]) + " " + str(m[l2n1v2_1]) + " " + str(m[l2n2v2_1]) + " " + str(m[l2n3v2_1]) + " " + str(m[l2n4v2_1]) + " " + str(m[l2n5v2_1]) + " " + str(m[l2n6v2_1]) + " " + str(m[l2n7v2_1]))
	s.add(Or(l2n1v1_1!=m[l2n1v1_1],l2n2v1_1!=m[l2n2v1_1],l2n3v1_1!=m[l2n3v1_1],l2n4v1_1!=m[l2n4v1_1],l2n5v1_1!=m[l2n5v1_1],l2n6v1_1!=m[l2n6v1_1],l2n7v1_1!=m[l2n7v1_1]))
	s.add(Or(l2n1v2_1!=m[l2n1v2_1],l2n2v2_1!=m[l2n2v2_1],l2n3v2_1!=m[l2n3v2_1],l2n4v2_1!=m[l2n4v2_1],l2n5v2_1!=m[l2n5v2_1],l2n6v2_1!=m[l2n6v2_1],l2n7v2_1!=m[l2n7v2_1]))

print("Finished in " + str(time.time() - start_time))


