function A=radixsorting_app(A,app,event)
pause("on")
r=max(A);
base=1;
while r/base>0
    if app.isWorking == 1
    pause(app.projectSpeed)
    A=countingsorting_app(app,event);
    base=base*10;
    bar(app.UIAxes, A)
    Y=A;
    bar(app.UIAxes,Y);
                     
    for i=1:1:length(A)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
    drawnow update
    else
        A=app.randomArray;
        Y=A;
        bar(app.UIAxes,Y);
                     
        for i=1:1:length(A)
            text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

        end
        
    end
    break
end
end
 