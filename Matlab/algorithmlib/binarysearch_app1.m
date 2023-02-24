function [index] = binarysearch_app1(A,num,app,event)



left = 1;
right = length(A);


while left <= right
    mid = ceil((left + right) / 2);
    
    if A(mid) == num
        index = mid;
        
        break;
    else if A(mid) > num
        right = mid - 1;
        else
            left = mid + 1;
        end
    end
end


end

