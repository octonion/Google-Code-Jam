#!/usr/bin/python
#
# Problem: Cheating a Boolean Tree
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


MAX = 10000000000

def compute():

    def left(i):
	return tree[2*(i+1)-1]
    
    def right(i):
	return tree[2*(i+1)]

    def evaluate():
	r =  (range((m-1)/2))[::-1]
	for i in r:
	    if itree[i][0] == 1:
		tree[i] = left(i) and right(i)
	    else:
		tree[i] = left(i) or right(i)
	return int(tree[0])

    def rec():

	def xleft(i):
	    return xtree[2*(i+1)-1]

	def xright(i):
	    return xtree[2*(i+1)]

	r = (range((m-1)/2))[::-1]
	for i in r: 
	    w = 0
	    if itree[i][1] == 1: # changeable
		if itree[i][0] == 1: #and
		    if left(i) and (not right(i)): #10
			mm = 1			
		    if (not left(i)) and right(i): #01
			mm = 1
		    if left(i) and right(i): #11
			mm = min(xleft(i), xright(i))
		    if (not left(i)) and (not right(i)): #00
			mm = min(xleft(i), xright(i)) + 1
		else:
		    if left(i) and (not right(i)): #10
			mm = 1			
		    if (not left(i)) and right(i): #01
			mm = 1
		    if left(i) and right(i): #11
			mm = min(xleft(i), xright(i)) + 1
		    if (not left(i)) and (not right(i)): #00
			mm = min(xleft(i), xright(i))
	    else: # not changeable
		if itree[i][0] == 1: #and
		    if left(i) and (not right(i)): #10
			mm = xright(i)			
		    if (not left(i)) and right(i): #01
			mm = xleft(i)
		    if left(i) and right(i): #11
			mm = min(xleft(i), xright(i))
		    if (not left(i)) and (not right(i)): #00
			mm = xleft(i) + xright(i)
		else:
		    if left(i) and (not right(i)): #10
			mm = xleft(i)			
		    if (not left(i)) and right(i): #01
			mm = xright(i)
		    if left(i) and right(i): #11
			mm = xleft(i) + xright(i)
		    if (not left(i)) and (not right(i)): #00
			mm = min(xleft(i), xright(i))
	    xtree[i] = mm
	return xtree[0]
	    
    m, v = map(int, raw_input().split())
    itree = []
    tree = []
    xtree = []
    for i in range((m-1)/2):
	g, c = map(int, raw_input().split())
	itree.append([g,c])
	tree.append(0)
	xtree.append(MAX)
    for i in range((m+1)/2):
	leaf = input()
	leaf = (leaf == 1)
	tree.append(leaf)
	xtree.append(MAX)

    if (evaluate() == v): # no changes needed
	return "0"
    else: # must change root
	zz = rec()
	if zz >= MAX:
	    return "IMPOSSIBLE"
	else:
	    return str(zz)

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
