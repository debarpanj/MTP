from z3 import *
import subprocess
import time
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
    out = subprocess.check_output("./a.out %s" % ' '.join(result), shell=True,)
    return list(map(float, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5,in6,in7 = Reals('in1 in2 in3 in4 in5 in6 in7')
l2n1v1_1,l2n2v1_1,l2n3v1_1,l2n4v1_1,l2n5v1_1,l2n6v1_1,l2n7v1_1 = Reals('l2n1v1_1 l2n2v1_1 l2n3v1_1 l2n4v1_1 l2n5v1_1 l2n6v1_1 l2n7v1_1')
l2n1v2_1,l2n2v2_1,l2n3v2_1,l2n4v2_1,l2n5v2_1,l2n6v2_1,l2n7v2_1 = Reals('l2n1v2_1 l2n2v2_1 l2n3v2_1 l2n4v2_1 l2n5v2_1 l2n6v2_1 l2n7v2_1')
ov1_1 = Real('ov1_1')
ov2_1= Real('ov2_1')


def NN(in1,in2,in3,in4,in5,in6,in7,l2n1_1,l2n2_1,l2n3_1,l2n4_1,l2n5_1,l2n6_1,l2n7_1):

		l2out_1,l2out_2,l2out_3,l2out_4,l2out_5,l2out_6,l2out_7 = Reals('l2out_1 l2out_2 l2out_3 l2out_4 l2out_5 l2out_6 l2out_7')
		l2out_1 = (in1 * -0.2693409442) + (in2 * 0.4474046706) + (in3 * -0.6313326646) + (in4 * -0.2347551214) + (in5 * 0.2832965113) + (in6 * 0.1805725961) + (in7 * -0.7819457895) 
		l2out_1 = If(l2out_1 < 0, 0, l2out_1)
		l2out_2 = (in1 * 0.4026940467) + (in2 * 0.5938360243) + (in3 * -0.4819919878) + (in4 * -0.3421926289) + (in5 * -0.3347666920) + (in6 * 0.2008163501) + (in7 * 0.3350919983) 
		l2out_2 = If(l2out_2 < 0, 0, l2out_2)
		l2out_3 = (in1 * 0.2598761292) + (in2 * 0.0748964644) + (in3 * 0.0825376355) + (in4 * 0.3048373253) + (in5 * 0.3481572979) + (in6 * 0.0012289883) + (in7 * 0.0693637266) 
		l2out_3 = If(l2out_3 < 0, 0, l2out_3)
		l2out_4 = (in1 * 0.5486459119) + (in2 * -0.3151942282) + (in3 * -0.4794701141) + (in4 * 0.4680852513) + (in5 * -0.6001567906) + (in6 * 0.4800917323) + (in7 * 0.2357107505) 
		l2out_4 = If(l2out_4 < 0, 0, l2out_4)
		l2out_5 = (in1 * -0.6680703856) + (in2 * -0.0624845112) + (in3 * 0.3008130092) + (in4 * -0.4698349995) + (in5 * -0.1902067874) + (in6 * 0.4570144143) + (in7 * -0.2827067655) 
		l2out_5 = If(l2out_5 < 0, 0, l2out_5)
		l2out_6 = (in1 * 0.0175990987) + (in2 * -0.0438237085) + (in3 * -0.0798098542) + (in4 * -0.1774660312) + (in5 * -0.3035666007) + (in6 * -0.2313977027) + (in7 * -0.2197268679) 
		l2out_6 = If(l2out_6 < 0, 0, l2out_6)
		l2out_7 = (in1 * -0.0791536480) + (in2 * -0.0120224758) + (in3 * 0.4896840455) + (in4 * 0.3921274778) + (in5 * 0.5722019212) + (in6 *  0.0731946812) + (in7 * -0.2789063777) 
		l2out_7 = If(l2out_7 < 0, 0, l2out_7)
		l3out_1 = Real('l3out_1')
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
s.add(ov1_1>0)
s.add(ov2_1>0)

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


