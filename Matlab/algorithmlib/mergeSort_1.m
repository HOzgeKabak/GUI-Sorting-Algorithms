function x = mergeSort_1(x,low,high,app,event)  
    Y=x;
    bar(app.UIAxes,Y);
                     
    for i=1:1:length(x)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
     if(low < high)
       middle = floor((low + high)/2);  
       if app.isWorking == 1
       x = mergeSort_1(x,low,middle,app,event); 
       else
          app.randomArray = x;
       end
       if app.isWorking == 1    
       x = mergeSort_1(x,middle + 1, high,app,event);
       else
          app.randomArray = x;
       end
       if app.isWorking == 1
           x = merge1(x, low, middle, high,app,event);
       else
          app.randomArray = x; 
       end
       bar(app.UIAxes, x)
       Y=x;
        bar(app.UIAxes,Y);

        for i=1:1:length(x)
            text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

        end
       drawnow update
     end          
   end  