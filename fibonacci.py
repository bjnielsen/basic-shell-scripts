#!/usr/bin/env python
# "Fibonacci sequences" using a sqrt to slow convergence.
# B. Nielsen

from math import sqrt
import time
import platform

print 'Architecture:', platform.uname()
CurrentVal = 0

def incrementdecades(decades):
    a = 1000
    while a <= decades:
        yield a
        a *= 10

def fibonacci(maxnum):
    a, b = 0, 1
    while a < maxnum:
        yield a
        a, b = sqrt(b), a + b

# 100000000     =    100,000,000 = 10^8
# 1000000000    =  1,000,000,000 = 10^9
# 10000000000   = 10,000,000,000 = 10^10
DefaultMaxDecade = 10000000000   # 10,000,000,000 = 10^10
for i in incrementdecades(DefaultMaxDecade):
    print 'sqrt(fibonicci) is calculating up to:', '%.0e' % i, '...',
    starttime = time.time()
    for n in fibonacci(i):
        CurrentVal = n
    #print 'Calculating sqrt(fibonicci) up to:', '%.0e' % CurrentVal,
    endtime = time.time()
    totaltime = endtime - starttime
    print 'and took: ', '%.3e' % totaltime, 'Seconds'


#i = 0
#while 1:
#	i = i + 1
#	print i

# In matlab, the sqrt of fibonacci numbers.
#function g = squibo(n)
#% This function calculates the first n "squibonacci" numbers.
#% $Revision: 1.1 $
#%
#g = zeros(1,n)
#g(1) = 1;
#g(2) = 1;
#
#for i = 3:n
#g(i) = sqrt(g(i-1)) + g(i-2);
#end

#    a, b = b, sqrt(a) + sqrt(b)
#    a, b = sqrt(b), sqrt(a) + sqrt(b)