#Longest common sequence
#A longest common subsequence (LCS) is the longest subsequence common to all sequences in a set of sequences.
x=[1,2,3,4,7,9]
y=[2,4,7,9,4,5]

def find_lcs(x,y):
    #Create a table of size [len(x)+1]x[len(y)+1]
    c = [[0 for i in range(len(x)+1)] for i in range(len(y)+1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            #Case 0: longest common sequence of either x/y and '' is ''
            if i==0 or j == 0:
                c[i][j]=''
            #Case 1: if x[i]==y[j], then lcs is whatever the longest common sequence of c[i-1][j-1]+x[i]/y[j]
            elif i>0 and j>0 and x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+str(x[i-1])

            #Case 2: if x[i]!=y[j], then lcs is whatever the longest common sequence of c[i-1][j] or c[j-1][i]
            elif i>0 and j>0 and x[i-1]!=y[j-1]:
                if len(c[i][j-1])>len(c[i-1][j]):
                    c[i][j]=c[i][j-1]
                else:
                    c[i][j]=c[i-1][j]

    return c[len(x)][len(y)]

print(f"Longest common subsequence of {x} and {y} is {find_lcs(x,y)}")

#Chain matrix multiplication
#To multiply two matrices of mn and np, we need mnp calc.
#for matrix A,B,C... we need to find a combo of 'mnp's that is the smallest.


A=[50,20]
B=[20,1]
C=[1,10]
D=[10,100]

def find_cmm(matrix_size):
    #create a table c, where c[i][j]=computational cost of M[i]xM[j]
    c = [[0 for i in range(len(matrix_size)+1)] for i in range (len(matrix_size)+1)]

    trace = [[0 for i in range(len(matrix_size)+1)] for i in range (len(matrix_size)+1)]
    #i takes value from 0 to no.matrix-1
    for index in range(1,len(matrix_size)):
        #We need to follow patterms such as (1,2),(2,3),(3,4);(1,3),(2,4);(1,4)
        for i in range(1,len(matrix_size)-index+1):
            j = i+index
            if i==j:
                pass
            else:
                #modify this to max_int
                min_cost=100000
                min_k=i
                for k in range(i,j):
                    cost=c[i][k]+c[k+1][j]+matrix_size[i-1][0]*matrix_size[i-1][1]*matrix_size[k][1]
                    if cost<min_cost:
                        min_cost=cost
                        min_k=k
                c[i][j]=min_cost
                trace[i][j]=min_k

    return c[1][len(matrix_size)]

print(f"Lowest computetaional cost CMM of {[A,B,C,D]} is {find_cmm([A,B,C,D])}")

#Knapsack Problem
profit = [60, 100, 120] 
weight = [10, 20, 30] 
W = 50

def knapSack(W, wt, val, n): 
  
    # Base Case 
    if n == 0 or W == 0: 
        return 0
  
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
  
    else: 
        #either: include last item
        #do not include last item
        return max( 
            val[n-1] + knapSack( 
                W-wt[n-1], wt, val, n-1), 
            knapSack(W, wt, val, n-1)) 
  
print (f"optimal solution for profit: {profit} and weight: {weight} is {knapSack(W, weight, profit, len(profit))}")
