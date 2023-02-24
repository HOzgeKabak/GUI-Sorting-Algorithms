
function x = buildmaxheap(x)
n=length(x);
% Build max-heap out of x
% Note: In practice, x xhould be passed by reference

for i = floor(n / 2):-1:1
    % Put children of x(i) in max-heap order
    x = maxheapify(x,i,n);
end

end

function x = maxheapify(x,i,heapsize)
% Put children of x(i) in max-heap order
% Note: In practice, x xhould be passed by reference

% Compute left/right children indices
ll = 2 * i; % Note: In practice, use left bit shift
rr = ll + 1; % Note: In practice, use left bit shift, then add 1 to LSB

% Max-heapify
if ((ll <= heapsize) && (x(ll) > x(i)))
    largest = ll;
else
    largest = i;
end
if ((rr <= heapsize) && (x(rr) > x(largest)))
    largest = rr;
end
if (largest ~= i)
    x = swap(x,i,largest);
    x = maxheapify(x,largest,heapsize);
end

end

function x = swap(x,i,j)
% Swap x(i) and x(j)
% Note: In practice, x xhould be passed by reference

val = x(i);
x(i) = x(j);
x(j) = val;

end