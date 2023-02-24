function array = merge1(array,low,middle,high,app,~)
pause('on')
Y=array;
bar(app.UIAxes,Y);
                     
    for i=1:1:length(array)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end

LLen = middle - low + 1;
RLen = high - middle;
left = zeros(1,LLen+1);
right = zeros(1,RLen+1);
for i=1:LLen
    left(i) = array(low+i-1);
end
for j=1:RLen
    right(j) = array(middle+j);
end
left(LLen+1) = inf;
right(RLen+1) = inf;
i = 1;
j = 1;
for k=low:high
    if app.isWorking == 1
        pause(app.projectSpeed)
        if left(i)<= right(j)
            array(k) = left(i);
            i = i + 1;
            bar(app.UIAxes, array)
            b = bar(app.UIAxes,array,'FaceColor','flat');
            b.CData(i,:) = [1 0 0];
            drawnow update
        else
            array(k) = right(j);
            j = j + 1;
            bar(app.UIAxes, array)
            b = bar(app.UIAxes,array,'FaceColor','flat');
            b.CData(j,:) = [1 0 0];
            drawnow update
            
        end
    else
        app.randomArray = array;
        break
    end
    
end
Y=array;
    bar(app.UIAxes,Y);
                     
    for i=1:1:length(array)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
    
end