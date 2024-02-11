from z3 import *
import subprocess
import time

set_option(rational_to_decimal=False)
set_option(precision=8)

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5,in6,in7 = Ints('in1 in2 in3 in4 in5 in6 in7')
l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1 = Ints('l1n1v1_1 l1n2v1_1 l1n3v1_1 l1n4v1_1 l1n5v1_1 l1n6v1_1 l7n1v1_1')
l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1 = Ints('l1n1v2_1 l1n2v2_1 l1n3v2_1 l1n4v2_1 l1n5v2_1 l1n6v2_1 l7n1v_1')
ov1_1 = Int('ov1_1')
ov2_1= Int('ov2_1')


def NN(in1,in2,in3,in4,in5,in6,in7,l1n1_1,l1n2_1,l1n3_1,l1n4_1,l1n5_1,l1n6_1,l1n7_1):
	l2out_1 = Int('l2out_1')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) + (in3 * l1n3_1) + (in4 * l1n4_1) + (in5 * l1n5_1) + (in6 * l1n6_1) + (in7 * l1n7_1) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	
	return l2out_1

s = Tactic('smt').solver()

# s.add(l1n1v1_1 >= 0, l1n1v1_1 < 11)
# s.add(l1n1v2_1 >= 0, l1n1v2_1 < 11)
# s.add(l1n2v1_1 >= 0, l1n2v1_1 < 11)
# s.add(l1n2v2_1 >= 0, l1n2v2_1 < 11)
# s.add(l1n3v1_1 >= 0, l1n3v1_1 < 11)
# s.add(l1n3v2_1 >= 0, l1n3v2_1 < 11)
# s.add(l1n4v1_1 >= 0, l1n4v1_1 < 11)
# s.add(l1n4v2_1 >= 0, l1n4v2_1 < 11)
# s.add(l1n5v1_1 >= 0, l1n5v1_1 < 11)
# s.add(l1n5v2_1 >= 0, l1n5v2_1 < 11)
# s.add(l1n6v1_1 >= 0, l1n6v1_1 < 11)
# s.add(l1n6v2_1 >= 0, l1n6v2_1 < 11)
# s.add(l1n7v1_1 >= 0, l1n7v1_1 < 11)
# s.add(l1n7v2_1 >= 0, l1n7v2_1 < 11)

s.add(NN(in1,in2,in3,in4,in5,in6,in7,l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1) == ov1_1)
s.add(NN(in1,in2,in3,in4,in5,in6,in7,l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1) == ov2_1)
while s.check(ov1_1 != ov2_1,Or(l1n1v1_1!=l1n1v2_1,l1n2v1_1!=l1n2v2_1,l1n3v1_1!=l1n3v2_1,l1n4v1_1!=l1n4v2_1,l1n5v1_1!=l1n5v2_1,l1n6v1_1!=l1n6v2_1,l1n7v1_1!=l1n7v2_1)) == sat:
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


	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1) == out[0])
	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1) == out[0])

# while s.check(ov1_1 != ov2_1,Or(l1n1v1_1!=l1n1v2_1,l1n2v1_1!=l1n2v2_1,l1n3v1_1!=l1n3v2_1,l1n4v1_1!=l1n4v2_1,l1n5v1_1!=l1n5v2_1,l1n6v1_1!=l1n6v2_1,l1n7v1_1!=l1n7v2_1)) == sat:
#     m = s.model()
#     i1 = RealVal(m[in1]).as_fraction()
#     inp1 = float(i1.numerator)/float(i1.denominator)
#     i2 = RealVal(m[in2]).as_fraction()
#     inp2 = float(i2.numerator)/float(i2.denominator)
#     i3 = RealVal(m[in3]).as_fraction()
#     inp3  = float(i3.numerator)/float(i3.denominator)
#     i4 = RealVal(m[in4]).as_fraction()
#     inp4 = float(i4.numerator)/float(i4.denominator)
#     i5 = RealVal(m[in5]).as_fraction()
#     inp5 = float(i5.numerator)/float(i5.denominator)
#     i6 = RealVal(m[in6]).as_fraction()
#     inp6 = float(i6.numerator)/float(i6.denominator)
#     i7 = RealVal(m[in7]).as_fraction()
#     inp7 = float(i7.numerator)/float(i7.denominator)
#     ia = str(inp1) + " " + str(inp2) + " " + str(inp3) + " " + str(inp4) + " " + str(inp5) + " " + str(inp6) + " " + str(inp7)
#     print(ia)
#     out = Cexec(ia)
#     s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1) == out[0])
#     s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1) == out[0])
	
	
	
print("hi")
while s.check(l1n1v1_1==l1n1v2_1,l1n2v1_1==l1n2v2_1,l1n3v1_1==l1n3v2_1,l1n4v1_1==l1n4v2_1,l1n5v1_1==l1n5v2_1,l1n6v1_1==l1n6v2_1,l1n7v1_1==l1n7v2_1) !=unsat:
	try:
	 m=s.model()
	except:
		break
	print(str(m[l1n1v1_1]) + " " + str(m[l1n2v1_1]) + " " + str(m[l1n3v1_1]) + " " + str(m[l1n4v1_1]) + " " + str(m[l1n5v1_1]) + " " + str(m[l1n6v1_1]) + " " + str(m[l1n7v1_1]) + " " + str(m[l1n1v2_1]) + " " + str(m[l1n2v2_1]) + " " + str(m[l1n3v2_1]) + " " + str(m[l1n4v2_1]) + " " + str(m[l1n5v2_1]) + " " + str(m[l1n6v2_1]) + " " + str(m[l1n7v2_1]))
	s.add(Or(l1n1v1_1!=m[l1n1v1_1],l1n2v1_1!=m[l1n2v1_1],l1n3v1_1!=m[l1n3v1_1],l1n4v1_1!=m[l1n4v1_1],l1n5v1_1!=m[l1n5v1_1],l1n6v1_1!=m[l1n6v1_1],l1n7v1_1!=m[l1n7v1_1]))
	s.add(Or(l1n1v2_1!=m[l1n1v2_1],l1n2v2_1!=m[l1n2v2_1],l1n3v2_1!=m[l1n3v2_1],l1n4v2_1!=m[l1n4v2_1],l1n5v2_1!=m[l1n5v2_1],l1n6v2_1!=m[l1n6v2_1],l1n7v2_1!=m[l1n7v2_1]))

print("Finished in " + str(time.time() - start_time))
