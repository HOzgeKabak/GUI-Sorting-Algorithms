function y = SelectionSort(x,app,~)
pause('on')
n = length(x);
for i=1:n
    if app.isWorking == 1
      pause(app.projectSpeed)
        min_index = i;
        for j=i+1:n
            
            if x(min_index)>x(j)
                min_index=j;
            end
           
        end
        %Swap
        if(min_index~=i)
        temp = x(min_index);
        x(min_index) = x(i);
        x(i) = temp;
        
         
        end
        y=x;
       bar(app.UIAxes, y)
         drawnow update
    else 
         y=x;
         bar(app.UIAxes, y)
       
    end
    
    break
end
y=x;
bar(app.UIAxes, y)


end