function array = bucketsorting_app(array,app,~)
    pause("on")
    k = max(array);
    bucket = zeros(1,k+1);
    
    for j = 1:numel(array)
        bucket(array(j)) = bucket(array(j)) + 1;
    end
    index = 1;
    if app.isWorking==1
    for i = 1:k+1
        for j = 1:bucket(i)
            array(index) = i;
            index = index + 1;
           
        end
         bar(app.UIAxes,array)
         Y=array;
        bar(app.UIAxes,Y);
                     
        for i=1:1:length(array)
            text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

        end
            drawnow update
    end
    else
        array=app.randomArray;
        Y=array;
        bar(app.UIAxes,Y);
                     
        for i=1:1:length(array)
            text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

        end
       
    end
   
end