function x=Mergesort_mid(A,app,event)
   n=length(A);
   if n==1
       x=A;
   else
   mid=ceil(n/2);
   A1= Mergesort_mid(A(1:mid));
   A2=Mergesort_mid(A(mid+1:n));
   x=merge_mid(A1,A2);
   end
end
function c=merge_mid(l,r)

    
lLen = length(l);  
rLen = length(r);  
cLen = lLen+rLen;
c = zeros(1,cLen); 


lIdx = 1;
rIdx = 1;
for cIdx = 1:cLen
  % Should we grab from 'a' or 'b' ???
  if lIdx > lLen
    % All done with 'a' vector, grab from 'b' vector.
    c(cIdx) = r(rIdx); 
    rIdx = rIdx + 1;
  elseif rIdx > rLen
    % All done with 'b' vector, grab from 'a' vector
    c(cIdx) = l(lIdx); 
    lIdx = lIdx + 1;
  elseif l(lIdx) <= r(rIdx)
     % a(i) <= b(i), grab from 'a' vector
     c(cIdx) = l(lIdx); 
     lIdx = lIdx + 1;
  else
    % b(i) < a(i), grab from 'b' vector
    c(cIdx) = r(rIdx); 
    rIdx = rIdx + 1;
  end
end
end