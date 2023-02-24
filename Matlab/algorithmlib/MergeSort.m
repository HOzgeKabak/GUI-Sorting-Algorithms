

function [result] = MergeSort(x)



n = length(x);
if n == 1
    
    result = x;
else
    q= floor(n/2);  
    r1 = MergeSort( x(1:q) );    
    r2 = MergeSort( x(q+1:n) );  
    result = Merge( r1, r2 );    
end
end
function M = Merge( R, L )


RLen = length(R);  
LLen = length(L);  
r = RLen+LLen;
M= zeros(1,r); 


j = 1;
i= 1;
for k = 1:r
  
  if j > RLen
   
    M(k) = L(i); 
     i = i + 1;
  elseif i > LLen
    
    M(k) = R(j); 
    j = j + 1;
  elseif R(j) <= L(i)
    
     M(k) = R(j); 
     j = j + 1;
  else
    
    M(k) = L(i); 
    i = i + 1;
  end
end

end

