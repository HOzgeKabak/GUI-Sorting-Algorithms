function [elements,times]=comp_counting(elements,times,app,event)
elements = [];
times = [];
for i=1:10
 
   
    a = randi([1 10000],1,1000*i);
    
     tic;
    countingSort_2(a);
    finish= toc;
  
   
    elements(i)=length(a);
    times(i)=finish;
    
end
    