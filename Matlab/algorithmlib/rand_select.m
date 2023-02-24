
function m=rand_select_app(A,p,q,i,~,~)
    if p==q
        m=A(p);
        return
    end
    if (i>0 && i<=q-p+1)

        r=partition(A,p,q);

        if (r-p==i-1)
            m=A(r);
            return 
        end
        if (r-p>i-1)
            m=rand_select(A,p,r-1,i);

            return 
        end
            m=rand_select(A,r+1,q,i-r+p-1);
        return 
    end
end
    function r=partition(A,p,q)
    x=A(q);
    n=p;
    for j=(p:q)
        if (A(j)<=x)
            A(j)=A(n);
            key=A(n);
            A(j)=key;
            n=n+1;

   
    A(q)=A(n);
    temp=A(n);
    A(q)=temp;
    r=n;
    return 
        end
    end
    end
   
     
