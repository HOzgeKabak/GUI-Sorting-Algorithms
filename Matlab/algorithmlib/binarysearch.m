function  [x]= binarysearch(m, y,app,event)
left=0; %Arrays starting point
right=length(m); %Arrays end point
while (left < right)
    midPt = ceil((left + right)/2); %Arrays midpoint value
    if m(midPt) == y % y is choosen number from user
        left = midPt;
        right = midPt; 
    elseif m(midPt) < y
        
        right = midPt-1;
    else
       
        left =  midPt + 1; 
    end
   
end
