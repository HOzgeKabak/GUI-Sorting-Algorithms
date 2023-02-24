function fibn=Fibonacci2(n,app,event)           % we are defining a function Fibonacci
fibn=[0 1 1];                           % initialiing first two values for fibonacci series
for i=3:n                            % since already two values are present we are starting the loop from third element 
    fibn(i)=fibn(i-2)+fibn(i-1);  
    bar(app.UIAxes,fibn)
    Y=fibn;
    for k=1:1:length(fibn)
        text(app.UIAxes, k:k, Y(k)', num2str(Y(k)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
    drawnow update% i th element in fibnochi series is the sum of previous two elements 
end
end