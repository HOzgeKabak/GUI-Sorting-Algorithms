

function fibn=fibonacci_app(n,app,~)
fibn=[0 1 1];
i=3;
while fibn(i-1)<n
    fibn(i)=fibn(i-2)+fibn(i-1);
    i=i+1;
    
end
fibn=fibn(1:end-1);
bar(app.UIAxes,fibn)
Y=fibn;
    for i=1:1:length(fibn)
        text(app.UIAxes, i:i, Y(i)', num2str(Y(i)','%0.2f'),'HorizontalAlignment','center','VerticalAlignment','bottom')
                            
    end
drawnow update

end