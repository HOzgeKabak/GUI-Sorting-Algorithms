
function Array=Insertion(Array)

 n=size(Array,2); %size of the array
 for j=2:n
     key=Array(j); %Key is equal to arrays j element
     i=j-1;
     while i>0 && Array(i)>key
         Array(i+1)=Array(i); %Changing two elements places if key is greater than other one
         i=i-1;
     end
     Array(i+1)=key;
 end
 
end
