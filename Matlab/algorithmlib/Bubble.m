
function array=Bubble(array)

n=length(array);
for i=1:n-1
    for j=n:-1:i+1
    if array(j)<array(j-1)
        key=array(j);
        array(j)=array(j-1);
        array(j-1)=key;
    end
    end
end

end
