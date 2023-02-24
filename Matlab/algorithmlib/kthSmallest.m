function y=kthSmallest(arr, l, r, k)
     
    
    if (k > 0 && k <= r - l + 1)
         
      
        pos = randomPartition(arr, l, r);
    end
        if (pos - l == k - 1)
            y=arr(pos);
            return 
        end
        if (pos - l > k - 1)
               kthSmallest(arr, l, pos - 1, k)             
            return 
        end
                kthSmallest(arr, pos + 1, r,k - pos + l - 1)
       
        return 
 
    

       
        end

        

 
 function arr=swap(arr, a, b)
    temp = arr(a);
    arr(a) = arr(b);
    arr(b) = temp;
 end
 function y=partition(arr, l, r)
    x = arr(r);
    i = l;
    for j=l:r
        if arr(j) <= x
            swap(arr, i, j)
            i =i+1;
    swap(arr, i, r)
    y=i;
    return 
        end
    end
 end
 
 function y=randomPartition(arr, l, r)
  
    pivot =randi(1,r);
    swap(arr, l + pivot, r)
    y=partition(arr, l, r);
    return
 end