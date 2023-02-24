function [elements,times]=comp_insertion(elements,times,app,event)
elements = [];
times = [];
for i=1:10
 
   
    a = randi([1 10000],1,10000*i);
    b=length(a);
    start = tic;
    Insertion(a);
    finish= toc;
    c=(finish-start);
   
    elements(i)=length(a);
    times(i)=finish;
    
end
end
 