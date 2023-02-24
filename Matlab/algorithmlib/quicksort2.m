function Array=quicksort2(Array,p,r)
if p<r
   
    [q,Array]=partition2(Array,p,r);
    Array=quicksort(Array,p,q-1);
    Array=quicksort(Array,q+1,r);
   
end
end

