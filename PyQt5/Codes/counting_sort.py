

def counting_sort(A):
    B=[]
    n=len(A)
    C=[0]*n
    for i in range(1,n):
        C[i]=0
    for j in range(0,n):
        C[A[j]]=C[A[j]]+1
    for i in range(1,n):
        C[i]=C[i]+C[i-1]

    for j in range(n,1,-1):
        B[C[A[j]]]=A[j]
        C[A[j]]=C[A[j]]-1


M=[54,78,96,35,2,10,76,90,5]
counting_sort(M)
print("M",M)