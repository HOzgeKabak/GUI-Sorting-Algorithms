function B=countingsorting_app(app,~)
pause('on')
arraymax = max(app.randomArray);
C=zeros(1,arraymax);
for i=1:arraymax
    C(i)=0;
end
for j=1:app.arrayLen
    C(app.randomArray(j))=C(app.randomArray(j))+1;
end
for i=2:arraymax
    C(i)=C(i)+C(i-1);
end

for j=app.arrayLen:-1:1
    if app.isWorking == 1
    pause(app.projectSpeed)
    B(C(app.randomArray(j))) = app.randomArray(j);
    bar(app.UIAxes, B)
    Y=B;
    bar(app.UIAxes,Y);
                     
    for i=1:1:length(B)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
    drawnow update
    C(app.randomArray(j)) = C(app.randomArray(j)) - 1;
    else
        B = app.randomArray;
        Y=B;
        bar(app.UIAxes,Y);
                     
        for i=1:1:length(B)
            text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')

        end
        break
    end
end
Y=B;
bar(app.UIAxes,Y);
                     
    for i=1:1:length(B)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
end

