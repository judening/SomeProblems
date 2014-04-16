#Calculate all the products of an integer array except the current index
#Example: [3,1,4,2] => [8,24,6,12]

def calProduct(teh_list):
    matrix = [[1 for x in xrange(2)] for x in xrange(len(teh_list))]

    prev = 1
    for i in range(1,len(teh_list)):
        prev = teh_list[i-1] * prev
        matrix[i][0] = prev
        
    prev = 1
    for x in range(len(teh_list)-2,-1,-1):
        prev = teh_list[x+1] * prev
        matrix[x][1] = prev
    
    for x in range(len(matrix)):
        print matrix[x][0]*matrix[x][1]
