
function f=fibonacci(n,~,~)
if n==1
    f=0; %First index of Fibonnaci Sequence is 0
else
    if n==2
        f=1; %Second index of Fibonnaci Sequence is 1
    else   
    f=fibonacci(n-1)+fibonacci(n-2); %Remaning indexis equal to the sum of the two elements before it
    end
end
