#Given an integer N, print out all the possible combination of binary numbers

def allBin(num):
    result , bin = [[]], (0,1)
    for i in xrange(num):
        result = [i+[j] for i in result for j in bin]
    print result
    
