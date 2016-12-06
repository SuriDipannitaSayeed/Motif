#!/bin/python

import sys

def digitsum(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=n/10
    return sum
l=[]
i=1
n = int(raw_input().strip())
for i in range(1,n+1):
    if((n%i)==0):
        l.append(digitsum(i))
l.sort()
print l
print str(l[len(l)-1])

