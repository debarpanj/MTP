from z3 import *
import subprocess
import time
from pytz import timezone 
from datetime import datetime

set_option(rational_to_decimal=True)
set_option(precision=10)
def Cexec(init_string):
    result = []
    fractions = init_string.split()
    
    for fraction in fractions:
        if '/' in fraction:
            numerator, denominator = map(int, fraction.split('/'))
            decimal = numerator / denominator
            result.append('{:.11f}'.format(decimal))
        else:
            result.append(fraction)
    out = subprocess.check_output("./a.exe %s" % ' '.join(result), shell=False,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5,in6,in7 = Reals('in1 in2 in3 in4 in5 in6 in7')
l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1 = Reals('l1n1v1_1 l1n2v1_1 l1n3v1_1 l1n4v1_1 l1n5v1_1 l1n6v1_1 l7n1v1_1')
l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1 = Reals('l1n1v2_1 l1n2v2_1 l1n3v2_1 l1n4v2_1 l1n5v2_1 l1n6v2_1 l7n1v_1')
b1v1_1=Real('b1v1_1')
b1v2_1=Real('b1v2_1')
ov1_1 = Real('ov1_1')
ov2_1= Real('ov2_1')


def NN(in1,in2,in3,in4,in5,in6,in7,l1n1_1,l1n2_1,l1n3_1,l1n4_1,l1n5_1,l1n6_1,l1n7_1,b1_1):
	l2out_1 = Real('l2out_1')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) + (in3 * l1n3_1) + (in4 * l1n4_1) + (in5 * l1n5_1) + (in6 * l1n6_1) + (in7 * l1n7_1) + b1_1
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

s.add(NN(in1,in2,in3,in4,in5,in6,in7,l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1,b1v1_1) == ov1_1)
s.add(NN(in1,in2,in3,in4,in5,in6,in7,l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1,b1v2_1) == ov2_1)


while s.check(ov1_1 != ov2_1,Or(l1n1v1_1!=l1n1v2_1,l1n2v1_1!=l1n2v2_1,l1n3v1_1!=l1n3v2_1,l1n4v1_1!=l1n4v2_1,l1n5v1_1!=l1n5v2_1,l1n6v1_1!=l1n6v2_1,l1n7v1_1!=l1n7v2_1,b1v1_1!=b1v2_1)) == sat:
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


	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l1n1v1_1,l1n2v1_1,l1n3v1_1,l1n4v1_1,l1n5v1_1,l1n6v1_1,l1n7v1_1,b1v1_1) == out[0])
	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,l1n1v2_1,l1n2v2_1,l1n3v2_1,l1n4v2_1,l1n5v2_1,l1n6v2_1,l1n7v2_1,b1v2_1) == out[0])
	try:
		ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
		print(ind_time)
	except:
		print("No time available")
	 
	st=s.statistics()
	print(st.get_key_value('time'))

print("hi")
while s.check(l1n1v1_1==l1n1v2_1,l1n2v1_1==l1n2v2_1,l1n3v1_1==l1n3v2_1,l1n4v1_1==l1n4v2_1,l1n5v1_1==l1n5v2_1,l1n6v1_1==l1n6v2_1,l1n7v1_1==l1n7v2_1,b1v1_1==b1v2_1)!=unsat:

	try:m=s.model()
	except:
		break
	print("Weights:")
	print(str(m[l1n1v1_1]) + " " + str(m[l1n2v1_1]) + " " + str(m[l1n3v1_1]) + " " + str(m[l1n4v1_1]) + " " + str(m[l1n5v1_1]) + " " + str(m[l1n6v1_1]) + " " + str(m[l1n7v1_1]) + " " + str(m[l1n1v2_1]) + " " + str(m[l1n2v2_1]) + " " + str(m[l1n3v2_1]) + " " + str(m[l1n4v2_1]) + " " + str(m[l1n5v2_1]) + " " + str(m[l1n6v2_1]) + " " + str(m[l1n7v2_1]))
	print("Biases:")
	print(str(m[b1v1_1]) + " " + str(m[b1v2_1]))
	s.add(Or(l1n1v1_1!=m[l1n1v1_1],l1n2v1_1!=m[l1n2v1_1],l1n3v1_1!=m[l1n3v1_1],l1n4v1_1!=m[l1n4v1_1],l1n5v1_1!=m[l1n5v1_1],l1n6v1_1!=m[l1n6v1_1],l1n7v1_1!=m[l1n7v1_1],b1v1_1!=m[b1v1_1]))
	s.add(Or(l1n1v2_1!=m[l1n1v2_1],l1n2v2_1!=m[l1n2v2_1],l1n3v2_1!=m[l1n3v2_1],l1n4v2_1!=m[l1n4v2_1],l1n5v2_1!=m[l1n5v2_1],l1n6v2_1!=m[l1n6v2_1],l1n7v2_1!=m[l1n7v2_1],b1v2_1!=m[b1v2_1]))

print("Finished in " + str(time.time() - start_time))


