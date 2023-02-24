function array = bucketsorting(array)
    k = max(array);
    bucket = zeros(1,k+1);
    
    for j = 1:numel(array)
        bucket(array(j)) = bucket(array(j)) + 1;
    end
    index = 1;
    for i = 1:k+1
        for j = 1:bucket(i)
            array(index) = i;
            index = index + 1;
        end
    end
end