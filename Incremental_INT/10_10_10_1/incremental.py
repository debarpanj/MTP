from z3 import *
import subprocess
import time

def Cexec(init_string):
	out = subprocess.check_output("./a.out %s" % init_string, shell=True,)
	return list(map(int, out.decode('utf-8').split()))

start_time = time.time()

in1,in2,in3,in4,in5,in6,in7,in8,in9,in10 = Ints('in1 in2 in3 in4 in5 in6 in7 in8 in9 in10')
l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5,l1n1v1_6,l1n1v1_7,l1n1v1_8,l1n1v1_9,l1n1v1_10 = Ints('l1n1v1_1 l1n1v1_2 l1n1v1_3 l1n1v1_4 l1n1v1_5 l1n1v1_6 l1n1v1_7 l1n1v1_8 l1n1v1_9 l1n1v1_10')
l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5,l1n2v1_6,l1n2v1_7,l1n2v1_8,l1n2v1_9,l1n2v1_10 = Ints('l1n2v1_1 l1n2v1_2 l1n2v1_3 l1n2v1_4 l1n2v1_5 l1n2v1_6 l1n2v1_7 l1n2v1_8 l1n2v1_9 l1n2v1_10')
l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5,l1n3v1_6,l1n3v1_7,l1n3v1_8,l1n3v1_9,l1n3v1_10 = Ints('l1n3v1_1 l1n3v1_2 l1n3v1_3 l1n3v1_4 l1n3v1_5 l1n3v1_6 l1n3v1_7 l1n3v1_8 l1n3v1_9 l1n3v1_10')
l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5,l1n4v1_6,l1n4v1_7,l1n4v1_8,l1n4v1_9,l1n4v1_10 = Ints('l1n4v1_1 l1n4v1_2 l1n4v1_3 l1n4v1_4 l1n4v1_5 l1n4v1_6 l1n4v1_7 l1n4v1_8 l1n4v1_9 l1n4v1_10')
l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5,l1n5v1_6,l1n5v1_7,l1n5v1_8,l1n5v1_9,l1n5v1_10 = Ints('l1n5v1_1 l1n5v1_2 l1n5v1_3 l1n5v1_4 l1n5v1_5 l1n5v1_6 l1n5v1_7 l1n5v1_8 l1n5v1_9 l1n5v1_10')
l1n6v1_1,l1n6v1_2,l1n6v1_3,l1n6v1_4,l1n6v1_5,l1n6v1_6,l1n6v1_7,l1n6v1_8,l1n6v1_9,l1n6v1_10 = Ints('l1n6v1_1 l1n6v1_2 l1n6v1_3 l1n6v1_4 l1n6v1_5 l1n6v1_6 l1n6v1_7 l1n6v1_8 l1n6v1_9 l1n6v1_10')
l1n7v1_1,l1n7v1_2,l1n7v1_3,l1n7v1_4,l1n7v1_5,l1n7v1_6,l1n7v1_7,l1n7v1_8,l1n7v1_9,l1n7v1_10 = Ints('l1n7v1_1 l1n7v1_2 l1n7v1_3 l1n7v1_4 l1n7v1_5 l1n7v1_6 l1n7v1_7 l1n7v1_8 l1n7v1_9 l1n7v1_10')
l1n8v1_1,l1n8v1_2,l1n8v1_3,l1n8v1_4,l1n8v1_5,l1n8v1_6,l1n8v1_7,l1n8v1_8,l1n8v1_9,l1n8v1_10 = Ints('l1n8v1_1 l1n8v1_2 l1n8v1_3 l1n8v1_4 l1n8v1_5 l1n8v1_6 l1n8v1_7 l1n8v1_8 l1n8v1_9 l1n8v1_10')
l1n9v1_1,l1n9v1_2,l1n9v1_3,l1n9v1_4,l1n9v1_5,l1n9v1_6,l1n9v1_7,l1n9v1_8,l1n9v1_9,l1n9v1_10 = Ints('l1n9v1_1 l1n9v1_2 l1n9v1_3 l1n9v1_4 l1n9v1_5 l1n9v1_6 l1n9v1_7 l1n9v1_8 l1n9v1_9 l1n9v1_10')
l1n10v1_1,l1n10v1_2,l1n10v1_3,l1n10v1_4,l1n10v1_5,l1n10v1_6,l1n10v1_7,l1n10v1_8,l1n10v1_9,l1n10v1_10 = Ints('l1n10v1_1 l1n10v1_2 l1n10v1_3 l1n10v1_4 l1n10v1_5 l1n10v1_6 l1n10v1_7 l1n10v1_8 l1n10v1_9 l1n10v1_10')

l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5,l1n1v2_6,l1n1v2_7,l1n1v2_8,l1n1v2_9,l1n1v2_10 = Ints('l1n1v2_1 l1n1v2_2 l1n1v2_3 l1n1v2_4 l1n1v2_5 l1n1v2_6 l1n1v2_7 l1n1v2_8 l1n1v2_9 l1n1v2_10')
l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5,l1n2v2_6,l1n2v2_7,l1n2v2_8,l1n2v2_9,l1n2v2_10 = Ints('l1n2v2_1 l1n2v2_2 l1n2v2_3 l1n2v2_4 l1n2v2_5 l1n2v2_6 l1n2v2_7 l1n2v2_8 l1n2v2_9 l1n2v2_10')
l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5,l1n3v2_6,l1n3v2_7,l1n3v2_8,l1n3v2_9,l1n3v2_10 = Ints('l1n3v2_1 l1n3v2_2 l1n3v2_3 l1n3v2_4 l1n3v2_5 l1n3v2_6 l1n3v2_7 l1n3v2_8 l1n3v2_9 l1n3v2_10')
l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5,l1n4v2_6,l1n4v2_7,l1n4v2_8,l1n4v2_9,l1n4v2_10 = Ints('l1n4v2_1 l1n4v2_2 l1n4v2_3 l1n4v2_4 l1n4v2_5 l1n4v2_6 l1n4v2_7 l1n4v2_8 l1n4v2_9 l1n4v2_10')
l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5,l1n5v2_6,l1n5v2_7,l1n5v2_8,l1n5v2_9,l1n5v2_10 = Ints('l1n5v2_1 l1n5v2_2 l1n5v2_3 l1n5v2_4 l1n5v2_5 l1n5v2_6 l1n5v2_7 l1n5v2_8 l1n5v2_9 l1n5v2_10')
l1n6v2_1,l1n6v2_2,l1n6v2_3,l1n6v2_4,l1n6v2_5,l1n6v2_6,l1n6v2_7,l1n6v2_8,l1n6v2_9,l1n6v2_10 = Ints('l1n6v2_1 l1n6v2_2 l1n6v2_3 l1n6v2_4 l1n6v2_5 l1n6v2_6 l1n6v2_7 l1n6v2_8 l1n6v2_9 l1n6v2_10')
l1n7v2_1,l1n7v2_2,l1n7v2_3,l1n7v2_4,l1n7v2_5,l1n7v2_6,l1n7v2_7,l1n7v2_8,l1n7v2_9,l1n7v2_10 = Ints('l1n7v2_1 l1n7v2_2 l1n7v2_3 l1n7v2_4 l1n7v2_5 l1n7v2_6 l1n7v2_7 l1n7v2_8 l1n7v2_9 l1n7v2_10')
l1n8v2_1,l1n8v2_2,l1n8v2_3,l1n8v2_4,l1n8v2_5,l1n8v2_6,l1n8v2_7,l1n8v2_8,l1n8v2_9,l1n8v2_10 = Ints('l1n8v2_1 l1n8v2_2 l1n8v2_3 l1n8v2_4 l1n8v2_5 l1n8v2_6 l1n8v2_7 l1n8v2_8 l1n8v2_9 l1n8v2_10')
l1n9v2_1,l1n9v2_2,l1n9v2_3,l1n9v2_4,l1n9v2_5,l1n9v2_6,l1n9v2_7,l1n9v2_8,l1n9v2_9,l1n9v2_10 = Ints('l1n9v2_1 l1n9v2_2 l1n9v2_3 l1n9v2_4 l1n9v2_5 l1n9v2_6 l1n9v2_7 l1n9v2_8 l1n9v2_9 l1n9v2_10')
l1n10v2_1,l1n10v2_2,l1n10v2_3,l1n10v2_4,l1n10v2_5,l1n10v2_6,l1n10v2_7,l1n10v2_8,l1n10v2_9,l1n10v2_10 = Ints('l1n10v2_1 l1n10v2_2 l1n10v2_3 l1n10v2_4 l1n10v2_5 l1n10v2_6 l1n10v2_7 l1n10v2_8 l1n10v2_9 l1n10v2_10')

ov1_1,ov1_2,ov1_3,ov1_4,ov1_5,ov1_6,ov1_7,ov1_8,ov1_9,ov1_10 = Ints('ov1_1 ov1_2 ov1_3 ov1_4 ov1_5 ov1_6 ov1_7 ov1_8 ov1_9 ov1_10')
ov2_1,ov2_2,ov2_3,ov2_4,ov2_5,ov2_6,ov2_7,ov2_8,ov2_9,ov2_10 = Ints('ov2_1 ov2_2 ov2_3 ov2_4 ov2_5 ov2_6 ov2_7 ov2_8 ov2_9 ov2_10')

tuple = Datatype('tuple')
tuple.declare('tuple',('1',IntSort()),('2',IntSort()),('3',IntSort()),('4',IntSort()),('5',IntSort()),('6',IntSort()),('7',IntSort()),('8',IntSort()),('9',IntSort()),('10',IntSort()))
tuple = tuple.create()
out1 = tuple.tuple(ov1_1,ov1_2,ov1_3,ov1_4,ov1_5,ov1_6,ov1_7,ov1_8,ov1_9,ov1_10)
out2 = tuple.tuple(ov2_1,ov2_2,ov2_3,ov2_4,ov2_5,ov2_6,ov2_7,ov2_8,ov2_9,ov2_10)

def NN(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,l1n1_1,l1n1_2,l1n1_3,l1n1_4,l1n1_5,l1n1_6,l1n1_7,l1n1_8,l1n1_9,l1n1_10,l1n2_1,l1n2_2,l1n2_3,l1n2_4,l1n2_5,l1n2_6,l1n2_7,l1n2_8,l1n2_9,l1n2_10,l1n3_1,l1n3_2,l1n3_3,l1n3_4,l1n3_5,l1n3_6,l1n3_7,l1n3_8,l1n3_9,l1n3_10,l1n4_1,l1n4_2,l1n4_3,l1n4_4,l1n4_5,l1n4_6,l1n4_7,l1n4_8,l1n4_9,l1n4_10,l1n5_1,l1n5_2,l1n5_3,l1n5_4,l1n5_5,l1n5_6,l1n5_7,l1n5_8,l1n5_9,l1n5_10,l1n6_1,l1n6_2,l1n6_3,l1n6_4,l1n6_5,l1n6_6,l1n6_7,l1n6_8,l1n6_9,l1n6_10,l1n7_1,l1n7_2,l1n7_3,l1n7_4,l1n7_5,l1n7_6,l1n7_7,l1n7_8,l1n7_9,l1n7_10,l1n8_1,l1n8_2,l1n8_3,l1n8_4,l1n8_5,l1n8_6,l1n8_7,l1n8_8,l1n8_9,l1n8_10,l1n9_1,l1n9_2,l1n9_3,l1n9_4,l1n9_5,l1n9_6,l1n9_7,l1n9_8,l1n9_9,l1n9_10,l1n10_1,l1n10_2,l1n10_3,l1n10_4,l1n10_5,l1n10_6,l1n10_7,l1n10_8,l1n10_9,l1n10_10):
	l2out_1,l2out_2,l2out_3,l2out_4,l2out_5,l2out_6,l2out_7,l2out_8,l2out_9,l2out_10 = Ints('l2out_1 l2out_2 l2out_3 l2out_4 l2out_5 l2out_6 l2out_7 l2out_8 l2out_9 l2out_10')
	l2out_1 = (in1 * l1n1_1) + (in2 * l1n2_1) + (in3 * l1n3_1) + (in4 * l1n4_1) + (in5 * l1n5_1) + (in6 * l1n6_1) + (in7 * l1n7_1) + (in8 * l1n8_1) + (in9 * l1n9_1) + (in10 * l1n10_1) 
	l2out_1 = If(l2out_1 < 0, 0, l2out_1)
	l2out_2 = (in1 * l1n1_2) + (in2 * l1n2_2) + (in3 * l1n3_2) + (in4 * l1n4_2) + (in5 * l1n5_2) + (in6 * l1n6_2) + (in7 * l1n7_2) + (in8 * l1n8_2) + (in9 * l1n9_2) + (in10 * l1n10_2) 
	l2out_2 = If(l2out_2 < 0, 0, l2out_2)
	l2out_3 = (in1 * l1n1_3) + (in2 * l1n2_3) + (in3 * l1n3_3) + (in4 * l1n4_3) + (in5 * l1n5_3) + (in6 * l1n6_3) + (in7 * l1n7_3) + (in8 * l1n8_3) + (in9 * l1n9_3) + (in10 * l1n10_3) 
	l2out_3 = If(l2out_3 < 0, 0, l2out_3)
	l2out_4 = (in1 * l1n1_4) + (in2 * l1n2_4) + (in3 * l1n3_4) + (in4 * l1n4_4) + (in5 * l1n5_4) + (in6 * l1n6_4) + (in7 * l1n7_4) + (in8 * l1n8_4) + (in9 * l1n9_4) + (in10 * l1n10_4) 
	l2out_4 = If(l2out_4 < 0, 0, l2out_4)
	l2out_5 = (in1 * l1n1_5) + (in2 * l1n2_5) + (in3 * l1n3_5) + (in4 * l1n4_5) + (in5 * l1n5_5) + (in6 * l1n6_5) + (in7 * l1n7_5) + (in8 * l1n8_5) + (in9 * l1n9_5) + (in10 * l1n10_5) 
	l2out_5 = If(l2out_5 < 0, 0, l2out_5)
	l2out_6 = (in1 * l1n1_6) + (in2 * l1n2_6) + (in3 * l1n3_6) + (in4 * l1n4_6) + (in5 * l1n5_6) + (in6 * l1n6_6) + (in7 * l1n7_6) + (in8 * l1n8_6) + (in9 * l1n9_6) + (in10 * l1n10_6) 
	l2out_6 = If(l2out_6 < 0, 0, l2out_6)
	l2out_7 = (in1 * l1n1_7) + (in2 * l1n2_7) + (in3 * l1n3_7) + (in4 * l1n4_7) + (in5 * l1n5_7) + (in6 * l1n6_7) + (in7 * l1n7_7) + (in8 * l1n8_7) + (in9 * l1n9_7) + (in10 * l1n10_7) 
	l2out_7 = If(l2out_7 < 0, 0, l2out_7)
	l2out_8 = (in1 * l1n1_8) + (in2 * l1n2_8) + (in3 * l1n3_8) + (in4 * l1n4_8) + (in5 * l1n5_8) + (in6 * l1n6_8) + (in7 * l1n7_8) + (in8 * l1n8_8) + (in9 * l1n9_8) + (in10 * l1n10_8) 
	l2out_8 = If(l2out_8 < 0, 0, l2out_8)
	l2out_9 = (in1 * l1n1_9) + (in2 * l1n2_9) + (in3 * l1n3_9) + (in4 * l1n4_9) + (in5 * l1n5_9) + (in6 * l1n6_9) + (in7 * l1n7_9) + (in8 * l1n8_9) + (in9 * l1n9_9) + (in10 * l1n10_9) 
	l2out_9 = If(l2out_9 < 0, 0, l2out_9)
	l2out_10 = (in1 * l1n1_10) + (in2 * l1n2_10) + (in3 * l1n3_10) + (in4 * l1n4_10) + (in5 * l1n5_10) + (in6 * l1n6_10) + (in7 * l1n7_10) + (in8 * l1n8_10) + (in9 * l1n9_10) + (in10 * l1n10_10) 
	l2out_10 = If(l2out_10 < 0, 0, l2out_10)
	
	out = tuple.tuple(l2out_1,l2out_2,l2out_3,l2out_4,l2out_5,l2out_6,l2out_7,l2out_8,l2out_9,l2out_10)
	
	return out

s = Tactic('smt').solver()

s.add(l1n1v1_1 > 0, l1n1v1_1 < 127)
s.add(l1n1v2_1 > 0, l1n1v2_1 < 127)
s.add(l1n1v1_2 > 0, l1n1v1_2 < 127)
s.add(l1n1v2_2 > 0, l1n1v2_2 < 127)
s.add(l1n1v1_3 > 0, l1n1v1_3 < 127)
s.add(l1n1v2_3 > 0, l1n1v2_3 < 127)
s.add(l1n1v1_4 > 0, l1n1v1_4 < 127)
s.add(l1n1v2_4 > 0, l1n1v2_4 < 127)
s.add(l1n1v1_5 > 0, l1n1v1_5 < 127)
s.add(l1n1v2_5 > 0, l1n1v2_5 < 127)
s.add(l1n1v1_6 > 0, l1n1v1_6 < 127)
s.add(l1n1v2_6 > 0, l1n1v2_6 < 127)
s.add(l1n1v1_7 > 0, l1n1v1_7 < 127)
s.add(l1n1v2_7 > 0, l1n1v2_7 < 127)
s.add(l1n1v1_8 > 0, l1n1v1_8 < 127)
s.add(l1n1v2_8 > 0, l1n1v2_8 < 127)
s.add(l1n1v1_9 > 0, l1n1v1_9 < 127)
s.add(l1n1v2_9 > 0, l1n1v2_9 < 127)
s.add(l1n1v1_10 > 0, l1n1v1_10 < 127)
s.add(l1n1v2_10 > 0, l1n1v2_10 < 127)
s.add(l1n2v1_1 > 0, l1n2v1_1 < 127)
s.add(l1n2v2_1 > 0, l1n2v2_1 < 127)
s.add(l1n2v1_2 > 0, l1n2v1_2 < 127)
s.add(l1n2v2_2 > 0, l1n2v2_2 < 127)
s.add(l1n2v1_3 > 0, l1n2v1_3 < 127)
s.add(l1n2v2_3 > 0, l1n2v2_3 < 127)
s.add(l1n2v1_4 > 0, l1n2v1_4 < 127)
s.add(l1n2v2_4 > 0, l1n2v2_4 < 127)
s.add(l1n2v1_5 > 0, l1n2v1_5 < 127)
s.add(l1n2v2_5 > 0, l1n2v2_5 < 127)
s.add(l1n2v1_6 > 0, l1n2v1_6 < 127)
s.add(l1n2v2_6 > 0, l1n2v2_6 < 127)
s.add(l1n2v1_7 > 0, l1n2v1_7 < 127)
s.add(l1n2v2_7 > 0, l1n2v2_7 < 127)
s.add(l1n2v1_8 > 0, l1n2v1_8 < 127)
s.add(l1n2v2_8 > 0, l1n2v2_8 < 127)
s.add(l1n2v1_9 > 0, l1n2v1_9 < 127)
s.add(l1n2v2_9 > 0, l1n2v2_9 < 127)
s.add(l1n2v1_10 > 0, l1n2v1_10 < 127)
s.add(l1n2v2_10 > 0, l1n2v2_10 < 127)
s.add(l1n3v1_1 > 0, l1n3v1_1 < 127)
s.add(l1n3v2_1 > 0, l1n3v2_1 < 127)
s.add(l1n3v1_2 > 0, l1n3v1_2 < 127)
s.add(l1n3v2_2 > 0, l1n3v2_2 < 127)
s.add(l1n3v1_3 > 0, l1n3v1_3 < 127)
s.add(l1n3v2_3 > 0, l1n3v2_3 < 127)
s.add(l1n3v1_4 > 0, l1n3v1_4 < 127)
s.add(l1n3v2_4 > 0, l1n3v2_4 < 127)
s.add(l1n3v1_5 > 0, l1n3v1_5 < 127)
s.add(l1n3v2_5 > 0, l1n3v2_5 < 127)
s.add(l1n3v1_6 > 0, l1n3v1_6 < 127)
s.add(l1n3v2_6 > 0, l1n3v2_6 < 127)
s.add(l1n3v1_7 > 0, l1n3v1_7 < 127)
s.add(l1n3v2_7 > 0, l1n3v2_7 < 127)
s.add(l1n3v1_8 > 0, l1n3v1_8 < 127)
s.add(l1n3v2_8 > 0, l1n3v2_8 < 127)
s.add(l1n3v1_9 > 0, l1n3v1_9 < 127)
s.add(l1n3v2_9 > 0, l1n3v2_9 < 127)
s.add(l1n3v1_10 > 0, l1n3v1_10 < 127)
s.add(l1n3v2_10 > 0, l1n3v2_10 < 127)
s.add(l1n4v1_1 > 0, l1n4v1_1 < 127)
s.add(l1n4v2_1 > 0, l1n4v2_1 < 127)
s.add(l1n4v1_2 > 0, l1n4v1_2 < 127)
s.add(l1n4v2_2 > 0, l1n4v2_2 < 127)
s.add(l1n4v1_3 > 0, l1n4v1_3 < 127)
s.add(l1n4v2_3 > 0, l1n4v2_3 < 127)
s.add(l1n4v1_4 > 0, l1n4v1_4 < 127)
s.add(l1n4v2_4 > 0, l1n4v2_4 < 127)
s.add(l1n4v1_5 > 0, l1n4v1_5 < 127)
s.add(l1n4v2_5 > 0, l1n4v2_5 < 127)
s.add(l1n4v1_6 > 0, l1n4v1_6 < 127)
s.add(l1n4v2_6 > 0, l1n4v2_6 < 127)
s.add(l1n4v1_7 > 0, l1n4v1_7 < 127)
s.add(l1n4v2_7 > 0, l1n4v2_7 < 127)
s.add(l1n4v1_8 > 0, l1n4v1_8 < 127)
s.add(l1n4v2_8 > 0, l1n4v2_8 < 127)
s.add(l1n4v1_9 > 0, l1n4v1_9 < 127)
s.add(l1n4v2_9 > 0, l1n4v2_9 < 127)
s.add(l1n4v1_10 > 0, l1n4v1_10 < 127)
s.add(l1n4v2_10 > 0, l1n4v2_10 < 127)
s.add(l1n5v1_1 > 0, l1n5v1_1 < 127)
s.add(l1n5v2_1 > 0, l1n5v2_1 < 127)
s.add(l1n5v1_2 > 0, l1n5v1_2 < 127)
s.add(l1n5v2_2 > 0, l1n5v2_2 < 127)
s.add(l1n5v1_3 > 0, l1n5v1_3 < 127)
s.add(l1n5v2_3 > 0, l1n5v2_3 < 127)
s.add(l1n5v1_4 > 0, l1n5v1_4 < 127)
s.add(l1n5v2_4 > 0, l1n5v2_4 < 127)
s.add(l1n5v1_5 > 0, l1n5v1_5 < 127)
s.add(l1n5v2_5 > 0, l1n5v2_5 < 127)
s.add(l1n5v1_6 > 0, l1n5v1_6 < 127)
s.add(l1n5v2_6 > 0, l1n5v2_6 < 127)
s.add(l1n5v1_7 > 0, l1n5v1_7 < 127)
s.add(l1n5v2_7 > 0, l1n5v2_7 < 127)
s.add(l1n5v1_8 > 0, l1n5v1_8 < 127)
s.add(l1n5v2_8 > 0, l1n5v2_8 < 127)
s.add(l1n5v1_9 > 0, l1n5v1_9 < 127)
s.add(l1n5v2_9 > 0, l1n5v2_9 < 127)
s.add(l1n5v1_10 > 0, l1n5v1_10 < 127)
s.add(l1n5v2_10 > 0, l1n5v2_10 < 127)
s.add(l1n6v1_1 > 0, l1n6v1_1 < 127)
s.add(l1n6v2_1 > 0, l1n6v2_1 < 127)
s.add(l1n6v1_2 > 0, l1n6v1_2 < 127)
s.add(l1n6v2_2 > 0, l1n6v2_2 < 127)
s.add(l1n6v1_3 > 0, l1n6v1_3 < 127)
s.add(l1n6v2_3 > 0, l1n6v2_3 < 127)
s.add(l1n6v1_4 > 0, l1n6v1_4 < 127)
s.add(l1n6v2_4 > 0, l1n6v2_4 < 127)
s.add(l1n6v1_5 > 0, l1n6v1_5 < 127)
s.add(l1n6v2_5 > 0, l1n6v2_5 < 127)
s.add(l1n6v1_6 > 0, l1n6v1_6 < 127)
s.add(l1n6v2_6 > 0, l1n6v2_6 < 127)
s.add(l1n6v1_7 > 0, l1n6v1_7 < 127)
s.add(l1n6v2_7 > 0, l1n6v2_7 < 127)
s.add(l1n6v1_8 > 0, l1n6v1_8 < 127)
s.add(l1n6v2_8 > 0, l1n6v2_8 < 127)
s.add(l1n6v1_9 > 0, l1n6v1_9 < 127)
s.add(l1n6v2_9 > 0, l1n6v2_9 < 127)
s.add(l1n6v1_10 > 0, l1n6v1_10 < 127)
s.add(l1n6v2_10 > 0, l1n6v2_10 < 127)
s.add(l1n7v1_1 > 0, l1n7v1_1 < 127)
s.add(l1n7v2_1 > 0, l1n7v2_1 < 127)
s.add(l1n7v1_2 > 0, l1n7v1_2 < 127)
s.add(l1n7v2_2 > 0, l1n7v2_2 < 127)
s.add(l1n7v1_3 > 0, l1n7v1_3 < 127)
s.add(l1n7v2_3 > 0, l1n7v2_3 < 127)
s.add(l1n7v1_4 > 0, l1n7v1_4 < 127)
s.add(l1n7v2_4 > 0, l1n7v2_4 < 127)
s.add(l1n7v1_5 > 0, l1n7v1_5 < 127)
s.add(l1n7v2_5 > 0, l1n7v2_5 < 127)
s.add(l1n7v1_6 > 0, l1n7v1_6 < 127)
s.add(l1n7v2_6 > 0, l1n7v2_6 < 127)
s.add(l1n7v1_7 > 0, l1n7v1_7 < 127)
s.add(l1n7v2_7 > 0, l1n7v2_7 < 127)
s.add(l1n7v1_8 > 0, l1n7v1_8 < 127)
s.add(l1n7v2_8 > 0, l1n7v2_8 < 127)
s.add(l1n7v1_9 > 0, l1n7v1_9 < 127)
s.add(l1n7v2_9 > 0, l1n7v2_9 < 127)
s.add(l1n7v1_10 > 0, l1n7v1_10 < 127)
s.add(l1n7v2_10 > 0, l1n7v2_10 < 127)
s.add(l1n8v1_1 > 0, l1n8v1_1 < 127)
s.add(l1n8v2_1 > 0, l1n8v2_1 < 127)
s.add(l1n8v1_2 > 0, l1n8v1_2 < 127)
s.add(l1n8v2_2 > 0, l1n8v2_2 < 127)
s.add(l1n8v1_3 > 0, l1n8v1_3 < 127)
s.add(l1n8v2_3 > 0, l1n8v2_3 < 127)
s.add(l1n8v1_4 > 0, l1n8v1_4 < 127)
s.add(l1n8v2_4 > 0, l1n8v2_4 < 127)
s.add(l1n8v1_5 > 0, l1n8v1_5 < 127)
s.add(l1n8v2_5 > 0, l1n8v2_5 < 127)
s.add(l1n8v1_6 > 0, l1n8v1_6 < 127)
s.add(l1n8v2_6 > 0, l1n8v2_6 < 127)
s.add(l1n8v1_7 > 0, l1n8v1_7 < 127)
s.add(l1n8v2_7 > 0, l1n8v2_7 < 127)
s.add(l1n8v1_8 > 0, l1n8v1_8 < 127)
s.add(l1n8v2_8 > 0, l1n8v2_8 < 127)
s.add(l1n8v1_9 > 0, l1n8v1_9 < 127)
s.add(l1n8v2_9 > 0, l1n8v2_9 < 127)
s.add(l1n8v1_10 > 0, l1n8v1_10 < 127)
s.add(l1n8v2_10 > 0, l1n8v2_10 < 127)
s.add(l1n9v1_1 > 0, l1n9v1_1 < 127)
s.add(l1n9v2_1 > 0, l1n9v2_1 < 127)
s.add(l1n9v1_2 > 0, l1n9v1_2 < 127)
s.add(l1n9v2_2 > 0, l1n9v2_2 < 127)
s.add(l1n9v1_3 > 0, l1n9v1_3 < 127)
s.add(l1n9v2_3 > 0, l1n9v2_3 < 127)
s.add(l1n9v1_4 > 0, l1n9v1_4 < 127)
s.add(l1n9v2_4 > 0, l1n9v2_4 < 127)
s.add(l1n9v1_5 > 0, l1n9v1_5 < 127)
s.add(l1n9v2_5 > 0, l1n9v2_5 < 127)
s.add(l1n9v1_6 > 0, l1n9v1_6 < 127)
s.add(l1n9v2_6 > 0, l1n9v2_6 < 127)
s.add(l1n9v1_7 > 0, l1n9v1_7 < 127)
s.add(l1n9v2_7 > 0, l1n9v2_7 < 127)
s.add(l1n9v1_8 > 0, l1n9v1_8 < 127)
s.add(l1n9v2_8 > 0, l1n9v2_8 < 127)
s.add(l1n9v1_9 > 0, l1n9v1_9 < 127)
s.add(l1n9v2_9 > 0, l1n9v2_9 < 127)
s.add(l1n9v1_10 > 0, l1n9v1_10 < 127)
s.add(l1n9v2_10 > 0, l1n9v2_10 < 127)
s.add(l1n10v1_1 > 0, l1n10v1_1 < 127)
s.add(l1n10v2_1 > 0, l1n10v2_1 < 127)
s.add(l1n10v1_2 > 0, l1n10v1_2 < 127)
s.add(l1n10v2_2 > 0, l1n10v2_2 < 127)
s.add(l1n10v1_3 > 0, l1n10v1_3 < 127)
s.add(l1n10v2_3 > 0, l1n10v2_3 < 127)
s.add(l1n10v1_4 > 0, l1n10v1_4 < 127)
s.add(l1n10v2_4 > 0, l1n10v2_4 < 127)
s.add(l1n10v1_5 > 0, l1n10v1_5 < 127)
s.add(l1n10v2_5 > 0, l1n10v2_5 < 127)
s.add(l1n10v1_6 > 0, l1n10v1_6 < 127)
s.add(l1n10v2_6 > 0, l1n10v2_6 < 127)
s.add(l1n10v1_7 > 0, l1n10v1_7 < 127)
s.add(l1n10v2_7 > 0, l1n10v2_7 < 127)
s.add(l1n10v1_8 > 0, l1n10v1_8 < 127)
s.add(l1n10v2_8 > 0, l1n10v2_8 < 127)
s.add(l1n10v1_9 > 0, l1n10v1_9 < 127)
s.add(l1n10v2_9 > 0, l1n10v2_9 < 127)
s.add(l1n10v1_10 > 0, l1n10v1_10 < 127)
s.add(l1n10v2_10 > 0, l1n10v2_10 < 127)

s.add(NN(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5,l1n1v1_6,l1n1v1_7,l1n1v1_8,l1n1v1_9,l1n1v1_10,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5,l1n2v1_6,l1n2v1_7,l1n2v1_8,l1n2v1_9,l1n2v1_10,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5,l1n3v1_6,l1n3v1_7,l1n3v1_8,l1n3v1_9,l1n3v1_10,l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5,l1n4v1_6,l1n4v1_7,l1n4v1_8,l1n4v1_9,l1n4v1_10,l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5,l1n5v1_6,l1n5v1_7,l1n5v1_8,l1n5v1_9,l1n5v1_10,l1n6v1_1,l1n6v1_2,l1n6v1_3,l1n6v1_4,l1n6v1_5,l1n6v1_6,l1n6v1_7,l1n6v1_8,l1n6v1_9,l1n6v1_10,l1n7v1_1,l1n7v1_2,l1n7v1_3,l1n7v1_4,l1n7v1_5,l1n7v1_6,l1n7v1_7,l1n7v1_8,l1n7v1_9,l1n7v1_10,l1n8v1_1,l1n8v1_2,l1n8v1_3,l1n8v1_4,l1n8v1_5,l1n8v1_6,l1n8v1_7,l1n8v1_8,l1n8v1_9,l1n8v1_10,l1n9v1_1,l1n9v1_2,l1n9v1_3,l1n9v1_4,l1n9v1_5,l1n9v1_6,l1n9v1_7,l1n9v1_8,l1n9v1_9,l1n9v1_10,l1n10v1_1,l1n10v1_2,l1n10v1_3,l1n10v1_4,l1n10v1_5,l1n10v1_6,l1n10v1_7,l1n10v1_8,l1n10v1_9,l1n10v1_10) == out1)
s.add(NN(in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5,l1n1v2_6,l1n1v2_7,l1n1v2_8,l1n1v2_9,l1n1v2_10,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5,l1n2v2_6,l1n2v2_7,l1n2v2_8,l1n2v2_9,l1n2v2_10,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5,l1n3v2_6,l1n3v2_7,l1n3v2_8,l1n3v2_9,l1n3v2_10,l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5,l1n4v2_6,l1n4v2_7,l1n4v2_8,l1n4v2_9,l1n4v2_10,l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5,l1n5v2_6,l1n5v2_7,l1n5v2_8,l1n5v2_9,l1n5v2_10,l1n6v2_1,l1n6v2_2,l1n6v2_3,l1n6v2_4,l1n6v2_5,l1n6v2_6,l1n6v2_7,l1n6v2_8,l1n6v2_9,l1n6v2_10,l1n7v2_1,l1n7v2_2,l1n7v2_3,l1n7v2_4,l1n7v2_5,l1n7v2_6,l1n7v2_7,l1n7v2_8,l1n7v2_9,l1n7v2_10,l1n8v2_1,l1n8v2_2,l1n8v2_3,l1n8v2_4,l1n8v2_5,l1n8v2_6,l1n8v2_7,l1n8v2_8,l1n8v2_9,l1n8v2_10,l1n9v2_1,l1n9v2_2,l1n9v2_3,l1n9v2_4,l1n9v2_5,l1n9v2_6,l1n9v2_7,l1n9v2_8,l1n9v2_9,l1n9v2_10,l1n10v2_1,l1n10v2_2,l1n10v2_3,l1n10v2_4,l1n10v2_5,l1n10v2_6,l1n10v2_7,l1n10v2_8,l1n10v2_9,l1n10v2_10) == out2)

while s.check(out1 != out2) == sat:
	m = s.model()
	ia = str(m[in1]) + " " + str(m[in2]) + " " + str(m[in3]) + " " + str(m[in4]) + " " + str(m[in5]) + " " + str(m[in6]) + " " + str(m[in7]) + " " + str(m[in8]) + " " + str(m[in9]) + " " + str(m[in10])
	print(ia)
	out = Cexec(ia)
	print(out)

	inp1 = m[in1]
	inp2 = m[in2]
	inp3 = m[in3]
	inp4 = m[in4]
	inp5 = m[in5]
	inp6 = m[in6]
	inp7 = m[in7]
	inp8 = m[in8]
	inp9 = m[in9]
	inp10 = m[in10]

	out_tup = tuple.tuple(out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7],out[8],out[9])

	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,l1n1v1_1,l1n1v1_2,l1n1v1_3,l1n1v1_4,l1n1v1_5,l1n1v1_6,l1n1v1_7,l1n1v1_8,l1n1v1_9,l1n1v1_10,l1n2v1_1,l1n2v1_2,l1n2v1_3,l1n2v1_4,l1n2v1_5,l1n2v1_6,l1n2v1_7,l1n2v1_8,l1n2v1_9,l1n2v1_10,l1n3v1_1,l1n3v1_2,l1n3v1_3,l1n3v1_4,l1n3v1_5,l1n3v1_6,l1n3v1_7,l1n3v1_8,l1n3v1_9,l1n3v1_10,l1n4v1_1,l1n4v1_2,l1n4v1_3,l1n4v1_4,l1n4v1_5,l1n4v1_6,l1n4v1_7,l1n4v1_8,l1n4v1_9,l1n4v1_10,l1n5v1_1,l1n5v1_2,l1n5v1_3,l1n5v1_4,l1n5v1_5,l1n5v1_6,l1n5v1_7,l1n5v1_8,l1n5v1_9,l1n5v1_10,l1n6v1_1,l1n6v1_2,l1n6v1_3,l1n6v1_4,l1n6v1_5,l1n6v1_6,l1n6v1_7,l1n6v1_8,l1n6v1_9,l1n6v1_10,l1n7v1_1,l1n7v1_2,l1n7v1_3,l1n7v1_4,l1n7v1_5,l1n7v1_6,l1n7v1_7,l1n7v1_8,l1n7v1_9,l1n7v1_10,l1n8v1_1,l1n8v1_2,l1n8v1_3,l1n8v1_4,l1n8v1_5,l1n8v1_6,l1n8v1_7,l1n8v1_8,l1n8v1_9,l1n8v1_10,l1n9v1_1,l1n9v1_2,l1n9v1_3,l1n9v1_4,l1n9v1_5,l1n9v1_6,l1n9v1_7,l1n9v1_8,l1n9v1_9,l1n9v1_10,l1n10v1_1,l1n10v1_2,l1n10v1_3,l1n10v1_4,l1n10v1_5,l1n10v1_6,l1n10v1_7,l1n10v1_8,l1n10v1_9,l1n10v1_10) == out_tup)
	s.add(NN(inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,l1n1v2_1,l1n1v2_2,l1n1v2_3,l1n1v2_4,l1n1v2_5,l1n1v2_6,l1n1v2_7,l1n1v2_8,l1n1v2_9,l1n1v2_10,l1n2v2_1,l1n2v2_2,l1n2v2_3,l1n2v2_4,l1n2v2_5,l1n2v2_6,l1n2v2_7,l1n2v2_8,l1n2v2_9,l1n2v2_10,l1n3v2_1,l1n3v2_2,l1n3v2_3,l1n3v2_4,l1n3v2_5,l1n3v2_6,l1n3v2_7,l1n3v2_8,l1n3v2_9,l1n3v2_10,l1n4v2_1,l1n4v2_2,l1n4v2_3,l1n4v2_4,l1n4v2_5,l1n4v2_6,l1n4v2_7,l1n4v2_8,l1n4v2_9,l1n4v2_10,l1n5v2_1,l1n5v2_2,l1n5v2_3,l1n5v2_4,l1n5v2_5,l1n5v2_6,l1n5v2_7,l1n5v2_8,l1n5v2_9,l1n5v2_10,l1n6v2_1,l1n6v2_2,l1n6v2_3,l1n6v2_4,l1n6v2_5,l1n6v2_6,l1n6v2_7,l1n6v2_8,l1n6v2_9,l1n6v2_10,l1n7v2_1,l1n7v2_2,l1n7v2_3,l1n7v2_4,l1n7v2_5,l1n7v2_6,l1n7v2_7,l1n7v2_8,l1n7v2_9,l1n7v2_10,l1n8v2_1,l1n8v2_2,l1n8v2_3,l1n8v2_4,l1n8v2_5,l1n8v2_6,l1n8v2_7,l1n8v2_8,l1n8v2_9,l1n8v2_10,l1n9v2_1,l1n9v2_2,l1n9v2_3,l1n9v2_4,l1n9v2_5,l1n9v2_6,l1n9v2_7,l1n9v2_8,l1n9v2_9,l1n9v2_10,l1n10v2_1,l1n10v2_2,l1n10v2_3,l1n10v2_4,l1n10v2_5,l1n10v2_6,l1n10v2_7,l1n10v2_8,l1n10v2_9,l1n10v2_10) == out_tup)

print(s.check(out1 == out2))
print(s.model())

print("Layer 1 weights are broken in " + str(time.time() - start_time) + " seconds")