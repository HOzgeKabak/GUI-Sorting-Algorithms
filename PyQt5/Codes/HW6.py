
def rand_select(A,p,q,i):
    if p==q:
        return A[p]

    if (i>0 and i<=q-p+1):

        r=partition(A,p,q)

        if (r-p==i-1):
            return A[r]
        if (r-p>i-1):
            return rand_select(A,p,r-1,i)

        return rand_select(A,r+1,q,i-r+p-1)


def partition(A,p,q):
    x=A[q]
    n=p
    for j in range(p,q):
        if (A[j]<=x):
            A[n],A[j]=A[j],A[n]
            n=n+1

    A[n],A[q]=A[q],A[n]
    return n

A=[1,54,78,85,96]
m=len(A)
z=4
y=rand_select(A,0,m-1,z)
print("y",y)